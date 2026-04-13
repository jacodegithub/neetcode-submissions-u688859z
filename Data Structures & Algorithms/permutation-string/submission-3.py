class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2): return False

        s1f = [0] * 26
        s2f = [0] * 26

        for i in range(len(s1)):
            s1f[ord(s1[i]) - ord('a')] += 1
            s2f[ord(s2[i]) - ord('a')] += 1

        if s1f == s2f:
            return True

        for i in range(len(s1), len(s2)):
            s2f[ord(s2[i]) - ord('a')] += 1
            s2f[ord(s2[i - len(s1)]) - ord('a')] -= 1

            if s1f == s2f:
                return True
        return False
