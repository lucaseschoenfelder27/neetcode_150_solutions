class Solution:
    # Time: O(?)
    # Space: O(?)
    def length_of_longest_substring(self, s: str) -> int:
        # TODO: Implement length_of_longest_substring
        print('got s: ', s)
        charSet = set()
        l = 0
        res = 0
        
        for r in range(len(s)):
            print('testing index ', r, 'current char: ', s[r])
            while s[r] in charSet:
                charSet.remove(s[l])
                l +=  1
            charSet.add(s[r])
            print('charSet:', charSet)
            res = max(res, r - l + 1)
        return res
        """ print('got s: ', s)
        #print('len(s): ', len(s))
        longest = 1
        if not s:
            return 0
        s_length = len(s) 
        if s_length == 1:
            return 1
        else:
            for i in range(1, s_length):
                possible_max_substring_length = s_length - i
                print('\ttesting index ', i, ' current char:', s[i])
                print('\t\tpossible_max_substring_length: ', possible_max_substring_length)
                
                if (longest > possible_max_substring_length):
                    break
                
                length = 1
                
                substring_set = set(s[i])
                #print('\tsubstring_set: ', substring_set)
                if (s[i-1] not in substring_set):
                    length = 1
                    substring_set.add(s[i-1])
                    
                    print('\t\t\tnow evaluating next char...')
                    while (s[i+length] not in substring_set and longest < possible_max_substring_length and i + length < s_length):
                        print('\t\t\t next char: ', s[i+length])
                        substring_set.add(s[i+length])
                        print('\t\t\tsubstring_set: ', substring_set)
                        length += 1
                    print('\t\tlength found: ', length + 1)
                    
                    longest = max(longest, length + 1)
        return longest """
 