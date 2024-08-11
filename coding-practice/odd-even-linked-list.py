# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        curr = head
        if head == None or head.next == None or head.next.next == None:
            return head
        odds = []
        while curr.next.next:
            odds.append(curr.next.val)
            curr.next = curr.next.next
            curr = curr.next
            if curr.next == None or curr.next.next == None:
                break
            print(curr.val)
        if curr.next:
            #print(curr.val)
            odds.append(curr.next.val)
        for elem in odds:
            curr.next = ListNode(elem)
            curr = curr.next
        return head
        