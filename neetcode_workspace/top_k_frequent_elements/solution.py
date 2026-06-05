class Solution:
    # Time: O(?)
    # Space: O(?)
    def top_k_frequent(self, nums: list[int], k: int) -> list[int]:
        # TODO: Implement top_k_frequent
        frequency_counter = {}
        for num in nums:
            if num not in frequency_counter:
                frequency_counter[num] = 1
            else:
                frequency_counter[num] = frequency_counter[num] + 1
        #print('frequency_counter: ', frequency_counter)
        res = [(key, val) for key,val in frequency_counter.items()]
        #print('res: ', res)
        return [x[0] for x in res[0:k]]
