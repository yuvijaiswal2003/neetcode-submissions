# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(-1)
        curr = dummy
        carry = 0
        
        # Change 'and' to 'or' so the loop runs until BOTH lists are exhausted
        while l1 or l2 or carry:
            # Reset current_sum to 0 for each new digit position
            current_sum = carry
            
            if l1:
                current_sum += l1.val
                l1 = l1.next
            if l2:
                current_sum += l2.val
                l2 = l2.next
                
            # Calculate the new carry and the digit to store
            carry = current_sum // 10
            curr.next = ListNode(current_sum % 10)
            
            # CRITICAL: Advance the result list pointer forward
            curr = curr.next
            
        return dummy.next