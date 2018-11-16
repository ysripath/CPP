class Solution {
public:
    bool canConstruct(string ransomNote, string magazine) {
        if (ransomNote.length() > magazine.length())
            return false;
        
        std::map<char,int> m;
        for (int i = 0; i < magazine.length(); i++)
        {
            auto itr = m.find(magazine[i]);
            if (itr == m.end())
            {
                m.insert(make_pair(magazine[i], 1));
            }
            else
            {
                itr->second++;
            }
        }
        
        for (int i = 0; i < ransomNote.length(); i++)
        {
            auto itr = m.find(ransomNote[i]);
            if (itr == m.end())
            {
                return false;
            }
            if (itr->second == 0)
                return false;
            else
                itr->second--;
        }
        return true;
    }
};
