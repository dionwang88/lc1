class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        rmap, mmap = {}, {}
        for r in ransomNote:
            if r in rmap:
                rmap[r] = rmap[r] + 1
            else:
                rmap[r] = 1
        for m in magazine:
            if m in mmap:
                mmap[m] += 1
            else:
                mmap[m] = 1

        for r in rmap:
            if r not in mmap:
                return False
            elif mmap[r] < rmap[r]:
                return False
        return True
