class Solution:
    def minWindow(self, s: str, t: str) -> str:
        slen = len(s)
        tlen = len(t)
        if tlen > slen: return ''
        
        min_len = float('inf')
        start_idx = 0

        for i in range(slen):
            t_count = {}
            for c in t:
                t_count[c] = t_count.get(c, 0) + 1
            # print(t_count)
            count = tlen
            for j in range(i, slen):
                if s[j] in t_count and t_count[s[j]] > 0:
                    count -= 1

                if s[j] in t_count:
                    t_count[s[j]] -= 1

                # print(t_count)
                if count == 0:
                    if j - i + 1 < min_len:
                        min_len = j - i + 1
                        start_idx = i
                    break
        
        return s[start_idx:start_idx + min_len] if min_len != float('inf') else ''
