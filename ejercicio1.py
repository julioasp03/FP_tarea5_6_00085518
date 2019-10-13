precio1=int(input("valor del primer dvd: "))
precio2=int(input("valor del segundo dvd: "))
precio3=int(input("valor del tercer dvd: "))
if (precio1 > precio2) and (precio1 > precio3):
    print("el total a pagar es: "+ str(precio2+precio3))
elif(precio2>precio1) and (precio2>precio3):
    print("el total a pagar es: "+ str(precio1+precio3))
else:
    print("el total a pagar es: "+ str(precio2+precio3))