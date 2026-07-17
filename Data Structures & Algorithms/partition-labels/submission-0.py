class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        lastIndex = {}

        for i,c in enumerate(s):
            lastIndex[c] = i
        
        result = []
        size = 0
        lastelement = 0
        for i, c in enumerate(s):
            size +=1
            lastelement = max(lastelement,lastIndex[c])

            if i == lastelement:
                result.append(size)
                size = 0
        return result