class MyQueue {
private:
    std::stack<int> st1;
    std::stack<int> st2;
    bool flag; // flag to denote where the elements are - false (st1), true (st2)
    int peekVal;
    void util() {
        if (flag) {
            while (!st2.empty()) {
                int temp = st2.top();
                st2.pop();
                st1.push(temp);
            }
        } else {
            while (!st1.empty()) {
                int temp = st1.top();
                st1.pop();
                st2.push(temp);
            }
        }
    }
    bool firstFlag;
public:
    /** Initialize your data structure here. */
    MyQueue() {
        flag = false;
        firstFlag = true;
    }
    
    /** Push element x to the back of queue. */
    void push(int x) {
        if (!flag)
        {
            st1.push(x);
        }
        else
        {
            util();
            flag = !flag;
            st1.push(x);
        }
        if (firstFlag) {
            peekVal = st1.top();
            firstFlag = !firstFlag;
        }
    }
    
    /** Removes the element from in front of queue and returns that element. */
    int pop() {
        if (!flag) {        
            util();
            flag = !flag;
        }
        int temp = st2.top();
        st2.pop();
        if (!st2.empty())
            peekVal = st2.top();
        
        if (st1.empty() && st2.empty())
            firstFlag = !firstFlag;
        
        return temp;
    }
    
    /** Get the front element. */
    int peek() {
        if (!st1.empty() || !st2.empty()) {
            return peekVal;
        } else 
            return -1;
    }
    
    /** Returns whether the queue is empty. */
    bool empty() {
        if (st1.empty()
           && st2.empty())
            return true;
        else
            return false;
    }
};

/**
 * Your MyQueue object will be instantiated and called as such:
 * MyQueue obj = new MyQueue();
 * obj.push(x);
 * int param_2 = obj.pop();
 * int param_3 = obj.peek();
 * bool param_4 = obj.empty();
 */
