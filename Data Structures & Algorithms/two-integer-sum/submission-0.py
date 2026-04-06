class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        if nums is None: return []
        
        d = {}
        for i in range(len(nums)):
            rem = target - nums[i]

            if rem in d:
                return [d[rem], i]
            d[nums[i]] = i
        return []
            
        