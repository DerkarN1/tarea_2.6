#Autor:Bryan Adriano Nazareno Quiñonez
#Fecha:30/06/2026
#Tema:
#funcion que cuenta el numero de cifras que tiene  un numero
def cuantascifras(num):
    if num<0:
        num=num*-1
    
    total = 0
    if num < 10:
        total=1
    elif num<100:
        total=2
    elif num<100:
        total=3
    
    return total





#funcion que cuenta el numero de cifras que tiene  un numero
def cuantascifras2(num):
    if num<0:
        num=num*-1
    
    total = 0
    n = 1
    while n < num:
        n = n *10
        total = total + 1
    
    return total

#Modificando una lista de enteros: paso por referencia
def modificalistaentero(lista):
    print("lista original ", lista)
    lista [0]= 22
    lista.append(10)
    print("nueva lista ", lista)
    
#Parametro opcionales en las funciones
def saludar(nombre="invitado", total=5):
    cont=0
    while cont < total:
        print(f"Hola {nombre}. Bienvenido!!")
        cont = cont + 1
        
#Diseñe la funcion que recibe 2 parametros opcionales. El primero indica la tabla de
#multiplicar y el segundo el limite a imprimir. Si no se pasan estos valores
#se imprimira la tabla del 10, desde 1 a 12

def tabla(num=10, limite=12):
    print("\nTabla de multiplicar{tabla}")
    for i in range(1, limite+1):
        print(f"{tabla} x {i} = {tabla*i}")
#    i = 0 
#    while i < limite:
#        print(num, "x" i + 1, "=", num * (i +1 ))
#        i = i + 1
        
#Funcion con un numero arbitrario de argumentos
def sumatoria(*numeros):
    suma = 0
    for n in numeros:
        suma = suma + n
        
    return suma

#funcion con parametros normales y arbitrario
def imprimirEquipo(campusPrincipal, *campus):
    print(f"\nEl campus principal es {campusPrincipal}")
    for cad in campus:
        print(f"Otros : {cad}")

num = -34
print(f"El numero de cifras de {num}es {cuantascifras(num)}")

num = 134
print(f"El numero de cifras de {num}es {cuantascifras2(num)}")
print(f"El numero de cifras de 1000 es {cuantascifras(1000)}")
print(f"El numero de cifras de 1234567890 es {cuantascifras(1234567890)}")

lista = [1,2,3,4]
modificalistaentero(lista)
print("La lista despues de la llamada a la funcion ", lista)

saludar()
print()
saludar("Ana")
saludar("Pedro",3)

tabla()
tabla(5)
tabla(3,6)

print(f"\nLa sumatoria de 1+2+3+4 es{sumatoria(1,2,3,4)}")
print(f"\nLa sumatoria de 1+2+3+4+5+6+7+8+9 es{sumatoria(1,2,3,4,5,6,7,8,9)}")
print(f"\nLa sumatoria de 1+2+3+4 es{sumatoria(10,110)}")
res= sumatoria(10,3,5) + sumatoria(3*3, 10, 90) + sumatoria(1,2)
print(f"\n El resultado de res es{res}")

imprimirEquipo("Campus administrativo", " Campus tachina", "Campus santa cruz"
              "Campus x", "Campus y" )
