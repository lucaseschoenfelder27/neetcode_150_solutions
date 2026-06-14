from leetcode_py import ListNode


class Solution:
    # Time: O(?)
    # Space: O(?)
    def add_two_numbers(
        self, l1: ListNode[int] | None, l2: ListNode[int] | None
    ) -> ListNode[int] | None:
        stack_l1 = []
        stack_l2 = []
        
        currentl1 = l1
        while currentl1:
            stack_l1.append(currentl1.val)
            currentl1 = currentl1.next
        
        currentl2 = l2
        while currentl2:
            stack_l2.append(currentl2.val)
            currentl2 = currentl2.next
        #for i in l1:
        #    stack_l1.append(i)
        #for i in l2:
        #    stack_l2.append(i)
        
        if sum(stack_l1) == 0 and sum(stack_l2) == 0:
            return ListNode.from_list([0])
        elif sum(stack_l1) == 0:
            return l2
        elif sum(stack_l2) == 0:
            return l1
        
        
        # [9, 9, 9, 9, 9, 9, 9], l2: [9, 9, 9, 9]
        # smallest_length = 4
        smallest_length = min(len(stack_l1), len(stack_l2))
        
        res = []
        overflow = 0
        
        for _ in range(smallest_length):
            #[7, 8, 9], [1, 2, 3]
            # 3, 9
            a, b = stack_l1.pop(0), stack_l2.pop(0)
            
            sum_ab = a + b # = 12
            if overflow != 0:
                sum_ab += overflow
            
            if sum_ab >= 10:
                overflow = sum_ab // 10 # 1 
                res.append(sum_ab % 10) # 2
            else: #[9, 7, 5]
                res.append(sum_ab)
                overflow = 0
        
        while stack_l1 or stack_l2:
            num = stack_l1.pop(0) if stack_l1 else stack_l2.pop(0)
            
            if overflow != 0:
                num += overflow
            
            if num >= 10:
                overflow = num // 10 
                res.append(num % 10)
            else:
                res.append(num)
                overflow = 0
        
        if overflow > 0:
            res.append(overflow)

        if res:
            res = ListNode.from_list(res)
            return res
        return None
        
        return res if res else None
