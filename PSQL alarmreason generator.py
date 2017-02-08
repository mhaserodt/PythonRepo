#for generating a list of PSQL ilike statements
alarms = ['alarm1',
'alarm2',
'alarm3',
'alarm4'
]


str2="%'"

print(alarms)
for rule in alarms: 
    print("or column ilike '%"+str(rule)+str2) 
    
