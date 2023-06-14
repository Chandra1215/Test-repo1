import re
def change_date_format(dt):
        return re.sub(r'(\d{4})-(\d{1,2})-(\d{1,2})', '\\3-\\2-\\1', dt)
dt1 = "2026-01-02"
print("Original date in YYY-MM-DD Format: ",dt1)
print("New date in DD-MM-YYYY Format: ",change_date_format(dt1))

from datetime import datetime
import pytz

utc_time = datetime.utcnow()
print(utc_time)



# create a timezone object for UTC and PDT
# # utc_timezone = pytz.timezone('UTC')
# # pdt_timezone = pytz.timezone('America/Los_Angeles')

# # # convert the UTC time to PDT time
# # pdt_time = utc_timezone.localize(utc_time).astimezone(pdt_timezone)

# # # format the PDT time as a string
# # pdt_time_str = pdt_time.strftime('%Y-%m-%d %H:%M:%S %Z%z')

# # # print the PDT time
# # print(pdt_time_str)


# # import datetime

# # now = datetime.datetime.now()

# # print(now)

# # # Weekday name (full version)
# # weekday_name = now.strftime("%A")
# # # Month name (full version)
# # month_name = now.strftime("%B")

# # # Current date and time in desired format
# # date_time_format = "{} {}, {} {}".format(weekday_name, month_name, now.day, now.year)

# # print("Current date and time:", date_time_format, now.strftime("%H:%M:%S"))



# import datetime

# date_str = '05/05/2023'  # dd/mm/yyyy format
# # Weekday name (full version)
# weekday_name = date_str.strftime("%A")
# # Month name (full version)
# month_name = date_str.strftime("%B")

# # Current date and time in desired format
# date_time_format = "{} {}, {} {}".format(weekday_name, month_name, date_str.day, date_str.year)

# print("Current date and time:", date_time_format, date_str.strftime("%H:%M:%S"))

# # date_obj = datetime.datetime.strptime(date_str, '%d/%m/%Y')
# # utc_obj = date_obj.astimezone(datetime.timezone.utc)

# # print(f"Date in UTC: {utc_obj}")









# import datetime

# # create a datetime object in local time zone
# dt_local = datetime.datetime.now()

# # create a UTC time zone with an offset of +0523
# tz_offset = datetime.timezone(datetime.timedelta(hours=5, minutes=23))
# dt_utc = dt_local.astimezone(tz_offset)

# print(f"UTC time with offset: {dt_utc}")


# weekday_name = dt_utc.strftime("%A")
# # Month name (full version)
# month_name = dt_utc.strftime("%B")

# # Current date and time in desired format
# date_time_format = "{} {}, {} {}".format(weekday_name, month_name, dt_utc.day, dt_utc.year)

# print("Current date and time:", date_time_format, dt_utc.strftime("%H:%M:%S"))




import datetime

# create a datetime object from the given date and time
dt_obj = datetime.datetime(2023, 5, 5, 12, 22, 59)
print (dt_obj)

weekday_name = dt_obj.strftime("%A")
# Month name (full version)
month_name = dt_obj.strftime("%B")

# Current date and time in desired format
date_time_format = "{} {}, {} {}".format(weekday_name, month_name, dt_obj.day, dt_obj.year)

print("Current date and time:", date_time_format, dt_obj.strftime("%H:%M:%S"))


# get the UTC time zone
utc_tz = datetime.timezone.utc

# convert the datetime object to UTC time zone
dt_utc = dt_obj.astimezone(utc_tz)

# print the UTC datetime in ISO 8601 format
print(f"UTC datetime: {dt_utc.isoformat()}")



