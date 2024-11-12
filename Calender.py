#To print A calendar using Python.

from calendar import*
year = int(input('Enter Year: '))
print(calendar(year,2,1,8,2))

#2 = 2 characters for days (Mon,Tue, Wed,Thu,Fri,Sat)
#1 = 1 line (row) for each week
#8 = 8 rows for each month
#3 = 3 columns for all months of the year
#code_with_luiz: