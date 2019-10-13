print("opcion 1: de fahrenheit a celcius\nopcion 2: de celcius a fahrenheit\nopcion 3: de kelvin a celius")
n=int(input("escoga una opcion: "))
if n==1:
    f=float(input("ingrese temperatura a convertir: "))
    convercion=(f-32)/(1.800)
    print("el resultado es "+str(convercion)+" grados celcius")
elif n==2:
    c=float(input("ingrese temperatura a convertir: "))
    convercion=(c*1.800)+32
    print("el resultado es "+str(convercion)+" grados fahrenheit")
else:
    k=float(input("ingrese temperatura a convertir:"))
    convercion=k-273.15
    print("el resultado es "+str(convercion)+" grados celcius")



