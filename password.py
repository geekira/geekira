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
