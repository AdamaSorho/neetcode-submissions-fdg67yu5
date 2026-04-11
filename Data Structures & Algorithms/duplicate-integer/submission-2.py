class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        uniqueNums = set(nums)

        if len(uniqueNums) != len(nums): 
            return True

        return False
        