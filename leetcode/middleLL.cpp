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
    ListNode* middleNode(ListNode* head) {
        if (head == NULL)
            return head;
        if (head->next == NULL)
            return head;
        if (head->next->next == NULL)
            return head->next;
        
        ListNode* h = head->next;
        ListNode* t = head;
        
        while (h != NULL 
              && h->next != NULL) {
            h = h->next->next;
            t = t->next;
        }
        
        if (h == NULL)
            return t;
        else if (h->next == NULL) {
            return t->next;
        }
    }
};
