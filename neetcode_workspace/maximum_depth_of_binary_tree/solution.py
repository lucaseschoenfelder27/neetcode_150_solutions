from leetcode_py import TreeNode


class Solution:
    # Time: O(?)
    # Space: O(?)
    def max_depth(self, root: TreeNode[int] | None) -> int:
        
        def max_dfs(root: TreeNode[int] | None, level: int) -> int:
            previous_level = level
            if not root:
                return previous_level
            else:
                return max (max_dfs(root.left, previous_level + 1), max_dfs(root.right, previous_level + 1))
        
        level = 0

        if not root:
            return level
        else:
            root.left, root.right = root.left, root.right
            return max(max_dfs(root.left, level + 1), max_dfs(root.right, level + 1))
