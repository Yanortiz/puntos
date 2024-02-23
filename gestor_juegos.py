import json

def cargar_juegos():
    try:
        with open('juegos.json', 'r') as file:
            juegos = json.load(file)
    except FileNotFoundError:
        juegos = []
    return juegos

def guardar_juegos(juegos):
    with open('juegos.json', 'w') as file:
        json.dump(juegos, file, indent=2)

def menu_gestion(juegos):
    while True:
        print("\nMenú de Gestión de Juegos:")
        print("1. Registrar juego")
        print("2. Modificar juego")
        print("3. Eliminar juego")
        print("4. Volver al menú principal")

        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            registrar_juego(juegos)
        elif opcion == "2":
            modificar_juego(juegos)
        elif opcion == "3":
            eliminar_juego(juegos)
        elif opcion == "4":
            print("Volviendo al menú principal...")
            break
        else:
            print("Opción no válida. Inténtalo de nuevo.")

def registrar_juego(juegos):
    nombre = input("Ingrese el nombre del juego: ")
    tiempo_por_partida = input("Ingrese el tiempo por partida (minutos): ")
    cantidad_jugadores = input("Ingrese la cantidad de jugadores: ")
    existencia = input("Ingrese la cantidad de juegos disponibles: ")

    nuevo_juego = {
        'nombre': nombre,
        'tiempo_por_partida': tiempo_por_partida,
        'cantidad_jugadores': cantidad_jugadores,
        'existencia': existencia
    }

    juegos.append(nuevo_juego)
    print(f"Juego '{nombre}' registrado exitosamente.")

def modificar_juego(juegos):
    nombre_a_modificar = input("Ingrese el nombre del juego a modificar: ")

    juego_existente = buscar_juego_por_nombre(juegos, nombre_a_modificar)

    if juego_existente:
        print(f"Modificando juego: {juego_existente['nombre']}")
        print("Deje el campo en blanco para mantener el valor actual.")

        tiempo_por_partida = input(f"Nuevo tiempo por partida ({juego_existente['tiempo_por_partida']} minutos): ")
        cantidad_jugadores = input(f"Nueva cantidad de jugadores ({juego_existente['cantidad_jugadores']}): ")
        existencia = input(f"Nueva cantidad de juegos disponibles ({juego_existente['existencia']}): ")

        juego_modificado = {
            'nombre': nombre_a_modificar,
            'tiempo_por_partida': tiempo_por_partida if tiempo_por_partida else juego_existente['tiempo_por_partida'],
            'cantidad_jugadores': cantidad_jugadores if cantidad_jugadores else juego_existente['cantidad_jugadores'],
            'existencia': existencia if existencia else juego_existente['existencia']
        }

        juegos.remove(juego_existente)
        juegos.append(juego_modificado)

        print(f"Juego '{nombre_a_modificar}' modificado exitosamente.")
    else:
        print(f"Juego '{nombre_a_modificar}' no encontrado.")

def buscar_juego_por_nombre(juegos, nombre):
    for juego in juegos:
        if juego['nombre'] == nombre:
            return juego
    return None
    


def eliminar_juego(juegos):
    nombre_a_eliminar = input("Ingrese el nombre del juego a eliminar: ")

    juego_existente = buscar_juego_por_nombre(juegos, nombre_a_eliminar)

    if juego_existente:
        confirmacion = input(f"¿Está seguro de eliminar el juego '{nombre_a_eliminar}'? (Sí/No): ").lower()
        if confirmacion == "si":
            juegos.remove(juego_existente)
            print(f"Juego '{nombre_a_eliminar}' eliminado exitosamente.")
        else:
            print("Operación de eliminación cancelada.")
    else:
        print(f"Juego '{nombre_a_eliminar}' no encontrado.")

def buscar_juego_por_nombre(juegos, nombre):
    for juego in juegos:
        if juego['nombre'] == nombre:
            return juego
    return None
    
pass
    
