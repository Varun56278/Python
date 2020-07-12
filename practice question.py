
quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {}."
print(myorder.format(quantity, itemno, price))


'''
quantity = 3
itemno = 567
price = 49.95
myorder = "I want {0} pieces of item {1} for {2} dollars."
print(myorder.format(quantity, itemno, price))
'''



'''
a = 5
b = 110
print('a = {0} , b = {1}'.format(a,b))
'''


'''
a = 5
b = 110
c = 97
d = 83
print('a = {} , b = {}'.format(a,b))
print('c = {} , d = {}'.format(c,d))
print('a = {0} , b = {}'.format(a,b))


'''





'''
#question = 2
def test(x,y=[]):
    y.append(x)
    return(y)
a = test(100)
b = test(200,[])
c = test(300)
print(a)
print(b)
print(c)
'''






'''
#question = 5
d = {1:'a', 2: 200,
     'b' : 300,
     'c':[5,9]}
#print(type(d))
v = str(d)
#print(type(v))
#print(v)
m = v.replace("{","")
#print(m)
n = m.replace(":","")
#print(m)
o = n.replace(",","")
#print(o)
p = o.replace(' ',"")
#print(p)
q = p.replace("'","")
#print(q)
r = q.replace("}","")
print(r)
print(len(r))
count1=0
count2=0

for i in r:
    if(i.isdigit()):
        count1=count1+1

    count2=count2+1
print("digit")    
print(count1)

print("word")    
print(count2)

'''












'''
#question = 5
d = {1:'a', 2: 200,
     'b' : 300,
     'c':[5,9]}
print(type(d))
v = str(d)
print(type(v))
print(v)

count1=0
count2=0

for i in v:
    if(i.isdigit()):
        count1=count1+1

    count2=count2+1
print("digit")    
print(count1)

print("ch")    
print(count2)

'''









'''
#question = 6
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


'''



















'''

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

'''





'''
#question = 3
a = [5,9,7]
print(a)
b = a
a[1] = 100
print(a)
print(b)

'''
