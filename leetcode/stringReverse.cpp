class Solution {
public:
    string reverseString(string s) {
        char* str = new char[s.length()+1];
        int k = 0;
        for (int i = s.length()-1; i >=0; i--)
        {
            str[k++] = s[i];
        }
        str[k] = '\0';
        return string(str);
    }
};
