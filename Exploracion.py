"""
PSEUDOCÓDIGO:
Algoritmo Exploración
-Hipótesis: 
    Seleccionando un rango de una lista, trasladar el valor max a la derecha dentro de ese rango
-Precondición:
    iniciar lista no nula
    elementos separados por espacios
-Entrada: 
    lista
-Tratamiento datos:
    Seleccionar el rango
    Crear subtabla del rango
    Coger mayor valor y trasladarlo a la derecha
-Salida:
    Subtabla con valor max a la derecha
"""
def obtener_rango_lista(lista):
    while True:
        try:
            inicio = int(input("Ingrese el índice de inicio del rango (0 a {}): ".format(len(lista) - 1)))
            fin = int(input("Ingrese el índice de fin del rango ({} a {}): ".format(inicio, len(lista) - 1)))
            if inicio < 0 or fin >= len(lista) or inicio > fin:
                print("El rango especificado es inválido. Inténtelo de nuevo.")
                continue
            return inicio, fin
        except ValueError:
            print("Por favor, ingrese valores numéricos.")

def mover_maximo_al_final(lista, inicio, fin):
    lista_rango = lista[inicio:fin+1]  # Obtener el rango de la lista especificado
    max_valor = max(lista_rango)  # Obtener el elemento con el valor numérico más alto en el rango
    
    indice_max_valor = lista.index(max_valor, inicio, fin+1)
    lista.pop(indice_max_valor)  # Eliminar el elemento de mayor valor del rango
    lista.append(max_valor)  # Agregar el elemento de mayor valor al final de la lista
    
    return lista

def main():
    lista = input("Ingrese una lista de números separados por espacios: ").split()
    lista = [int(num) for num in lista]  # Convertir elementos de la lista a enteros
    print("Lista ingresada:", lista)
    
    inicio, fin = obtener_rango_lista(lista)
    nueva_lista = lista[:]
    rango_lista = mover_maximo_al_final(nueva_lista, inicio, fin)
    
    print("Lista con el elemento de mayor valor en el rango movido al final:", rango_lista)

if __name__ == "__main__":
    main()
