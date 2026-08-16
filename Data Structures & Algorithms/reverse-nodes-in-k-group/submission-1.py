# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def getreverse(self,temp:ListNode)->ListNode:
        prev=None
        curr=temp
        while curr:
            t=curr.next
            curr.next=prev
            prev=curr
            curr=t
        return prev
    def getkthnode(self,temp:ListNode, k:int)->ListNode:
        t=temp
        while k>1 and t:
            t=t.next
            k-=1
        return t
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        temp=head
        prevnode=None
        while temp:
            kthnode=self.getkthnode(temp,k)
            if kthnode==None:
                if prevnode:
                    prevnode.next=temp
                break
            nextnode=kthnode.next
            kthnode.next=None
            self.getreverse(temp)
            if temp==head:
                head=kthnode
            else:
                prevnode.next=kthnode
            prevnode=temp
            temp=nextnode

        return head
            
        
        