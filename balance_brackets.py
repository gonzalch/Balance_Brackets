'''
Python solution for checking if string of brackets is balanced.
For example, "()[]{}" is balanced while "](){" is not.
'''

# Test cases
brackets = ["([])", "[]{}", "()[]{}", "([)]", "](){", "(())", "(()(", "((("]
parantheses = ["(())", "(()(", "((("]

def balance_brackets(str):
    # Map left bracket to right bracket
    bracket_map = {'(': ')', '[': ']', '{': '}'}
    # Stack to hold left brackets
    bracket_stack = []

    # If empty string, already balanced
    if len(str) is 0:
        return True

    # If length of string is odd, cannot be balanced
    if len(str) % 2 is 1:
        return False

    # Iterate through string
    for bracket in str:
        # If left bracket is found, push onto stack
        if bracket in bracket_map:
            bracket_stack.append(bracket)
        else:
            # If right bracket is found, stack cannot be empty
            if not bracket_stack:
                return False
            # Else, pop from stack and check mapping
            elif bracket is bracket_map[bracket_stack.pop()]:
                continue
            else:
                return False

    # If stack is empty, string is balanced
    return len(bracket_stack) is 0

def balance_parentheses(str):
    count = 0

    # If empty string, already balanced
    if len(str) is 0:
        return True

    # If length of string is odd, cannot be balanced
    if len(str) % 2 is 1:
        return False

    # Iterate through string
    for bracket in str:
        # If left bracket is found, increment counter
        if bracket is "(":
            count = count + 1
        # Else, check if counter is greater than 0 and decrement
        else:
            if count > 0 :
                count = count -1
            # If it is not greater than zero, return false
            else:
                return False

    # If count is zero, string is balanced
    if count is 0:
        return True
    else:
        return False

def main():
    for str in brackets:
        print str, balance_brackets(str)

    for str in parantheses:
        print str, balance_parentheses(str)


if __name__ == '__main__':
    main()
