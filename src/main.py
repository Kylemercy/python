import random
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lower = "abcdefghijklmnopqrstuvwxyz"
number = "0123456789"
symbol =" @#*.,&!?"
all = upper+lower+symbol+number
length = 15
password = "".join(random.sample(all, length))
print("The password generated for you is ", password)
name = input("what's your name? \n")
s_name = input("what's your surname? \n")
gmail = "@gmail.com"
mail =  number + symbol + gmail
len = 7
g_mail = "".join(random.sample(mail,len))
print(f"The email generated for you is {name}{s_name}{g_mail}{gmail}")
