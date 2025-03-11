//пытаемся отгадать число у компа.
#include<iostream>
#include<cstdlib>
#include<ctime>
using namespace std;
int main (){
        srand(time(0));
        bool done;
        do{
                int j, i=rand()%100;
                while (true){
                        cout<<"Какое число вы загадали?";
                        cin>>j;
                        if(i>j){
                                cout<<"Мое число больше"<<endl;
                        }
                        else{
                                if(i<j){
                                        cout<<"Мое число меньше"<<endl;
                                }
                                else{
                                        cout<<"Ты угадал"<<endl;
                                        break;
                                }
                        }
                }
                cout<<"Продолжить? (y/n) ";
                char c;
                done=(c!='y');
                cin>>c;
        }while(!done);
}