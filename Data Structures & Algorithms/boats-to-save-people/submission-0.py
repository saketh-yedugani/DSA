class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        result=0
        L=0
        R=len(people)-1
        while L<=R:
            remain=limit-people[R]
            R-=1
            result+=1
            if L<=R and remain>=people[L]:
                L+=1
        return result