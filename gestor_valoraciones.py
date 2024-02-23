import json

def cargar_valoraciones():
    try:
        with open('valoraciones.txt', 'r') as file:
            lines = file.readlines()
            valoraciones = [json.loads(line.strip()) for line in lines]
    except FileNotFoundError:
        valoraciones = []
    except Exception as e:
        print(f"Error al cargar las valoraciones: {e}")
        valoraciones = []
    return valoraciones

def guardar_valoraciones(valoraciones):
    with open('valoraciones.txt', 'w') as file:
        for valoracion in valoraciones:
            json_str = json.dumps(valoracion)
            file.write(json_str + '\n')

def menu_consultas_valoraciones(juegos, valoraciones):
    while True:
        print("\nMenú de Consultas y Valoraciones:")
        print("1. Consultar juego")
        print("2. Valorar juego")
        print("3. Revisar puntuaciones (Top 3)")
        print("4. Volver al menú principal")

        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            consultar_juego(juegos)
        elif opcion == "2":
            valorar_juego(juegos, valoraciones)
        elif opcion == "3":
            revisar_puntuaciones(valoraciones)
        elif opcion == "4":
            print("Volviendo al menú principal...")
            break
        else:
            print("Opción no válida. Inténtalo de nuevo.")

def buscar_juego_por_nombre(juegos, nombre):
    for juego in juegos:
        if juego["nombre"].lower() == nombre.lower():
            return juego
    return None

def consultar_juego(juegos):
    nombre_a_consultar = input("Ingrese el nombre del juego a consultar: ")

    juego_existente = buscar_juego_por_nombre(juegos, nombre_a_consultar)

    if juego_existente:
        print("\nInformación del juego:")
        for key, value in juego_existente.items():
            print(f"{key.capitalize()}: {value}")
    else:
        print(f"Juego '{nombre_a_consultar}' no encontrado.")

def guardar_valoracion(valoraciones, nombre_juego, valoracion):
    nueva_valoracion = {"nombre": nombre_juego, "valoracion": valoracion}
    valoraciones.append(nueva_valoracion)

def valorar_juego(juegos, valoraciones):
    nombre_a_valorar = input("Ingrese el nombre del juego a valorar: ")

    juego_existente = buscar_juego_por_nombre(juegos, nombre_a_valorar)

    if juego_existente:
        valoracion = input("Ingrese la valoración del juego (1-5): ")
        if valoracion.isdigit() and 1 <= int(valoracion) <= 5:
            guardar_valoracion(valoraciones, nombre_a_valorar, int(valoracion))
            print(f"Juego '{nombre_a_valorar}' valorado exitosamente.")
        else:
            print("La valoración debe ser un número entre 1 y 5.")
    else:
        print(f"Juego '{nombre_a_valorar}' no encontrado.")

def revisar_puntuaciones(valoraciones):
    if valoraciones:
        top_juegos = sorted(valoraciones, key=lambda x: x['valoracion'], reverse=True)[:3]

        print("\nTop 3 Juegos con más Valoraciones:")
        for i, juego in enumerate(top_juegos, start=1):
            print(f"{i}. Juego: {juego['nombre']}, Valoración: {juego['valoracion']}")
    else:
        print("No hay valoraciones disponibles.")
    pass