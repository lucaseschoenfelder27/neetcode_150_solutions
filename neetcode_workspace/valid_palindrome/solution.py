class Solution:
    # Time: O(?)
    # Space: O(?)
    def is_palindrome(self, s: str) -> bool:
        # TODO: Implement is_palindrome
        normalized = "".join(char for char in s.lower() if char.isalnum())
        #print('normalized: ', normalized)
        length = len(normalized)
        if (length == 0):
            return True
        else:
            for i in range(0, length // 2):
                if (normalized[i] != normalized[-(i + 1)]):
                    return False
        return True
