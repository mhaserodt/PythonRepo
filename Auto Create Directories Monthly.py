# -*- coding: utf-8 -*-
"""
Created on Fri Feb  3 14:43:29 2017

@author: marc.haserodt
A snippet of code used in another project.
"""
## automatically creates a new directory named MONTH YEAR based on what the prior month was.
import os
import datetime
today = datetime.date.today()
first = today.replace(day=1)
lastMonth = first - datetime.timedelta(days=1)
print (lastMonth.strftime("%B"))

newpath = r'C:\Users\marc.haserodt\Desktop\\' + lastMonth.strftime("%b %Y") + '\\'
if not os.path.exists(newpath):
    os.makedirs(newpath)