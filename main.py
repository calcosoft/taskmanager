from taskmanager import TaskManager
from ia_service import create_simple_tasks



def print_menu():
    print("\nBienvenido al Task Manager\n")
    print("1. Añadir tarea")
    print("2. Listar tareas")
    print("3. Marcar tarea como completada")
    print("4. Eliminar tarea")
    print("5. Crear tareas simples")
    print("6. Salir")
    
def main():
    manager = TaskManager()

    while True:
        print_menu()
        try:
           choice = int(input("Elige una opcion: "))

           match choice:
            case 1:
                description = input("Ingrese la descripción de la tarea: ")
                manager.add_task(description)
            case 2:
                manager.list_tasks()
            case 3:
                id = int(input("Ingrese el ID de la tarea a marcar como completada: "))
                manager.complete_task(id)
            case 4:
                id = int(input("Ingrese el ID de la tarea a eliminar: "))
                manager.delete_task(id)
            case 5:
                description = input("Ingrese la descripción de la tarea compleja: ")
                subtasks = create_simple_tasks(description)
                for subtask in subtasks:
                    if not subtask.startswith("Error:"):
                        manager.add_task(subtask)   
                    else:
                        print(subtask)
                        break
            case 6:
                print("Saliendo del Task Manager.")
                break
            case _:
                print("Opción no válida. Por favor, seleccione una opción válida.")
        except ValueError:
          print("Opción no válida. Por favor, seleccione una opción válida.")



if __name__ == "__main__":
    main()
