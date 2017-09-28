class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        https://discuss.leetcode.com/topic/6148/my-really-simple-java-o-n-solution-accepted/2
        用hashmap记录每个点所存在的连续范围的边界，也就是key是最小值，value是该范围的长度，key是最大值，value同样是该范围的长度。
        如果一个新的点在hashmap中，则continue
        如果一个新的点不在hashmap中，则检查n-1和n+1是否在hashmap中，分别对应的left和right，如果不在返回0，
        如果在则返回以该点作为边界点的范围长度，所以新的连续长度就是sum = left+right+1
        然后再更新新的连续长度的边界，讲n-left和n+right更新为新的长度sum
        """
        if not nums:
            return 0
        res = 0
        nmap = {}
        for n in nums:
            if n not in nmap:
                left = nmap.get(n - 1) if n - 1 in nmap else 0
                right = nmap.get(n + 1) if n + 1 in nmap else 0
                newSum = left + right + 1
                nmap[n] = newSum
                res = max(res, newSum)
                
                # extend the length to the boundary(s) of the sequence will do nothing if n has no neighbors
                nmap[n - left] = newSum
                nmap[n + right] = newSum
            else:
                continue
        return res
