/*
// Definition for a Node.
class Node {
public:
    int val = NULL;
    Node* prev = NULL;
    Node* next = NULL;
    Node* child = NULL;

    Node() {}

    Node(int _val, Node* _prev, Node* _next, Node* _child) {
        val = _val;
        prev = _prev;
        next = _next;
        child = _child;
    }
};
*/
class Solution {
public:
    Node* util(Node* head) {
        Node* node = head;
        
        Node* temp = node->next;
        
        node->next = node->child;
        node->child->prev = node;
        node->child = NULL;
        //node = node->next;
        while(node->next) {
            node = node->next;
            if (node->child) {
                util(node);                
            }
        }
        node->next = temp;
        if (temp)
            temp->prev = node;
        return head;
    }
    
    Node* flatten(Node* head) {
        Node* node = head;
        
        while (node) {
            if (node->child)
                node = util(node);
            node = node->next;
        }
        return head;
    }
};
