from random import *
n=0
num=randrange(1,10)
cont=0
while(n!=num):
    n=int(input("ingrese un numero: "))
    if n>num:
        print(str(n)+" es mayor")
    elif n<num:
        print(str(n)+" es menor")
    else:
        print("felicidades")
    cont+=1
print("realizo "+str(cont)+" intentos")
