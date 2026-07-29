class Solution {
public:
    int trap(vector<int>& arr) {
        int n=arr.size();
        int l=0;
        int l_max=0;
        int r=n-1;
        int r_max=0;
        int ans=0;
         while(l<r){
            if(arr[l]<arr[r]){
              if(arr[l]>l_max){
                l_max=arr[l];
              }else {
            ans+=(l_max-arr[l]);
              }
            l++;
            }else {

            if(arr[r]>r_max){
                r_max=arr[r];
              }else {
            ans+=r_max-arr[r];
              }
            r--;
            }
         }
         return ans;
    }
};
