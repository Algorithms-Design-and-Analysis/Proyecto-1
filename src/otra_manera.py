import itertools

def calcular_combinaciones(n):
    caracteres = ['I', 'D']
    combinaciones = list(itertools.product(caracteres, repeat=n))
    return combinaciones

def contar_configuraciones_contador(configuracion_actual, forma_movimiento):
    
    resultados = []

    for configuracion in configuracion_actual:
        configuracion = configuracion.copy()
        for posicion in range(len(configuracion)):
            configuracion_1 = configuracion.copy()
            if "r" in configuracion_1[posicion] and forma_movimiento[int(configuracion_1[posicion][1])-1] == 'I' and posicion-1 >= 0 and 'r' not in configuracion_1[posicion-1]:
                configuracion_1[posicion-1] = configuracion_1[posicion]
                configuracion_1[posicion] = 'p'
                resultados.append(configuracion_1)
            elif "r" in configuracion_1[posicion] and forma_movimiento[int(configuracion_1[posicion][1])-1] == 'D' and posicion+1 <= len(configuracion_1)-1 and 'r' not in configuracion_1[posicion+1]:
                configuracion_1[posicion+1] = configuracion_1[posicion]
                configuracion_1[posicion] = 'p'
                resultados.append(configuracion_1)
            
    return resultados

def extraer_respuesta(matriz):

    configuraciones_unicas = [[]]
    
    for forma in matriz:
        movimiento_final = forma[-1]
        for configuracion in movimiento_final:
            if configuracion not in configuraciones_unicas:
                configuraciones_unicas.append(configuracion)
    
    return (len(configuraciones_unicas)-1) % 998244353

def contar_configuraciones(ranas_cantidad, configuracion_inicial, movimientos_realizar):
    
    
    # Calcula todas las permutaciones de movimientos posibles para cada rana, por ejemplo 
    # para dos ranas [(I,I), (I,D), (D,I), (D,D)]
    formas_movimientos = calcular_combinaciones(ranas_cantidad)

    # Matriz dp, cada fila corresponde a una forma de moverse y cada columna a la cantidad 
    # de movimientos realizados con esa forma. El caso base en la matriz es la columna 0
    # que contiene la configuracion inicial ya que solo existe un configuración sin hacer 
    # movimientos (la inicial)

    identificador = 1
    for posicion in range(len(configuracion_inicial)):
        if configuracion_inicial[posicion] == "r":
            configuracion_inicial[posicion] = "r" + str(identificador)
            identificador += 1

    formaMovimientos_cantidadMovimientos = [ [[configuracion_inicial] if i == 0 else [] for i in range(movimientos_realizar+1)] for _ in range(len(formas_movimientos)) ]

    # Iteracion sobre las formas de moverse
    for i in range(len(formaMovimientos_cantidadMovimientos)):
        # Iteracion sobre la cantidad de movimientos con esa forma de moverse
        for movimiento_realizar in range(1, movimientos_realizar+1):
            formaMovimientos_cantidadMovimientos[i][movimiento_realizar] = contar_configuraciones_contador(formaMovimientos_cantidadMovimientos[i][movimiento_realizar-1], formas_movimientos[i])

    # Busca entre las formas de moverse, cual es la que da más configuraciones despues de
    # realizar los m movimientos
    return extraer_respuesta(formaMovimientos_cantidadMovimientos)
    
def main():
    casos_numero = input()
    for _ in range(int(casos_numero)):
        caso = input().split(" ")
        print(contar_configuraciones(int(caso[1]), list(caso[3]), int(caso[2])))

if __name__=='__main__':
    main()