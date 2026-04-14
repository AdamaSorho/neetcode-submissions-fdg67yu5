class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = defaultdict(int)
        pq, result = [], []

        for n in nums:
            counter[n] += 1

        for n, count in counter.items():
            heapq.heappush(pq, (count, n))
            if len(pq) > k:
                heapq.heappop(pq)

        for i in range(k):
            _, num = heapq.heappop(pq)
            result.append(num)

        return result