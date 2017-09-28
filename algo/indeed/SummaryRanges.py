class SummaryRanges:
    def summaryRanges(self, lst):
        i, j = 0, 0
        ret = []
        for i in xrange(len(lst) - 1):
            if lst[i + 1] - lst[i] == 1:
                continue
            else:
                if i == j:
                    ret.append(str(lst[i]) + ',')
                elif i > j:
                    ret.append(str(lst[j]) + '-' + str(lst[i]) + '/' + str(i - j + 1) + ',')
                j = i + 1
        if i + 1 == j:
            ret.append(str(lst[i + 1]))
        elif i > j:
            ret.append(str(lst[j]) + '-' + str(lst[i]) + '/' + str(i - j + 1))
        return ret

lst = [-3, -2, 1, 2, 2, 2, 3, 3, 5, 8, 10, 11, 12, 15]
sr = SummaryRanges()
print sr.summaryRanges(lst)
'''
不要忘记处理最后一部分字符，如果是连续的直到尾部，则i > j, 如果最后一个字符是单个的，则i == j
'''
