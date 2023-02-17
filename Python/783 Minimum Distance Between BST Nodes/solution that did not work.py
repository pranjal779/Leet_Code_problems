# Time Complexity: O(N). Space Complexity: O(N).

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def minDiffInBST(self, root: TreeNode) -> int:
        self.values = []
        
        self.inorder_traverse(root)
        
        min_distance = sys.maxsize
        
        prev = None
        
        for val in self.values:
            if prev:            
                distance = val - prev
                min_distance = min(min_distance, distance)
            prev = val
            
        
        return min_distance
        
    def inorder_traverse(self, root):
        
        if not root:
            return 
        
        
        self.inorder_traverse(root.left)
        self.values.append(root.val)
        
        self.inorder_traverse(root.right)
