// https://www.hackerrank.com/challenges/maximum-element/copy-from/24256137
#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>
int stack[100000];
 long int top=-1;
void push();
void display();
void pop();
long int maxElement = 0;
int main() {

    int type;
    long int N;
    long int i;
    scanf("%ld",&N);
    for( i=0;i<N;i++)
        {
    scanf("%d",&type);
    switch(type)
        {
        case 1: push();break;
        case 2: pop();break;
        case 3:display();        
    }
    }
    
    return 0;
}

void pop() {
    long int x1=0,i1;
    --top;
    for(i1=0;i1<=top;i1++)
        if(x1<=stack[i1])x1=stack[i1];
    maxElement = x1;
}
void push() {
    long int x;
    scanf("%ld",&x);
    if (maxElement < x) {
        maxElement = x;
    }
    stack[++top]=x;
    return;
}

void display()
    {
    printf("%ld\n",maxElement);
    return;
 }
