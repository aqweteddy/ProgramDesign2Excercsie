import random


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
            

def gen_one_data(input_f, output_f):
    # r = [f'{random.randint(0, 5):.2f}']
    r = [f'{random.uniform(0, 100000000):.2f}']
    op = list("+-*/")

    for i in range(random.randint(30, 70)):
        o = random.choice(op)
        r.append(o)
        r.append(str(random.uniform(0, 100000000)))
    if len("".join(r)) >= 2048:
         print('err')
    input_f.writelines([infix_to_postfix(r), '\n'])
    output_f.writelines([f'{eval("".join(r)):.2f}', '\n'])


with open('input6', 'w') as f1:
    with open('output6', 'w') as f2:
        for i in range(8000):
            gen_one_data(f1, f2)
