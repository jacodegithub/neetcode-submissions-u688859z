class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if target not in nums:
            return -1

        if len(nums) == 1:
            return 0

        l, r = 0, len(nums)-1
        k = 0
        if nums[l] > nums[r]:
            while l <= r:
                mid = (l + r) // 2
                if nums[mid] > nums[mid+1]:
                    k = mid
                    break
                elif nums[0] < nums[mid]:
                    l = mid + 1
                else:
                    r = mid - 1

            if nums[0] > target:
                l, r = k + 1, len(nums)-1
            else:
                l, r = 0, k

        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        
        return -1


        
        