/**
 *  * Definition for singly-linked list.
 *   * struct ListNode {
 *    *     int val;
 *     *     ListNode *next;
 *      *     ListNode(int x) : val(x), next(NULL) {}
 *       * };
 *        */
class Solution {
public:
    bool hasCycle(ListNode *head) {
        ListNode* h = head;
        ListNode* t = head;
        
        if (head == NULL)
            return false;
        
        if (head->next == NULL)
            return false;
        
        h = head->next;
        if (h->next == NULL)
            return false;
        while (h->next->next != NULL)
        {
            if (h == t)
                return true;
            h = h->next->next;
            if (h->next == NULL)
                return false;
            t = t->next;
        }
        return false;
    }
};
