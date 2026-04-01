class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        max_profit = 0
        for i in range(1, len(prices)):
            sell_price = prices[i]
            buy_price = min(prices[:i])
            profit = sell_price - buy_price
            if profit > max_profit:
                max_profit = profit
        return max_profit


        