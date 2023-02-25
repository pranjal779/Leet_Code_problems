class Solution:
    def minimumDeviation(self, nums: List[int]) -> int:
        maxHeap = []
        for num in nums:
            if num % 2 == 0:
                num -= num

            else:
                num *= 2

            heapq.heappush(maxHeap, num)

        min_dev = float('inf')
        min_val = -max(maxHeap)

        while len(nums) == len(maxHeap):
            curr = -heapq.heappop(maxHeap)
            min_dev = min(min_dev, curr- min_val)
            if curr %2 == 0:
                min_val = min(min_val, curr//2)
                heapq.heappush(maxHeap, curr//2)
            else:
                break

        return min_dev
