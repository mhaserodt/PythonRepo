# -*- coding: utf-8 -*-
"""
Created on Fri Feb  3 11:55:24 2017

@author: marc.haserodt
"""
#import stuff
import os
import psycopg2 as pg
import pandas as pd
from pandas.io.sql import read_sql
import datetime
#make a new directory
newpath = r'C:\Users\marc.haserodt\Desktop\Reporting\\' + lastMonth.strftime("%b %Y") + '\\'
if not os.path.exists(newpath):
    os.makedirs(newpath)

#create datetime stuff so we can get the month.
#get today's date
today = datetime.date.today()
#create a variable that is the first day of the current month
first = today.replace(day=1)
#subtract 1 from the first day of the current month to get last month
lastMonth = first - datetime.timedelta(days=1)
#print just to make sure it's getting last month
print (lastMonth.strftime("%B"))

#create filenames and sheetnames variables
#Filename ReportOutput.xlsx
filename = (lastMonth.strftime("%B") + 'ReportOutput.xlsx')

#sheets LastMonth Captured, LastMonth Returns, LastMonth Sales
capturedsheet = (lastMonth.strftime("%B") + ' Captured')
returnedsheet = (lastMonth.strftime("%B") + '  Returns')
salessheet = (lastMonth.strftime("%B") + '  Sales')
#Creates the excel file
writer = pd.ExcelWriter(newpath + filename)

#connect to Psql 
conn = pg.connect("dbname='DBname' user='user.name' host='db.link' password='PutPswdHere'")
cur = conn.cursor()

#Captured sheet SQL code
captured =  """
select 
a.column::date as "Date"
,b.Column2 as "RefNumber"
,round(a.column::numeric, 2) as "Amount"
from schema.table a
inner join  schema2.table2  b
on a.column1 = b.column2
where a.column = 'keyword'
and (a.datecolumn::date >= date_trunc('month', current_date - interval '1' month)
and a.datecolumna::date < date_trunc('month', current_date))
order by 1 asc, 2 asc
limit 5000
"""
#create variable DF from the SQL results
df = read_sql(captured, conn, coerce_float=True)
#show what's in DF
print (df)

#write sheet LastMonth Captured in the above created excel file and add results stored in DF
df.to_excel(writer, sheet_name = capturedsheet, index=False)

#Sales sheet SQL code
sales =  """
select 
date_column::date as "Date"
,column_Ref_number as "RefNumber"
,Column_amount::numeric as "Amount"
from schema.table
where column_ID = 'ID number'
and date_column::date >= date_trunc('month', current_date - interval '1' month)
and date_column::date < date_trunc('month', current_date)
order by 1 asc, 2 asc
limit 5000
"""
#create variable DF from the SQL results
df = read_sql(sales, conn, coerce_float=True)
#show what's in DF
print (df)

#write sheet LastMonth Sales in the above created excel file and add results stored in DF
df.to_excel(writer, sheet_name = salessheet, index=False)

#Returns sheet SQL code
returns =  """
select 
a.column_date::date as "Date"
,b.column_Ref_number as "RefNumber"
,round(a.amount::numeric,2) as "Amount"
from schema.table a
left join other_table b
on a.IDnumber= b.IDnumber
where b.column_id='ID numnber'
and a.column_date::date >= date_trunc('month', current_date - interval '1' month)
and a.column_date::date < date_trunc('month', current_date)
and a.amount > 0
-- group by a.column_date::date 
order by 1 asc, 2 asc 
limit 5000
"""
#create variable DF from the SQL results
df = read_sql(returns, conn, coerce_float=True)
#show what's in DF
print (df)

#create sheet LastMonth Returned in the above created excel file and add results stored in DF
df.to_excel(writer, sheet_name=returnedsheet, index=False)

#save the excel file
writer.save()

#close connections
cur.close()
conn.close()