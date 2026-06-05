class Solution:
    # Time: O(?)
    # Space: O(?)
    def search(self, nums: list[int], target: int) -> int:
        def binary_search(left: int, right: int) -> int:
            #print('\t\t starting search with left=', left, ' right=', right)
            
            while left <= right:
                mid = (left + right) // 2
                
                #print('\t\t nums[left]=', nums[left], ' nums[right]=', nums[right], ' nums[mid]=', nums[mid])
                if nums[mid] == target:
                    return mid
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
                
                #print('\t\t\t should now search between left=', left, ' right=', right)
            return -1
                
        #print('nums: ', nums, 'target: ', target)
        #res = nums[0]
        l, r = 0, len(nums) - 1
        while l < r:
            m = (l + r) // 2 
            
            #print('\t\t nums[l]=', nums[l], ' nums[r]=', nums[r], ' nums[m]=', nums[m])
            
            if nums[m] > nums[r]:
                l = m + 1
            else:
                r = m
        
        #print('\t after while, l=', l, ' r=', r)
        
        pivot = l
        
        result = binary_search(0, pivot - 1)
        if result != -1:
            return result
        
        return binary_search(pivot, len(nums) - 1)