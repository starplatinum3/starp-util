
import datetime

now=datetime.datetime.now()

time1=now+datetime.timedelta(minutes=46)
print (time1)

# end_time=datetime.datetime(year=2022,hour=3, minute=0, second=0)
# end_time=datetime.datetime.now()
# end_time=datetime.time(hour=3, minute=0, second=0)
# end_time=datetime.datetime(year=now.year,month=now.month,day=now.day,hour=3, minute=0, second=0)
# end_time=datetime.datetime(year=now.year,month=now.month,day=now.day,hour=19, minute=38, second=0)
# start_time=datetime.datetime(year=now.year,month=now.month,day=now.day,hour=19, minute=38, second=0)
# start_time=datetime.datetime(year=now.year,month=now.month,day=now.day,hour=18, minute=30, second=0)
# start_time=datetime.datetime(year=now.year,month=now.month,day=now.day,hour=19, minute=1, second=0)
# start_time=datetime.datetime(year=now.year,month=now.month,day=now.day,hour=15, minute=5, second=0)
# start_time=datetime.datetime(year=now.year,month=now.month,day=now.day,hour=14, minute=45, second=0)
# start_time=datetime.datetime(year=now.year,month=now.month,day=now.day,hour=4, minute=45, second=0)
start_time=datetime.datetime(year=now.year,month=now.month,day=now.day,hour=14, minute=51, second=0)

# end_time=start_time+datetime.timedelta(hours=1,minutes=41)
# end_time=start_time+datetime.timedelta(hours=0,minutes=46+6+9+1+21)
# end_time=start_time+datetime.timedelta(hours=0,minutes=46)
end_time=start_time+datetime.timedelta(hours=3,minutes=49)
# end_time 2023-02-21 18:34:00
# end_time 2023-02-18 15:51:00
# end_time 2023-02-21 08:34:00
# end_time=start_time+datetime.timedelta(hours=1,minutes=41)
print("end_time",end_time)
# 2023-02-18 20:46:51.729911
# end_time 2023-02-18 16:28:00
# need_time 2023-02-18 13:07:00

# 2023-02-05 22:48:50.916384
# end_time 2023-02-05 20:11:00
# start_time=datetime.datetime(year=now.year,month=now.month,day=now.day,hour=19, minute=38, second=0)
# need_time=start_time-datetime.timedelta(hours=0,minutes=54+17+7)
# need_time=start_time-datetime.timedelta(hours=0,minutes=54+17+7+40)
# need_time=start_time-datetime.timedelta(hours=0,minutes=54+17+7+40)
need_time=start_time-datetime.timedelta(hours=1,minutes=38)

# need_time 2023-02-05 17:03:00
print("need_time",need_time)
# need_time 2023-02-05 17:12:00
# need_time 2023-02-05 16:32:00

# need_time 2023-02-05 18:20:00
# 2023-02-05 22:33:16.070707
# need_time 2023-02-05 18:20:00

# 7：38 - 54 
# 6：54-38=16
# 6： 44  24
# 6：20 
# 2023-02-05 22:24:34.626443
# end_time 2023-02-05 21:19:00

# now.hour=3
# now.minute=0
# now.second=0
# start_time=end_time-datetime.timedelta(minutes=46)
# print ("start_time")
# print (start_time)
# 2022-07-11 13:37:48.587907
# start_time
# 2022-07-11 02:14:00


def check_error(error):
    error_str=str(error)
    check_error_list=["ConnectTimeout",""]
    for check_error_name in check_error_list:
        if error_str in check_error_name:
            return True
    return False
