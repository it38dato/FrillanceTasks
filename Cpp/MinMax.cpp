#include <iostream>
    #include <stdlib.h>
    using namespace std;
    int main()
    {
        system("chcp 1251>0");
        const int arraysize = 5;
        int a [arraysize] = {18, 3, 4, 7, 7};
        int min=a[0], k=0, min2=a[1], k2=1, q;
        if (min>min2){
            q=min;
            min=min2;
            min2=q;

            q=k;
            k=k2;
            k2=q;
        }

        for (int i = 2; i < arraysize; i++){
            if (a[i]<min){
                min2=min;
                k2=k;
                min=a[i];
                k=i;
            }
            else{
                if(a[i]<min2){
                    min2=a[i];
                    k2=i;
                }

            }
        }
         cout << "min2=" << min2 << endl;
         cout << "k2=" << k2 << endl;
         cout << "min=" << min << endl;
         cout << "k=" << k << endl;
        return 0;
    }