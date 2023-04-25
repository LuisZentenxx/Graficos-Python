#Se define la clase con un constructor com parámetros: nombre y nota del estudiante.
class Estudiante:
    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota

#Se crea un método para inscribir a los estudiantes.
def inscribir_estudiantes():
    num_estudiante = 1
    estudiantes = {} #Se crea un diccionario vacío para almacenar a los estudiantes.

    #Se utiliza un ciclo while para permitir registrar hasta 30 estudiantes mientas la longitud del diccionario sea menor a 30.
    while len(estudiantes) < 30:
        #Se pide al usuario que ingrese el nombre o la palabra OK, la función upper convierte el dato ingresado en mayusculas.
        nombre = input(f"\nIngrese el nombre del estudiante {num_estudiante} (sino 'OK' para finalizar) --> ").upper()


        #Si el usuario ingresa 'OK', se sale del ciclo while.
        if nombre == "OK":
            break

        #Si el nombre del estudiante ya fue ingresado anteriormente, se muestra un mensaje de error y continúa el ciclo.
        elif nombre in estudiantes:
            print("\nEl nombre ya ha sido registrado. Por favor ingrese otro nombre.")
            continue

        #Se solicita que el usuario ingrese la nota del estudiante dentro del rango establecido como un dato decimal.
        nota = float(input(f"Ingrese la nota del estudiante {num_estudiante} (entre 1.0 y 7.0): "))

        #Si la nota ingresada es inválida, se muestra un mensaje de error y continúa el ciclo.
        if nota < 1.0 or nota > 7.0:
            print("\nLa nota ingresada es inválida. Por favor ingrese una nota entre 1.0 y 7.0.")
            continue

        #Si el nombre y la nota del estudiante son válidos, se crea un objeto "Estudiante" y se agrega al diccionario "estudiantes".
        estudiantes[nombre] = Estudiante(nombre, nota)

        num_estudiante += 1

    #Se retorna el diccionario "estudiantes" con los datos ya registrados.
    return estudiantes

#Método para almacenar los datos de los estudiantes en un archivo de texto.
def almacenar_datos(estudiantes):
    #Aquí se abre el archivo "notas_estudiantes.txt" en modo escritura (w = write) y se le agrega un alias para su facil acceso.
    with open('notas_estudiantes.txt', 'w') as archivoEstudiantes:
        #Se recorre el diccionario y se escribe en el archivo cada nombre y nota separados por una coma y una línea nueva.
        for nombre, estudiante in estudiantes.items():
            archivoEstudiantes.write(nombre + ',' + str(estudiante.nota) + '\n')

#Función principal del programa.
def main():
    #Se llama a la función para registrar a los estudiantes.
    estudiantes = inscribir_estudiantes()

    #En cada iteracion se asigna la clave del diccionario a "nombre" y el valor del diccionario a "estudiante".
    #Y permite ver todos los elementos dentro del diccionario en forma de una lista de tuplas.
    print("Datos de los estudiantes registrados:") 
    for nombre, estudiante in estudiantes.items(): 
        print("Nombre: {}, Nota: {}".format(estudiante.nombre, estudiante.nota))

    #Se llama al método para almacenar los datos de los estudiantes en un archivo de texto.
    almacenar_datos(estudiantes)

#Se verifica si se está ejecutando este archivo como el programa principal.
if __name__ == '__main__':
    #Si se está ejecutando como programa principal, se llama a la función "main".
    main()
