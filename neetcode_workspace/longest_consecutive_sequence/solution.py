class Solution:
    # Time: O(?)
    # Space: O(?)
    def longest_consecutive(self, nums: list[int]) -> int:
        # TODO: Implement longest_consecutive
        nums_set = set(nums)
        #print('nums_set: ', nums_set)
        sequence = 0
        for num in nums:
            #print('processing ', num)
            if (num - 1) not in nums_set:
                length = 0
                #current = num
                #count = 1
                while(num + length) in nums_set:
                    length += 1
                
                sequence = max(sequence, length)
        return sequence