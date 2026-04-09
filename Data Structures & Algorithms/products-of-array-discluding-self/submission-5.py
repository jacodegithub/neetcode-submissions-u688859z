class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        output = [nums[0]]

        for i in range(1, n):
            output.append(output[-1] * nums[i])

        right_product = 1
        for i in range(n-1, -1, -1):
            if i == n-1:
                output[i] = output[i-1]
            if i == 0:
                output[i] = right_product
            else:
                output[i] = output[i-1] * right_product
            right_product *= nums[i]
        
        return output