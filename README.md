# RPA Case
Example of RPA-bot on Python.

## Algorithm 

Bot:

1) visits webpage [Fedresurs](https://fedresurs.ru)
2) scrapes info about company
3) downloads PDF file
4) visits [Kadarbitr](https://kad.arbitr.ru)
5) scrapes info about company's bankruptcy cases
6) sends info to database

## Starting bot

1) Install requirements
```
pip install -r requirements.txt
```
2) Add path to Excel file with companies' inns *(file main.py, line 15)*
```
companies_inns = ExcelWorker.get_companies_inns("name_of_your_file.xlsx")
```
You can use file **companies.xlsx** from src/excel folder.

<img width="489" alt="Datatable from companies.xlsx" src="https://github.com/iglebov/rpa_case/assets/41822761/28ae32c6-d2b0-497b-8f15-73ced6863fa2">

3) Add data for database connection *(file main.py, line 31)*
```
  db_worker = DBWorker(
      user="Your user",
      host="localhost",
      port="Your port",
      password="Your password",
      database="Your database",
  )
```
4) Execute **main.py**
```
python main.py
```
## Info about databases

This example works with databases 'companies' and 'cases'.

1) To create Database 'companies' write text from **create_companies_table.txt** in database client *(I used PostgreSQL)*
```
CREATE TABLE companies (
inn CHAR ( 10 ) PRIMARY KEY,
name_fedresurs VARCHAR ( 50 ) NULL,
ogrn CHAR ( 13 ) NULL,
bankruptcy_cases TEXT [] NULL,
pdf_path VARCHAR ( 100 ) NULL,
name_full VARCHAR ( 50 ) NULL,
name VARCHAR ( 50 ) NULL,
fio VARCHAR ( 50 ) NULL,
okato VARCHAR ( 50 ) NULL,
oktmo VARCHAR ( 50 ) NULL,
okpo VARCHAR ( 50 ) NULL,
address TEXT [] NULL,
status VARCHAR ( 50 ) NULL
);
```
Table **companies** *(visual, from file BD_info.xlsx)*
<img width="1196" alt="Datatable 'companies' from BD_Info.xlsx" src="https://github.com/iglebov/rpa_case/assets/41822761/df73b501-2140-48bc-9c38-206f6671b3ef">


2) To create Database 'cases' write text **from create_cases_table.txt** in database client
```
CREATE TABLE cases (
case_name CHAR ( 20 ) PRIMARY KEY,
judge VARCHAR ( 100 ) NULL,
plaintiff VARCHAR ( 100 ) NULL,
applicants TEXT [] NULL,
third_parties TEXT [] NULL,
other_parties TEXT [] NULL
);
```
Table **cases** *(visual, from file BD_info.xlsx)*

<img width="750" alt="Datatable 'cases' from BD_Info.xlsx" src="https://github.com/iglebov/rpa_case/assets/41822761/e047aa0c-9f9f-48b9-a6ba-b41f030640f2">

### How to see results

To see results you can check data in your database or execute **results.py** *(add data for database connection before executing)*
```
python results.py
```

## License

[WTFPL](https://en.wikipedia.org/wiki/WTFPL): do the f* (anything) you want.
