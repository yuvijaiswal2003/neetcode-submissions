class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit=[]
        for i in range(len(prices)-1):
            k=0
            for j in range(i+1, len(prices)):
                k=prices[j]-prices[i]
                if k>0:
                    profit.append(k)
        if len(profit)!=0:
            return max(profit)
        return 0    
