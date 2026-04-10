class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if nums is None or len(nums) == 0: return 0
        num_set = set(nums)
        # print(num_set)
        longest_con_seq = 0
        for num in num_set:
            length = 0
            while num-length in num_set:
                length += 1
                longest_con_seq = max(longest_con_seq, length)
        return longest_con_seq