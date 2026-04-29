class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res, window = [], nums[0: k]

        heapq.heapify_max(window)
        res.append(heapq.heappop(window))

        l = 0
        for r in range(k, len(nums)):
            l += 1
            window = nums[l: r + 1]
            heapq.heapify_max(window)
            res.append(heapq.heappop(window))

        return res
        