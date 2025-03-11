/*Составить программу, печатающую таблицу факториалов от 0 до 7. В программе должна быть создана и использована функция, вычисляющая факториал своего аргумента*/
#include<stdio.h>
    /*void main()
    {
        int n;
        for (int i=1;i<=7;i++)
        {
            //printf("%d\n",i);
            f=f*i;
            printf("%d!\t%d\n",i,f);
        }
    }*/
    int fact(int n, int j)
    {
        /*n=n*j;
        return n;*/
        return n*j;
    }
    void main(void)
    {
        int f=1, i;
        for (i=1;i<=7;i++)
        {
            f=fact(f,i);
            printf("%d!\t%d\n",i,f);
        }
    }