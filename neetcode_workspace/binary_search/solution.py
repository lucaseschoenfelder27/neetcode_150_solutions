class Solution:
    # Time: O(?)
    # Space: O(?)
    def search(self, nums: list[int], target: int) -> int:
        def binary_search(l: int, r: int, nums: list[int], target: int) -> int:
            #print('searching for ', target, ' l: ', l, ', r: ', r)
            if l > r:
                return -1
            
            #print('l + (r - l) =', l, ' + (', r, ' - ', l, ') // 2')
            m = l + (r - l) // 2
            print('m: ', m)
                
            if nums[m] == target:
                return m
            if nums[m] < target:
                return binary_search(m + 1, r, nums, target)
            return binary_search(l, m - 1, nums, target)
            
        index = binary_search(0, len(nums) - 1,  nums, target)
        #print('index: ', index)
        return index
