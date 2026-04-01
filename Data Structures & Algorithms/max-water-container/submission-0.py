class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left, right = 0, len(heights) - 1
        area = 0
        max_area = 0
        while (left < right):
            width = min(heights[left], heights[right])
            area = min(heights[left], heights[right]) * (right - left)
            if area > max_area:
                max_area = area
            if width == heights[left]:
                left += 1
            else:
                right -= 1
        return max_area