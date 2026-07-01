#Autor:Bryan Adriano Nazareno Quiñonez
#Fecha:30/06/2026
#Tema:pr
def potencia(base,exponente):
    x = 1
    contador = 1
    while(contador <= exponente):
        x = x * base
        contador = contador +1
    
    return x

res = potencia(2,5)
print(f"El resultado de 2 elevado a la 5 es: {res}")


base = 3
exponente = 4
res = potencia(base,exponente)
print(f"El resultado de {base} elevdo ala {exponente} es{res}")

print(f"El resultado de 5 elevado al cubo es {potencia(5,3)}")

res = potencia(property(2,5))
print(f"El resultado de potencia (2, potencia(2,5)) es {res}")

#Parametros nombrados
res = potencia(exponente=4, base=3)
print(res)