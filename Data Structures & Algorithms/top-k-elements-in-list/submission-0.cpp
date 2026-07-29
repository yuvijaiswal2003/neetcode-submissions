class Solution {
public:
    vector<int> topKFrequent(vector<int>& num, int k) {
        int n=num.size();
        vector<int>ans;
       unordered_map<int,int>m;
        for(auto it:num)
        {
            m[it]++;
        }
        vector<pair<int,int>>v;
            for(auto it:m)
            {
                pair<int,int>p;
                p.first=it.second;
                p.second=it.first;
                v.push_back(p);
            }
        
        sort(v.begin(),v.end());
        int n1=v.size();
        while(k-- && n1>=0)
        {
            ans.push_back(v[n1-1].second);
            n1--;
        }
        return ans;
    }
};
