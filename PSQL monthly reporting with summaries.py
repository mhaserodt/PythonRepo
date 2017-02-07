# -*- coding: utf-8 -*-
"""
Created on Tue Feb  7 14:56:43 2017

@author: marc.haserodt
"""
#import stuff
import os
import psycopg2 as pg
import pandas as pd
from pandas.io.sql import read_sql
import datetime
#create datetime stuff so we can get the month.
#get today's date
today = datetime.date.today()
#create a variable that is the first day of the current month
first = today.replace(day=1)
#subtract 1 from the first day of the current month to get last month
lastMonth = first - datetime.timedelta(days=1)
#print just to make sure it's getting last month
print (lastMonth.strftime("%B"))

#make a new directory
newpath = r'C:\Users\marc.haserodt\Desktop\Reporting\\' + lastMonth.strftime("%b %Y") + '\\'
if not os.path.exists(newpath):
    os.makedirs(newpath)

#create filenames and sheetnames variables
#Filename = CompanyLastMonthReport.xlsx
filename = ('Company' + lastMonth.strftime("%B") + 'Report.xlsx')

#sheets LastMonth Captured, LastMonth Returns, LastMonth Sales
capturedsheet = (lastMonth.strftime("%B") + ' Captured')
returnssheet = (lastMonth.strftime("%B") + '  Returns')
salessheet = (lastMonth.strftime("%B") + '  Sales')
#Creates the excel file in the directory we created above.
writer = pd.ExcelWriter(newpath + filename)

#connect to Psql password must be stored in a .pgpass file(the better more secure option), or appended as pg.connect(password='')
conn = pg.connect("dbname='DB name here' user='user.name' host='hostname'")
cur = conn.cursor()

#Captured sheet SQL code.  In this example, needed data is in different tables.
company_captured =  """
select 
to_char(a.datecolumn::date, 'MM/DD/YYYY') as "Date"
,b.referenceID as "RefNumber"
,a.moneyamount::money as "Amount"
from schema1.table1 a
inner join  schema2.table2  b
on a.orderid = b.orderid
where a.companyid = 'CompanyIDNumber'
and (a.datecolumn::date >= date_trunc('month', current_date - interval '1' month)
and a.datecolumn::date < date_trunc('month', current_date))
order by 1 asc, 2 asc
"""
#create variable DF from the SQL results
df = read_sql(company_captured, conn, coerce_float=True)
#show a little of what's in DF
print ("Captured")
print (df.head())

#Captured sheet daily summary SQL code
company_captured_summary =  """
select 
distinct (to_char(datecolumn::date, 'MM/DD/YYYY')) as "Date"
,sum(moneyamount::money) as "Amount"
,((sum(moneyamount))*0.020)::money as "Fee @ 2.0%"
from schema1.table1
where companyid = 'CompanyIDNumber' and
(datecolumn::date >= date_trunc('month', current_date - interval '1 month') and datecolumn::date < date_trunc('month', current_date))
group by 1
"""
#create variable DF2 from the summary SQL results
df2 = read_sql(company_captured_summary, conn, coerce_float=True)
#show a little of what's in DF2
print ("Captured Summary")
print (df2.head())


#create sheet LastMonth Captured in the above created excel file and add results stored in DF and DF2
df.to_excel(writer, sheet_name=capturedsheet, index=False)
df2.to_excel(writer, sheet_name=capturedsheet, index=False, startcol=5)

#Sales sheet SQL code
company_sales =  """
select 
to_char(datecolumn::date, 'MM/DD/YYYY') as "Date"
,referenceID as "RefNumber"
,moneyamount::money as "Amount"
from schema3.table3
where companyid = 'CompanyIDNumber'
and datecolumn::date >= date_trunc('month', current_date - interval '1' month)
and datecolumn::date < date_trunc('month', current_date)
order by 1 asc, 2 asc
"""
#create variable DF from the SQL results
df = read_sql(ostock_sales, conn, coerce_float=True)
#show a little of what's in DF
print ("Sales")
print (df.head())


#Sales sheet daily summary SQL code
company_sales_summary =  """
select 
distinct (to_char(datecolumn::date, 'MM/DD/YYYY')) as "Date"
,sum(current_order_amount::money) as "Sales Amount"
from schema3.table3
where companyid = 'CompanyIDNumber' and
(datecolumn::date >= date_trunc('month', current_date - interval '1 month') and datecolumn::date < date_trunc('month', current_date))
group by 1
"""
#create variable DF2 from the summary SQL results
df2 = read_sql(company_sales_summary, conn, coerce_float=True)
#show a little of what's in DF2
print ("Sales summary")
print (df2.head())


#create sheet LastMonth Sales in the above created excel file and add results stored in DF and DF2
df.to_excel(writer, sheet_name=salessheet, index=False)
df2.to_excel(writer, sheet_name=salessheet, index=False, startcol=5)


#Returns sheet SQL code
company_returns =  """
select 
to_char(a.datecolumn::date, 'MM/DD/YYYY') as "Date"
,b.referenceID as "RefNumber"
,a.moneyamount::money as "Amount"
from schema4.table4 a
left join schema5.table5 b
on a.orderid= b.orderid
where b.companyid = 'CompanyIDNumber'
and a.datecolumn::date >= date_trunc('month', current_date - interval '1' month)
and a.datecolumn::date < date_trunc('month', current_date)
and a.amount > 0
-- group by a.datecolumn::date 
order by 1 asc, 2 asc 
"""
#create variable DF from the SQL results
df = read_sql(company_returns, conn, coerce_float=True)
#show a little of what's in DF
print ("Returns")
print (df.head())

#Returns sheet daily summary SQL code
company_returns_summary =  """
select 
distinct (to_char(a.datecolumn::date, 'MM/DD/YYYY')) as "Date"
,sum(a.moneyamount::money) as "Refunded Amount"
from schema4.table4 a
left join schema5.table5 b
on a.orderid= b.orderid
where b.companyid = 'CompanyIDNumber' and
(a.datecolumn::date >= date_trunc('month', current_date - interval '1 month') and a.datecolumn::date < date_trunc('month', current_date))
group by 1
"""
#create variable DF2 from the summary SQL results
df2 = read_sql(company_returns_summmary, conn, coerce_float=True)
#show a little of what's in DF2
print ("Returns")
print (df2.head())

#create sheet LastMonth Returns in the above created excel file and add results stored in DF
df.to_excel(writer, sheet_name=returnssheet, index=False)
df2.to_excel(writer, sheet_name=returnssheet, index=False, startcol=5)

#save the excel file  See sample excel file "CompanyJanuaryReport.xlsx"
writer.save()

#close connections
cur.close()
conn.close()