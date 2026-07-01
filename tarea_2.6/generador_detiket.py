#Autor:Bryan Adriano Nazareno Quinonez
#fecha:30/06/2026
#Tema:Diseña una función para generar un ticket de compra. Recibe el precio base y, de forma opcional, un porcentaje de descuento (por defecto 0). 
#Usa un condicional para aplicar el descuento solo si es mayor a cero.


def generar_ticket(precio_base, descuento=0):
    total = precio_base
    
    if descuento > 0:
        ahorro = precio_base * (descuento / 100)
        total -= ahorro
        print(f"Descuento aplicado ({descuento}%): -${ahorro:.2f}")
    else:
        print("No se aplicó ningún descuento.")
        
    print(f"Total a pagar: ${total:.2f}")
    return total

# Ejemplo de uso:
generar_ticket(100, 15)  # Con descuento del 15%
generar_ticket(50)       # Sin descuento