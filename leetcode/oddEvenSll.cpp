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
    ListNode* oddEvenList(ListNode* head) {
        
        ListNode* e = head;
        ListNode* o = head;
        
        int count = 0;
        if (head == NULL
           || head->next == NULL 
           || head->next->next == NULL)
            return head;
        
        count = 1;
        e = head->next;
        
        ListNode* eH = e;
        
        while (e->next)
        {            
                o->next = e->next;
                if (o->next->next)
                    e->next = o->next->next;
                else
                {
                    e->next = NULL;
                    o = o->next;
                     o->next = eH;
                    return head;
                }
                o = o->next;
                o->next = eH;
                e = e->next;            
        }
        e->next = NULL;
        return head;
        
    }
};
