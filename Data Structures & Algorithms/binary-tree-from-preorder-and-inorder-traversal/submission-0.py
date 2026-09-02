# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        #  inorder - left, root, right
        # preorder - root, left, right
        # postorder - left, right, root

        if not preorder or not inorder:
            return None

        root = preorder[0]
        node = TreeNode(root)

        rootIdx = inorder.index(root)

        node.left = self.buildTree(preorder[1:rootIdx+1], inorder[:rootIdx])
        node.right = self.buildTree(preorder[rootIdx+1:], inorder[rootIdx+1:])

        # preorder[2] inorder[2]
        # preorder[3,4] inorder[3,4]
        return node