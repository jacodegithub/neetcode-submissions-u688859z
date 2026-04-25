class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)

        while l < r:
            mid = (l + r) // 2
            total_hr = 0

            for b in piles:
                total_hr += (b + mid - 1) // mid
            
            if total_hr <= h:
                r = mid
            else:
                l = mid + 1

        return r
            
        




        