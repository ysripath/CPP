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
    ListNode* utilHead;
    ListNode* util(ListNode* node) {
        if (node->next == NULL) {
            utilHead = node;
            return node;
        }
        ListNode* temp = util(node->next);
        temp->next = node;
        return node;
    }
    ListNode* reverseList(ListNode* head) {
        if (head == NULL 
           || head->next == NULL)
            return head;
        ListNode* node = util(head);
        node->next = NULL;
        head = utilHead;
        return head;
    }
};
