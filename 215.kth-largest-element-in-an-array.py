#
# @lc app=leetcode id=215 lang=python3
#
# [215] Kth Largest Element in an Array
#

# @lc code=start
# class Solution:
#     # My 1st Solution: O(nlogn)
#     def findKthLargest(self, nums: List[int], k: int) -> int:
#         sortedNums = sorted(nums)
#         return sortedNums[len(sortedNums)-k]

class Solution:
    # Kevin's Solution: https://www.youtube.com/watch?v=FrWq2rznPLQ&list=PLi9RQVmJD2fYXgBAUfaN5MXgYPUTbzqeb&index=49
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # Use heaps! -- heap in Python: heapq
            # Heap data structure is mainly used to represent a priority queue. 
            # Each time the smallest of heap element is popped(minheap).
            # Whenever elements are pushed or popped, heap structure in maintained.
            # The heap[0] element also returns the smallest element each time
            # heapify - convert the iterable into a heap 
            # heappush - insert the element, the order is adjusted
            # heappop - remove and return the smallest element 
        heap = []
        for num in nums:
            heapq.heappush(heap, num)
        for _ in range(len(nums) - k):
            heapq.heappop(heap)
        return heapq.heappop(heap)

        
# @lc code=end

