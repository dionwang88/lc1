class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        v1 = [int(i) for i in version1.split('.')]
        v2 = [int(i) for i in version2.split('.')]
        i, j = 0, 0
        while i < len(v1) and j < len(v2):
            if v1[i] > v2[i]:
                return 1
            elif v1[i] < v2[i]:
                return -1
            i += 1
            j += 1
        while i < len(v1):
            if v1[i] > 0:
                return 1
            i += 1
        while j < len(v2):
            if v2[j] > 0:
                return -1
            j += 1
        return 0

sol = Solution()
print sol.compareVersion('1.1.2', '1.1.2.0.1')
