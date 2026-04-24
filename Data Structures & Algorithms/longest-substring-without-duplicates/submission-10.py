class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        mp = {}
        l, n, res = 0, len(s), 0

        for r in range(n):
            if s[r] in mp:
                l = max(mp[s[r]] + 1, l)

            mp[s[r]] = r
            res = max(res, r - l + 1)

        return res

        