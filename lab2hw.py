##4
>>> bruce=6
>>> bruce+4
10

##5

# P= principal amount(initial investment)
# r= annual nominal interest rate (as a decimal)
# n= number of times the interest is compounded per year
# t= number of years 

p = 10000
n = 12
r = 0.08	#8%
t_years = input("number of years that the money will be compounded for:")
t = int(t_years)

#calculate final amount after t years
A = p*(1+(r/n))**(n*t)
print("final amount after t years:", A)


##6
>>> 5%2
1
>>> 9%5
4
>>> 15%12
3
>>> 12%15
12
>>> 6%6
0
>>> 0%7
0
>>> 7%0
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ZeroDivisionError: integer division or modulo by zero

zero is not a divisible number 



##7 & 8 
 
current_time = int(input("please input current time in 24 hour format:"))	
alarm_hr = int(input("please input number of hours to wait:"))
day_in_hour = 24

alarm_time = alarm_hr + current_time	#how many hours till alarm
alarm = 0		#alarm time
alarm_ampm = 0	#with AM or PM


#if alarm won't ring in the next 24 hours 
if alarm_time > day_in_hour:
	alarm_time2 = alarm_time/day_in_hour
	alarm = int((alarm_time2%1)*day_in_hour)	#to get rid of the day

#if alarm rings in the same day
else:
	alarm = alarm_time

if alarm <24 & alarm >12:
	alarm_ampm = alarm-12 
	print("alarm will ring at", alarm_ampm, "pm")

elif alarm == 24:
	print("alarm will ring at", 12, "am")
else:
	print("alarm will ring at", alarm, "am")
