import datetime
import datetime as dt   #libray datetime, return all and more
import time             #libray date, return only date, week, hours, year,....

today = dt.datetime.now()
time = today.now()
hours = today.time()
day = today.today()
temp = today.ctime()
print("print time: ")
print(time)
print("hours: ",hours)
print("day: ", day)
print("tmp: ", temp)

