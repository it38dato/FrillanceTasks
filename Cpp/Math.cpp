/*Для вводимого с консоли значения вещественной переменной а, напечатать таблицу значений функций вида:
    sin(a)=...
    arccos(a)==...
    ехр(a).==...
    ln(a)=^...
    ceil(a)=...
    floor(a)=...
    sqrt(a)=…
    pow(2,a)=...
    На месте a должно отображаться число, введенное с клавиатуры, на месте ... - значение соответствующей функции. */
#include<stdio.h>
    #include<curses.h>
    #include<math.h>
    const float Pi=3.1415927;
    void main()
    {
      float a;
      a=30.0;
      printf("Напишите число: "); scanf("%f",&a);
      printf("sin(a)=%4.2lf\n",sin(a*Pi/180.0));
      printf("arccos(a)=%4.2lf\n",acos(a*Pi/180.0));
      printf("exp(a)=%4.2lf\n",exp(a));
      printf("ln(a)=%4.2lf\n",log(a));
      printf("ceil(a)=%4.1lf\n",ceil(a));
      printf("floor(a)=%4.1lf\n",floor(a));
      printf("sqrt(a)=%4.2lf\n",sqrt(a));
      printf("pow(2,a)=%4.2lf\n",pow(2,a));
      getch();
    } 