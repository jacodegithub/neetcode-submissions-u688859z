class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1 = len(s1)
        n2 = len(s2)
        word1 = ''.join(sorted(s1))

        i, j = 0, n1
        while i < j and j <= n2:
            word2 = ''.join(sorted(s2[i:j]))
            print(i, j, word1, word2)
            if word1 == word2:
                return True
            i += 1
            j += 1
        return False