import sys

class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if(len(s) == 0):
            return 0
        map = {}
        count = -20000000
        i = 0
        for j in range(len(s)):
            if s[j] in map:
                idx = map.get(s[j])
                while i <= idx:
                    del map[s[i]]
                    i += 1
                map[s[j]] = j
            else:
                map[s[j]] = j
                count = max(count, len(map))
        return count

s = Solution()
print(s.lengthOfLongestSubstring("bpfbhmipx"))
