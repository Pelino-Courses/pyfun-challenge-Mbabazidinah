from datetime import datetime #module importation
def dayBetweenDates(date1,date2,dateFormat="%Y-%m-%d"): #this is function creation
# this is parameter block and error checking
 try:
    date1=datetime.strptime(date1,dateFormat)
    date2=datetime.strptime(date2,dateFormat)
    #providing return of uotput
    return abs((date2-date1).days)
 except ValueError as e:
    raise ValueError(f"invalid format, user this format {dateFormat} error {e}")
 
day=dayBetweenDates("2025-8-5","2024-2-10") #object ctreation with dates examples.
print(day) #printing result