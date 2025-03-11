#include<iostream>
    #include<fstream>
    using namespace std;
    int main(){
        
        fstream f("text.txt");
        const int n=100;
        int a[n];
        for (int i=0; i<n; ++i){
            f>>a[i];
        }
        int x;
        cout<<"VVedite iskonoe chislo";
        cin>>x;
        for (int i=0; i<n; ++i){
            if (x==a[i]){
                cout<<"chislo" << x << " nahoditsia po indeksu "
                    <<i;
                break;
            }
        }
    }