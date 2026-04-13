class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i, j = 0, 0
        ch = set()
        max_len = 0
        for j in range(len(s)):
            while s[j] in ch:
                ch.remove(s[i])
                i += 1
            ch.add(s[j])
            max_len = max(max_len, j-i+1)
        return max_len