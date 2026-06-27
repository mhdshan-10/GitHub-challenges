
# Armstrong number checker

num = int(input("enter a number :- "))

digits = len(str(num))
n = num
total = 0

while n > 0 :
    digit = n % 10
    total = total + digit ** digits
    n //= 10

if total == num :
    print("Armstrong Number")
else :
    print("Not Armstrong Number")

