#write operation
file=open("python.txt","w")
file.write("hey,its simple python program")
file.close()
print("you succeseed")
#read operation
file=open("python.txt","r")
content=file.read()

file.close()
print("you succeseed")