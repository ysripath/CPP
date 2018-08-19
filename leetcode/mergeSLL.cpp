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
    ListNode* mergeTwoLists(ListNode* l1, ListNode* l2) {
        if (l1 == NULL 
           && l2 == NULL)
            return NULL;
        
        if (l1 == NULL)
            return l2;
        if (l2 == NULL)
            return l1;
        
        ListNode* head = NULL;
        ListNode* node = NULL;
        
        while (l1 && l2)
        {
            if (l1->val <= l2->val)
            {
                if (head == NULL) {
                    head = l1;
                    l1 = l1->next;
                    node = head;
                }
                else {
                    node->next = l1;
                    node = node->next;
                    l1 = l1->next;
                }
            }
            else
            {
                if (head == NULL) {
                    head = l2;
                    l2 = l2->next;
                    node = head;
                }
                else {
                    node->next = l2;
                    node = node->next;
                    l2 = l2->next;
                }
            }
        }
        
        if (l1 == NULL 
           && l2 == NULL) {
            node->next = NULL;
            return head;
        }
        
        if (l1 == NULL) {
            node->next = l2;
        }
        else
        {
            node->next = l1;
        }
        return head;
    }
};
