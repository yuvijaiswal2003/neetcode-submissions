class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit=[]
        i,j=0,1
        for j in range(1,len(prices)):
            k=prices[j]-min(prices[i:j])
            if k>0:
                profit.append(k)
        if len(profit)!=0:
            return max(profit)
        return 0
