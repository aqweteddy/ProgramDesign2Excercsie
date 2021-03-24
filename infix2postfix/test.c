#include <stdio.h>
#include <string.h>
#include <ctype.h>
#define MAX 5000


int priority(char);
int is_op(char);
int isdigit_or_point(char);

inline int priority(char op)
{
    switch (op) {
    case '+':
    case '-':
        return 1;
    case '*':
    case '/':
        return 2;
    default:
        return 0;
    }
}

inline int isdigit_or_point(char a)
{
    return isdigit(a) || a == '.';
}

inline int is_op(char a)
{
    const char* op = "+-*/()";
    for(int i = 0; i<strlen(op);++i) {
        if(a == op[i]) return 1;
    }
    return 0;
}

void inToPostfix(char* infix, char* postfix)
{
    char stack[MAX];
    int i, j, top;

    memset(stack, 0, sizeof stack);
    for (i = 0, j = 0, top = 0; infix[i] != '\0'; i++) {
        switch (infix[i]) {
        case '(': // 運算子堆疊
            stack[++top] = infix[i];
            break;
        case '+':
        case '-':
        case '*':
        case '/':
            while (priority(stack[top]) >= priority(infix[i])) {
                postfix[j++] = ' ';
                postfix[j++] = stack[top--];
            }
            stack[++top] = infix[i]; // 存入堆疊
            break;
        case ')':
            while (stack[top] != '(') { // 遇 ) 輸出至 (
                postfix[j++] = ' ';
                postfix[j++] = stack[top--];
            }
            top--; // 不輸出 (
            break;
        default: // 運算元直接輸出
            if(is_op(infix[i - 1])) postfix[j++] = ' ';
            postfix[j++] = infix[i];
        }
    }
    while (top > 0) {
        postfix[j++] = ' ';
        postfix[j++] = stack[top--];
    }
}

int main()
{
    char infix[4098], postfix[10000];

    while (fgets(infix, 4098, stdin)) {
        memset(postfix, 0, sizeof postfix);
        if (infix[strlen(infix) - 1] == '\n') {
            infix[strlen(infix) - 1] = 0;
        }
        inToPostfix(infix, postfix);
        puts(postfix);
    }

    return 0;
}