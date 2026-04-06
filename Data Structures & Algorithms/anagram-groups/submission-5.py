class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if strs is None: return []

        groups: defaultdict = defaultdict(list)
        answer = []

        for word in strs:
            sorted_word = ''.join(sorted(word))
            groups[sorted_word].append(word)

        return list(groups.values())
            
        