#Autor:Bryan Adriano Nazareno Quinonez
#fecha:30/06/2026
#Tema:Crea una función que reciba una cantidad indeterminada de números. Recórrelos con un bucle y calcula la suma únicamente de los números que sean pares.

def sumar_pares(*numeros):
    suma = 0
    for num in numeros:
        if num % 2 == 0:  
            suma += num
    return suma

# Ejemplo de uso:
resultado = sumar_pares(1, 2, 3, 4, 5, 6, 7, 8)
print("La suma de los números pares es:", resultado)
