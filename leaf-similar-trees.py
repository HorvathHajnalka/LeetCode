# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def leafSimilar(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        """
        def depth_first_search( start):
            #mielőtt a szomszédos elemhez ugranánk, a mélyéig elmegyünk a kapcsolatoknak
            visited =   # Ebben a halmazban tároljuk a meglátogatott csúcsokat.
            result = []  # Ebben a listában tároljuk a megtalált csúcsok sorrendjét.
            # Elindítjuk a mélységi keresést a kezdőcsúccsal.
            def dfs(node):
                visited.add(node)
                if node.left == None and node.right == None:
                    result.append(node.val) #levél
                    node = visited[-1]
                elif node.left:
                    dfs(node.left) #ha mindig a szomszédra hívjuk mélyebbre megy
                elif node.rigth:
                    dfs(node.right)
            dfs(start)
            return result
        res1 =  depth_first_search(root1)
        res2 =  depth_first_search(root2)
        print(res1, res2)
        return res1 == res2
        """
        def dfs_preorder(root):
            if not root:
                return []

            result = []
            if root.left == None and root.right == None:
                result.append(root.val)
            result += dfs_preorder(root.left)
            result += dfs_preorder(root.right)
            return result
        res1 =  dfs_preorder(root1)
        res2 =  dfs_preorder(root2)
        print(res1, res2)
        return res1 == res2