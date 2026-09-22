
class Solution:
   def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
       if(headA == headB):
           return headA
       len1 = 0
       len2 = 0
       ll1 = headA
       ll2 = headB
       endA = None
       endB = None
       while(ll1 or ll2):
           if(ll1):
               len1+=1
               if(not ll1.next):
                   endA = ll1
               ll1 = ll1.next
           if(ll2):
               len2 += 1
               if(not ll2.next):
                   endB = ll2
               ll2 = ll2.next
           
           if(ll1 and ll2 and ll1 == ll2):
               return ll1
           
       
       if endA == endB:
           diff = abs(len1-len2)
           leni = 0
           if len1 > len2:
               while(headA and leni < diff):
                   headA = headA.next
                   leni+=1
               
               while(headA and headB):
                   if headA == headB:
                       return headA
                   headA = headA.next
                   headB = headB.next

           else:
               while(headB and leni < diff):
                   headB = headB.next
                   leni+=1
               
               while(headA and headB):
                   if headA == headB:
                       return headA
                   headA = headA.next
                   headB = headB.next
       else:
           return None
        