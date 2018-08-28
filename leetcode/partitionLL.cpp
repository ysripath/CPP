/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    ListNode* insertNode(ListNode* head, int val) {
        if (head == NULL) {
            head = new ListNode(val);
            return head;
        }
        
        ListNode* node = head;
        while(node->next) {
            node = node->next;
        }
        node->next = new ListNode(val);
        return head;
        
    }
    ListNode* joinList(ListNode* node1, ListNode* node2) {
        if (node1 == NULL)
            return node2;
        if (node2 == NULL)
            return node1;
        ListNode* node = node1;
        
        while (node->next) {
            node = node->next;
        }
        node->next = node2;
        return node1;
    }
    ListNode* partition(ListNode* head, int x) {
        ListNode* nodeL = NULL;
        ListNode* nodeE = NULL;
        ListNode* nodeG = NULL;
        if (head == NULL)
            return NULL;
        if (head->next == NULL)
            return head;
        ListNode* node= head;
        
        while (node) {
            if (node->val < x) {
                nodeL = insertNode(nodeL, node->val);
            } /*else if (node->val == x) {
                nodeE = insertNode(nodeE, node->val);
            }*/ else {
                nodeG = insertNode(nodeG, node->val);
            }
            node =  node->next;
            
        }
        
        head = joinList(nodeL, nodeE);
        head = joinList(head, nodeG);
        
        return head;        
        
    }
};
