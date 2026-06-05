from leetcode_py import TreeNode


class Solution:
    # Time: O(?)
    # Space: O(?) 
    def level_order(self, root: TreeNode[int] | None) -> list[list[int]]:
        res = []

        def dfs(node, depth):
            if not node:
                return None
            if len(res) == depth:
                res.append([])
            
            res[depth].append(node.val)
            dfs(node.left, depth + 1)
            dfs(node.right, depth + 1)
            
        dfs(root, 0)
        return res
            
"""         ([3, 9, 20, None, None, 15, 7], [[3], [9, 20], [15, 7]]),
            ([1], [[1]]),
            ([], []),
            ([1, 2, 3, 4, 5, 6, 7], [[1], [2, 3], [4, 5, 6, 7]]),
            ([1, 2, None, 3, None, 4, None, 5], [[1], [2], [3], [4], [5]]),
            ([1, None, 2, None, 3], [[1], [2], [3]]),
            ([1, 2, None, 3, None], [[1], [2], [3]]), """

