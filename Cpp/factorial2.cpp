/*Составить программу вычисления факториала n! = 1*2*3*...*n тремя способами - с использованием цикла while, цикла do-while и цикла for.*/
/*#include<stdio.h>
    void main()
    {
      int n,j=1,i=1;
      printf("Введите число: ");scanf("%d",&n);
      while (i<=n)
      {
        j*=i;
        i++;
      }
      printf("%d!=%d\n",n,j);
    } */
/*#include<stdio.h>
    void main()
    {
      int n,j,i;
      printf("Введите число: ");scanf("%d",&n);
      for (j=1,i=1; i<=n; i++)
      {       
        j*=i;
      }
      printf("%d!=%d\n",n,j);
    }*/
#include<stdio.h>
    void main()
    {
      int n,j=1,i=1;
      printf("Введите число: ");scanf("%d",&n);
      do
      {
        j*=i; i++;
      }
      while (i<=n);
      printf("%d!=%d\n",n,j);
    } 