# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        left = 0
        current_node = head
        while current_node and current_node.next:
            x, y = current_node.val, current_node.next.val
            gcd_node = ListNode(math.gcd(x, y))
            gcd_node.next = current_node.next
            current_node.next = gcd_node
            # Move to the next pair (skipping the newly inserted node)
            current_node = gcd_node.next
        return head
