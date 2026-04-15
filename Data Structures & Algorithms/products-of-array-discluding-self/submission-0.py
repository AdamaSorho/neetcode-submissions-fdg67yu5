class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod, zeros, n = 1, 0, len(nums)

        for num in nums:
            if num: prod *= num
            else: zeros += 1

        if zeros > 1: return [0] * n

        res = [0] * n 

        for i, n in enumerate(nums):
            if zeros: res[i] = 0 if n else prod
            else: res[i] = prod // n

        return res
        