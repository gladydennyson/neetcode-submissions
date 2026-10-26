# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return

        slow = fast = l1 = head

        # Find the end of the first half
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        # Separate the two halves
        l2 = slow.next
        slow.next = None

        # Reverse the second half
        previous = None
        current = l2

        while current:
            temp = current.next
            current.next = previous
            previous = current
            current = temp

        l2 = previous

        # Merge the two halves
        while l2:
            temp1 = l1.next
            temp2 = l2.next

            l1.next = l2
            l2.next = temp1

            l1 = temp1
            l2 = temp2
            
