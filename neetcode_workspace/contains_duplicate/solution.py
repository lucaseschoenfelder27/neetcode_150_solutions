class Solution:
    # Time: O(?)
    # Space: O(?)
    def contains_duplicate(self, nums: list[int]) -> bool:
        # TODO: Implement contains_duplicate
        duplicate = {} # {1 : False, 2: False, 3: False}
        for num in nums:
            if num not in duplicate:
                duplicate[num] = False
            else:
                #print('duplicate:', duplicate)
                return True
        return False
        
""" ([1, 2, 3, 1], True),
            ([1, 2, 3, 4], False),
            ([1, 1, 1, 3, 3, 4, 3, 2, 4, 2], True),
            ([1], False),
            ([1, 1], True),
            ([0, 0], True),
            ([-1, -1], True),
            ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], False),
            ([10, 9, 8, 7, 6, 5, 4, 3, 2, 1], False),
            ([1, 2, 3, 4, 5, 1], True),
            ([-1000000000, 1000000000, -1000000000], True),
            ([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0], True) """