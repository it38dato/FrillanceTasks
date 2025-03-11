'''
Результаты анализов приходят в зашифрованном виде в файле medicine.xlsx. На сервере лежат таблицы de.med_an_name, de.med_name для расшифровки показаний. В ответе приложите два файла - скрипт python и результат работы (xlsx).
Легкий режим: Вы забираете данные с листа 'easy'. Нужно отыскать пациентов, у которых не в норме хотя бы один анализ. Вывести телефон, имя, название анализа и заключение 'Повышен' или 'Понижен'. Сохранить в xlsx.
Сложный режим: Вы забираете данные с листа 'hard'. Нужно отыскать пациентов, у которых не в норме два и более анализов. Вывести телефон, имя, название анализа и заключение 'Повышен', 'Понижен' или 'Положительный'. Сохранить в xlsx.
Дополнительно сохраните таблицу с расшифрованными значениями и результатами анализа в таблице xxxx_med_results в базе данных (помните про 4 буквы в начале, идентифицирующие вашу таблицу).
'''
import pandas as pd
import psycopg2
conn = psycopg2.connect(database = "edu",
    host = "de-edu-db.chronosavant.ru",
    user = "de13ma",
    password = "meriadocbrandybuck",
    port = "5432")
conn.autocommit = False
cursor = conn.cursor()
sel = input('Please select the mode (e/h/q): ') 
while (sel.lower() != "e" or sel.lower() != "h" or sel.lower() != "q"): 
    if sel.lower() == "e": 
        # Чтение из файла
        df = pd.read_excel( 'medicine.xlsx', sheet_name='easy', header=0, index_col=None )
        print( df )
        cursor.execute("CREATE TABLE de13ma.gabn_med_easy (patient_code int, analysis varchar, value numeric);")
        # Выполнение SQL кода вставки в базу данных
        cursor.executemany( """INSERT INTO de13ma.gabn_med_easy (patient_code, analysis, value)
            VALUES (%s, %s, %s)""", df.values.tolist() )
        # Выполнение SQL кода в базе данных с возвратом результата
        #cursor.execute( "SELECT * FROM de.med_an_name" )
        #cursor.execute( "SELECT * FROM de.med_name" )
        cursor.execute("""CREATE TABLE de13ma.gabn_med_easy1 AS (
            SELECT 
                * 
            FROM (
                SELECT 
                        --*
                        dmn.phone,
                        dmn.name,
                        dma.name AS analysis,  
                        (CASE 
                                WHEN dmt.value<dma.min_value 
                                        THEN 'Понижен'
                                WHEN dmt.value>dma.max_value 
                                        THEN 'Повышен'
                        --ELSE
                          --'Это нормально'
                        END) AS results--,
                        --dmt.value,
                        --dma.min_value,
                        --dma.max_value
                FROM de13ma.gabn_med_easy AS dmt
                LEFT JOIN de.med_name AS dmn
                        ON dmt.patient_code = dmn.id
                LEFT JOIN de.med_an_name AS dma
                        ON dmt.analysis = dma.id
                ) AS temp_result
                WHERE results IS NOT null);""")
        conn.commit()
        cursor.execute("SELECT * from de13ma.gabn_med_easy1;")
        records = cursor.fetchall()
        for row in records:
            print( row )
        # Формирование DataFrame
        names = [ x[0] for x in cursor.description ]
        df = pd.DataFrame( records, columns = names )
        df
        print( df )
        # Запись в файл
        df.to_excel( 'gabn_med_res_e.xlsx', sheet_name='easy', header=True, index=False )
        break; 
    elif sel.lower() == "h": 
        df = pd.read_excel( 'medicine.xlsx', sheet_name='hard', header=0, index_col=None )
        print( df )
        cursor.execute("CREATE TABLE de13ma.gabn_med_hard (patient_code int, analysis varchar, value varchar);")
        cursor.executemany( """INSERT INTO de13ma.gabn_med_hard (patient_code, analysis, value)
            VALUES (%s, %s, %s)""", df.values.tolist() )
        cursor.execute("""create table de13ma.gabn_med_hard1 as (
	    with t2 as (
	        select 
		    name,
		    count(*) as cnt 
		from (
		    select 
			--*,
			mn.phone,
			mn.name,
			man.name AS analysis,
			(case 
		            when 
			        lower(gmh.value) = 'положит.' 
				or lower(gmh.value) = 'положительно' 
				or lower(gmh.value) = '+' 
			    then 
			        'Положительный'
			    when 
				lower(gmh.value) = 'отриц.'
				or lower(gmh.value) = '-' 
				or lower(gmh.value) = 'отр' 
			    then 
				'Отрицательный'
			    when 
				cast(gmh.value as numeric) > cast(man.max_value as numeric)
			    then 
				'Повышен' 
			    when 
				cast(gmh.value as numeric) < cast(man.min_value as numeric)
			    then 
				'Понижен'
			    when 
			    	cast(gmh.value as numeric) >= cast(man.min_value as numeric)  
				and cast(gmh.value as numeric) <= cast(man.max_value as numeric)  
			    then 
				'Это нормально'
                        else 
			    'Не определено'  
			end) as results--,		
			--gmh.value,
			--man.min_value,
			--man.max_value
			from de13ma.gabn_med_hard as gmh
			left join de.med_name as mn
			    on gmh.patient_code = mn.id
			left join de.med_an_name as man
			    on gmh.analysis = man.id
			where 
			    (case 
			        when 
				    lower(gmh.value) = 'положит.' 
				    or lower(gmh.value) = 'положительно' 
				    or lower(gmh.value) = '+' 
				then 
				    'Положительный'
				when 
				    lower(gmh.value) = 'отриц.'
				    or lower(gmh.value) = '-' 
				    or lower(gmh.value) = 'отр' 
				then 
				    'Отрицательный'
				when 
				    cast(gmh.value as numeric) > cast(man.max_value as numeric)
				then 
				    'Повышен' 
				when 
				    cast(gmh.value as numeric) < cast(man.min_value as numeric)
				then 
				    'Понижен'
				when 
				    cast(gmh.value as numeric) >= cast(man.min_value as numeric)  
				    and cast(gmh.value as numeric) <= cast(man.max_value as numeric)  
				then 
				    'Это нормально'
			    else 
				'Не определено'  
			    end) in ('Положительный', 'Повышен' ,'Понижен')) as t1
		        group by name
		        having count(*) > 1)
	            select 
		        * 
	            from (
		        select 
			    --*,
			    mn.phone,
			    mn.name,
			    man.name AS analysis,
			    (case 
				when 
				    lower(gmh.value) = 'положит.' 
				    or lower(gmh.value) = 'положительно' 
				    or lower(gmh.value) = '+' 
				then 
				    'Положительный'
				when 
				    lower(gmh.value) = 'отриц.'
				    or lower(gmh.value) = '-' 
				    or lower(gmh.value) = 'отр' 
				then 
				    'Отрицательный'
				when 
				    cast(gmh.value as numeric) > cast(man.max_value as numeric)
				then 
				    'Повышен' 
				when 
				    cast(gmh.value as numeric) < cast(man.min_value as numeric)
				then 
				    'Понижен'
				when 
				    cast(gmh.value as numeric) >= cast(man.min_value as numeric)  
				    and cast(gmh.value as numeric) <= cast(man.max_value as numeric)  
				then 
				    'Это нормально'
			    else 
				'Не определено'  
			    end) as results--,		
			    --gmh.value,
			    --man.min_value,
			    --man.max_value
		            from de13ma.gabn_med_hard as gmh
		            left join de.med_name as mn
			        on gmh.patient_code = mn.id
		            left join de.med_an_name as man
			        on gmh.analysis = man.id
		            where 
			        (case 
				    when 
				        lower(gmh.value) = 'положит.' 
					or lower(gmh.value) = 'положительно' 
					or lower(gmh.value) = '+' 
				    then 
					'Положительный'
				    when 
					lower(gmh.value) = 'отриц.'
					or lower(gmh.value) = '-' 
					or lower(gmh.value) = 'отр' 
				    then 
					'Отрицательный'
				    when 
					cast(gmh.value as numeric) > cast(man.max_value as numeric)
				    then 
					'Повышен' 
				    when 
					cast(gmh.value as numeric) < cast(man.min_value as numeric)
				    then 
					'Понижен'
				    when 
					cast(gmh.value as numeric) >= cast(man.min_value as numeric)  
					and cast(gmh.value as numeric) <= cast(man.max_value as numeric)  
				    then 
					'Это нормально'
			        else 
				    'Не определено'  
			        end) in ('Положительный', 'Повышен' ,'Понижен')) as t1
	                where name in (
		            select 
			        name 
		            from t2)
	                order by name, results);""")
        conn.commit()
        cursor.execute("SELECT * from de13ma.gabn_med_hard1;")
        records = cursor.fetchall()
        for row in records:
            print( row )
        # Формирование DataFrame
        names = [ x[0] for x in cursor.description ]
        df = pd.DataFrame( records, columns = names )
        df
        print( df )
        # Запись в файл
        df.to_excel( 'gabn_med_res_h.xlsx', sheet_name='easy', header=True, index=False )
        break; 
    elif sel.lower() == "q":
        break;
    else: 
        sel = input('Please select the mode (e/h/q): ')
# Закрываем соединение
cursor.close()
conn.close()

