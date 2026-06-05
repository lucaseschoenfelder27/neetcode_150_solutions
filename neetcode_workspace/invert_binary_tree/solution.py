from leetcode_py import TreeNode

""" [
            ([4, 2, 7, 1, 3, 6, 9], [4, 7, 2, 9, 6, 3, 1]),
            ([2, 1, 3], [2, 3, 1]),
            ([], []),
            ([1], [1]),
            ([1, 2], [1, None, 2]),
            ([1, None, 2], [1, 2]),
            ([1, 2, 3, 4, 5], [1, 3, 2, None, None, 5, 4]),
            ([1, 2, 3, None, None, 4, 5], [1, 3, 2, 5, 4]),
            ([1, 2, 3, 4, 5, 6, 7], [1, 3, 2, 7, 6, 5, 4]),
            ([5, 3, 8, 2, 4, 7, 9], [5, 8, 3, 9, 7, 4, 2]),
            ([10, 5, 15, None, 6, 12, 20], [10, 15, 5, 20, 12, 6]),
            ([1, 2, None, 3], [1, None, 2, None, 3]),
            ([0, -1, 1], [0, 1, -1]),
            ([100, 50, 150], [100, 150, 50]),
            ([1, 2, 3, None, 4, None, 5], [1, 3, 2, 5, None, 4]),
        ] """

class Solution:
    # Time: O(?)
    # Space: O(?)
    # class TreeNode(object):
    #     def __init__(self, val=0, left=None, right=None):
    #         self.val = val
    #         self.left = left
    #         self.right = right
    def invert_tree(self, root: TreeNode[int] | None) -> TreeNode[int] | None:
        #print('\t\t root: ', root)
        if not root:
            return None
        root.left, root.right = root.right, root.left

        self.invert_tree(root.left)
        self.invert_tree(root.right)

        return root

"""          [4, 2, 7, 1, 3, 6, 9], [4, 7, 2, 9, 6, 3, 1]),
            ([2, 1, 3], [2, 3, 1]),
            ([], []),
            ([1], [1]),
            ([1, 2], [1, None, 2]),
            ([1, None, 2], [1, 2]),
            ([1, 2, 3, 4, 5], [1, 3, 2, None, None, 5, 4]),
            ([1, 2, 3, None, None, 4, 5], [1, 3, 2, 5, 4]),
            ([1, 2, 3, 4, 5, 6, 7], [1, 3, 2, 7, 6, 5, 4]),
            ([5, 3, 8, 2, 4, 7, 9], [5, 8, 3, 9, 7, 4, 2]), """