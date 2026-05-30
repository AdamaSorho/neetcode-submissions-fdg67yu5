class Solution:
    def search(self, nums: List[int], target: int) -> int:
        pivot = self.rotated_min_index(nums)

        if target == nums[pivot]:
            return pivot

        result = self.binary_search(nums, target, pivot + 1, len(nums) - 1)

        if result != -1:
            return result
        
        return self.binary_search(nums, target, 0, pivot - 1)
        

    def binary_search(self, nums: List[int], target: int, left: int, right: int) -> int:
        while left <= right:
            m = left + ((right - left) // 2)

            if target < nums[m]:
                right = m - 1
            elif target > nums[m]:
                left = m + 1
            else:
                return m

        return -1
        

    def rotated_min_index(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1

        if nums[0] < nums[r]:
            return l

        res = l

        while l <= r:
            m = l + ((r - l) // 2)

            if nums[m] > nums[l]:
                res = m
                r = m - 1
            else:
                l = m + 1

        return res
        