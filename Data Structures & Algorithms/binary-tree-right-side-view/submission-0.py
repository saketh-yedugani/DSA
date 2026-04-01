# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        stack = collections.deque()
        stack.append(root)

        while stack:
            rightView=None
            stack_length=len(stack)
            for i in range(stack_length):
                node = stack.popleft()
                if node:
                    rightView=node
                    stack.append(node.left)
                    stack.append(node.right)
            if rightView:
                result.append(rightView.val)
        return result
