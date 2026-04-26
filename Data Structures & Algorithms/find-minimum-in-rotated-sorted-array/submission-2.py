class Solution:
    def findMin(self, nums: List[int]) -> int:
        if nums[0] < nums[len(nums)-1] or len(nums) == 1:
            return nums[0]
        l, r = 0, len(nums)-1
        res = 0
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] > nums[mid+1]:
                res = nums[mid+1]
                break
            elif nums[mid] > nums[0]:
                l = mid + 1
            else:
                r = mid
        return res
        