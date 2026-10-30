class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1
        max = 0

        while left < right:
            area = min(heights[right], heights[left]) * (right - left)
            if area > max:
                max = area
            if heights[left] <= heights[right]:
                left += 1
            else:
                right -= 1

        return max 