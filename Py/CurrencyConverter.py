from pprint import pprint
import requests
data = requests.get('https://www.cbr-xml-daily.ru/daily_json.js').json()
dictionaryU=data['Valute']['USD']
dictionaryE=data['Valute']['EUR']
dictionaryC=data['Valute']['CNY']
'''
lists=[dictionaryU, dictionaryE, dictionaryC]
for index in lists:
  print(index)
'''
'''
print(dictionaryU['Value'],dictionaryU['Name'])
print(dictionaryE['Value'],dictionaryE['Name'])
print(dictionaryC['Value'],dictionaryC['Name'])
'''
'''
dollar=float(input("Enter the dollar rate: "))
euro=float(input("Enter the euro exchange rate: "))
yuan=float(input("Enter the yuan exchange rate: "))
'''
dollar=dictionaryU['Value']
euro=dictionaryE['Value']
yuan=dictionaryC['Value']
print("Dollar exchange rate: ",dollar)
print("Euro exchange rate: ",euro)
print("Yuan exchange rate: ",yuan)
print("1) Convert to dollars, Euros, yuan\n2) Transfer from dollars, Euros, yuan\n")
choise=int(input("Choose your actions:\n"))
if choise==1:
  ruble=float(input("Enter the number of rubles: "))
  resultDollar=ruble/dollar
  resultEuro=ruble/euro
  resultYuan=ruble/yuan
  print("The result of your transfer = ", '{:.2f}'.format(resultDollar))
  print("The result of your transfer = ", '{:.2f}'.format(resultEuro))
  print("The result of your transfer = ", '{:.2f}'.format(resultYuan))
elif choise==2:
  d=float(input("Enter the number of dollars: "))
  e=float(input("Enter the number of euroes: "))  
  y=float(input("Enter the number of yuans: "))
  resultDollar=d*dollar
  resultEuro=e*euro
  resultYuan=y*yuan
  print("The result of your transfer = ", '{:.2f}'.format(resultDollar))
  print("The result of your transfer = ", '{:.2f}'.format(resultEuro))
  print("The result of your transfer = ", '{:.2f}'.format(resultYuan))
else:
  print("Error! Enter only 1 or 2")
  exit(0)