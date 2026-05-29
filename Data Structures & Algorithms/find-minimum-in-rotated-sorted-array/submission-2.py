class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1

        if nums[l] < nums[r]:
            return nums[l]

        res = nums[l]

        while l <= r:
            m = l + ((r - l) // 2)

            if nums[m] < res:
                res = nums[m]
                r = m - 1
            else:
                l = m + 1

        return res



        