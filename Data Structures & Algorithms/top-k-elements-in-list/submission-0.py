class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count=defaultdict(int)
        for i in nums:
            count[i]+=1
        
        checker= sorted(count.items(), key=lambda items:items[1], reverse=True)
        print(checker)
        final=[]
        for i in checker[:k]:
            final.append(i[0])

        return final