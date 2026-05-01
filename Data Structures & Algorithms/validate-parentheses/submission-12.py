class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) <= 1:
            return False

        mp = {'(': ')', '{': '}', '[': ']'}
        q = []

        for c in s:
            if c in mp:
                q.append(c)
            elif not q:
                return False
            elif mp[q.pop()] != c:
                return False

        return not q
        