"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':

        head_copy = curr_copy = Node(0)
        curr = head
        hashmap = {}
        while curr != None:            
            curr_copy.next = Node(curr.val)
            hashmap[curr] = curr_copy.next
            curr_copy = curr_copy.next
            curr = curr.next
        curr_copy.next = None

        curr_copy = head_copy.next
        curr = head
        while curr != None:           
            curr_copy.random = hashmap[curr.random] if curr.random else None
            curr_copy = curr_copy.next
            curr = curr.next

        return head_copy.next

        
