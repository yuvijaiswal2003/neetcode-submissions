# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        arr=[]
        for lst in lists:
            while lst:
                arr.append(lst.val)
                lst=lst.next
        arr.sort()
        dummy=ListNode(-1)
        temp=dummy
        for num in arr:
            newnode=ListNode(num)
            temp.next=newnode
            temp=temp.next
        return dummy.next
        