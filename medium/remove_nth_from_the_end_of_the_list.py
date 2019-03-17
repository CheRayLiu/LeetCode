"""
Given a linked list, remove the n-th node from the end of list and return its head.
Time: O(N)
Space: O(1)
"""
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        start = ListNode(None)
        start.next = head
        fast = start
        slow = start
        for i in range(n+1):
            fast = fast.next
        
        while (fast != None):
            slow = slow.next
            fast = fast.next
        slow.next = slow.next.next
        return start.next