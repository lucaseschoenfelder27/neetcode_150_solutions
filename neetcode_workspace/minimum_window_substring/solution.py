from collections import Counter

def contains_all(string, substring):
    c1, c2 = Counter(string), Counter(substring)
    return all(c1[x] >= c2[x] for x in c2)

class Solution:
    # Time: O(?)
    # Space: O(?)
    def min_window(self, s: str, t: str) -> str:
        # TODO: Implement min_window
        len_s = len(s)
        len_t = len(t)
        #print('s: ', s, ' len_s: ', len_s)
        #print('t: ', t, ' len_s: ', len_t)
        
        if  len_t > len_s:
            return ""
        
        t_count = {}
        for r in range(len_t):
            t_count[t[r]] = 1 + t_count.get(t[r], 0)
        #print('t_count: ', t_count)
        
        max_window_to_search = len_s - len_t
        #print('\tmax_window_to_search: ', max_window_to_search)
        
        count = {}
        res = 0
        substrings = []
        min_l = len_s
        for r in range(len_s):
            count[s[r]] = 1 + count.get(s[r], 0)
            #print('\t testing from index ', r, ' current char: ', s[r])
            
            total_needed = t_count.copy()
            l = r
            len_subs = 0
            #print('sum(total_needed.values(): ', sum(total_needed.values()))
            subs = ""
            while sum(total_needed.values()) > 0 and (r + len_subs) < len_s:
                #print('\t\tadding character ', s[l])
                subs += s[l + len_subs]
                #print('subs so far: ', subs)
                if s[len_subs + r] in total_needed.keys():
                    total_needed[s[len_subs + r ]] -= 1
                    if total_needed[s[len_subs + r]] == 0:
                        del total_needed[s[len_subs + r]]
                #print('total_needed: ', total_needed)
                len_subs += 1
                #print('r + l + 1:', r + l + 1)
            if (contains_all(subs, t)):
                substrings.append((subs, len_subs))
                #min_l = min(min_l, len_subs)
                
        #print('substrings: ', substrings)
        if not substrings:
            return ""
        else:
            smallest = min(substrings, key=lambda x: x[1])
            return smallest[0]
