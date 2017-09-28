class Solution:
    def __init__(self):
        self.strobo = {'0':'0','1':'1','6':'9','8':'8','9':'6'}

    def isStrobogrammatic(self, num):
        nums = [i for i in str(num)]
        if len(num) % 2 == 1:
            if nums[len(num) / 2] not in ['1', '8']:
                return False
        i, j = 0, len(nums) - 1
        while i < j:
            if nums[i] in self.strobo:
                if self.strobo[nums[i]] == nums[j]:
                    i += 1
                    j -= 1
                else:
                    return False
            else:
                return False
        return True

sol = Solution()
print sol.isStrobogrammatic(68189)
