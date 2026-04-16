class Solution:
    def reorganizeString(self, s: str) -> str:
        count =Counter(s)
        maxHeap=[]
        for char,cnt in count.items():
            maxHeap.append([-cnt,char])
        heapq.heapify(maxHeap)
        
        prev =None
        result =""

        while maxHeap or prev:
            if prev and not maxHeap:
                return ""

            cnt, char = heapq.heappop(maxHeap)
            result+=char
            cnt += 1

            if prev:
                heapq.heappush(maxHeap,prev)
                prev =None
            
            if cnt!=0:
                prev = [cnt,char]
        return result