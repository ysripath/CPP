/*
// Definition for a Node.
class Node {
public:
    int val;
    vector<Node*> children;

    Node() {}

    Node(int _val, vector<Node*> _children) {
        val = _val;
        children = _children;
    }
};
*/
class Solution {
public:
    vector<int> postorder(Node* root) {
        vector<int> rV;
        if (root == NULL)
            return rV;
        std::stack<Node*> st;
        std::stack<Node*> printStack;
        
        st.push(root);
        while (!st.empty())
        {
            Node* node = st.top();
            st.pop();
            auto itr = node->children.begin();
            while (itr != node->children.end())
            {
                st.push(*itr);
                itr++;
            }
            printStack.push(node);
        }
        
        
        while(!printStack.empty())
        {
            rV.push_back(printStack.top()->val);
            printStack.pop();
        }
        return rV;
    }
};
