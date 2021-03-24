#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#define MAXLEN 4096
#define MAX_QLEN 2048
typedef struct {
    double queue[MAXLEN];
    int size;
} QUEUE;

QUEUE new_queue()
{
    QUEUE q;
    memset(q.queue, -1, sizeof q.queue);
    q.size = 0;
    return q;
}

int push(QUEUE* q, double num)
{
    if (MAX_QLEN <= q->size) {
        return -1;
    }
    q->queue[q->size++] = num;
    return 0;
}

double pop(QUEUE* q)
{
    if (q->size == 0) {
        return -1;
    }
    double ret = q->queue[q->size - 1];
    q->queue[--q->size] = -1;
    return ret;
}

void solve(char* line)
{
    QUEUE q = new_queue();
    char* p = strtok(line, " ");

    do {
        if (!strcmp(p, "+")) {
            double a = pop(&q);
            double b = pop(&q);
            push(&q, a + b);
        } else if (!strcmp(p, "-")) {
            double a = pop(&q);
            double b = pop(&q);
            push(&q, b - a);
        } else if (!strcmp(p, "*")) {
            double a = pop(&q);
            double b = pop(&q);
            push(&q, a * b);
        } else if (!strcmp(p, "/")) {
            double a = pop(&q);
            double b = pop(&q);
            push(&q, b / a);
        } else {
            int ret = push(&q, atof(p));
            if (ret == -1) {
                puts("Queue length is out of range");
                return;
            }
        }
        p = strtok(NULL, " ");
    } while (p != NULL);
    if(q.size != 1) puts("err");
    printf("%.2lf\n", pop(&q));
}

int main()
{
    char line[MAXLEN];

    while (fgets(line, MAXLEN, stdin)) {
        line[strlen(line) - 1] = 0;
        solve(line);
    }
    return 0;
}