











a = input("Enter the name of the file:")

lines = 0
words = 0
characters = 0
for line in a:
    wordslist = line.split()
    lines = lines + 1
    words = words + len(wordslist)
    characters = characters + len(line)
print(lines)
print(words)
print(characters)


a = input("Enter the name of the file:")
count = 0
count1 = 0
for i in a:
    b = a.upper()
    count = count + 1
    
    s = a.lower()
    count1 = count1 + 1

print(b)
print(s)

a = "this "
b = "is"
c = "a"
d = "ram"
print(a.capitalize() + b.capitalize() +  c.capitalize() +  d.capitalize())


ch = input("Enter the name of the file:")
vowels = 0
consonant = 0
special = 0
for i in ch:
  if (ch == 'a' or ch == 'e' or ch == 'i' 
                        or ch == 'o' or ch == 'u'): 
                vowels += 1
  else:
                consonant += 1


else: 
            special += 1
print(vowels)
print(consonant)
print(special)

word = 'WAP to input a multi word string and produce a string in which first letter of each word is capitalized'

result = word.find('letter')
print("Substring 'letter' found at index:",result)
 

a = input("Enter the name of the string:")
sub_str = input("Enter the name of the word:") 
if (a.find(sub_str) == -1): 
        print("NO") 
else: 
        print("YES")

