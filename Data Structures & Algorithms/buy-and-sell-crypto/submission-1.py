class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        min_price = prices[0]
        for sell in prices:
            res = max(res,sell - min_price)
            min_price = min(sell,min_price)
        return res 
        