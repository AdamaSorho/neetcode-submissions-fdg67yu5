class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        setNums = set(nums)
        longest = 0

        for num in setNums:
            if (num - 1) not in setNums:
                length = 1
                
                while (num + length) in setNums:
                    length += 1

                longest = max(longest, length)

        return longest
        