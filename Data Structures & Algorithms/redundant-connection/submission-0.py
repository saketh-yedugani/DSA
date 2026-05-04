class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        N = len(edges)
        par = []
        for i in range(N+1):
            par.append(i)
        rank = [1] * (N+1)

        def find(n1):
            res = par[n1]
            while res!=par[res]:
                par[res] = par[par[res]]
                res = par[res]
            return res

        
        def union(n1,n2):
            p1,p2 = find(n1),find(n2)
            if p1 == p2:
                return False
            
            if rank[p1] > rank[p2]:
                par[p2] = p1
            else:
                par[p1] = p2
            return True
        
        for n1,n2 in edges:
            if not union(n1,n2):
                return [n1,n2]