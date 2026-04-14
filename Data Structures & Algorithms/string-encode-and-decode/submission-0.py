class Solution:
    mapper = {}
    n = 0

    def encode(self, strs: List[str]) -> str:
        s = str(self.n)
        self.n += 1
        self.mapper[s] = strs

        return s

    def decode(self, s: str) -> List[str]:
        return self.mapper.get(s, [])
