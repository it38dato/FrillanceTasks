#include<iostream>
#include<string>
using namespace std;
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
void doska_player(string indent){
    cout<<indent<<"-"<<d[6]<<"-|-"<<d[7]<<"-|-"<<d[8]<<"-"<<endl;
    cout<<indent<<"-"<<d[3]<<"-|-"<<d[4]<<"-|-"<<d[5]<<"-"<<endl;
    cout<<indent<<"-"<<d[0]<<"-|-"<<d[1]<<"-|-"<<d[2]<<"-"<<endl;
}
int doska(){
    cout<<"подсказка хода"<<endl;
    cout<<"-7-|-8-|-9-"<<endl;
    cout<<"-4-|-5-|-6-"<<endl;
    cout<<"-1-|-2-|-3-"<<endl;
    doska_player("");
    int hod;    
    cout<<"ваш ход: ";
    cin>>hod;
    while(hod>9 || hod<1 || d[hod-1]!='-'){
        cout<<"введите правильный ход: ";
        cin>>hod;
    }
    return hod;
}
bool finish_win(char player){
    int win[][3]={{0,1,2},{3,4,5},{6,7,8},{0,3,6},{1,4,7},{2,5,8},{6,4,2},{0,4,8}};
    for(int i=0; i<8; i++){
        int count=0;
        for(int j=0; j<3; j++){
            if(d[win[i][j]]==player){
                count++;
            }
        }
        if(count==3){
            return true;
        }
    }
    return false;
}
char play_and_get_winner(){
    int turn=1;
    while(!finish_win('x') && !finish_win('o')){
        clear();
        int hod=doska();
        cout<<"Вы ввели: "<<hod<<endl;
        if(turn%2==1){
            d[hod-1]='x';
            if(finish_win('x')){
                cout<<"player X: поздравляю, вы выйграли"<<endl;
                return 'x';
            }
        }else{
            d[hod-1]='o';
            if(finish_win('o')){
                cout<<"player O: поздравляю, вы выйграли"<<endl;
                return 'o';
            }
        }
        turn++;
        if(turn==10){
            cout<<"Ничья"<<endl;
        }
    }
    return 'D';
}
int main(){
    cout<<"Welcome"<<endl;
    string reply="y";
    int x_wins=0, o_wins=0, ties=0;
    while(reply=="y"){
        clear_doska();
        char winner=play_and_get_winner();
        doska_player("\t");
        switch(winner){
            case 'x':
                x_wins++;
                break;
            case 'o':
                o_wins++;
                break;
            case 'D':
                ties++;
                break;
        }
        cout<<" Статистика Игрока Х: " <<x_wins<<", Игрока О: "<<o_wins<<" И нeчьи "<<ties<<endl;
        cout<<"Хотите продолжить?(y/n) ";
        cin>>reply;
        while(reply!="y" && reply!="n"){
            cout<<"Пожалуйста, введите правильный ответ(y/n) ";
            cin>>reply;
        }
    }
    return 0;
}