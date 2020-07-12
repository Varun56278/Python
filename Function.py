
def sumdata(data):
    total = 0
    for element in data:
        if type(element)==type([]):
            total=total+sumdata(element)
        else:
                total=total+element
        return total
print(sumdata([2, 32,[34, 46],[56, 67]]))






def sum_1(arr):
    result = 0
    for x in arr:
        result += x
    return result

def sum_2(arr):
    result = sum(arr)
    return result
if __name__ == "__main__":
    arr = [10, 20, 30, 40, 50]
    print ('sum_1: {}'.format(sum_1(arr)))
    print ('sum_2: {}'.format(sum_2(arr)))















def getSum(piece):
    if len(piece)==0:
        return 0
    else:
        return piece[0] + getSum(piece[1:]) 
print(getSum([1, 3, 4, 2, 5]))
















def square_sum(n):
     if n==1:
         return 1
     else:
         return n*n +square_sum(n-1)
print(square_sum(4))









def counter(c):
    if c<=0:
        return c
    else:
        return c+counter(c-1)
print(counter(5))



def a(name):
    print("My name is" +name)

print(a("Sachin"))



