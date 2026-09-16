# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        '''
        def printList(node):
            while node is not None:
                print(f"{node.val}", end="")
                if node.next is not None:
                    print("->", end="")
                node = node.next
        '''

        curr = head
        leng = 0
        while curr != None:
            curr = curr.next
            leng += 1   

        if leng == n:
            head = head.next
        else:
            curr = head
            for i in range(leng - n - 1):
                curr = curr.next
            curr.next = curr.next.next

        return head
        
        
            


        
        