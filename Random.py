
import random
print ("A random number between 0 and 1 is : ", end="") 
print (random.random()) 
  
# using seed() to seed a random number 
random.seed(5) 
  
# printing mapped random number 
print ("The mapped random number with 5 is : ", end="") 
print (random.random()) 
  
# using seed() to seed different random number 
random.seed(7) 
  
# printing mapped random number 
print ("The mapped random number with 7 is : ", end="") 
print (random.random()) 
  
# using seed() to seed to 5 again 
random.seed(5) 
  
# printing mapped random number 
print ("The mapped random number with 5 is : ",end="") 
print (random.random()) 
  
# using seed() to seed to 7 again  
random.seed(7) 
  
# printing mapped random number 
print ("The mapped random number with 7 is : ",end="") 
print (random.random()) 






import random
print ("A random number from list is : ",end="") 
print (random.choice([1, 4, 8, 10, 3]))

print ("A random number from range is : ",end="") 
print (random.randrange(20, 50, 3)) 





import random
a = random.randint(100, 200)
print(a)
