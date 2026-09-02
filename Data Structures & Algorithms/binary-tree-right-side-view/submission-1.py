# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
        # 2 4 1 3 5 inorder
        # 1 2 4 3 5 preorder
        # [1] [2 3] [4 5] level order


        # 2 4 5 1 3 inorder
        # 1 2 4 5 3 preorder
        # 2 4 5 3 1 postorder
        # [1] [2 3] [4] [5] level order

        if not root:
            return []
        queue = deque([root])
        res = []
        while len(queue) > 0:
            n = len(queue)
            level = []
            for _ in range(n):
                node = queue.popleft()
                level.append(node.val)
                for child in [node.left, node.right]:
                    if child:
                        queue.append(child)
            res.append(level[-1])
        return res

