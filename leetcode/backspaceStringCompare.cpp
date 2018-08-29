class Solution {
public:
    bool backspaceCompare(string S, string T) {
        stack<char> st1;
        stack<char> st2;
        
        int l1 = S.length();
        
        for (int i = 0; i < l1; i++) {
            if (S[i] == '#') {
                if (st1.empty())
                    continue;
                st1.pop();
            } else {
                st1.push(S[i]);
            }
        }
        
        l1 = T.length();
        
        for (int i = 0; i < l1; i++) {
            if (T[i] == '#') {
                if (st2.empty())
                    continue;
                st2.pop();
            } else {
                st2.push(T[i]);
            }
        }
        
        if (st1.size() != st2.size()) {
            return false;
        }
        
        while (st1.size()) {
            if (st1.top() == st2.top()) {
                st1.pop();
                st2.pop();
                continue;
            }
            else
                return false;
        }
        return true;
    }
};
