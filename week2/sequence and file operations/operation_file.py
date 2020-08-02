import os
newfile=open("Mukesh.txt","r")

for i in range(1,20):
    text = str(i) + "\t hello, me you cool\n"
    newfile.write("\n Hello, welcome to Python:")


for i in range(1,10):
    print(newfile.read())

newfile.seek(5)
print(newfile.tell())
os.rename("Edureka.txt","Python.txt")
os.remove("Edureka.txt")

newfile.close()

