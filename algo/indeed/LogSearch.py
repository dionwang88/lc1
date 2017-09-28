class LogSearch:
    def __init__(self, fileName):
        self.fileName = fileName
    '''
    这里主要注意的是如何对map进行排序，一个是对key排序，一个是对value排序返回key的顺序
    还有就是怎么对map的map的value排序
    '''
    def search(self, query):
        lineMap = {}
        queryList = self.getQuery(query)
        print queryList
        i = 0
        with open(self.fileName, 'r') as f:
            for line in f:
                i += 1
                data = line[:-1].split(' ')
                tempMap = {}
                for word in data:
                    if word in tempMap:
                        tempMap[word] = tempMap[word] + 1
                    else:
                        tempMap[word] = 1
                for q in queryList:
                    if type(q) == list:
                        countA, countB = 0, 0
                        if q[0] in tempMap:
                            countA = tempMap[q[0]] * 2
                        if q[1] in tempMap:
                            countB = tempMap[q[1]] * 2
                        total = countA + countB
                        if total > 0:
                            lineMap[i] = total
                    elif type(q) == str:
                        if q in tempMap:
                            count = tempMap[q]
                            lineMap[i] = count

        lm = {}
        for m in sorted(lineMap, key=lineMap.get):
            count = lineMap[m]
            if count not in lm:
                valueList = [m]
                lm[count] = valueList
            else:
                valueList = lm[count]
                valueList.append(m)
                lm[count] = valueList
        print sorted(lineMap.values())
        ret = []
        for r in reversed(sorted(lm)):
            valueList = sorted(lm[r])
            for v in valueList:
                ret.append(v)
        return ret

    def getQuery(self, query):
        ret = []
        for q in query:
            if '&' in q:
                index = q.find('&')
                A = q[:index]
                B = q[index+1:]
                ret.append([A, B])
            else:
                ret.append(q)
        return ret

ls = LogSearch('README.md')
ret = ls.search(['Apache','Spark&Hadoop'])
for q in ret:
    print q
