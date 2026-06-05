from leetcode_py import TreeNode


class Solution:
    # Time: O(?)
    # Space: O(?)
    def kth_smallest(self, root: TreeNode[int] | None, k: int) -> int:
        # TODO: Implement kth_smallest
        arr = []

        def dfs(node):
            if not node:
                return None
            arr.append(node.val)
            dfs(node.left)
            dfs(node.right)
        

        dfs(root)
        arr.sort()
        return arr[k-1]
