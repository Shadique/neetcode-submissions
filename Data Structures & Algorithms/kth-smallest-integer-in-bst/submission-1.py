# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        cnt = 0
        def inorder(cur):
            nonlocal cnt
            if cur is None:
                return
            left = inorder(cur.left)
            if left is not None:
                return left
            cnt += 1
            if cnt == k:
                return cur.val
            return inorder(cur.right)

        return inorder(root)