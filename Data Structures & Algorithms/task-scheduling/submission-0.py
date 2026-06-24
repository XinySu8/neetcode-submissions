class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        maxHeap = [-cnt for cnt in count.values()]
        heapq.heapify(maxHeap)

        times = 0
        q = deque()
        while maxHeap or q:
            times += 1
            if maxHeap:
                cnt = heapq.heappop(maxHeap)
                cnt += 1
                if cnt != 0:
                    q.append([cnt, times + n])
            if q and q[0][1] == times:
                heapq.heappush(maxHeap, q.popleft()[0])
            
        return times

            



