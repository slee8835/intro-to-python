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