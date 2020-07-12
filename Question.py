data = 'SACHIN IS A GOOD BOY. HE IS LEARNING PUBLIC SPEAKING. HE IS A SOFTWARE ENGINEER. '
numofchars = len(data)
numofwords = len(data.split())
numoflines = len(data.splitlines())
print(numofchars,numofwords,numoflines )









a = open(r'C:\Users\varun\OneDrive\Desktop\boy.txt')
data = a.read()
numofchars = len(data)
numofwords = len(data.split())
numoflines = len(data.splitlines())
print(numofchars,numofwords,numoflines)










num = int(input("enter the value of star"))
for i in range(1,num+1):
    print("* "*i)


num = int(input("enter the value of star"))
for i in range(num): 
    for j in range(num): 
         print("$", end=' ') 
    print()






Number = int(input(" Please Enter any Number: "))
count = 0

for i in range(2, (Number//2 + 1)):
    if(Number % i == 0):
        count = count + 1
        break

if (count == 0 and Number != 1):
    print(" %d is a Prime Number" %Number)
else:
    print(" %d is not a Prime Number" %Number)

    

o = open(r'C:\Users\varun\OneDrive\Desktop\kp.txt','r')

full_stops = 0

'''
for stop in o:
    full_stops+= stop.count('.')
print(full_stops)

'''







for stop in o:
    if  stop.endswith('.'):
        print(stop)
    else:
        print(stop.replace('\n','')+('.'))











a1 = int(input("enter the number of first student"))
a2 = int(input("enter the number of second student"))
a3  = int(input("enter the number of third student"))
a4 = int(input("enter the number of fourth student"))
a5 = int(input("enter the number of fifth student"))
total = a1 + a2 + a3 + a4 + a5 
print(total)
average = total/5
print(average)



a = int(input("enter the value of number"))
b = a*a
print(b)


a = int(input("enter the value of number"))
b = a*a*a
print(b)

d = int(input("enter the value of diameter of circle"))
r = d/2
print(r)
area = 3.14*r*r
print(area)

a = int(input("enter the number "))
b = int(input("enter the number "))
c  = int(input("enter the number"))
d = int(input("enter the number "))


cubea = a*a*a
print(cubea)

cubeb = b*b*b
print(cubeb)

cubec = c*c*c
print(cubec)

cubed = d*d*d
print(cubed)


if (cubea+cubeb+cubec==cubed):
    print("Condition satisfied")

else :
   print("Condition not satisfied")

l = int(input("enter the value of length of a rectangle  "))
b = int(input("enter the value of breadth of a rectangle "))
area = l*b
print(area)
perimeter = 2*(l+b)
print(perimeter)

a = int(input("enter the value of side of square"))
area = a*a
print(area)

principle = int(input("enter the number of principle"))
rate  = int(input("enter the number of rate"))
time = int(input("enter the number of time"))
simpleinterest = principle*rate*time/100
totalamount = principle*(1+rate*time)
print(simpleinterest)
print(totalamount)

DAYS_IN_WEEK = 7
  
  
def find( number_of_days ): 
  
    
    year = int(number_of_days / 365) 
    week = int((number_of_days % 365) / 
                DAYS_IN_WEEK) 
    days = (number_of_days % 365) % DAYS_IN_WEEK 
      
    print("years = ",year, 
          "\nweeks = ",week, 
          "\ndays = ",days) 
      
 
number_of_days = 200
find(number_of_days)

c = 'g'
print("The ASCII value of '" + c + "' is",ord(c))



a = int(input("enter the number"))
print(chr(a))


number_of_days = 200
DAYS_IN_WEEK = 7
    
year = int(number_of_days / 365) 
week = int((number_of_days % 365) / 
                DAYS_IN_WEEK) 
days = (number_of_days % 365) % DAYS_IN_WEEK 
      
print("years = ",year, 
          "\nweeks = ",week, 
          "\ndays = ",days) 
      
 
print(number_of_days)

a = int(input("enter the value"))
b = int(input("enter the value"))
quotient=a//b
remainder=a%b
print("quotient is "  ,  quotient)
print("remainder is " ,  remainder)



a = int(input("enter the value"))
b = int(input("enter the value"))
quotient=a//b
remainder=a%b
print("quotient is "  ,  quotient)
print("remainder is " ,  remainder)


a = int(input("enter the number "))
b = int(input("enter the number "))
if(a>b):
    print("Largest number is ",a)
else:
    print("Largest number is ",b)

inches = int(input("enter the number "))
yard = inches*0.0277
feet = inches*0.0833
print("yard is ",yard)
print("feet is ",feet)

b = int(input("enter the number "))
h = int(input("enter the number "))
areaoftriangle = 1/2*b*h
print(areaoftriangle)


Totalgrade = 100
grade = int(input("enter the value of mark"))
if grade>= 50:
  print("pass")
else:
 print("fail")

a = int(input("enter the number "))

if(a%2==0):
    print("even number is ",a)
else:
    print("odd number is ",a)

a = int(input("enter the first number"))
b = int(input("enter the second number"))
c = int(input("enter the third number"))
if(a>b):
    print("greater value is a =",a)
elif(b>c):
    print("greater value is b =",b)
else:
    print("greater value is c =",c)

totalgrage = 100
grade = int(input("enter the value of mark"))
if grade>= 40:
    print("pass")
else:
    print("fail")


age = int(input("enter the age of person"))
if(age>=18):
    print("eligible for license")
else:
    print("not eligible for license")


year = int(input("Enter Year"))


if year % 4 == 0 and year % 100 != 0:
    print(year, "is a Leap Year")
elif year % 100 == 0:
    print(year, "is not a Leap Year")
elif year % 400 ==0:
    print(year, "is a Leap Year")
else:
    print(year, "is not a Leap Year")

a = int(input("enter the value of number"))
if  (a%2==0):
  print("even")
else:
 print("odd")

a = int(input("enter the value"))
if(a%7==0):
    print("divisible by 7")
else:
    print("not divisible by 7")

name = str(input("enter the name"))
age = int(input("enter the age"))
if (age>=18):
    print(name,"teenager")
else:
    print(name,"child")

    
theory = int(input("enter the number "))
practical = int(input("enter the number "))
if(theory+practical>100):
    print("mark")
else:
    print(theory+practical)
    

import datetime
inputDate = input("Enter the date in format 'dd/mm/yy' : ")
day,month,year = inputDate.split('/')
isValidDate = True
try :
     datetime.datetime(int(year),int(month),int(day))
except ValueError :
      isValidDate = False
if(isValidDate) : 
        print ("date is valid ") 
else : 
        print ("date is not valid")

a = 0
while a<10:
     a+= 1
     print(a)

a = 11
while a > 1:
     a= a-1
     print(a)

a = 50
while a<90:
     a+= 1
     print(a)

n = int(input("enter number to calculate sum"))
average = 0
sum = 0
for num in range(0, n+1):
    sum = sum+num
print( sum )


n = int(input("enter number to calculate sum"))
sum = 0
for num in range(0, n+1,2):
    sum = sum+num
print( sum )


a = int(input("enter the value"))
for num in range(1,a+1):
    if(num % 2 == 0):
        print(num)

a = int(input("enter the value"))
for num in range(1,a+1):
    if(num % 2 == 1):
        print(num)



n = int(input("enter number to calculate sum"))
average = 0
sum = 0
for num in range(0, n+1):
    sum = sum+num
    average = sum / n
print( sum )
print(average)

n=int(input("Enter the number of terms: "))
sum1=0
for i in range(1,n+1):
    sum1=sum1+(1/i)
print("The sum of series is",round(sum1,2))

n = int(input("enter number to calculate sum"))
sum = 0
average = 0
for num in range(0,n+1):
    if(num % 2 == 0):
       print(num)
    sum = sum+num
average = sum/n
print("sum of even number",sum)
print("sum of even number",average)



n = int(input("enter number to calculate sum"))
sum = 0
average = 0
for num in range(0,n+1):
    if(num % 2 == 1):
       print(num)
    sum = sum+num
average = sum/n
print("sum of even number",sum)
print("average of even number",average)



n = int(input("enter number to maximum value"))
sum = 0
average = 0
for num in range(1,n+1):
    if(num % 2 == 0):
       print("{0}".format(num))
       sum = sum + num
       average =  sum/n
print("sum of even number",sum)
print("average of even number",average)

n = int(input("enter number to maximum value"))
sum = 0
average = 0
for num in range(1,n+1):
    if(num % 2 != 0):
       print("{0}".format(num))
       sum = sum + num
       average =  sum/n
print("sum of even number",sum)
print("average of even number",average)

n=int(input("Enter the number to print the tables :"))
for i in range(1,11):
    print(n,"x",i,"=",n*i)
    
a = "\nhe\n is a mobile"
print ("The string after resolving escape character is : ") 
print (a)


n = int(input("enter the value of factorial"))
factorial = 1
for i in range(1, n+1):
    factorial = factorial*i
print(factorial)

n=int(input("Enter an integer:"))
for i in range(1,n+1):
    if(n%i==0):
        print(i)

num = int(input("Enter  number : "))
print( bin(num))

num = int(input("Enter  number : "))
print( oct(num))

a =int(input("Enter the decimal value : "))
print( hex(a))

dec =int(input("Enter the binary value : "))

print(bin(dec))


dec =int(input("Enter the oct value : "))

print(oct(dec))

dec =int(input("Enter the oct value : "))

print(hexa(dec))

binary =int(input("Enter the oct value : "))

print(oct(binary))

binary =int(input("Enter the oct value : "))

print(hexa(binary))


a=int(input("Enter first number:"))
b=int(input("Enter second number:"))
c=int(input("Enter third number:"))
d=[]
d.append(a)
d.append(b)
d.append(c)
for i in range(0,3):
    for j in range(0,3):
        for k in range(0,3):
            if(i!=j&j!=k&k!=i):
                print(d[i],d[j],d[k])

a = float(input("enter the value"))
b = float(input("enter the value"))
if(a > b):
     maximum = a
else:
     minimum = b
while(True):
    if(maximum % a == 0 and minimum % b == 0):
        print("\n LCM of {0}and {1} = {2}".format(a,b, maximum))
        break;
    maximum = maximum + 1













string = input("enter the string")
count1=0
count2=0

for i in string:
    if(i.isdigit()):
        count1=count1+1

    count2=count2+1
print("digit")    
print(count1)

print("ch")    
print(count2)







d = {1:'a', 2: 200,
     'b' : 300,
     'c':[5,9]}
print(type(d))
print(d[2])

a = int(len(d))
print(a)
b = (len(d))
print(b)

print(d.keys())
print(d.values())
print(len(d.keys()))
print(len(d.values()))
























#question = 1
m = str([5,9,[1,2,[5,6]],9,6])
print(m)
print(type(m))
v = m.replace("[","")
print(v)
u = v.replace("]","")
print(u)
h = u.split(',')
print(h)
print(type(h))
print(len(h))    
sum = 0
for i in h:
    sum = sum + int(i)
print(sum)








#question = 3
a = [5,9,7]
print(a)
b = a
a[1] = 100
print(a)
print(b)
















#Python Program for Program to find area of a circle
r = int(input("enter the value"))
c = 3.14*r*r
print(c)


#Python Program for compound interest
p = int(input("enter the value"))
r = int(input("enter the value"))
t = int(input("enter the value"))
n = int(input("enter the value"))
a = p*(1+r/n)*pow(nt)
print(a)

#Python Program for simple interest
p = int(input("enter the value"))
r = int(input("enter the value"))
t = int(input("enter the value"))
m = p*r*t/100
print(m)


#Python Program for factorial of a number
num = int(input("enter the value"))
factorial = 1
for i in range(1,num + 1):
       factorial = factorial*i
print("The factorial of",num,"is",factorial)


#Python Program for factorial of a number
num = int(input("enter the value"))
factorial = 1

if num < 0:
   print("Sorry, factorial does not exist for negative numbers")
elif num == 0:
   print("The factorial of 0 is 1")
else:
   for i in range(1,num + 1):
       factorial = factorial*i
print("The factorial of",num,"is",factorial)



#Python program to add two numbers
a = int(input("enter the value"))
b = int(input("enter the value"))
c = a/b
print(c)


