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
    
    ListNode* removeNthFromEnd(ListNode* head, int n) {
       int count = 0;
        ListNode* node = head;
        
        while (node != NULL)
        {
            count++;
            node = node->next;
            
        }
        
        int k = count - n;
      // k--;       
        if (k == 0)
        {
            if (head->next)
            {
                ListNode* temp = head;
                head = head->next;
                delete temp;
                return head;
            }
            else
                return NULL;
        }
                 
        count = 0;
        node = head;
        ListNode* prev = head;
        
        while (count != k
              && node)
        {
            prev = node;
            node = node->next;
            count++;
        }
        
        if (count == k)
        {
            if (node->next)
                prev->next = node->next;
            else
                prev->next = NULL;
            
            delete node;
        }
        return head;
    }
};
