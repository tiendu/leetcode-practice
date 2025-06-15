# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def addTwoNumbers(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    dummy = ListNode(0)  # Dummy node to build the result list
    current = dummy  # Pointer to the current node in result list
    carry = 0  # Variable to store carry-over value during addition

    while l1 or l2 or carry:  # Continue while either list has nodes or there's a carry
        # Get current values from the two lists (0 if list is exhausted)
        x = l1.val if l1 else 0
        y = l2.val if l2 else 0
        total = x + y + carry  # Add the values along with the carry

        carry = total // 10  # Update carry (for next digit)
        current.next = ListNode(total % 10)  # Create new node with current digit

        current = current.next  # Move pointer forward
        if l1: l1 = l1.next  # Advance list l1 if not at end
        if l2: l2 = l2.next  # Advance list l2 if not at end

    return dummy.next  # Skip the dummy node and return the result list

