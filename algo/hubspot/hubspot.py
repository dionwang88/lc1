import json
import urllib2
from datetime import datetime

req = urllib2.Request('https://candidate.hubteam.com/candidateTest/v1/partners?userKey=f91a8dd0f2529f0853f4187ee66a')
response = urllib2.urlopen(req)
the_page = response.read()

data = json.loads(the_page)

# build the partners map (key -> country, value -> map (key -> startDate, value -> email list))
partners = {}
for partner in data['partners']:
    country = str(partner['country'])
    email = str(partner['email'])
    if country not in partners:
        pmap = {}
        dateList = partner['availableDates']
        sortList = sorted(dateList)
        emailList = set()
        if len(sortList) > 1:
            for i in xrange(1, len(sortList)):
                date1 = datetime.strptime(sortList[i - 1], '%Y-%m-%d')
                date2 = datetime.strptime(sortList[i], '%Y-%m-%d')
                if (date2 - date1).days == 1:
                    emailList.add(email)
                    pmap[date1] = emailList
        partners[country] = pmap
    else:
        pmap = partners[country]
        dateList = partner['availableDates']
        sortList = sorted(dateList)
        if len(sortList) > 1:
            for i in xrange(1, len(sortList)):
                date1 = datetime.strptime(sortList[i - 1], '%Y-%m-%d')
                date2 = datetime.strptime(sortList[i], '%Y-%m-%d')
                if (date2 - date1).days == 1:
                    if date1 in pmap:
                        emailList = pmap[date1]
                        emailList.add(email)
                    else:
                        emailList = set()
                        emailList.add(email)
                        pmap[date1] = emailList

# get the country max common start date

countryCountMap = {}

for country in partners:
    pmap = partners[country]
    dateCountMap = {}

    maxCount = 0
    for startDate in pmap:
        length = len(pmap[startDate])
        if length in dateCountMap:
            dlist = dateCountMap[length]
            dlist.append(startDate)
        else:
            dlist = []
            dlist.append(startDate)
            dateCountMap[length] = dlist

    if len(pmap) == 0:
        countryCountMap[country] = (0, None)
    else:
        maxLen = sorted(dateCountMap)[-1]
        dlist = dateCountMap[maxLen]
        earliest = sorted(dlist)[0]

        countryCountMap[country] = (maxLen, earliest)

# get the result list
result = []

for country in countryCountMap:
    maxCount, startDate = countryCountMap[country]
    pmap = partners[country]
    guest = {}
    if len(pmap) == 0:
        guest['attendeeCount'] = 0
        guest['attendees'] = []
        guest['name'] = country
        guest['startDate'] = None
    else:
        emailList = pmap[startDate]
        assert maxCount == len(emailList)
        print country, maxCount, startDate.strftime('%Y-%m-%d')
        guest['attendeeCount'] = maxCount
        guest['attendees'] = list(emailList)
        guest['name'] = country
        guest['startDate'] = startDate.strftime('%Y-%m-%d')
    result.append(guest)


# submit the result
import requests
jdata = {}
jdata['countries'] = result
data_json = json.dumps(jdata)

url = 'https://candidate.hubteam.com/candidateTest/v1/results?userKey=f91a8dd0f2529f0853f4187ee66a'
headers = {'Content-type': 'application/json'}
r = requests.post(url, data=data_json, headers=headers)