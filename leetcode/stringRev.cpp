class Solution {
public:
    string reverseString(string s) {
        
        if (s.empty())
            return s;
        int l = s.length();
        char str[l+1];
        int k = 0;
        for (int i = l-1; i >=0; i--) {
            str[k++] = s[i];
        }
        str[k] = '\0';
        return string(str);
    }
};
