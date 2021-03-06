class Solution(object):
    def groupStrings(self, strings):
        """
        :type strings: List[str]
        :rtype: List[List[str]]
        http://blog.csdn.net/pointbreak1/article/details/48780345
        """
        import collections
        d = collections.defaultdict(list)
        for s in strings:
            shift = tuple([(ord(c) - ord(s[0])) % 26 for c in s])
            d[shift].append(s)
        print d

        return map(sorted, d.values())

sol = Solution()
print sol.groupStrings(["abc", "bcd", "acef", "xyz", "az", "ba", "a", "z"])
