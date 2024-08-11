# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def searchBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        """
        def inorder_traversal(root, v):
            if root:
                print(root.val)
                print(v)
                if root.val == v:
                    print("done",root)
                    return root
                else:
                    inorder_traversal(root.left,v)
                    inorder_traversal(root.right,v)
            
            
        ret = inorder_traversal(root,val)
        print(ret)
        return ret
        """
        def inorder_traversal(root, key):
            if root is None:
                return root
            if key < root.val:
                return inorder_traversal(root.left, key)  
            elif key > root.val:
                return inorder_traversal(root.right, key) 
            else: 
                return root       
            
        return inorder_traversal(root,val) 