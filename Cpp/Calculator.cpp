#include <iostream>
using namespace std;
int main()
{
  string repeat="y";
  while (repeat == "y"){
      int numb1, numb2;
      cout<<("Enter number1: ");
      cin>>numb1;
      cout<<("Enter number2: ");
      cin>>numb2;
      char operation;
      cout<<("Enter the operation: ");
      cin>>operation;
      if (operation == '+')
          cout<<(numb1 + numb2)<<endl;
      else if (operation == '-')
          cout<<(numb1 - numb2)<<endl;
      else if (operation == '*')
          cout<<(numb1 * numb2)<<endl;
      else if (operation == '/'){
          if (numb2 == 0)
              cout<<("You cant divide by zero!")<<endl;
          else
              cout<<(numb1 / numb2)<<endl;
      }else{
          cout<<("Invalid operation")<<endl;
      }
      cout<<("Do you want to continue? (y/n): ");
      cin>>repeat;
      if (repeat == "n"){
          break;
      }
      while (repeat!="y" && repeat!="n"){
          cout<<("Please enter the correct answer (y/n): ");
          cin>>repeat;
      }
  }
  return 0;
}