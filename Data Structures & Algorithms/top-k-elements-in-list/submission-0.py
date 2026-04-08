class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if nums is None: return []
        groups: defaultdict = defaultdict(int)

        for num in nums:
            groups[num] += 1

        sorted_items = sorted(groups.items(), key=lambda x: x[1], reverse=True)
        sorted_dict = dict(sorted_items)

        return list(sorted_dict.keys())[:k]

            
        