# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        slow = head
        if head.next:
            fast = head.next

            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next

            prev = None
            curr = slow.next
            slow.next = None

            '''
            def printList(node):
                while node is not None:
                    print(f"{node.val}", end="")
                    if node.next is not None:
                        print("->", end="")
                    node = node.next
            '''

            while curr:
                nextNode = curr.next
                curr.next = prev
                prev = curr
                curr = nextNode

            curr1 = head
            curr2 = prev

            while curr1 and curr2:
                temp1 = curr1.next
                curr1.next = curr2
                curr1 = temp1
                temp2 = curr2.next
                curr2.next = temp1
                curr2 = temp2


        
