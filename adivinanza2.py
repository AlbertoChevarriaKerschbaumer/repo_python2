#ADIVINANZA
contador=1
numero=7
print ("Existe un numero secreto de 0 y 9 que debes adivinar, tienes 3 intentos!!!")
print("")
while contador<=3:
    a=int(input("ingresa el numero: "))
    if (a==numero):
        print("Bravo acertaste!!!")
        break
    else:
        contador=contador+1
print("")
print("La proxima vez sera!!!")
return