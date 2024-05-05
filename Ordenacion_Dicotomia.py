"""
PSEUDOCÓDIGO:
Algoritmo ordenacion_dicotomia (Selection sort) 
-Hipótesis: 
    Reordenar tabla cogiendo un valor (evaluando) de la tabla original y en la tabla nueva por dicotomía evalúa su
    nueva posición
-Precondición:
    iniciar tabla no nula
    elementos separados por espacios
-Entrada: 
    Tabla
-Tratamiento datos:
    Coger elemento de arr
    Comparar con elementos ordenados de la nueva tabla (dicotomía repetitiva)
    Colocar en su posición
    Seguir con el siguiente
-Salida:
    Tabla reordenada
"""
import array

# Función de ordenación por inserción dicotómica
def ordenar_dicotomicamente(arr):
    n = len(arr)
    for i in range(0, n):
        evaluando = arr[i]
        inicial, final = 0, i
        while inicial < final:
            medio = (inicial + final) // 2
            if evaluando < arr[medio]:
                final = medio
            else:
                inicial = medio + 1
        for j in range(i, inicial, -1):
            arr[j] = arr[j-1]
        arr[inicial] = evaluando

# Función para ingresar un array desde la entrada estándar
def ingresar_array():
    try:
        elementos = list(map(int, input("Ingrese los elementos del array separados por espacios: ").split()))
        return array.array('i', elementos)
    except ValueError:
        print("Ingrese números enteros válidos.")
        return ingresar_array()

# Función principal del programa
def main():
    while True:
        print("\nMenú:")
        print("1. Ordenar un array")
        print("2. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            # Obtener el array del usuario
            array_desor = ingresar_array()

            # Ordenar el array por inserción dicotómica
            ordenar_dicotomicamente(array_desor)

            # Mostrar el array ordenado
            print("Array ordenado:", array_desor)

        elif opcion == "2":
            print("¡Hasta luego!")
            break

        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")

if __name__ == "__main__":
    main()
