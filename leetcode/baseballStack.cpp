class Solution {
public:
    int calPoints(vector<string>& ops) {
        std::stack<int> st;
        
        
        auto itr = ops.begin();
        while (itr != ops.end()) {
            string s = *itr;
            if (std::isdigit(s[0]) || s[0] =='-') {
                int val = atoi(s.c_str());
                st.push(val);
            } else if (s[0] == 'C') {
                if (!st.empty()) {
                    st.pop();
                } else {
                    // invalid i/p
                    return -1;
                }
            } else if (s[0] == 'D') {
                int temp = st.top();
                st.push(temp*2);                
            } else if (s[0] == '+') {
                int val1 = st.top();
                st.pop();
                if (st.empty()) {
                    st.push(val1);
                    st.push(val1);
                } else {
                    int val2 = st.top();
                    st.push(val1);
                    st.push(val1+val2);
                }
            } else {
                // invalid
                return -1;
            }
            itr++;
        }
        
        
        int sum = 0;
        while (!st.empty()) {
            sum += st.top();
            st.pop();
        }
        return sum;
        
    }
};
