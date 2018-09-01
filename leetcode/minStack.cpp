class MinStack {
private:
    std::stack<int> st;
    std::stack<int> mSt;
public:
    /** initialize your data structure here. */
    MinStack() {
        
    }
    
    void push(int x) {
        st.push(x);
        if (mSt.empty()
           || x <= mSt.top()) {
            mSt.push(x);
        } 
    }
    
    void pop() {
        int temp = st.top();
        st.pop();
        if (temp == mSt.top()) {
            mSt.pop();
        }
    }
    
    int top() {
        if (st.empty())
            return -1;
        return st.top();
    }
    
    int getMin() {
        if (mSt.empty())
            return -1;
        return mSt.top();
    }
};

/**
 * Your MinStack object will be instantiated and called as such:
 * MinStack obj = new MinStack();
 * obj.push(x);
 * obj.pop();
 * int param_3 = obj.top();
 * int param_4 = obj.getMin();
 */
