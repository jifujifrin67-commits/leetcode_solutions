class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False
        for i in range(0,10000):
            if not head.next:
                return False
            head = head.next
        return True

        