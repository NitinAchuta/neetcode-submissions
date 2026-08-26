class MyLinkedList:
    class ListNode:
        def __init__(self, val=0, next=None):
            self.val = val
            self.next = next

    def __init__(self):
        self.headPtr = self.ListNode()
        self.size = 0

    def get(self, index: int) -> int:

        if index < 0 or index >= self.size:
            return -1
        
        curr = self.headPtr.next

        for _ in range(index):
            curr = curr.next
        return curr.val

    def addAtHead(self, val: int) -> None:

        # newNode = ListNode(val)

        # prevHead = self.headPtr.next
        # self.headPtr.next = newNode
        # newNode.next = prevHead
        # self.size += 1
        self.addAtIndex(0, val)

    def addAtTail(self, val: int) -> None:
        self.addAtIndex(self.size, val)

    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.size or index < 0:
            return

        prev = self.headPtr

        for _ in range(index):
            prev = prev.next
        
        newNode = self.ListNode(val)
        newNode.next = prev.next
        prev.next = newNode

        self.size += 1

        # 2
        # [] -> 0 -> 1 -> 2 -> 3

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.size:
            return
        
        prev = self.headPtr

        for _ in range(index):
            prev = prev.next

        prev.next = prev.next.next

        self.size -= 1



# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)