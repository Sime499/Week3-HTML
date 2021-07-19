number=int(input("please enter a number:"))
factorial =1 

if number <0:
    print( "can not be factorial")

elif number is "0 "or "1" :
     print(1)

else: 
    for i in  range (number):
        factorial = factorial * (i+1)
print(factorial)

