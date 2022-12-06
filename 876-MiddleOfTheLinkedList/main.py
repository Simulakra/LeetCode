# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 65ms / 13.8MB
        tmp=head
        while(True):
            if(head.next==None):
                break
            tmp=tmp.next
            if(head.next.next==None):
                break
            head=head.next.next
        return tmp
