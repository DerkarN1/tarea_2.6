#Autor:Bryan Adriano Nazareno Quinonez
#fecha:30/06/2026
#Tema:Diseña una función que reciba una lista de números. Debe recorrerla para contar cuántos números son positivos, 
# cuántos negativos y cuántos son cero, devolviendo los tres conteos a la vez.

def clasificar_numeros(lista_numeros):
    positivos = 0
    negativos = 0
    ceros = 0
    
    for num in lista_numeros:
        if num > 0:
            positivos += 1
        elif num < 0:
            negativos += 1
        else:
            ceros += 1
            
    return positivos, negativos, ceros

# Ejemplo de uso:
mis_numeros = [-2, 5, 0, 10, -8, 0, 3]
pos, neg, cer = clasificar_numeros(mis_numeros)

print(f"Positivos: {pos}, Negativos: {neg}, Ceros: {cer}")
