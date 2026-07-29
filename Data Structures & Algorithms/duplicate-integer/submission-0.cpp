class Solution {
public:
    bool hasDuplicate(vector<int>& num) {
      map<int ,int>m;
      for(int i=0; i<num.size(); i++ )
      {
        m[num[i]]++;
      }
      for(auto i: m)
      {
        if(i.second>1)
        {
            return 1;
        }
      }
      return 0;
    }
};
