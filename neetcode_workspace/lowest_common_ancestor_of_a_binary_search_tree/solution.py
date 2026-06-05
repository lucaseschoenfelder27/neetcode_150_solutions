from leetcode_py import TreeNode


class Solution:
    # Time: O(?)
    # Space: O(?)
    def lowest_common_ancestor(
        self, root: TreeNode[int] | None, p: TreeNode[int], q: TreeNode[int]
    ) -> TreeNode[int] | None:
        # TODO: Implement lowest_common_ancestor
        
        if not root or not p or not q:
            return None
        if (max(p.val, q.val) < root.val):
            return self.lowest_common_ancestor(root.left, p, q)
        elif (min(p.val, q.val) > root.val):
            return self.lowest_common_ancestor(root.right, p, q)
        else:
            return root

        