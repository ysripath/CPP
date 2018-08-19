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
    int carry;
    int rem;
    bool carryFlag;
    void getCarry(int val) {
        carry = val/10;
        rem = val%10;
        carryFlag = true;
    }
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        ListNode* head = NULL;
        ListNode* node = NULL;
        
        while (l1 && l2)
        {
            int sum = l1->val + l2->val;
            if (carryFlag) {
                sum += carry;
                carryFlag = false;
            }
            if (sum > 9)
            {
                getCarry(sum);
                if (head == NULL)
                {
                    head = new ListNode(rem);
                    node = head;
                }
                else
                {
                    node->next = new ListNode(rem);
                    node = node->next;
                }
            }
            else
            {
                if (head == NULL)
                {
                    head = new ListNode(sum);
                    node = head;
                }
                else
                {
                    node->next = new ListNode(sum);
                    node = node->next;
                }
            }
            l1 = l1->next;
            l2 = l2->next;
        }
        
        if (l1 == NULL && l2 == NULL) {
            
        if (carryFlag) {
            node->next = new ListNode(carry);
        }
            return head;
            
        }
        if (l1 == NULL) {
            while (l2) {
                int sum = l2->val;
                if (carryFlag) {
                    sum += carry;
                    carryFlag = false;                    
                }
                
                if (sum > 9) {
                    getCarry(sum);
                    
                    node->next = new ListNode(rem);
                    node = node->next;
                }
                else {
                    node->next = new ListNode(sum);
                    node = node->next;
                }
                l2 = l2->next;
            }
        }
        else if (l2 == NULL) {
            while (l1) {
                int sum = l1->val;
                if (carryFlag) {
                    sum += carry;
                    carryFlag = false;                    
                }
                
                if (sum > 9) {
                    getCarry(sum);
                    
                    node->next = new ListNode(rem);
                    node = node->next;
                }
                else {
                    node->next = new ListNode(sum);
                    node = node->next;
                }
                l1 = l1->next;
            }
        }
        
        if (carryFlag) 
        {
            node->next  = new ListNode(carry);
        }
        
        return head;
    }
};
