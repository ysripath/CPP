class Solution {
public:
    bool isValid(string s) {
        int l = s.length();
        std::stack<char> st;
        for (int i = 0; i < l; i++)
        {
            char c = s[i];
            switch(c)
            {
                case '(': {
                    st.push(c);
                    
                } break;
                case ')': {
                    if (st.empty())
                        return false;
                    char top = st.top();
                    if (top == '(')
                        st.pop();
                    else
                        return false;
                } break;
                case '{': {
                    st.push(c);
                } break;
                case '}': {
                    if (st.empty())
                        return false;
                     char top = st.top();
                    if (top == '{')
                        st.pop();
                    else
                        return false;
                } break;
                case '[': {
                    st.push(c);
                } break;
                case ']': {
                    if (st.empty())
                        return false;
                     char top = st.top();
                    if (top == '[')
                        st.pop();
                    else
                        return false;
                } break;
                default: return false;
            }
        }
        if (st.empty())
            return true;
        else
            return false;
    }
};
