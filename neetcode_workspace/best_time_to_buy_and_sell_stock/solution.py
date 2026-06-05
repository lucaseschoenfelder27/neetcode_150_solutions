class Solution:
    # Time: O(?)
    # Space: O(?)
    def max_profit(self, prices: list[int]) -> int:
        # TODO: Implement max_profit
        possible_profit = []
        if len(prices) == 1:
            return 0
        for i in range(len(prices)):
            for j in range(i + 1, len(prices)):
                possible_profit.append(prices[j] - prices[i])
        #print('possible_profit: ', possible_profit)
        max_profit = max(possible_profit)
        if (max_profit > 0):
            return max_profit
        else:
            return 0
