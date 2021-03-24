import random, string


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
    r = [f'{int(random.uniform(0, 1000))}']
    op = list("+-*/")

    r_bracket_fl = 0

    for i in range(random.randint(60, 100)):
        o = random.choice(op)
        r.append(o)
        if random.randint(0, 5) == 0:
            r_bracket_fl += 1
            r.append('(')
        num = random.choice([f'{random.uniform(0, 1000):.2f}', random.choice(string.ascii_lowercase)])
        r.append(num)
        if random.randint(0, 3) == 0 and r_bracket_fl > 0:
            r_bracket_fl -= 1
            r.append(')')
    
    while r_bracket_fl > 0:
        r.append(')')
        r_bracket_fl -= 1

    if len("".join(r)) >= 2048:
         print('err')
    else:
        output_f.writelines([infix_to_postfix(r)[1:], '\n'])
        input_f.writelines([''.join(r), '\n'])


with open('input3', 'w') as f1:
    with open('output3', 'w') as f2:
        for i in range(10000):
            gen_one_data(f1, f2)
