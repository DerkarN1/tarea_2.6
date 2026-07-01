#Autor:Bryan Adriano Nazareno Quinonez
#fecha:30/06/2026
#Tema:Crea un sistema de cobro para un gimnasio. La función recibe la tarifa_base y un parámetro opcional es_estudiante (por defecto False).
#Si es estudiante, aplica un 20% de descuento. El programa debe retornar tanto el monto del descuento aplicado como el total final a pagar.

def calcular_cobro_gimnasio(tarifa_base, es_estudiante=False):
    if es_estudiante:
        descuento_aplicado = tarifa_base * 0.20 
    else:
        descuento_aplicado = 0.0
        
    total_final = tarifa_base - descuento_aplicado
    return descuento_aplicado, total_final

# Ejemplo de uso:
# Caso 1: Es estudiante
desc, total = calcular_cobro_gimnasio(50.0, es_estudiante=True)
print(f"Estudiante -> Descuento: ${desc:.2f}, Total: ${total:.2f}")

# Caso 2: No es estudiante
desc_regular, total_regular = calcular_cobro_gimnasio(50.0)
print(f"Regular    -> Descuento: ${desc_regular:.2f}, Total: ${total_regular:.2f}")


