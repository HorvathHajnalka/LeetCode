# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None or head.next == None:
            return head
        prev = None
        curr = head
        while curr:
            nextp = curr.next
            curr.next = prev
            prev = curr
            curr = nextp
        return prev
        