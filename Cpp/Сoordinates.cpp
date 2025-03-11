//Составить программу, принимающую с клавиатуры декартовы координаты точки и печатающую сферические координаты. Преобразование координат должно быть выполнено функцией типа void по формулам
    #include<stdio.h>
    #include<math.h>
    /*void sphere(double x, double y, double z, double *r, double *q, double *fi)
    {
        int a;
        *r=sqrt(x*x+y*y+z*z);
        *q=acos(z/(*r));
        if (x!=0){
            *fi=atan(y/x);
        }
    }
    void main(void)
    {
        double x, y, z, r, q, fi;
        printf("x=");scanf("%lf",&x);
        printf("y=");scanf("%lf",&y);
        printf("z=");scanf("%lf",&z);
        sphere(x, y, z, &r, &q, &fi);
        printf("%lf\n%lf\n%lf\n",r,q,fi);
    }*/
    const double pi=3.1415927;
    void sphere(double x, double y, double z, double *r, double *q, double *fi)
    {
        int a;
        *r=sqrt(x*x+y*y+z*z);
        *q=acos(z/(*r))*180.0/pi;
        if (x!=0){
            *fi=atan(y/x)*180.0/pi;
        }
    }
    void main(void)
    {
        double x, y, z, r, q, fi;
        printf("x=");scanf("%lf",&x);
        printf("y=");scanf("%lf",&y);
        printf("z=");scanf("%lf",&z);
        sphere(x, y, z, &r, &q, &fi);
        printf("%lf\n%lf\n%lf\n",r,q,fi);
    }