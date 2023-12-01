"""
Module to implement functions related to balanced expressions using stacks.
"""


def is_balanced(expression):
    """
    Check if the given expression has balanced parentheses, curly braces, and square brackets.
    Returns True if balanced, False otherwise.
    """
    stack = []
    opening_brackets = "({["
    closing_brackets = ")}]"

    for char in expression:
        if char in opening_brackets:
            stack.append(char)
        elif char in closing_brackets:
            if not stack or opening_brackets.index(stack.pop()) != closing_brackets.index(char):
                return False

    return not stack  # True if the stack is empty, meaning all brackets are balanced


def main():
    """
    Main function to demonstrate the is_balanced function with sample expressions.
    """
    EXPRESSION1 = "([]{})"
    EXPRESSION2 = "([)]"
    print(is_balanced(EXPRESSION1))  # Output: True
    print(is_balanced(EXPRESSION2))  # Output: False


if __name__ == "__main__":
    main()
