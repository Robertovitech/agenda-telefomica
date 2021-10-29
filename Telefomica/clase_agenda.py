class Agenda:
    def __init__(self, datos):
        self.__datos = datos
    
    def input_values(self):
        self.__name = input('Ingrese su nombre y apellido: ').strip()
        self.__parentesco = input('Ingrese su parentesco (enter si no desea poner parentesco): ').strip()
        self.__telefono = input('Introduzca su numero de teléfono (9 dígitos): ').strip()
        self.check_inputs()
        
#----------Verifica los atributos del constructor, retorna True or False----------
    def check_inputs(self): 
        return self.__name.isdigit() == False and self.__parentesco.isdigit() == False and self.__telefono.isdigit() == True and len(self.__telefono) == 9
#----------------------------------------------------------------------------------

    def list_users(self):
        table = """\
+------------------------------------------------------------------------------------------+
|  ID  |            NOMBRE COMPLETO                   |     PARENTESCO    |    TELÉFONO    |
|------------------------------------------------------------------------------------------|
{}
+------------------------------------------------------------------------------------------+\
"""
        table = table.format('\n'.join(
            '| {:<5}| {:<45}|    {:<15}|    {:<9}   |'.format(*row)
            for row in self.__datos))
        print(table)

    def add_user(self):
        agrega_data = []
        
        if(self.check_inputs()):
            if(self.__datos == []):
                agrega_data.append(1)
            else:
                agrega_data.append(self.__datos[-1][0] + 1)
                
            agrega_data.append(self.__name)
            
            if(self.__parentesco == ''):
                agrega_data.append('-')
            else:
                agrega_data.append(self.__parentesco)
                
            agrega_data.append(int(self.__telefono))
            self.__datos.append(agrega_data)
            
            print('√ El usuario ha sido agregado con éxito.')
        else:
            print('--> Debe ingresar correctamente los datos. <--')
                  
    def edit_user(self):
        if(self.__datos != []):
            valor = False
            userID = input('Ingrese ID del usuario: ')
            for info in self.__datos:
                if(userID.isdigit() and int(userID) in info):
                    valor = True
                    elemento = info    
            if(valor):
                self.input_values()
                if(self.check_inputs()):
                    elemento[1] = self.__name
                    if(self.__parentesco != ''):
                        elemento[2] = self.__parentesco
                    else:
                        elemento[2] = '-'
                    elemento[3] = int(self.__telefono)
                    print(f'√ Usuario {userID} editado correctamente.')
                else:
                    print('--> Debe ingresar correctamente los datos. <--')
            else:
                print(f'--> No exite el usuario con ID {userID}. <--')
        else:
            print('--> No hay usuarios en el registro que se puedan editar. <--')

    def delete_user(self):
        if(self.__datos != []):
            valor = False
            userID = input('Ingrese ID del usuario: ')
            for index, info in enumerate(self.__datos):
                if(userID.isdigit() and int(userID) in info):
                    valor = True
                    elemento = index
            if(valor):
                decision = input(f'¿Seguro que desea eliminar al usuario {userID} S/N?: ').strip()
                if(decision == 'S' or decision == 's'):
                    del self.__datos[elemento]
                    print('El usuario ha sido eliminado')
                elif(decision == 'N' or decision == 'n'):
                    return
                else:
                    print('Debes eligir S o N')
            else:
                print(f'--> No existe usuario con ID {userID}. <--')    
        else:
            print('--> No hay usuarios en el registro que se puedan eliminar. <--')