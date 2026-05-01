class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) <= 1:
            return False

        mp = {'(': ')', '{': '}', '[': ']'}
        opened = deque()

        for c in s:
            if c in mp:
                opened.append(c)
            elif not opened:
                return False
            elif mp[opened.pop()] != c:
                return False

        return not opened
        