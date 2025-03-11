#include <iostream>
using namespace std;
int age(int current_date, int current_month, int current_year, int birth_date, int birth_month, int birth_year)
{
  //если дата рождения больше текущей даты рождения тогда не считайте в этом месяце и добавьте 30 к дате так как вычесть дату и получить оставшиеся дни
  int month[]={31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};
  if (birth_date > current_date)
  {
    current_month = current_month - 1;
    current_date = current_date + month[birth_month-1];
  }
  //если месяц рождения превышает текущий месяц, то  Не считайте в этом году и добавьте 12 к месяц, чтобы мы могли вычесть и выяснить различия
  if (birth_month > current_month)
  {
    current_year = current_year - 1;
        current_month = current_month + 12;
  }
    // вычислить дату, месяц, год
    int calculated_date = current_date - birth_date;
    int calculated_month = current_month - birth_month;
    int calculated_year = current_year - birth_year;
  // печать нынешнего возраста
    cout<<"Present Age:"<<endl;
    cout<<"Years: "<<calculated_year<<" Months: "<<calculated_month<<" Days: "<<calculated_date<<endl;
  return 0;
}
int main()
{
  int current_date, current_month, current_year, birth_date, birth_month, birth_year;
  //код пользователя
  cout<<"Today:"<<endl;
  cout<<"DD: ";
  cin>>current_date;
  cout<<"MM: ";
  cin>>current_month;
  cout<<"YYYY: ";
  cin>>current_year;
  //рождение дд // мм // гггг
  cout<<"You'r Birthday:"<<endl;
  cout<<"DD: ";
  cin>>birth_date;
    cout<<"MM: ";
  cin>>birth_month;
    cout<<"YYYY:";
  cin>>birth_year;
  age(current_date, current_month, current_year, birth_date, birth_month, birth_year);
  system("pause");
  return 0;
}