class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxprofit=0
        bestbuy=prices[0]
        for price in prices:
            if price> bestbuy:
                maxprofit=max(maxprofit, price-bestbuy)
            else:
                bestbuy=price
        return maxprofit

