# -*- coding: utf-8 -*-
"""
Created on Fri Feb  3 13:51:58 2017

@author: marc.haserodt
A snippet of code used to get the prior month name
"""
## create a filename based on the date.

import psycopg2 as pg
import pandas as pd
from pandas.io.sql import read_sql
import datetime
today = datetime.date.today()
first = today.replace(day=1)
lastMonth = first - datetime.timedelta(days=1)
print (lastMonth.strftime("%B"))