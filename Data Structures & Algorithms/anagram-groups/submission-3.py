class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mapper = defaultdict(list)

        for word in strs:
            s = "".join(sorted(word))
            mapper[s].append(word)

        return list(mapper.values())
