class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zero_cnt = 0
        for i in nums:
            if i == 0:
                zero_cnt += 1
        if zero_cnt > 1: return [0] * len(nums)

        result = [[x for j, x in enumerate(nums) if j != i] for i, num in enumerate(nums)]
        # print(result)
        return [math.prod(p) for p in result]