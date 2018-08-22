class Solution {
public:
    char findTheDifference(string s, string t) {
        char val1 = 0;
        
        int sS = s.length();
        
        for (int i = 0; i < sS; i++)
        {
            val1 ^= s[i];
        }
        
        int tS = t.length();
        
        for (int i = 0; i <tS; i++)
        {
            val1 ^= t[i];
        }
        
        return (val1);
    }
};
