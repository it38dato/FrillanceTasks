/*Преобразовать следующую программу:
    #include<stdio.h>
    #include<conio.h>
    void main()
    {
     int j; char k; double a;
     j=21; k=’m’; a=3.1415926;
     printf("PRINT INTEGER j =%d\n",j);
     printf("PRINT SYMBOL k=%c\n" ,k);
     printf("PRINT LONG FLOAT a=%lf \n",a);
     printf("PRINT STRING");
     getch();
    }
    так, чтобы в первой строке было напечатано:
    Value of symbol k = R, Value of integer j = -14,
     во второй строке:
    Value of float variable а is 1.652730E+02
    в экспоненциальной форме (по формату %е), а в третьей строке текст:
     END of PROGRAMM.*/
#include<stdio.h>
    #include<curses.h>
    void main()
    {
      int j; char k; double a;
      j=21; k='R'; a=1.652730E+02;
      printf("Value of symbol k=%c\n",k);
      printf("Value of float variable a is %e\n",a);
      printf("End of programm\n");
      getch();
    } 