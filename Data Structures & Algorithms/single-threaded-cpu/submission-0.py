class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        for i,t in enumerate(tasks):
            t.append(i)
        tasks.sort(key = lambda t: t[0])
        result = []
        minHeap = []
        i=0
        time =tasks[0][0]

        while minHeap or i<len(tasks):
            while i<len(tasks) and time >= tasks[i][0]:
                heapq.heappush(minHeap,[tasks[i][1],tasks[i][2]])
                i+=1
        
            if not minHeap:
                time = tasks[i][0]
            else:
                proctime,index=heapq.heappop(minHeap)
                time +=proctime
                result.append(index)
        return result