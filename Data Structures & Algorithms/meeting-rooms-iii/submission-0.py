class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings.sort()
        avaliable = []
        for i in range(n):
            avaliable.append(i)
        used = []  #[(end_time, room_number)]
        count = [0] * n #count of meeting rooms avaliable

        for start, end in meetings:
            while used and used[0][0] <= start:
                _,room = heapq.heappop(used)
                heapq.heappush(avaliable,room)
            
            if not avaliable:
                end_time,room = heapq.heappop(used)
                end = end_time + (end - start)
                heapq.heappush(avaliable,room)
            
            room = heapq.heappop(avaliable)
            heapq.heappush(used,(end,room))
            count[room] += 1
        
        return count.index(max(count)) # count.index will go from index 0 to the end in sequence and find the max from the values

