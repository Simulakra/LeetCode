# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # 162ms / 13.9MB
        temp=ListNode()
        sonuc=temp
        while(l1 != None or l2 != None ):
            if(l1 != None and l2 != None):
                sonuc.val+=l1.val+l2.val
            elif(l1 != None):
                sonuc.val+=l1.val
            elif(l2 != None):
                sonuc.val+=l2.val
                
            if(l1 != None):
                l1=l1.next
            if(l2 != None):
                l2=l2.next
                
            if(sonuc.val>=10):
                sonuc.next=ListNode()
                sonuc.val%=10
                sonuc.next.val=1
            if(l1 != None or l2 != None):
                if(sonuc.next == None):
                    sonuc.next=ListNode()
                sonuc=sonuc.next
        return temp
