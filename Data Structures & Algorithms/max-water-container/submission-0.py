class Solution:
    def maxArea(self, heights: List[int]) -> int:
        result = 0
        left, right = 0, len(heights) - 1
        while left < right:
            w = right - left
            h = min(heights[left], heights[right])
            area = w * h
            result = max(area, result)
            if heights[left] < heights[right]:
                left += 1
            elif heights[right] < heights[left]:
                right -= 1
            else: left += 1
        return result