# Este programa contiene múltiples violaciones 
# a las convenciones de nombres de variables

# Instrucciones:
#  - Analiza el programa y encuentra todas las violaciones 
#    a las convenciones de nombres de variables descritas 
#    en la lista de chequeo del capítulo 11 "The powe of 
#    variable names" del libro "Clean Code" de Robert C. Martin.
#  - Para cada violación, explica por qué el nombre no cumple
#    con la convención y propon un nombre alternativo que 
#    respete las buenas prácticas.
#  - Refactoriza el programa para corregir todas las violaciones
#    y asegúrate de que sea más legible y mantenible.

PI = 3.14159  # ¿Por qué se usa "PI" aquí?
# Porque es PI es una constante

valores = [10, 20, 30, 40, 50]  # ¿Qué representa "g"?
# Representa na lista de números, en este caso el nombre no cumple con la condición de describir lo que representa.
# Alternativa: valores
# valores = [10, 20, 30, 40, 50]

def calculo_estadísticas(x, y):
# calc tampoco describe su función de forma intuitiva
    media = sum(x) / len(x)  # ¿Qué representa "temp"?
    # Representa una división entre otras 2 variables, en este caso el nombre no cumple con la longitud propuesta como para deducir que representa.
    # Alternativa: media
    # media =  sum(x) / len(x)
    max_x = max(x)  # ¿Qué representa "z"?
    # Representa el valor máximo de x
    min_x = min(x)  # ¿Qué representa "w"?
    # Representa el valor mínimo de x
    return media, max_x, min_x
    # Estos nombres tampoco describen lo que representan
    # Alternativa: max_x y min_x
    # max_x = max(x)
    # min_x = min(x)

# RED = 1
# GREEN = 2
# BLUE = 3
# Estos nombres tampoco describen lo que representan pero tampoco cumplen una función en el código.

# Función con un nombre que no describe su propósito
# Alternativa: procesar_informacion
def procesar_informacion():
    # Uso de nombres de variables booleanas poco claros
    # Alternativa: ejecutar_proceso
    ejecutar_proceso = True  # ¿Qué significa "flag"?
    # Una varible de tipo booleano que indica si se debe ejecutar un proceso o no, en este caso el nombre no cumple con la condición de describir lo que representa.
    if ejecutar_proceso:
        # Uso de nombres de variables que no describen su propósito
        calcular_resultado = calculo_estadísticas(valores, PI)
        print("Resultados:", calcular_resultado)

for i in range(len(valores)):
# i vale en este caso porque es una varible de bucle
    print("Elemento", i, ":", valores[i])

# Llamada a la función principal
procesar_informacion()