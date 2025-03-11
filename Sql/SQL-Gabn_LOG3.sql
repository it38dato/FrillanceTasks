/*На основании таблиц DE.LOG и DE.IP постройте структурированную таблицу посещений DE13MA.XXXX_LOG ( DT DATE, LINK VARCHAR( 50 ), USER_AGENT VARCHAR( 200 ), REGION VARCHAR( 30 ) ). Также постройте отчет DE13MA.XXXX_LOG_REPORT ( REGION VARCHAR( 30 ), BROWSER VARCHAR( 10 ) ) – в каких областях какой браузер является наиболее используемым.
Под USER_AGENT подразумевается вся строка описания клиента, под BROWSER – только название браузера (Opera, Safari…). XXXX означает ваши 4 уникальные буквы.
Важные замечания (вплоть до причины незачета задания):
1. Не используйте регулярные выражения там, где можно обойтись без них.
2. То, что вы видите в выводе клиента – это не всегда именно то, что содержится в базе данных.*/
/*create table DE13MA.GABN_LOG as (
	select 
		to_date (substring (dl.data from '\d{8}'), 'YYYYMMDD') as DT,
		cast (split_part (substring (replace (substring (dl.data, strpos (dl.data, 'http://')), chr(9), '+'), 1, strpos (replace (substring (dl.data, strpos(dl.data, 'http://')), chr(9), '|'), '/5.0') -1), '+', 1) as VARCHAR(50)) LINK,
		cast (split_part (replace (substring (dl.data from 1), chr(9), '+'), '+', 8 ) as VARCHAR(200)) USER_AGENT,
		cast (split_part (di.data, chr(9), 2) as VARCHAR(30)) REGION
	from de.log as dl
	left join de.ip as di
	on
		substring (dl.data, 1, strpos (dl.data, chr(9))) = 
			substring (di.data, 1, strpos (di.data, chr(9))));*/
create table DE13MA.GABN_LOG_REPORT as (SELECT
		region, 
		browser--, 
		--cnt
	FROM (select
		t1.* , 
		ROW_NUMBER() OVER (PARTITION BY region ORDER BY cnt DESC) as numb
	FROM (select 
			cast (split_part (di.data, chr(9), 2) as VARCHAR(30)) REGION, 
			cast (split_part (substring (replace (substring (dl.data, strpos(dl.data, 'http://')), chr(9), '+'), 1, strpos (replace (substring (dl.data, strpos (dl.data, 'http://')), chr(9), '|'), '/5.0') -1), '+', 4) as VARCHAR(10)) BROWSER,
			count(1) as cnt
		from de.log as dl
		--order by dl.data
		left join de.ip as di
		--on dl.data=di.data;
		on 
			substring (dl.data, 1, strpos (dl.data, chr(9))) =
				substring (di.data, 1, strpos (di.data, chr(9)))	
		--order by region
		group by region, browser) 
		as t1)
	as t2
	WHERE numb = 1);