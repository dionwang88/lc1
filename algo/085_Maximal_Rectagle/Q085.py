class Solution(object):
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        使用三个数组分别记录该节点到左边的距离，到右边的距离，和高度, left, right, and height
        对每一行来说：
            循环所有的列：
                如果matrix[i][j] == 1, 则height[j]++; 如果matrix[i][j] == 0, 则height[j] = 0
                如果matrix[i][j] == 1, left[j] = max(left[j], cur_left); 如果matrix[i][j] == 0, left[j] = 0, cur_left = j + 1
                如果matrix[i][j] == 1, right[j] = min(right[j], cur_right); 如果matrix[i][j] == 0, right[j] = n, cur_right = j
                maxArea = max(maxArea, (right[j] - left[j]) * height[j])
        """
        if not matrix or not matrix[0]:
            return 0
        m, n = len(matrix), len(matrix[0])
        left = [0 for _ in xrange(n)]
        right = [n for _ in xrange(n)]
        height = [0 for _ in xrange(n)]
        maxArea = 0
        for i in xrange(m):
            cur_left, cur_right = 0, n
            for j in xrange(n): #compute height (can do this from either side)
                if matrix[i][j] == '1':
                    height[j] += 1
                else:
                    height[j] = 0

            for j in xrange(n): # compute left (from left to right)
                if matrix[i][j] == '1':
                    left[j] = max(left[j], cur_left)
                else:
                    left[j] = 0
                    cur_left = j + 1

            for j in xrange(n - 1, -1, -1): # compute right (from right to left)
                if matrix[i][j] == '1':
                    right[j] = min(right[j], cur_right)
                else:
                    right[j] = n
                    cur_right = j

            for j in xrange(n): # compute the area of rectangle (can do this from either side)
                maxArea = max(maxArea, (right[j] - left[j]) * height[j])

        return maxArea
