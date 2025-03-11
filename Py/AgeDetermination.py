def age(current_date, current_month, current_year, birth_date, birth_month, birth_year):
    #если дата рождения больше текущей даты рождения тогда не считайте в этом месяце и добавьте 30 к дате так как вычесть дату и получить оставшиеся дни
    month =[31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if (birth_date > current_date):
        current_month = current_month - 1
        current_date = current_date + month[birth_month-1]
    #если месяц рождения превышает текущий месяц, то Не считайте в этом году и добавьте 12 к месяц, чтобы мы могли вычесть и выяснить различия
    if (birth_month > current_month):
        current_year = current_year - 1;
        current_month = current_month + 12;
    # вычислить дату, месяц, год
    calculated_date = current_date - birth_date;
    calculated_month = current_month - birth_month;
    calculated_year = current_year - birth_year;
    # печать нынешнего возраста
    print("Present Age:")
    print("Years:", calculated_year, "Months:", calculated_month, "Days:", calculated_date)
print("Today:")
# код пользователя
current_date = int(input("DD: "))
current_month = int(input("MM: "))
current_year = int(input("YYYY: "))
# рождение дд // мм // гггг
print("You'r Birthday:")
birth_date = int(input("DD: "))
birth_month = int(input("MM: "))
birth_year = int(input("YYYY: "))
age(current_date, current_month, current_year, birth_date, birth_month, birth_year)