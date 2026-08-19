class Solution:
    def findMedianSortedArrays(self, a: List[int], b: List[int]) -> float:
        n1=len(a)
        n2=len(b)
        n=n1+n2
        i,j=0,0
        idx2=n//2
        idx1=idx2-1
        cnt=0
        id1el=-1
        id2el=-1
        while (i<n1 and j<n2):
            if a[i]<b[j]:
                if cnt==idx1:
                    id1el=a[i]
                if cnt==idx2:
                    id2el=a[i]
                i+=1
                cnt+=1
            else:
                if cnt==idx1:
                    id1el=b[j]
                if cnt==idx2:
                    id2el=b[j]
                j+=1
                cnt+=1
        while i<n1:
            
            if cnt==idx1:
                id1el=a[i]
            if cnt==idx2:
                id2el=a[i]
            i+=1
            cnt+=1
        while j<n2:
            if cnt==idx1:
                id1el=b[j]
            if cnt==idx2:
                id2el=b[j]
            j+=1
            cnt+=1
        if n%2==1:
            return id2el
        return (id1el+id2el)/2
        