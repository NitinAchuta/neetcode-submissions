# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return

        slow = head
        fast = head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        secondHalf = slow.next
        slow.next = None

        # Reverse everything onwards from secondHalf
        def reverseList(head: Optional[ListNode]) -> ListNode:
            # Pass the half to reverse into this
            curr = head
            prev = None

            while curr:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp

            return prev


        secondPointer = reverseList(secondHalf)
        firstPointer = head

        while secondPointer:
            temp1 = firstPointer.next
            temp2 = secondPointer.next

            firstPointer.next = secondPointer
            secondPointer.next = temp1

            firstPointer = temp1
            secondPointer = temp2



         
        

        