class Solution:
    def minWindow(self, s: str, t: str) -> str:
        slen = len(s)
        tlen = len(t)
        if tlen > slen: return ''
        
        min_len = float('inf')
        start_idx = end_idex = 0, 0
        res = ''

        t_count = {}
        for c in t:
            t_count[c] = 1 + t_count.get(c, 0)

        i, j = 0, 0
        count = tlen
        while j < slen:
            if s[j] in t_count and t_count[s[j]] > 0:
                count -= 1

            if s[j] in t_count:
                t_count[s[j]] -= 1
            # print(t_count, s[i], s[j], 'count - ', count)

            while count == 0:
                if j-i+1 < min_len:
                    res = s[i:j+1]
                    min_len = j-i+1
                    start_idx = i
                # print(min_len, start_idx, j, s[i:j+1], res)
                if s[i] in t_count:
                    t_count[s[i]] += 1
                if s[i] in t_count and t_count[s[i]] > 0:
                    count += 1
                i += 1
            
            j += 1
        
        return res
