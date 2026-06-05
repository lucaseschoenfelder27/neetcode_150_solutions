class Solution:
    # Time: O(?)
    # Space: O(?)
    def daily_temperatures(self, temperatures: list[int]) -> list[int]:
        res = [0] * len(temperatures)
        stack = []
        
        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                stack_t, stack_i = stack.pop()
                res[stack_i] = i - stack_i
            stack.append((t, i))
        
        #print('res: ', res)
        return res
 