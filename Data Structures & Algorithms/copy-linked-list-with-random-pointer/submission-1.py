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
         
        temp=head
        d={}
        while temp:
            newnode=Node(temp.val)
            d[temp]=newnode
            temp=temp.next
        temp=head
        while temp:
            copynode=d[temp]
            if temp.next:
                copynode.next=d[temp.next]
            if temp.random:
                copynode.random=d[temp.random]
            else:
                copynode.random=None
            temp=temp.next
        return d[head] if head!=None else None
        

        
        