/*Создайте таблицу de13ma.XXXX_SALARY_HIST, где XXXX - ваш идентификатор. В таблице должна быть SCD2 версия таблицы de.HISTGROUP (поля PERSON, CLASS, SALARY, EFFECTIVE_FROM, EFFECTIVE_TO). Возьмите в работу таблицы
de13ma.XXXX_SALARY_HIST и de.SALARY_PAYMENTS. Напишите SQL скрипт, выводящий таблицу платежей сотрудникам. В таблице должны быть поля PAYMENT_DT, PERSON, PAYMENT, MONTH_PAID, MONTH_REST. Результат выполнения сохраните в таблицу de13ma.XXXX_SALARY_LOG.
1. MONTH_PAID - суммарно выплачено в месяце,
2. MONTH_REST - осталось выплатить за месяц.
Проверяется в первую очередь понимание как соединять фактовую таблицу с SCD2 таблицей (нельзя все расчеты сделать над DE.SALARY_PAYMENTS, ведь работнику могут недоплатить или переплатить).
В ответе приложите SQL-скрипт, таблица de13ma.XXXX_SALARY_LOG должна быть заполнена.*/
/*create table de13ma.gabn_SALARY_HIST as (
	select 
		PERSON,
		CLASS,
		SALARY,
		dt as effective_from,
		coalesce((
			lead(dt) 
			over (
				partition by person 
				order by dt) - interval '1 day')::date,  
			to_date('9999-12-31', 'YYYY-MM-DD')) as effective_to
	from de.HISTGROUP);*/
--select * from de13ma.gabn_SALARY_HIST;
--select * from de.SALARY_PAYMENTS;
/*create table de13ma.gabn_SALARY_LOG as (
	select --*--,
		dgsh.person as PERSON,
		dsp.dt as PAYMENT_DT,
		dsp.payment as PAYMENT,
		--sum(dsp2.payment) as MONTH_PAID,
		--sum(dsp.payment) over (order by dsp.dt between dgsh.effective_from and dgsh.effective_to) as MONTH_PAID,
		sum(dsp.payment) over (partition by dsp.payment order by dsp.dt) as MONTH_PAID,
		dgsh.salary-sum(dsp.payment) as MONTH_REST--,
		--dgsh.salary
	from de13ma.GABN_SALARY_HIST as dgsh
	inner join de.SALARY_PAYMENTS as dsp 
		on dgsh.person=dsp.person 
	--inner join de.SALARY_PAYMENTS as dsp2 
	--	on dsp.dt >= dsp2.dt
	where dsp.dt between dgsh.effective_from and dgsh.effective_to
	group by dgsh.person,
		dsp.dt,
		dsp.payment,
		dgsh.salary--,
		--dgsh.effective_from,
		--dgsh.effective_to
	order by dgsh.person,
		dsp.dt);*/
select * from de13ma.gabn_SALARY_LOG;