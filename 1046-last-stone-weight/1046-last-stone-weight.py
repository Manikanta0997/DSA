class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        for i in range(len(stones)):
            stones[i] = -1 * stones[i]
        maxHeap = stones
        heapq.heapify(maxHeap)
        while len(maxHeap) > 1:
            x = heapq.heappop(maxHeap)
            y = heapq.heappop(maxHeap)
            if y > x:
                heapq.heappush(maxHeap, x - y)
        if len(maxHeap) == 1:
            return abs(heapq.heappop(maxHeap))
        return 0