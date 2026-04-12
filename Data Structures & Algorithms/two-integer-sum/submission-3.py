class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indexes = {}
        indexes[nums[0]] = 0
        n = len(nums)

        for i in range(1, n):
            remainder = target - nums[i]

            if indexes.get(remainder) is not None:
                return [indexes.get(remainder), i]

            indexes[nums[i]] = i
            

        return []
        
        