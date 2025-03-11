/*Заполнить вещественный массив из 20 элементов случайными вещественными числами в диапазoне от - 3.0 до +3.0. Вывести на экран пронумерованный столбец значений элементов массива. Определить и вывести номер и значение наибольшего элемента массива.*/
/*#include<stdio.h>
    #include<stdlib.h>
    void main()
    {
        double arr[20];
        int i;
        srand(time(0));
        for(i=0;i<20;i++){
            arr[i]=-3.0+6.0*rand()/(float)RAND_MAX;
            printf("%d %5.2lf\n",i+1,arr[i]);
        }
        printf("\n");
        float max=arr[0];
        int number;
        for(i=0;i<20;i++){
            if (max<arr[i])
            {
                max=arr[i];
                number=i+1;
            }
        }
        printf("%5.2lf\t%d\n",max,number);
    }*/
 /*#include<stdio.h>
    #include<stdlib.h>
    void main()
    {
        float arr[20];
        int i;
        for(i=0;i<20;i++){
            arr[i]=rand()%(3+3+1)-3;
            printf("%d %5.2lf\n",i+1,arr[i]);
        }
        printf("\n");
        float max=arr[0];
        for(i=0;i<20;i++){
            if (max<arr[i])
            {
                max=arr[i];
            }
        }
        printf("%lf\n",max);
    }*/
/*#include<stdio.h>
    #include<stdlib.h>
    void main()
    {
        float arr[20];
        int i;
        for(i=0;i<20;i++){
            arr[i]=rand()%(3+3+1)-3;
            printf("%d %5.2lf\n",i,arr[i]);
        }
    }*/
#include<stdio.h>
    #include<stdlib.h>
    void main()
    {
        float arr[20];
        int i;
        for(i=0;i<20;i++){
            arr[i]=rand()%(3+3+1)-3;
            printf("Array=%5.2lf\n",arr[i]);
        }
    } 