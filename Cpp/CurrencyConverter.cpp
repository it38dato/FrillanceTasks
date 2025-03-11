#include <iostream>
using namespace std;
int main()
{
  float dollar, euro, yuan;
  cout<<"current dollar data: ";
  cin>>dollar;
        cout<<"current euro data: ";
  cin>>euro;
        cout<<"current yuan data: ";
  cin>>yuan;
  //cout<<dollar<<" "<<euro<<" "<<yuan<<" "<<endl;
  cout<<"1) Convert to dollars, Euros, yuan"<<endl<<"2) Transfer from dollars, Euros, yuan"<<endl<<"Choose your actions: ";
  int choise;
  cin>>choise;
  //cout<<choise; 
  if (choise==1){
    float ruble, resultDollar, resultEuro, resultYuan;
    cout<<"Enter the number of rubles: ";
    cin>>ruble;
    resultDollar=ruble/dollar;
    resultEuro=ruble/euro;
    resultYuan=ruble/yuan;
    cout<<"The result of your transfer = "<<resultDollar<<endl<<"The result of your transfer = "<<resultEuro<<endl<<"The result of your transfer = "<<resultYuan<<endl;
  } else if (choise==2) {
    float d, e, y, resultDollar, resultEuro, resultYuan;
    cout<<"Enter the number of dollars: ";
    cin>>d;
    cout<<"Enter the number of euroes: ";
    cin>>e;
    cout<<"Enter the number of yuans: ";
    cin>>y;
    resultDollar=d*dollar;
    resultEuro=e*euro;
    resultYuan=y*yuan;
    cout<<"The result of your transfer = "<<resultDollar<<endl<<"The result of your transfer = "<<resultEuro<<endl<<"The result of your transfer = "<<resultYuan<<endl;
  } else {
    cout<<"Error! Enter only 1 or 2: "<<endl;
    exit(0);
  }
  //system("pause");
  return 0;
}