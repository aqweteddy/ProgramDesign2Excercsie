OPERATORS = set(['+', '-', '*', '/', '(', ')', '^'])  # set of operators

PRIORITY = {'+':1, '-':1, '*':2, '/':2, '^':3} # dictionary having priorities 


def infix_to_postfix(expression): #input expression
    stack = [] # initially stack empty
    output = '' # initially output empty
    for ch in expression:
        if ch not in OPERATORS:  # if an operand then put it directly in postfix expression
            output += ' '
            output+= ch
        elif ch=='(':  # else operators should be put in stack
            stack.append('(')
        elif ch==')':
            while stack and stack[-1]!= '(':
                output += ' '
                output+=stack.pop()
            stack.pop()
        else:
            # lesser priority can't be on top n higher or equal priority    

             # so pop and put in output   
            while stack and stack[-1]!='(' and PRIORITY[ch]<=PRIORITY[stack[-1]]:
                output += ' '
                output+=stack.pop()

            stack.append(ch)

    while stack:
        output += ' '
        output += stack.pop()

    return output

while 1:
    try:
        infix = input()
    except  EOFError:
        break
    
    postfix = infix_to_postfix(infix)
    print(postfix[1:])