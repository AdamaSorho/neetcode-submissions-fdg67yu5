class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mapper = {}

        for word in strs:
            s = "".join(sorted(word))
            if s in mapper:
                mapper[s].append(word)
            else:
                mapper[s] = [word]

        answer = []

        for _, v in mapper.items():
            answer.append(v)

        return answer
        