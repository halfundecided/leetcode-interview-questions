#
# @lc app=leetcode id=973 lang=python3
#
# [973] K Closest Points to Origin
#

# @lc code=start
# class Solution:
#     # My 1st Solution
#     def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
#         distances = []
#         result = []
#         for i in range(len(points)):
#             distance = (points[i][0] * points[i][0]) + (points[i][1] * points[i][1])
#             distances.append((points[i], distance))
      
#         distances.sort(key=lambda tup: tup[1])
#         for i in range(0, K):
#             result.append(distances[i][0])
            
#         return result

class Solution:
    # Solution from Discussion: https://leetcode.com/problems/k-closest-points-to-origin/discuss/294389/Easy-to-read-Python-min-heap-solution-(-beat-99-python-solutions-)
    # Using MaxHeap!
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        heap = []

        for (x, y) in points:
            distance = -(x * x + y * y)
            if len(heap) == K:
                heapq.heappushpop(heap, (distance, x, y))
            else:
                heapq.heappush(heap, (distance, x, y))
        
        return [(x, y) for (distance, x, y) in heap]
    
        
# @lc code=end

