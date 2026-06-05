from itertools import combinations

class Solution:
    # Time: O(?)
    # Space: O(?)
    def three_sum(self, nums: list[int]) -> list[list[int]]:
        # TODO: Implement three_sum
        triplets = list(combinations(nums, 3))
        #print('triplets: ', triplets)
        zero_sum_sets = set()
        #zero_sum = []
        for triplet in triplets:
            if (triplet[0] + triplet[1] + triplet[2]) == 0:
                zero_sum_sets.add(tuple(sorted(triplet)))
                    #zero_sum_sets.add(frozenset(set(triplet)))
                #zero_sum.append(triplet)
        #print('zero_sum_sets: ', zero_sum_sets)
        #print('set: ', set(zero_sum))
        return [list(t) for t in zero_sum_sets]
