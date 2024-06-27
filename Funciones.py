import random

# Función para agregar una película al diccionario
def agregar_pelicula(peliculas):
    cod = random.randint(1, 1000)
    nombre = input("Ingrese el nombre de la película: ")
    anio = input("Ingrese el año de la película: ")
    categoria = input("Ingrese la categoría de la película: ")
    actores = input("Ingrese los actores de la película (separados por coma): ").split(',')
    director = input("Ingrese el nombre del director de la película: ")

    pelicula = {
        "cod": cod,
        "nombre": nombre,
        "anio": anio,
        "categoria": categoria,
        "actores": actores,
        "director": director
    }

    peliculas[cod] = pelicula
    print(f"Película {nombre} agregada correctamente.")

# Función para listar todas las películas
def listar_peliculas(peliculas):
    if not peliculas:
        print("No hay películas registradas.")
    else:
        print("Listado de películas:")
        for cod, pelicula in peliculas.items():
            print(f"Código: {cod}")
            print(f"Nombre: {pelicula['nombre']}")
            print(f"Año: {pelicula['anio']}")
            print(f"Categoría: {pelicula['categoria']}")
            print(f"Actores: {', '.join(pelicula['actores'])}")
            print(f"Director: {pelicula['director']}")
            print()

# Función para buscar películas por categoría
def buscar_pelicula_por_categoria(peliculas):
    categoria_buscada = input("Ingrese la categoría a buscar: ")
    encontradas = []

    for cod, pelicula in peliculas.items():
        if pelicula["categoria"].lower() == categoria_buscada.lower():
            encontradas.append(pelicula)

    if not encontradas:
        print(f"No se encontraron películas en la categoría '{categoria_buscada}'.")
    else:
        print(f"Películas encontradas en la categoría '{categoria_buscada}':")
        for pelicula in encontradas:
            print(f"Nombre: {pelicula['nombre']}")
            print(f"Año: {pelicula['anio']}")
            print(f"Actores: {', '.join(pelicula['actores'])}")
            print(f"Director: {pelicula['director']}")
            print()

# Función para sumar todos los años registrados en el diccionario de películas
def sumar_anios_peliculas(peliculas):
    suma_anios = 0
    for cod, pelicula in peliculas.items():
        suma_anios += int(pelicula['anio'])
    return suma_anios

# Función principal que ejecuta el menú
def menu():
    peliculas = {}
    while True:
        print("Menú:")
        print("1. Agregar película")
        print("2. Listar películas")
        print("3. Buscar película por categoría")
        print("4. Salir")

        opcion = input("Ingrese una opción: ")

        if opcion == '1':
            agregar_pelicula(peliculas)
        elif opcion == '2':
            listar_peliculas(peliculas)
        elif opcion == '3':
            buscar_pelicula_por_categoria(peliculas)
        elif opcion == '4':
            # Guardar las películas en un archivo txt antes de salir
            guardar_peliculas_en_archivo(peliculas)
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida. Intente de nuevo.")

# Función para guardar las películas en un archivo txt
def guardar_peliculas_en_archivo(peliculas):
    with open('peliculas.txt', 'w') as archivo:
        for cod, pelicula in peliculas.items():
            archivo.write(f"Código: {cod}\n")
            archivo.write(f"Nombre: {pelicula['nombre']}\n")
            archivo.write(f"Año: {pelicula['anio']}\n")
            archivo.write(f"Categoría: {pelicula['categoria']}\n")
            archivo.write(f"Actores: {', '.join(pelicula['actores'])}\n")
            archivo.write(f"Director: {pelicula['director']}\n\n")

# Iniciar el programa
if __name__ == "__main__":
    menu()
