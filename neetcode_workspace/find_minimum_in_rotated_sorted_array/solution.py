class Solution:
    # Time: O(?)
    # Space: O(?)
    def find_min(self, nums: list[int]) -> int:
        res = nums[0]
        l, r = 0, len(nums) - 1

        while l <= r:
            #print ('\t searching with l: ', l, ', r: ', r)
            #print('\t\t res = ', res, ' nums[l] = ', nums[l], ' nums[r] = ', nums[r])
            if nums[l] < nums[r]:
                res = min(res, nums[l])
                break
            
            m = (l + r) // 2
            #print('\t\t\t m = ', m, ' nums[m] = ', nums[m])
            res = min(res, nums[m])
            #print('\t\t\t  res = ', res)
            if nums[m] >= nums[l]:
                l = m + 1
            else:
                r = m - 1
        return res
