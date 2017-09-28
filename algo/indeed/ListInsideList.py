/**
 *
 首先得到每个元素的个数的map
 然后以个数最多的那个长度创建数组
 开始循环数组长度
 然后再循环map，每个key取出来则value值减一
 */
def getMinLists(li):
    ret = []
    mapList = {}
    for l in li:
        if l in mapList:
            mapList[l] = mapList[l] + 1
        else:
            mapList[l] = 1
    maxNum = sorted(mapList.values())[-1]
    print maxNum
    for i in xrange(maxNum):
        inList = []
        for key in mapList:
            if mapList[key] > 0:
                inList.append(key)
                mapList[key] = mapList[key] - 1
        ret.append(inList)
    return ret

li = [1,1,2,2,2,3,3,3,3,3,4,4,5,5,6,7,8]
ret = getMinLists(li)
for l in ret:
    print l
