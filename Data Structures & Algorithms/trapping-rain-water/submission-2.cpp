class Solution {
public:
    int trap(vector<int>& arr) {
        int n=arr.size();
        int ans=0;
        stack<int>st;
        for(int i=0;i<n;i++){
         while(!st.empty()&&arr[st.top()]<arr[i]){
            int t=arr[st.top()];
            st.pop();
            if(st.empty())break;
            int j=st.top();
            int l=min(arr[st.top()],arr[i]);
            ans+=(l-t)*(i-j-1);
            //st.pop();
            }
            st.push(i);
         }
         return ans;
    }
};
