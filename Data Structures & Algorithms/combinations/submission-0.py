class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        curcomb=[]
        comb=[]
        self.helper(1,curcomb,comb,n,k)
        return comb
    
    def helper(self,i,curcomb,comb,n,k):
        if len(curcomb) == k:
            comb.append(curcomb.copy())
            return 
        if i>n or len(curcomb)>k:
            return
        
        curcomb.append(i)
        print(curcomb)
        self.helper(i+1,curcomb,comb,n,k)

        curcomb.pop()
        self.helper(i+1,curcomb,comb,n,k)

