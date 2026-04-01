class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        checker={')':'(','}':'{',']':'['}

        for i in s:
            if i in checker:
                if stack and stack[-1]==checker[i]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(i)
        
        return True if not stack else False