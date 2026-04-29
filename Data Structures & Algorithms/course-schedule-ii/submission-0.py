class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        preMap = defaultdict(list)
        for crs, prev in prerequisites:
            preMap[crs].append(prev)

        output = []
        cycle = set()
        visit = set()

        def dfs(crs):
            if crs in cycle:
                return False
            if crs in visit:
                return True
            
            cycle.add(crs)
            for p in preMap[crs]:
                if dfs(p) == False:
                    return False
            cycle.remove(crs)
            visit.add(crs)
            output.append(crs)
            return True
        


        for c in range(numCourses):
            if dfs(c) == False:
                return []
        return output