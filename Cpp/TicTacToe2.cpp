#include<iostream>
using namespace std;
//char d[9]={ '-', '-', '-', '-', '-', '-', '-', '-', '-'};
char d[9]={};
void clear(){
    for(int i=0; i<50; i++){
        cout<<endl;
    }
}
void clear_doska(){
    for(int i=0; i<9; i++){
        d[i]='-';
    }
}
void doska_player(){
    cout<<"ход игроков"<<endl;
    cout<<"-"<<d[6]<<"-|-"<<d[7]<<"-|-"<<d[8]<<"-"<<endl;
    cout<<"-"<<d[3]<<"-|-"<<d[4]<<"-|-"<<d[5]<<"-"<<endl;
    cout<<"-"<<d[0]<<"-|-"<<d[1]<<"-|-"<<d[2]<<"-"<<endl;
}
int doska(){
    cout<<"подсказка хода"<<endl;
    cout<<"-7-|-8-|-9-"<<endl;
    cout<<"-4-|-5-|-6-"<<endl;
    cout<<"-1-|-2-|-3-"<<endl;
    doska_player("");
    //cout<<"ход игроков"<<endl;
    //cout<<"-"<<d[6]<<"-|-"<<d[7]<<"-|-"<<d[8]<<"-"<<endl;
    //cout<<"-"<<d[3]<<"-|-"<<d[4]<<"-|-"<<d[5]<<"-"<<endl;
    //cout<<"-"<<d[0]<<"-|-"<<d[1]<<"-|-"<<d[2]<<"-"<<endl;
    int hod;
    cout<<"ваш ход: ";
    cin>>hod;
    while(hod>9 || hod<1 || d[hod-1]!='-'){
        cout<<"введите правильный ход: ";
        cin>>hod;
    }
    return hod;
}
int main(){
    clear_doska();
    int turn=0;
    for(int i=0; i<9; i++){
        clear();
        int hod=doska();
        cout<<"Вы ввели: "<<hod<<endl;
        if(i%2==0){
            d[hod-1]='x';
        }else{
            d[hod-1]='o';
        }
        turn++;
    }
    doska_player();
    return 0;
}