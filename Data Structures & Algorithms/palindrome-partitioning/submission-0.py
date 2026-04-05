class Solution:
    def partition(self, s: str) -> List[List[str]]:
        result = []
        pali_present = []

        def dfs(i):
            if i>= len(s):
                result.append(pali_present.copy())
                return
            
            for j in range(i,len(s)):
                if self.isPali(s,i,j):
                    pali_present.append(s[i:j+1])
                    dfs(j+1)
                    pali_present.pop()
        dfs(0)
        return result
    
    def isPali(self,s,l,r):
        while l<r:
            if s[l]!=s[r]:
                return False
            l+=1
            r-=1
        return True