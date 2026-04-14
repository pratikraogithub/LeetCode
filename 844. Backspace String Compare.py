class Solution:
    def build(self, string):
        stack = []  # This will store the final characters after processing

        # Loop through each character in the string
        for ch in string:
            if ch == "#":
                # If it's a backspace and stack is not empty → remove last character
                if stack:
                    stack.pop()
            else:
                # If it's a normal character → add to stack
                stack.append(ch)

        # Return the processed string as a list
        return stack

    def backspaceCompare(self, s, t):
        # Build both processed strings and compare them
        return self.build(s) == self.build(t)