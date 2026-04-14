class Solution:
    def calPoints(self, operations: List[str]) -> int:
        #defined a stack
        stack = []

        #loop through operations
        for op in operations:
            if op == '+':
                # stack[-1] is top element in in stack and stack[-2] is second top element 
                # as it is a list its work like list[-1] is last element and list[-2] is second last element
                stack.append(stack[-1] + stack[-2])

            elif op == 'C':
                stack.pop()

            elif op == 'D':
                stack.append(2 * stack[-1])

            else:
                # type conversion from string to int
                stack.append(int(op))
        
        # sum of stack element
        return sum(stack)
