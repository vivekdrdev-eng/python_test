from datetime import datetime, date, timedelta

# now = datetime.now()
# print(now)

# def today(date_objet):
#     return datetime.strptime(date_objet, '%Y-%m-%d')
# print(today("2026-03-01"))
# from datetime import datetime
#
# date_string = "2026-03-01"
# date_object = datetime.strptime(date_string, "%Y-%m-%d")
# print(date_object)
# def days_cal(date_1 ,date_2):
#     d1 = datetime.strptime(date_1, '%Y-%m-%d')
#     d2 = datetime.strptime(date_2, '%Y-%m-%d')
#     difference = (d2 - d1)
#
#     return difference.days
# result = days_cal("2026-01-01", "2026-02-01")
# print(result,"days")

def get_next_date():
    today = datetime.now()
    return today + timedelta(days=7)
result = get_next_date()
print(result,"days")

def calculate_age(dob):
    today = datetime.today()
    return today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))
date_of_birth = date(1999,5,10)
print(calculate_age(date_of_birth))

def time_stamp():
    today = datetime.now().timestamp()
    return today
print(time_stamp())

