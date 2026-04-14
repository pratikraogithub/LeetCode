class Solution:
    def clearDigits(self, s: str) -> str:
        stack = [] # to store characters

        for str in s:
            # isdigit is used for identifying the digits
            if str.isdigit():
                if stack:
                    # remove the closest letter to the left
                    stack.pop()
            else:
                 # add letter to stack
                stack.append(str)

        return "".join(stack)