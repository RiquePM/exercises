import unittest
from datetime import datetime


#---------------------------------------------#
#               My Solution                   #
#---------------------------------------------#

def date_time(time):
    datetime_obj = datetime.strptime(time, '%d.%m.%Y %H:%M')
    datetime_str = datetime.strftime(datetime_obj, "%d %B %Y year %H hours %M minutes")
    if "1 hours" in datetime_str:
        datetime_str = datetime_str.replace("hours", "hour")
    if "1 minutes" in datetime_str: 
        datetime_str = datetime_str.replace("minutes", "minute") 
    datetime_lst = datetime_str.split() 
    for i in datetime_lst:
        if i[0] == "0":
            k = i[1:]
            datetime_lst.insert(datetime_lst.index(i), k)
            datetime_lst.remove(i)
    datetime_str = " ".join(datetime_lst)  
    return datetime_str

#---------------------------------------------#
#             Better Solutions                #
#---------------------------------------------#

#from datetime import datetime

#def checkio(time):
    #dt = datetime.strptime(time, '%d.%m.%Y %H:%M')
    #hour = 'hour' if dt.hour == 1 else 'hours'    
    #minute = 'minute' if dt.minute == 1 else 'minutes'
    #return dt.strftime(f'%-d %B %Y year %-H {hour} %-M {minute}') --> on windows: %# insted of %-

#def date_time(time):
    #d = datetime.strptime(time, "%d.%m.%Y %H:%M")
    #h = "hour" if d.hour == 1 else "hours"
    #m = "minute" if d.minute == 1 else "minutes"
    #return f"{d.day} {d.strftime('%B')} {d.year} year {d.hour} {h} {d.minute} {m}"

#def date_time(time: str) -> str:
    #dt = datetime.strptime(time, '%d.%m.%Y %H:%M')
    #return dt.strftime(f'%-d %B %Y year %-H hour{(dt.hour != 1)*"s"} %-M minute{(dt.minute != 1)*"s"}')    

#def checkio(dt):
    #dt = datetime.strptime(dt, '%d.%m.%Y %H:%M')
    #p = lambda attr: attr + 's' * (getattr(dt, attr) != 1)
    #return dt.strftime(f'%-d %B %Y year %-H {p("hour")} %-M {p("minute")}')

#---------------------------------------------#
#                   Tests                     #
#---------------------------------------------#

class TestDateTimeConverter(unittest.TestCase):
    def test_date_time_converter(self):
        self.assertEqual(
            date_time("01.01.2000 00:00"),
            "1 January 2000 year 0 hours 0 minutes"
            )

        self.assertEqual(
            date_time("09.05.1945 06:30"),
            "9 May 1945 year 6 hours 30 minutes"
            ) 

        self.assertEqual(
            date_time("20.11.1990 03:55"),
            "20 November 1990 year 3 hours 55 minutes"
            )

        # the datetime strftime() methods require year >= 1900
        #self.assertEqual(
        #    date_time("11.04.1812 01:01"),
        #    "11 April 1812 year 1 hour 1 minute"
        #    ) 


if __name__ == '__main__':
	unittest.main()
