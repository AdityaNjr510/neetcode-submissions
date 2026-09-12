# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        curr1 = list1
        curr2 = list2
        curr = ListNode()
        head = curr
        if not curr1:
            return curr2
        if not curr2:
            return curr1

        while curr1 and curr2:
            if curr1.val < curr2.val:
                curr.val = curr1.val
                if not curr1.next:
                    curr.next = curr2
                    return head
                curr1 = curr1.next
            else:
                curr.val = curr2.val
                if not curr2.next:
                    curr.next = curr1
                    return head
                curr2 = curr2.next
            curr.next = ListNode()
            curr = curr.next

        curr.next = None

        return head

