class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack=[]
        result=0
        for i in operations:
            if i=="+":
                result+=stack[-1]+stack[-2]
                stack.append(stack[-1]+stack[-2])
            elif i=="D":
                result+=(2*stack[-1])
                stack.append(2*stack[-1])
            elif i=="C":
                result -= stack.pop()
            else:
                result+=int(i)
                stack.append(int(i))
        return result