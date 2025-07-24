#Eroor handling is a proces, used to handle the errores in real prg
#using try and except block
#example
try:
    a=int(input("enter a number: "))
    print("yes,you'r in right way")
except ValueError:
    print("pleace enter integer value")
