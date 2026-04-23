class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()
        res, l, n = 0, 0, len(s)

        for c in s:
            while l < n and c in charSet:
                res = max(res, len(charSet))
                charSet.remove(s[l])
                l += 1
            
            charSet.add(c)

        res = max(res, len(charSet))
        
        return res
        