# Time: O(n)
# Space: O(n)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
  def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
    if not root:
      return []

    ans = []
    q = collections.deque([root])
    isLeftToRight = True

    while q:
      currLevel = []
      for _ in range(len(q)):
        if isLeftToRight:
          node = q.popleft()
          currLevel.append(node.val)
          if node.left:
            q.append(node.left)
          if node.right:
            q.append(node.right)
        else:
          node = q.pop()
          currLevel.append(node.val)
          if node.right:
            q.appendleft(node.right)
          if node.left:
            q.appendleft(node.left)
      ans.append(currLevel)
      isLeftToRight = not isLeftToRight

    return ans
