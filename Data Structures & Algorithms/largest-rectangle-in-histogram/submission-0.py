class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        heights.append(0)
        res = 0
        for i in range(len(heights)):
            while stack and heights[stack[-1]] > heights[i]:
                h = heights[stack.pop()]
                left = stack[-1] if stack else -1
                width = i - left - 1
                res = max(res, width * h)
            stack.append(i)
        return res


        