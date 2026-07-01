#Autor:Bryan Adriano Nazareno Quinonez
#fecha:30/06/2026
#Tema:Crea una función que reciba una lista de calificaciones. Usa un bucle para revisar cada nota: si la nota es menor a 5, 
#súmale un punto de "asistencia". Si por error se incluye una nota superior a 10, la nota debe quedar en 10. La lista original debe quedar modificada.

def corregir_calificaciones(notas):
    for i in range(len(notas)):
        
        if notas[i] < 5:
            notas[i] += 1

        if notas[i] > 10:
            notas[i] = 10

# Ejemplo de uso:
mis_notas = [4.5, 3.0, 8.5, 11.2, 7.0]
corregir_calificaciones(mis_notas)
print("Notas modificadas:", mis_notas)

