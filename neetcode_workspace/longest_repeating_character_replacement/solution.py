class Solution:
    # Time: O(?)
    # Space: O(?)
    def character_replacement(self, s: str, k: int) -> int:
        # TODO: Implement character_replacement
        #print(s)
        count = {}
        res = 0
        
        l = 0
        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)
            
            while (r - l + 1) - max(count.values()) > k:
                count[s[l]] -= 1
                l += 1
            
            #print('\tcount: ', count)
            #print('\tr: ', r, ' l :', l)
            res = max(res, r - l + 1)
        return res
