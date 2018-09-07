class Solution {
public:
    string toLowerCase(string str) {
        int l = str.length();
        
        for (int i = 0; i < l; i++) {
            
            if ((int)str[i] >= (int)'a'
               || ((int)str[i] < (int)'A' || (int)str[i] > (int)'Z')) {
                continue;
            } else {
                str[i] = (int)str[i] + 32;
            }
        }
        return str;
        
    }
};
