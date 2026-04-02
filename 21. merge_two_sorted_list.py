# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        # list1 and list2 are HEAD nodes of two linked lists
        
        # Step 1: Create a dummy node
        # This helps simplify edge cases (like empty list)
        dummy = ListNode(0)
        current = dummy  # Pointer to build the new list

        # Step 2: Traverse both lists until one or both list becomes empty
        while list1 and list2:
            
            # Compare values of current nodes
            if list1.val < list2.val:
                current.next = list1   # Attach smaller node
                list1 = list1.next    # Move list1 forward
            else:
                current.next = list2
                list2 = list2.next

            current = current.next   # Move current forward
            # dummy → 1 → 1 → 2 → ...
            #  ↑ current

            # dummy → 1 → 1 → 2 → ...
            #         ↑ current

        # Step 3: Attach remaining elements
        # Only one of these will run
        if list1:
            current.next = list1
        if list2:
            current.next = list2

        # Step 4: Return merged list (skip dummy node)
        return dummy.next
    
    
# Important Insight
# 👉 Python variables store references, not copies
# So:
# current = dummy
# means:
# both point to SAME node


# current = current.next
# Now:
# dummy → 1 → 2 → 4
#          ↑
#       current
# 👉 current moves forward
# 👉 dummy stays at start


# Notes:
# 'current' always points to the LAST node of the result list
# Move current forward so next node is attached at the end
# Remaining list is already sorted, so attach directly