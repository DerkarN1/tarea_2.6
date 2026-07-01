#Autor:Bryan Adriano Nazareno Quinonez
#fecha:30/06/2026
#Tema:Crea una función que simule el registro de un usuario con los parámetros nombre, rol y nivel_acceso.
#Usa condicionales para verificar si el rol es "Admin" y el nivel es mayor a 5 para otorgar permisos especiales. Invócala cambiando el orden de los argumentos.

def registrar_usuario(nombre, rol, nivel_acceso):
    print(f"Registrando a {nombre} ({rol}) con nivel {nivel_acceso}...")
    
    if rol == "Admin" and nivel_acceso > 5:
        print("¡Acceso concedido con permisos especiales de Administrador!")
    else:
        print("Acceso estándar otorgado.")

# Invocación cambiando el orden de los argumentos
registrar_usuario(nivel_acceso=8, nombre="Carlos", rol="Admin")

