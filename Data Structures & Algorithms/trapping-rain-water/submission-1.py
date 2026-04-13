class Solution:
    def trap(self, height: List[int]) -> int:
        water = 0
        for i in range(len(height)):
            l = i - 1
            r = i + 1

            left_max_height, right_max_height = 0, 0
            while l >= 0:
                if height[i] < height[l]: left_max_height = max(left_max_height, height[l])
                l -= 1

            while r < len(height):
                if height[i] < height[r]: right_max_height = max(right_max_height, height[r])
                r += 1
                
            mark_height = min(right_max_height, left_max_height)

            if mark_height > 0:
                water += mark_height - height[i]

        return water