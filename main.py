import gestor_juegos
import gestor_valoraciones

juegos = gestor_juegos.cargar_juegos()
valoraciones = gestor_valoraciones.cargar_valoraciones()

while True:
        print("Menú Principal:")
        print("1. Gestión de Juegos")
        print("2. Consultas y Valoraciones")
        print("3. Salir")

        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            gestor_juegos.menu_gestion(juegos)
        elif opcion == "2":
            gestor_valoraciones.menu_consultas_valoraciones(juegos, valoraciones)
        elif opcion == "3":
            print("Saliendo...")
            gestor_juegos.guardar_juegos(juegos)
            gestor_valoraciones.guardar_valoraciones(valoraciones)
            break
        else:
            print("Opción no válida. Inténtalo de nuevo.")
