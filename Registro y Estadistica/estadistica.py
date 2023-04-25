def procesar_estadistica():

    notas = [] # Inicializa una lista vacía para guardar las notas
    aprobados = 0 # Inicializa la variable para el conteo de la cantidad de estudiantes aprobados
    reprobados = 0  #Inicializa la variable para el conteo de la cantidad de estudiantes reprobados

    with open('notas_estudiantes.txt', 'r') as archivo:   #Abre el archivo (notas_estudiantes) para leerlo

        for linea in archivo:   #Realiza una iteración sobre cada línea del archivo
            nombre, nota_str = linea.strip().split(',') #Separa el nombre y la nota de la línea
            nota = float(nota_str) #Convierte la nota de un string a un número decimal
            notas.append(nota) #Agrega la nota a la lista de notas

        #Si la nota es mayor a 4.0, en la variable aprobados se le agrega 1 (estudiante aprobado).
        #De lo contrario, a la variable reprobados se le agrega 1 (estudiante reprobado).
            if nota >= 4.0:
                aprobados += 1  
            else:
              reprobados += 1 
    
    #Se calcula la nota promedio, encuentra la nota máxima y minima del curso y devuelve los resultados como una tupla.
    nota_promedio = sum(notas) / len(notas)
    nota_maxima = max(notas)
    nota_minima = min(notas) 
    return (nota_promedio, nota_maxima, nota_minima, aprobados, reprobados)


def main():
    #Se llama a la función para procesar el archivo de las estadísticas
    nota_promedio, nota_maxima, nota_minima, aprobados, reprobados = procesar_estadistica()

    # Imprime la nota promedio, nota minima y máxima formateada como un número decimal con dos dígitos después del punto.
    print("Estadísticas del curso:")
    print("Nota promedio: {:.2f}".format(nota_promedio)) 
    print("Nota máxima: {:.2f}".format(nota_maxima))
    print("Nota mínima: {:.2f}".format(nota_minima))
    print("Cantidad de aprobados: {}".format(aprobados)) # Imprime la cantidad de estudiantes que han aprobados
    print("Cantidad de reprobados: {}".format(reprobados)) # Imprime la cantidad de estudiantes que han reprobado

#Permite llamar a la función principal si se está ejecutando como el programa principal
if __name__ == '__main__':
    main()
