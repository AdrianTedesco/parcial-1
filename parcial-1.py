#hola mundo2x
matriz = []
matriz.append([1, 2, 3])
matriz.append([4, 5, 6])
matriz.append([7, 8, 9])
for fila in matriz:
    print(fila)

''' Crea un programa que pida un número al usuario un número de mes 
(por ejemplo, el 4) y diga cuántos días tiene 
(por ejemplo, 30). Debes usar una matriz para su parametrización 
y una función para la recuperación del dato'''

def obtener_dias_del_mes(mes):
    # Matriz con los días de cada mes (índice 0 = enero, índice 11 = diciembre)
    dias_por_mes = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    # Verificar si el mes está en el rango válido
    if 1 <= mes <= 12:
        return dias_por_mes[mes - 1]
    else:
        return "Mes inválido"

# Solicitar al usuario que ingrese un número de mes
mes = int(input("Introduce el número del mes (1-12): "))

# Obtener y mostrar el número de días del mes
dias = obtener_dias_del_mes(mes)
print(f"El mes {mes} tiene {dias} días.")
