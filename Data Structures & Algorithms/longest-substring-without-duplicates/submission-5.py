class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()
        res, l, n = 0, 0, len(s)

        for r in range(n):
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1

            res = max(res, r - l + 1)
            charSet.add(s[r])

        res = max(res, len(charSet))
        
        return res
        