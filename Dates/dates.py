import datetime

x = datetime.datetime.now()
print(x)

'''
Return the year and name of weekday:
'''
print(x.year)
print(x.strftime("%A"))

# Creating Date Objects

x = datetime.datetime(2020, 5, 17)
print(x)

# The strftime() Method

# Display the name of the month

x = datetime.datetime(2018, 6, 1)
print(x.strftime("%B"))
