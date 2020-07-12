
import os
import shutil

dirs = 'ship'

main = 'zebra'

for root, subdirs, files in os.walk(dirs):

    print('root', root)
    print('subdirs', subdirs)
    print('files', files)
    for file in files:
        path = os.path.join(root, file)
        shutil.move(path, main)






import os
import shutil
print(dir(os))
print(os.listdir())


for file in os.listdir():
   if   file.endswith('.txt'):
     print(file)


filenames = ['boy.txt', 'tiger.txt','kite.txt']
with open('file.txt', 'w') as outfile:
    for o in filenames:
        with open(o) as infile:
            outfile.write(infile.read())

 
o = shutil.copy('file.txt', 'varsha.word')

#wap to get sum of all number value
#example data = [1,5[5,9],[9,][7,8,[2,3]],5]"a" , ["c",a]]

function using








import os
import shutil
print(dir(os))
#os.chdir(r'C:\Users\varun\OneDrive\Documents\new')
#os.rename('bhu.txt','satyam.txt')
#print(os.getcwd())
#os.mkdir('movies')


print(os.listdir(r'C:\Users\varun\OneDrive\Documents\new'))


#for file in os.listdir(r'C:\Users\varun\OneDrive\Documents\new'):
   #if   file.endswith('.txt'):
     #print(file)
#os.popen('copy mission.txt  shubham.txt')      

#o = shutil.copy('bobby.txt', 'ravi.xlml')
#os.popen('copy bobby.txt  shubham.csv')

#open('boy.txt','a').close()
#open('kite.txt','a').close()
#open('tiger.txt','a').close()
#open('file.txt','a').close()


filenames = ['boy.txt', 'tiger.txt','kite.txt']
with open('file.txt', 'w') as outfile:
    for o in filenames:
        with open(o) as infile:
            outfile.write(infile.read())
