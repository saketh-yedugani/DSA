class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        L=max(weights)
        R=sum(weights)
        result = R

        def capShip(cap):
            ships = 1
            currCap=cap
            for w in weights:
                if currCap-w < 0:
                    ships += 1
                    currCap = cap
                currCap -= w
            return ships <= days

        while L<=R:
            cap=(L+R) // 2
            if capShip(cap):
                result=min(result,cap)
                R= cap - 1
            else:
                L = cap + 1
        return result
