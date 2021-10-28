from clase_agenda import *

def main_menu(datos):
    print("""
    +=================================================+
    |                   TELEFOMICA                    |
    |  		          Agenda                      |
    |=================================================|
    | Menú principal                                  |
    | 1- Listar contactos                             |
    | 2- Agregar contacto                             |
    | 3- Editar contacto                              |
    | 4- Eliminar Usuario                             |
    | 5- Salir                                        |
    +=================================================+   
          """)
    option = input('¿Qué opción deseas elegir?: ')
    newUser = Agenda(datos)
    
    if(option.strip().isdigit() and int(option) == 1):
        newUser.list_users()
        
    elif(option.strip().isdigit() and int(option) == 2):    
        newUser.input_values()
        newUser.add_user()
    
    elif(option.strip().isdigit() and int(option) == 3):
        newUser.edit_user()
    
    elif(option.strip().isdigit() and int(option) == 4):
        newUser.delete_user()
    
    elif(option.strip().isdigit() and int(option) == 5):
        print('¡Que tengas un buen día, adios!')
        return
    else:
        print('-> Debes introducir correctamente las opciones de nuestro menú. <-')
        
    main_menu(datos)

#---------------------------------------------------------------------------------
datos = []
main_menu(datos)   