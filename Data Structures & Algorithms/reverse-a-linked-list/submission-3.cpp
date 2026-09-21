/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */

class Solution {
public:
    ListNode* reverseList(ListNode* head) {
        // Base case: If head is null or only one node, return head
        if (head == nullptr || head->next == nullptr) {
            return head;
        }
        
        // Recursively reverse the rest of the list
        ListNode* newHead = reverseList(head->next);
        
        // Make the next node point to the current node
        head->next->next = head;
        
        // Break the original next link
        head->next = nullptr;
        
        return newHead; // Return the new head of the reversed list
    }
};
