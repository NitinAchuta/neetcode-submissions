# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        def recursion(prev, curr: Optional[ListNode]):
            print(prev, curr)
          
            if not curr.next:
                curr.next = prev
                return curr
            else:
                temp = curr
                temp2 = prev
                curr = curr.next
                prev = temp

                temp.next = temp2
                return recursion(prev, curr)

            
        
        prev = None
        curr = head
        if not head:
            return head

        return recursion(prev, curr)
        