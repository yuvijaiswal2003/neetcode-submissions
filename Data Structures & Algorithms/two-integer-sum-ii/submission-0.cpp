class Solution {
public:
    vector<int> twoSum(vector<int>& num, int t) {
       int i=0; 
       int j=num.size()-1;
       int sum=num[i]+num[j];
       while(i<j)
       {
        if(sum==t)
        {
            return {i+1,j+1};
        }
        else if(sum>t)
        {
            sum-=num[j];
            j--;
            sum+=num[j];
        }
        else
        {
            sum-=num[i];
            i++;
            sum+=num[i];
        }
       }
       return {i+1,j+1};
    }
};
