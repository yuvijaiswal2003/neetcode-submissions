class Solution {
public:
    bool isPalindrome(string s) 
    {
        string t="";
        for(auto i:s)
        {
            if(isalnum(i))
            {
                t.push_back(tolower(i));
            }
        }
        for(int j=0; j<t.size(); j++)
        {
            if(t[j]!=t[t.size()-j-1])
            {
                return 0;
            }
        }
        return 1;
    }
};
