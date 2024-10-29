
def isBalanced(s):
    opening = {
        '(': ')',
        '[' : ']',
        '{' : '}'
    }
    closing = ['}', ')', ']']
    stack = []
    for i in range(len(s)):
        char = s[i]
        if char in opening:
            stack.append(char)
        elif len(stack) == 0 or stack.pop() != char:
            return 'NO'
    if stack.empty: 
        return 'YES' 
    else: 
        return 'NO'
    
    
    # Write your code here

if __name__ == '__main__':

    result = isBalanced(s)

    print(result)


