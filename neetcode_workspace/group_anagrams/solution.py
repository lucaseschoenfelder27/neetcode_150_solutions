class Solution:
    # Time: O(?)
    # Space: O(?)
    '''
    Input: strs = ["eat","tea","tan","ate","nat","bat"]

    Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
    '''
    def group_anagrams(self, strs: list[str]) -> list[list[str]]:
        # TODO: Implement group_anagrams
        out = []
        res = {}
        for str in strs:
            #set_str = set(str)
            #print('set(str): ', set_str)
            key = "".join(sorted(set(str)))
            #print('item: ', item, 'key: ', key)
            if key not in res:
                res[key] = []
            res[key].append(str)
        #print('res: ', res)
        res_output = sorted([sorted(res[val]) for val in res], key=len)
        print('res_output: ', res_output)
        return res_output
