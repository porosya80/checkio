#!/home/porosya/.local/share/virtualenvs/checkio-VEsvC6M1/bin/checkio --domain=py run date-and-time-converter

# https://py.checkio.org/mission/date-and-time-converter/

# Computer date and time format consists only of numbers, for example: 21.05.2018 16:30
# Humans prefer to see something like this: 21 May 2018 year, 16 hours 30 minutes
# Your task is simple - convert the input date and time from computer format into a "human" format.
# 
# 
# 
# Input:Date and time as a string
# 
# Output:The same date and time, but in a more readable format
# 
# Precondition:
# 0<date<= 31
# 0<month<= 12
# 0<year<= 3000
# 0<hours<24
# 0<minutes<60
# 
# 
# END_DESC

MONTHS = {1: 'January', 2: 'February', 3: 'March',
          4: 'April', 5: 'May', 6: 'June',
          7: 'July', 8: 'August', 9: 'September',
          10: 'October', 11: 'November', 12: 'December'}


def date_time(time: str) -> str:

    return f'{int(time[:2])} {MONTHS[int(time[3:5])]} {time[6:10]} year {int(time[11:13])} {"hours" if int(time[11:13]) != 1 else "hour"} {int(time[14:])} {"minutes" if int(time[14:]) != 1 else "minute"}'