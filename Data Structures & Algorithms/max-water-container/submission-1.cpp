class Solution {
public:
    int maxArea(vector<int>& h) {
        int n=h.size();
        int i=0;
        int j=n-1;
        int maxarea=0;
        while(i<j)
        {
          int area=(j-i)*(min(h[i],h[j]));
          maxarea=max(maxarea,area);
         if(h[i]<h[j])
         {
            i++;
         }
         else
         {
            j--;
         }
        }
        return maxarea;
    }
};
