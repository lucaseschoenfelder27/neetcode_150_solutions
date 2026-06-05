from leetcode_py import TreeNode


class Solution:
    # Time: O(?)
    # Space: O(?)
    left_check = staticmethod(lambda val, limit: val < limit)
    right_check = staticmethod(lambda val, limit: val > limit)
    
    def is_valid_bst(self, root: TreeNode[int] | None) -> bool:
        if not root:
            return True
        if (not self.is_valid(root.left, root.val, self.left_check) or
            not self.is_valid(root.right, root.val, self.right_check)):
            return False

        return self.is_valid_bst(root.left) and self.is_valid_bst(root.right)

    def is_valid(self, root: TreeNode[int] | None, limit: int, check) -> bool:
        if not root:
            return True
        if not check(root.val, limit):
            return False
        return (self.is_valid(root.left, limit, check) and
                self.is_valid(root.right, limit, check))

        