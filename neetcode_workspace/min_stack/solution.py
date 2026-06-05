class MinStack:
    # Time: O(?)
    # Space: O(?)
    def __init__(self) -> None:
        self.stack = []
        self.min_stack = []
        pass

    # Time: O(?)
    # Space: O(?)
    def push(self, val: int) -> None: 
        self.stack.append(val)
        if self.min_stack:
            min_val = min(self.min_stack[-1], val)
        else:
            min_val = (val)
        
        self.min_stack.append(min_val)
        pass

    # Time: O(?)
    # Space: O(?)
    def pop(self) -> None:
        if self.stack:
            self.stack.pop()
            self.min_stack.pop()
        pass

    # Time: O(?)
    # Space: O(?)
    def top(self) -> int:
        if self.stack:
            return self.stack[-1]
        else:
            return None
        return 0

    # Time: O(?)
    # Space: O(?)
    def get_min(self) -> int:
        if self.min_stack:
            return self.min_stack[-1]
        else:
            return None
        return 0
