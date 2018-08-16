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
    ListNode* removeElements(ListNode* head, int val) {
        
        if (head == NULL)
            return head;
        if (head->next == NULL) {
            if (head->val == val)
            {
                delete head;
                return NULL;
            }
            else
                return head;
        }
        
        
        while(head->val == val
             && head->next != NULL) {
            ListNode* temp = head;
            head = head->next;
            delete temp;
        }
        
        if (head->val == val) {
            delete head;
            return NULL;
        }
        ListNode* node = head;
        while (node->next != NULL) {
            if (node->next->val == val)
            {
                ListNode* temp = node->next;
                node->next = temp->next;
                temp = NULL;
                delete temp;
            }
            else
                node = node->next;
        }
        return head;
    }
};
