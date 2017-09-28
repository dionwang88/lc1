class Solution:
    def singleNumber(self, nums):
        '''
        这类题的通用解法
        如果所有元素都是连续出现了三次 那么把所有这些数字按位加起来 那么每一位都应该是三的倍数
        那么除以3余数是0 如果这时候有个数只有一次 那么除以3会有余数 所以把这些所有的数按位加起来
        然后按位模3 之后的数就是多出来的数
        '''
        cnt = [0] * 32
        for num in nums:
            i = 31
            while num and i >= 0:
                cnt[i] += num & 1
                num >>= 1
                i -= 1
        result = 0
        for i in range(32):
            if cnt[i] % 3 == 1:
                result += 1 << (31 - i)
        return result if result < (1 << 31) else result - (1 << 32)
