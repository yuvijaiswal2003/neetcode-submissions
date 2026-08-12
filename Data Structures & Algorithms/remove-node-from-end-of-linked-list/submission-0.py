class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        dummynode=ListNode(-1)
        slow=dummynode
        fast=dummynode
        dummynode.next=head

        for _ in range(n+1):
            fast=fast.next
        while fast is not None:
            fast=fast.next
            slow=slow.next

        slow.next=slow.next.next

        return dummynode.next

        
            
            
        

        
           

        
        