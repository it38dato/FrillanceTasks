import requests 
from bs4 import BeautifulSoup 
#import re
from selenium import webdriver

#browser = webdriver.Chrome("/usr/bin/chromedriver")
'''driver = webdriver.Chrome()
driver.get("https://www.google.com/")
driver.quit()'''

'''from selenium.webdriver.chrome.options import Options
chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
d = webdriver.Chrome('/usr/bin/chromedriver',chrome_options=chrome_options)
d.get('https://www.google.com/')'''

dictUrls = {
    'freelance.habr.com':'https://freelance.habr.com/tasks?categories=development_all_inclusive%2Cdevelopment_backend%2Cdevelopment_frontend%2Cdevelopment_prototyping%2Cdevelopment_desktop%2Cdevelopment_bots%2Cdevelopment_games%2Cdevelopment_scripts%2Cdevelopment_voice_interfaces%2Cdevelopment_other%2Cadmin_servers%2Cadmin_network%2Cadmin_databases%2Cadmin_other%2Cother_engineering',
    'career.habr.com':'https://career.habr.com/vacancies?remote=true&s[]=2&s[]=3&s[]=82&s[]=72&s[]=6&s[]=1&s[]=83&s[]=77&s[]=76&s[]=19&s[]=89&s[]=187&s[]=130&s[]=17&s[]=22&s[]=18&s[]=49&sort=date&type=all',
    #'irkutsk.hh.ru':'https://irkutsk.hh.ru/search/vacancy?text=&excluded_text=автор%2C+наставник%2C+1с%2C+С%23&professional_role=160&professional_role=96&professional_role=113&professional_role=114&professional_role=112&salary=&currency_code=RUR&experience=doesNotMatter&employment=part&employment=project&accept_temporary=true&schedule=shift&schedule=flexible&schedule=remote&order_by=publication_time&items_on_page=50&L_save_area=true&hhtmFrom=vacancy_search_filter',
    #'irkutsk.hh.ru':'https://irkutsk.hh.ru/search/vacancy?excluded_text=автор%2C+наставник%2C+1с%2C+С%23&order_by=publication_time&employment=part&employment=project&schedule=shift&schedule=flexible&schedule=remote&professional_role=160&professional_role=96&professional_role=113&professional_role=114&professional_role=112&saved_search_id=82072405&no_magic=true&accept_temporary=true&L_is_autosearch=true',    
    'irkutsk.hh.ru':'https://irkutsk.hh.ru',
    #'japanlife-auto.ru':'https://japanlife-auto.ru/statistika/',
}
parsDict = dict()
keyList = []
valList = []

for key,url in dictUrls.items():
    #print("Сайт: ", key)
    #print("Cсылка: ", url)
    try:
        response = requests.get(url)
        print(response)
        #print(url[8:25])
        
        if url[8:26]==key or url[7:25]==key:
            print("Это данные из сайта: ", key)
            src = response.text
            #print(src)
            soup = BeautifulSoup(src, "html.parser")
            contents = soup.find_all(class_="content-list__item")
            step = 0

            for content in contents:
                #task, date, price = (content.find(class_="task__title").text, content.find(class_="params__published-at").text, content.find(class_="task__price").text) 
                step = step + 1

                if step <= 2:
                    task = content.find('a').get_text()
                    link = content.find('a')                
                    date = content.find(class_="params__published-at").text
                    price = content.find(class_="task__price").text
                    place = "Удаленно"
                    print(f"{step} Задача: {task}\nДата: {date}\nЦена: {price}\nСсылка: https://{key + link['href']}\nМесто: {place}")
                    keyList.append(task)
                    valList.append('https://'+key + link['href'])
                    valList.append(date)
                    valList.append(price)
                    valList.append(place)
                else :
                    #print(f"{step}")
                    continue
        elif url[8:23]==key or url[7:22]==key:
            print("Это данные из сайта: ", key)
            src = response.text
            #print(src)
            soup = BeautifulSoup(src, "html.parser")
            contents = soup.find_all(class_="vacancy-card__info")
            step = 0

            for content in contents:
                step = step + 1

                if step <= 2:
                    task = content.find(class_="vacancy-card__title").text
                    link = content.find(class_="vacancy-card__title-link")
                    place = content.find(class_="vacancy-card__meta").text
                    price = "-"
                    date = "-"
                    #print(f"{step} Задача: {task}\nСсылка: https://{key + link['href']}\nМесто: {place}\nЦена: {price}")
                    print(f"{step} Задача: {task}\nДата: {date}\nЦена: {price}\nСсылка: https://{key + link['href']}\nМесто: {place}")
                    keyList.append(task)
                    valList.append('https://'+key + link['href'])
                    valList.append(date)
                    valList.append(price)
                    valList.append(place)
                else :
                    #print(f"{step}")
                    continue
        elif url[8:21]==key or url[7:20]==key:
            print("Это данные из сайта: ", key)
            src = response.text
            #print(src)
            soup = BeautifulSoup(src, "html.parser")
            #contents = soup.find_all(class_="vacancy-serp-content")
            #contents = soup.findall("div", id="a11y-main-content")
            #contents = soup.find_all(class_=re.compile(r"vacancy-info(.*?)", re.DOTALL))
            #soup.find_all('a', {'href': re.compile(r'crummy\.com/')})
            #Placemark = re.findall(r"<Placemark>(.*?)</Placemark>", file, re.DOTALL)
            #print(contents)
            step = 0

            '''for content in contents:
                step = step + 1
                if step <= 2:
                    task = content.find(class_="bloko-header-section-2").text
                    print(f"{step} Задача: {task}\nСсылка: https://")
                else :
                    print(f"{step}")
                    continue'''
        elif url[8:25]==key or url[7:24]==key:
            print("Это данные из сайта: ", key)
            src = response.text
            #print(src)
            soup = BeautifulSoup(src, "html.parser")
            contents = soup.find_all(class_="goods")
            step = 0

            '''for content in contents:
                step = step + 1
                header = content.find('a')
                print(f"{step} Задача: {header['href']}\n")'''
        else:
            #print(url[:8])
            #print("Это данные из сайта ТРЕБУЕТСЯ ДОРАБОТКА (ФУНКЦИИ): ", key)
            continue
    except requests.exceptions.MissingSchema:
        print("Некорректная ссылка -", url)
#print(keyList)
#print(valList)
remainder = (len(valList)//len(keyList))

for numeration in range(len(keyList)):
    parsDict[keyList[numeration]] = [valList[y] for y in range(remainder*numeration,remainder*numeration+remainder)]

#print(parsDict)





