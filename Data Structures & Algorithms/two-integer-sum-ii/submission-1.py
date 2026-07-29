class Solution:
    def twoSum(self, num: List[int], target: int) -> List[int]:
        i=0
        n=len(num)
        j=n-1
        while(i<j):
            if num[i]+num[j]==target:
                return [i+1,j+1]
            elif num[i]+num[j]>target:
                j-=1
            else:
                i+=1
        
        