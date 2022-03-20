# 1 Test MDP
password = input()
repeat = input()

def validate(text1, text2):
    if password == repeat:
       print("Correct")
    else:
       print("Not Correct")
validate(password, repeat) 

#2 Create their own PIN codes
pin = input()
try:
    pin = int(input)
    print("PIN code is created")
except ValueError:
    print("Please enter a number")  
    
#Primary conditions for password validation :
1.Minimum 8 characters.
2.The alphabets must be between [a-z]
3.At least one alphabet should be of Upper Case [A-Z]
4.At least 1 number or digit between [0-9].
5.At least 1 character from [ _ or @ or $ ]

import re

password = "R@m@_f0rtu9e$"
flag = 0
while True:
    if (len(password) < 8):
        flag = -1
        break
    elif not re.search("[a-z]", password):
        flag = -1
        break
    elif not re.search("[A-Z]", password):
        flag = -1
        break
    elif not re.search("[0-9]", password):
        flag = -1
        break
    elif not re.search("[_@$]", password):
        flag = -1
        break
    elif re.search("\s", password):
        flag = -1
        break
    else:
        flag = 0
        print("Valid Password")
        break

if flag == -1:
    print("Not a Valid Password")


