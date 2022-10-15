"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        res = []
        if root == None:
            return []
        for c in root.children:
            res +=  self.postorder(c)
        res.append(root.val)
        return res
