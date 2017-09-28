'''
这道题用到了滑动窗口 sliding window 双指针 还有两个字典
一个字典是用来存储words里面有哪些词 并且分别出现了几次 另一个表就是遍历的时候用来和第一个表进行比较
然后双指针就是用来做滑动窗口用的
注意一下外面的那个大循环 因为不一定匹配是从第一个开始的 比如'aafoobar' ['foo', 'bar']
所以要分别在lenWord的范围内都做起始点查一遍
内循环就是遍历整个数组 然后最里面的那个while就是用来处理当比如foo出现了两次 但是bar还没有 就需要移动窗口的情况
注意count变量的使用
'''
class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        if len(words) == 0:
    		return []
    	# initialize d, l, ans
    	l = len(words[0])
    	d = {}
    	for w in words:
    		if w in d:
    			d[w] += 1
    		else:
    			d[w] = 1
    	i = 0
    	ans = []

    	# sliding window(s)
    	for k in range(l): # 注意：这里循环的是一个word的长度，因为要了解主字符串从每一个位置的substring的情况
    		left = k
    		subd = {}
    		count = 0
    		for j in xrange(k, len(s)-l+1, l):
    			tword = s[j:j+l]
    			# valid word
    			if tword in d:
    				if tword in subd:
    					subd[tword] += 1
    				else:
    					subd[tword] = 1
    				count += 1
    				while subd[tword] > d[tword]:
    					subd[s[left:left+l]] -= 1
    					left += l
    					count -= 1
    				if count == len(words):
    					ans.append(left)
    			# not valid
    			else:
    				left = j + l
    				subd = {}
    				count = 0

    	return ans
