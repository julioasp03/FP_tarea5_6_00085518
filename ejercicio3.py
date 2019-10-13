cont=0
n=0
ciclos="s"
while(ciclos !="n"):
    n=int(input("escriba un numero par: "))
    if n%2==0:
        cont+=1
    else:
        print(str(n)+" no es un numero par. ")
    ciclos=input("quiere escribir otro numero par?(s/n)")
print("ha escrito "+ str(cont) +" numeros pares")


