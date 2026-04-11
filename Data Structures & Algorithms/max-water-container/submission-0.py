class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_area = 0
        for l in range(len(heights)):
            for r in range(l+1, len(heights)):
                area = (r - l) * min(heights[l], heights[r])
                max_area = max(max_area, area)
        return max_area
        