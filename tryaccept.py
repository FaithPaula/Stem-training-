#try,except in python to catch errors

try :
   Div = 10/0
   value = int(input("Enter a number : "))
   print(value)
except  ValueError:
    print("invalid number entered")   
except ZeroDivisionError :
    print("Divided by Zero")  