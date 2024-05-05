"""
PSEUDOCÓDIGO:
Algoritmo ordenacion_topologica (Busqueda en profundidad, a través de grafos) 
-Hipótesis: 
    Consultar el orden de tareas y no ir a la siguiente sin haber consultado la anterior.
-Entrada: 
    ingresar primera tarea, tarea siguente...(veces que haya tareas diferentes)
-Tratamiento datos:
    a través de dfs (busqueda en profundidad)
    ordenar tareas
-Salida:
    Establecer Grafo 

    --EJEMPLO--
Bienvenido al programa de ordenación topológica de grafos
Ingrese una arista en el formato 'nodo_origen nodo_destino' (o 'fin' para terminar): t1 t2
Ingrese una arista en el formato 'nodo_origen nodo_destino' (o 'fin' para terminar): t2 t3
Ingrese una arista en el formato 'nodo_origen nodo_destino' (o 'fin' para terminar): t3 t4
Ingrese una arista en el formato 'nodo_origen nodo_destino' (o 'fin' para terminar): fin

Grafo ingresado: {'t1': ['t2'], 't2': ['t3'], 't3': ['t4']}

Orden topológico: ['t1', 't2', 't3', 't4']
"""



def orden_topologico(grafo):
    visitados = set()
    stack = []

    def dfs(nodo):
        visitados.add(nodo)
        for vecino in grafo.get(nodo, []):
            if vecino not in visitados:
                dfs(vecino)
        stack.append(nodo)

    for nodo in grafo:
        if nodo not in visitados:
            dfs(nodo)

    return stack[::-1] #Devuelva desde la tarea previa obligatoria a la siguiente en orden.

def ingresar_tareas():
    grafo = {}
    while True:
        arista = input("Ingrese una tarea en el formato 'tarea_previa[t(1)] tarea_siguiente[t(2)]' (o 'fin' para terminar): ").split()
        if arista[0].lower() == 'fin':
            break
        if len(arista) != 2:
            print("Formato incorrecto. Debe ser 'tarea_previa tarea_siguiente'.")
            continue
        origen, destino = arista
        grafo.setdefault(origen, []).append(destino)
    return grafo

def main():
    print("Bienvenido al programa de ordenación topológica de grafos")
    grafo = ingresar_tareas()
    print("\nGrafo ingresado:", grafo)
    orden = orden_topologico(grafo)
    print("\nOrden topológico:", orden)

if __name__ == "__main__":
    main()
