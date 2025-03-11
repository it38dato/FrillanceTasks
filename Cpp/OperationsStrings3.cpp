/*Добавление и удаление имен в списке*/
#include <iostream>
    #include <cmath>
    #include <fstream>
    #include <cstring>
    #include <vector>
    using namespace std;
    int main() {
        int q;
        string w;
        vector <string> name;
        for (;true;){ // besconechni cikl
            cout<<"1-dobavit\n"<<"2-udalit\n"<<"3-pechay\n";
            cin>>q;
            if(q==1){
                cout<<"vvedite imya:";
                cin>>w;
                name.push_back(w);
            }
            else{
                if(q==2){
                    cout<<"vvedite imya:";
                    cin>>q;
                    name.erase(name.begin() + (q-1));
                }
                else{
                    if(q==3){
                        for(int i=0;i<name.size();i++){
                            cout<<i+1<<" "<<name[i]<<endl;
                        }
                    }
                }
            }
        }
        return 0;
    }