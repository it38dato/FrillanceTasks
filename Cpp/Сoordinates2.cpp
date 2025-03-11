//нам нужно создать функцию, которая принимает в качестве аргументов полярные координаты точки p и ф и передает в вызывающую эту функцию программу декартовы координаты точки Х и У, вычисляемые по формулам: *X=p*Cos(ф), Y=p*Sin(ф)
#include<stdio.h>
    #include<math.h>
    const double pi180=3.1415927/180;
    void DECART(double r, double f, double *x, double *y)
    {
        *x=r*sin(f*pi180);
        *y=r*cos(f*pi180);
    }
    void main()
    {
        double r,f,x,y;
        scanf("%lf %lf",&r,&f);
        DECART(r,f,&x,&y);
        printf("%lf %lf",x,y);
    }