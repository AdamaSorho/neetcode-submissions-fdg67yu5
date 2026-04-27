class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = defaultdict(int)
        res, l, n, maxFreq = 0, 0, len(s), 0

        for r in range(n):
            freq[s[r]] += 1
            maxFreq = max(maxFreq, freq[s[r]])

            while (r - l + 1) - maxFreq > k:
                freq[s[l]] -= 1
                l += 1
            
            res = max(res, r - l + 1)

        return res

