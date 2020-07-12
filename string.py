

a = input('enter the the string :')
b = {} 
for i in a:
    if i in b:
        b[i] += 1
    else: 
        b[i] = 1

print(str(b))






'''


a = input('enter the the string :')
b = {} 
for i in a:
    if i in b:
        b[i] += 1
    else: 
        b[i] = 1

print(str(b))


a = input("Enter string:")
b = a.swapcase()
print(b)
c = b.replace('2','#')
print(c)
d = c.replace('$','%')
print(d)

a = input("Enter string:")
b = a.replace(' ','-')
c = a.replace('/t','#')
d = a.replace('2','/')
print(b)
print(c)
print(d)



name = "tom" 
mychar = 'a' 

print(name)
print(mychar)


fruit1 = input('Please enter the name of first fruit:\n')
fruit2 = input('Please enter the name of second fruit:\n')

if fruit1 < fruit2:
    print(fruit1 + " comes before " + fruit2 + " in the dictionary.")
elif fruit1 > fruit2:
    print(fruit1 + " comes after " + fruit2 + " in the dictionary.")
else:
    print(fruit1 + " and " + fruit2 + " are same.")

a = 'WAP to count the number of words and number of characters in a given line of text except the spaces'
#a = 'WAP to extract specified number of characters from a given position from a string'
b = 'WAP to extract specified number of characters from a given position from a string'
if (a==b):
    print('This string is compare')
else:
    print('This string is not compare')






a = 'WAP to count the number of words and number of characters in a given line of text except the spaces'
b = 'WAP to extract specified number of characters from a given position from a string'
c = a+b
print(c)






str1 = input("Please Enter Your Own String : ")

str2 = str1
str3 = str1[:]

print("The Final String : Str2  = ", str2)
print("The Final String : Str3  = = ", str3)

a = 'WAP to count the number of words and number of characters in a given line of text except the spaces'
b = 'WAP to extract specified number of characters from a given position from a string'
c = a+b
print(c)


#a = 'WAP to count the number of words and number of characters in a given line of text except the spaces'
#b = a
#print(b)



a = 'suitimus'



v = reversed(a)

if list(a) == list(v):
    
    print("The string is a palindrome.")
else:
    
    print("The string is not a palindrome.")
    





a = 'WAP to count the number of words and number of characters in a given line of text except the spaces'
b = a[: : -1]
print(b)




a = 'WAP to count the number of words and number of characters in a given line of text except the spaces'
b = 'WAP to extract specified number of characters from a given position from a string'

if (len(a)>len(b)):
    print('a is lengthier')
else:
    print('b is lengthier')
    



a = 'WAP to count the number of words and number of characters in a given line of text except the spaces'
print(len(a))



a = 'WAP to count the number of words and number of characters in a given line of text except the spaces'
ch = 0
for ch in a:
    ch = a.count('a')
print(ch)

#a=''this is test code. python code'
# t = 3
# h =2
# is =4
# s =6
# e =4




a = int(input("enter the value :"))
sum = 0
for i in range(0, a+1):
    print(i)
    sum = sum + i
print(sum)
   




a = [34,78,45,12,78,57,91,65,44,98]
n = 0
for n in a:
    if(n%2==0):
        print('even')
    else:
        print('odd')

   

s=list(input("Enter the string :"))
n=[]

for j in s:
    if j not in n:
        n.append(j)
        count=0
        for i in range(len(s)):
            if j==s[i]:
                count+=1

        print("{},{}".format(j,count))


'''



