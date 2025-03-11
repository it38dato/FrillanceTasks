import schedule
import requests
def greeting():
    todos_dict={
        '08:00':'Drink coffee',
        '11:00':'Work meeting',
        '23:59':'Hack the Planet!'
    }
    print("day's tasks")
    for k, v in todos_dict.items():
        print(f'{k}-{v}')
    response = requests.get(url='https://yobit.net/api/3/ticker/btc_usd')
    data = response.json()
    #print(data)
    #btc_price = data.get('btc_usd').get('last')
    btc_price = f"BTC: {round(data.get('btc_usd').get('last'), 2)}$\n"
    print(btc_price)
def main():
    #greeting()
    '''schedule.every(4).seconds.do(greeting)
    schedule.every(5).minutes.do(greeting)
    schedule.every().hour.do(greeting)'''
    schedule.every().day.at('12:00').do(greeting)
    schedule.every().thursday.do(greeting)
    schedule.every().friday.at('23:45').do(greeting)
    while True:
        schedule.run_pending()
if __name__=='__main__':
    main()