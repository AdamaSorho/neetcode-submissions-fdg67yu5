class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()
        res, n, l, = 0, len(s), 0

        for r in range(n):
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1

            res = max(res, r - l + 1)
            charSet.add(s[r])

        return res 