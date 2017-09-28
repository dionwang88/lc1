class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s or len(s) == 0:
            return s
        vowels = list('aeiouAEIOU')
        chars = list(s)
        start, end = 0, len(chars) - 1
        while start < end:
            while start < end and chars[start] not in vowels:
                start += 1
            while start < end and chars[end] not in vowels:
                end -= 1

            temp = chars[start]
            chars[start] = chars[end]
            chars[end] = temp

            start += 1
            end -= 1
        return ''.join(chars)
