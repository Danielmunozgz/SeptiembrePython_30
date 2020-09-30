#Crear menú con tres opciones: 
#1. Opcion 1: Temperaturas
#2. Opcion 2: Datos de Personas
#3. Opción 3: Salir 
import os
import math

def Temperaturas():
    print("***TEMPERATURAS***")
    #Ingresar N temperaturas
    #Mostrar el promedio de las temperaturas ingresadas
    sum=0
    veces=int(input("Cuantas temperaturas desea ingresar?: "))
    for x in range(veces):
        temp=float(input("Digite una temperatura: "))
        sum = sum+temp
    
    print("El promedio de las temperaturas ingresadas es: ", round((sum/veces),2))
    pausa=input("Presione una tecla para continuar")
    
def Personas():
    print("***DATOS PERSONAS***")
    pausa=input("Presione una tecla para continuar")

seguir=True
while seguir:
    os.system('cls')
    print("1. Temperaturas")
    print("2. Datos de Personas")
    print("3. Salir")
    op=int(input("Ingrese una opción 1,2,3: "))
    if(op==1):
        Temperaturas()
    elif(op==2):
        Personas()
    elif(op==3):
        print("Finalizando")
        break
    else:
        print("Ingrese una opción válida...")