<<<<<<< HEAD
#For generating a list of PSQL ilike statements.  Was created for a specific project but made generic to protect sensitive information

=======
#for generating a list of PSQL ilike statements
>>>>>>> 9df6081cc9aee484724a54e5b5b48d145322854d
alarms = ['alarm1',
'alarm2',
'alarm3',
'alarm4'
]


str2="%'"

print(alarms)
for rule in alarms: 
    print("or column ilike '%"+str(rule)+str2) 
    
