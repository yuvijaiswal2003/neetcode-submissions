class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxprofit=0
        bestbuy=prices[0]
        for p in prices:
            if p>bestbuy:
                maxprofit=max(maxprofit, p-bestbuy)
            else:
                bestbuy=p
        return maxprofit