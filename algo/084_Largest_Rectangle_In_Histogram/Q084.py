class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        brute force solution
        """
        if not heights:
            return 0
        if len(heights) == 1:
            return heights[0]

        localMax, globalMax = heights[0], heights[0]
        for i in xrange(1, len(heights)):
            length = 1
            localMax = heights[i]
            localMin = heights[i]
            for j in xrange(i - 1, -1, -1):
                localMin = min(localMin, min(heights[j + 1], heights[j]))
                length += 1
                localMax = max(localMin * length, localMax)
            globalMax = max(globalMax, localMax)

        return globalMax

    def largestRectangleArea1(self, heights):
        # 首先 主体思路就是对于每个bar 我们都去求出以当前的bar为最低的bar的面积 然后所有这些面积的最大值就是结果
        # 在求以当前bar为最低bar的面积的时候 最难的就是要确定这个最低bar的左边界还有右边界
        # stack解法就是巧妙地解决了这个问题
        # 最重要的  stack里存的是索引 不是值
        # stack里存的的都是递增的序列 如果碰到小于栈顶的  那么 就计算栈顶的元素的面积 这个元素的面积
        # 左边界就是它自己  右边界就是这个小于它的元素  然后弹出  然后如果栈顶的还是大 那么继续计算
        # 因为存的是索引  所以宽度计算都是正确的
        #
        # 1) Create an empty stack.
        # 2) Start from first bar, and do following for every bar ‘hist[i]’ where ‘i’ varies from 0 to n-1.
        # ……a) If stack is empty or hist[i] is higher than the bar at top of stack, then push ‘i’ to stack.
        # ……b) If this bar is smaller than the top of stack, then keep removing the top of stack while top of the stack is greater.
        # Let the removed bar be hist[tp]. Calculate area of rectangle with hist[tp] as smallest bar.
        # For hist[tp], the ‘left index’ is previous (previous to tp) item in stack and ‘right index’ is ‘i’ (current index).
        # 3) If the stack is not empty, then one by one remove all bars from stack and do step 2.b for every removed bar.
        #
        # Create an empty stack. The stack holds indexes of hist[] array
        # The bars stored in stack are always in increasing order of their heights.
        stack = []
        max_area = 0 # Initalize max area
        tp = 0 # To store top of stack
        area_with_top = 0 # To store area with top bar as the smallest bar
        i = 0
        # Run through all bars of given histogram
        while i < len(heights):
            # If this bar is higher than the bar on top stack, push it to stack
            if len(stack) == 0 or heights[stack[-1]] <= heights[i]:
                stack.append(i)
                i += 1
            # If this bar is lower than top of stack, then calculate area of rectangle
            # with stack top as the smallest (or minimum height) bar. 'i' is
            # 'right index' for the top and element before top in stack is 'left index'
            else:
                tp = stack.pop()
                # Calculate the area with hist[tp] stack as smallest bar
                minBar = i if len(stack) == 0 else i - stack[-1] -1
                area_with_top = heights[tp] * minBar
                # update max area, if needed
                max_area = max(max_area, area_with_top)
        # Now pop the remaining bars from stack and calculate area with every popped bar as the smallest bar
        while len(stack) > 0:
            tp = stack.pop()
            minBar = i if len(stack) == 0 else i - stack[-1] - 1
            area_with_top = heights[tp] * minBar
            max_area = max(max_area, area_with_top)

        return max_area

sol = Solution()
print sol.largestRectangleArea1([2,1,5,6,2,3])
