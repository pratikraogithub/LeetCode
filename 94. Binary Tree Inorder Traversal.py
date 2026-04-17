# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack = []          # Stack to simulate recursion (stores nodes)
        result = []         # Final inorder result (list of values)
        curr = root         # Start from root

        # Continue until:
        # 1. We still have nodes to explore (curr != None)
        # OR
        # 2. There are nodes in stack waiting to be processed
        while curr or stack:

            # Step 1: Go as LEFT as possible
            # Push all left nodes into stack
            while curr:
                stack.append(curr)     # Save current node to process later
                curr = curr.left       # Move to left child

            # Step 2: No more left nodes
            # Pop from stack (this is the "ROOT" step of inorder)
            curr = stack.pop()

            # Add the node value to result (visit the node)
            result.append(curr.val)

            # Step 3: Move to RIGHT subtree
            curr = curr.right

        # Return the final inorder traversal
        return result
    
# Step-by-step intuition
# Keep going left → push nodes
# When no left → pop
# Process node
# Go right

# | Step                 | Meaning             |
# | -------------------- | ------------------- |
# | `while curr`         | Go deep left        |
# | `stack.append(curr)` | Save node for later |
# | `stack.pop()`        | Come back to node   |
# | `result.append()`    | Visit node          |
# | `curr = curr.right`  | Explore right       |
