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
    bool oddFlag;
    ListNode* utilHead;
    ListNode* utilReverse(ListNode* node) {
        if (node->next == NULL) {
            utilHead = node;
            return node;
            
        }
        
        
        ListNode* temp = utilReverse(node->next);
        
        temp->next = node;
        return node;
    }
    
    ListNode* findMid(ListNode* head) {
        ListNode* h = head->next;
        ListNode* t = head;
        
        while (h->next && h->next->next)
        {
            h = h->next->next;
            t = t->next;
        }
        if (h->next == NULL)
            oddFlag = false;
        else {
            oddFlag = true;
            t = t->next;
        }
        
        return t;
              
    }
    bool isPalindrome(ListNode* head) {
        if (head == NULL)
            return true;
        
        if (head->next == NULL)
            return true;
        
        if (head->next->next == NULL)
        {
            if (head->val == head->next->val)
                return true;
            else
                return false;
        }
        
        
        ListNode* midHead = findMid(head);
        
        if (oddFlag)
        {
            ListNode* tail = utilReverse(midHead->next);
            ListNode* temp1 = new ListNode(midHead->val);
            temp1->next = NULL;
            tail->next = temp1;
            
            ListNode* h = head;
            tail = utilHead;
            midHead->next = NULL;
            while (tail
                  && h )
            {
                if (tail->val != h->val)
                    return false;
                tail = tail->next;
                h = h->next;
            }
            
            if (tail == NULL && h == NULL)
            {
                return true;
            }
            return false;
            
        }
        else
        {
            ListNode* tail = utilReverse(midHead->next);
            tail->next = NULL;
            
            ListNode* h = head;
            tail = utilHead;
            midHead->next = NULL;
            while (tail
                  && h )
            {
                if (tail->val != h->val)
                    return false;
                tail = tail->next;
                h = h->next;
            }
            
            if (tail == NULL && h == NULL)
            {
                return true;
            }
            return false;
            
        }
    }
};
