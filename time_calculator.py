def add_time(start, duration, dayofweek = False):
    #stores the hour and minutes in variables, as well as the AM PM
    am_pm = start.split()[1]
    hour = int(start.split(":")[0])
    minute = int(start.split(":")[1].split()[0])
    duration_hour = int(duration.split(":")[0])
    duration_minute = int(duration.split(":")[1])
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    days_passed = 0

    #determine if the minutes result in an additional hour
    new_minute = int(minute) + int (duration_minute)
    if new_minute > 60:
      duration_hour += 1
      new_minute -= 60
    
    #get the new hour
    new_hour = hour + duration_hour
    
    #based on time of day, determine how many days have passed, and the actual hour
    if am_pm == "AM":
        if new_hour > 24:
            days_passed = new_hour//24
            new_hour = new_hour%24
        if new_hour > 12:
            new_hour -= 12
            am_pm = "PM"
        if new_hour == 12:
            am_pm = "PM"
        if new_hour == 0:
            new_hour = 12
            am_pm = "AM"


    elif am_pm == "PM":
        new_hour += 12
        if new_hour > 24:
            days_passed = new_hour//24
            new_hour = new_hour%24
        if new_hour > 12:
            new_hour -= 12
        else:
            am_pm = "AM"
        if new_hour == 0:
            new_hour = 12
            am_pm = "AM"


    #determines day of the week        
    if dayofweek != False:
        dayofweek = dayofweek.title()
        day_index = days.index(dayofweek)
        day_shift = days_passed%7
        final_day = day_shift + day_index
        if final_day > 6:
            final_day -= 7
        
        new_day = (days[final_day])


    if dayofweek == False:
        if days_passed == 0:
            new_time = "{0}{3}{1:02d} {2}".format(new_hour,new_minute,am_pm,":")
        elif days_passed == 1:
            new_time = "{0}{3}{1:02d} {2} (next day)".format(new_hour,new_minute,am_pm,":")
        else:
            new_time = "{0}{3}{1:02d} {2} ({4} days later)".format(new_hour,new_minute,am_pm,":",days_passed)
            


    else:
        if days_passed == 0:
            new_time = "{0}{3}{1:02d} {2}, {4}".format(new_hour,new_minute,am_pm,":",new_day)
        elif days_passed == 1:
            new_time = "{0}{3}{1:02d} {2}, {4} (next day)".format(new_hour,new_minute,am_pm,":",new_day)
        else:
            new_time = "{0}{3}{1:02d} {2}, {4} ({5} days later)".format(new_hour,new_minute,am_pm,":",new_day,days_passed)
        
    return new_time


#test cases
print(add_time("3:00 PM", "3:10"))
# Returns: 6:10 PM

print(add_time("11:30 AM", "2:32", "Monday"))
# Returns: 2:02 PM, Monday

print(add_time("11:43 AM", "00:20"))
# Returns: 12:03 PM

print(add_time("10:10 PM", "3:30"))
# Returns: 1:40 AM (next day)

print(add_time("11:43 PM", "24:20", "tueSday"))
# Returns: 12:03 AM, Thursday (2 days later)

print(add_time("6:30 PM", "205:12"))
# Returns: 7:42 AM (9 days later)

print(add_time("3:30 PM", "2:12", "Monday"))
# Returns: 5:42 PM, Monday