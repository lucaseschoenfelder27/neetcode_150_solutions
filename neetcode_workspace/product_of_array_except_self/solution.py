class Solution:
    # Time: O(?)
    # Space: O(?)
    def product_except_self(self, nums: list[int]) -> list[int]:
        # TODO: Implement product_except_self
        res = [1] * len(nums)
        
        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]
        
        suffix = 1
        for i in range(len(nums) -1, -1, -1):
            res [i] *= suffix
            suffix *= nums[i]
        #print('res: ', res)
        return res
