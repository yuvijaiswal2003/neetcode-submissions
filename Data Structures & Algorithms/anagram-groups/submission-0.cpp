class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& str) 
    {
       vector<vector<string>>s;
       map<string,vector<string>>m;
       for(auto it:str)
       {
        string temp=it;
        sort(it.begin(),it.end());
        m[it].push_back(temp);
       }
        for(auto it: m)
       {
        s.push_back(it.second);
       }
       
       return s;
    }
};
