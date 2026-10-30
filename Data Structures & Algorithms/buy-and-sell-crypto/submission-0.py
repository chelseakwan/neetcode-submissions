class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0
        right = 1
        max_profit = 0

        while right in range(len(prices)):
            if prices[right] > prices[left]:
                profit = prices[right] - prices[left]
                if profit > max_profit:
                    max_profit = profit
                right += 1
            else:
                left = right
                right += 1

        return max_profit