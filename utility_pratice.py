# def format_username(first_name, Last_name):
#     first = first_name.strip().lower()
#     last = Last_name.strip().lower()
#     return f"{first_name}.{last}"
# print(format_username("Vivek", "Dr"))
import configparser


# def format_usernames(first_name, Last_name):
#     first = first_name.strip().title()
#     last = Last_name.strip().lower()
#     return f"{first}.{last}"
# print(format_usernames("vivek", "Dr"))
#
# #value checker
# def empty_value_check(value):
#     if value == "":
#         return True
#     if isinstance(value,str) and value.strip() == "":
#         return True
#     return False
# print(empty_value_check(""))
# print(empty_value_check("vivek dr"))
#
# #email masking
# def email_mask(email):
#     name, domain = email.split("@")
#     if len(name)<=2:
#         masked_name = name[0]+"*"
#         print(masked_name,"---------")
#     else:
#         masked_name = name[0]+ "*" *(len(name)-2)+ name[-1]
#     return f"{masked_name}@{domain}"
# print(email_mask("vivek.dr.dev@gmail.com"))
#
# #list clear
# def list_clear(data):
#     result = []
#     for item in data:
#         if item not in result:
#             result.append(item)
#     return result
# print(list_clear([1,2,2,3,4,5,5]))


# logger
# def log(*args,**kwargs):
#     level = kwargs.get("level","INFO")
#     for message in args:
#         print(f"{level}:{message}")
# log("server started","Db connected",level="Debug")

# load configure

def load_config(**kwargs):
    return {
        "debug": kwargs.get("debug", True),
        "host": kwargs.get("host", "localhost"),
        "port": kwargs.get("port", 8000),
    }

