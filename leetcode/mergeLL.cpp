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
    // Method to Split the linked list
    void splitList(ListNode* head, ListNode** a, ListNode** b) {
        if (head == NULL)
        {
            return;
        }
        // use hare and tortise method;
        
        ListNode* h = head;
        ListNode* t = head;
        ListNode* tail = NULL;
        while (t->next && t->next->next) {
            t = t->next->next;
            tail = h;
            h = h->next;
        }
        if (t->next) {
            tail = h;
            h = h->next;
        }
        tail->next = NULL;
        *a = head;
        *b = h;
    }
    
    ListNode* merge(ListNode* a, ListNode* b) {
       
        
        if (!a && !b)
            return NULL;
        if (!a && b)
            return b;
        if (a && !b)
            return a;
         ListNode* head = NULL;
        if (a->val <= b->val) {
            head = a;
            a->next = merge(a->next, b);
        } else {
            head = b;
            b->next = merge(a, b->next);
        }
        return head;
    }
    
    ListNode* sortList(ListNode* head) {
        
        ListNode* a = NULL;
        ListNode* b = NULL;
        if (head == NULL
           || head->next == NULL)
            return head;
        
        ListNode* head2 = NULL;
        
        splitList(head, &a, &b);
        a = sortList(a);
        b = sortList(b);
        
        head2 = merge(a, b);
        
        return head2;
    }
};
