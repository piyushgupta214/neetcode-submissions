class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0 
        right = len(heights) - 1
        maxArea = min(heights[left], heights[right]) * (right - left)
        while left < right:
            if heights[left] <= heights[right]:
                left = left +1
            else:
                right = right -1
            maxArea = max(maxArea, min(heights[left], heights[right]) * (right - left))
        
        return maxArea
        