saldo=1000
print("desea hacer un deposito o un retiro")
opcion=int(input("1-deposito\n2-retiro\n"))
if opcion==1:
    n=int(input("cuanto desea depositar: "))
    print("su saldo actual es: "+str(saldo+n)+"$")
else:
    n=int(input("cuanto desea retirar: "))
    print("su saldo actual es: "+str(saldo-n)+"$")
