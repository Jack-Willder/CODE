// C program using fibonacci series
#include<stdio.h>
int main() {
    int limit;
    int t1=0;
    int t2=1;
    int nextterm;
    printf("Enter a number : ");
    scanf("%d",&limit);
    if(limit>=0)
    {
        nextterm=t1;
        printf("\n%d", nextterm);
    }
    if(limit>=1)
    {
        nextterm=t2;
        printf("\n%d", nextterm);
    }
    for (int i=3;i<=limit;i++)
    {
        nextterm=t1+t2;
        printf("\n%d", nextterm);
        t1=t2;
        t2=nextterm;
    }
    return 0;
}
