# Create -> Crear e inserta
# Read -> Leer o Listar
# Update -> Actualizar
# Delete -> Borrar

import csv
import os


TABLA_CLIENTES = '.Clientes.csv'
SCHEMA_CLIENTES = ['nombre', 'compañia', 'email', 'cargo']
Clientes = []

# DECLARACIONES DE FUNCIONES
# ************************ #
# * Operaciones del CRUD * #
# ************************ #

def _inicializar_clientes_archivo():
    global Clientes

    with open(TABLA_CLIENTES, mode='r') as f:
        reader = csv.DictReader(f,fieldnames=SCHEMA_CLIENTES)

        for row in reader:
            Clientes.append(row)

def _grabar_clientes_archivo():
    global Clientes

    tmp_tabla_nombre = '{}.tmp'.format(TABLA_CLIENTES)
    with open(tmp_tabla_nombre, mode='w') as f:
        writer = csv.DictWriter(f, fieldnames=SCHEMA_CLIENTES)
        writer.writerows(Clientes)

    os.remove(TABLA_CLIENTES)
    os.rename(tmp_tabla_nombre, TABLA_CLIENTES)

def crear_usuario(cliente):
    global Clientes

    cliente_existe = buscar_usuario(cliente['nombre'])

    if cliente_existe:
        print('\nEl cliente ya existe en la Base de Datos\n')
    else:
        Clientes.append(cliente)
        print('\n!Hemos AGREGADO Correctamente el Cliente¡')

    input('Presiona ENTER para continuar\n')


def listar_usuario():
    global Clientes

    print('________________________________________________________________')
    print('| Indice | Nombre Cliente | Compañia   |    email    | Cargo')
    print('----------------------------------------------------------------')
    for index, cliente in enumerate(Clientes):

        print('    {uid}    | {nombre}       | {compania} | {email}      | {cargo}'.format(
            uid=index,
            nombre=cliente['nombre'],
            compania=cliente['compañia'],
            email=cliente['email'],
            cargo=cliente['cargo']
        ))

    input('\nPresiona ENTER para continuar\n')


def actualizar_cliente(index, cliente_actualizar):
    global Clientes

    # if len(Clientes) -1 >= index:
    for idx, cliente in enumerate(Clientes):
        if index == idx:
            Clientes[index] = cliente_actualizar
            print('\n!Cliente actualizado con exito¡')
            break
        else:
            print('\nNo fue posible actualizar el cliente, No se encuentra en la Base de Datos')
        
    input('Presiona ENTER para continuar\n')


def eliminar_usuario(index):
    global Clientes

    for idx, cliente in enumerate(Clientes):
        if index == idx:
            Clientes.pop(index)
            print('!Cliente eliminado con exito¡')
            break
    else:
        print('No fue posible Eliminar el cliente, No se encontró en la Base de Datos')
    
    input('Presiona ENTER para continuar\n')



def buscar_usuario(nombre_cliente):
    global Clientes 
    contar = 0

    for idx, cliente in enumerate(Clientes):
        if nombre_cliente == cliente['nombre']:
            print('________________________________________________________________')
            print('| Indice | Nombre Cliente | Compañia   |    email    | cargo')
            print('----------------------------------------------------------------')
            print('    {uid}    | {nombre}       | {compania} | {email} | {cargo}'.format(
            uid=idx,
            nombre=cliente['nombre'],
            compania=cliente['compañia'],
            email=cliente['email'],
            cargo=cliente['cargo']
            ))
            print('')
            return True
            break
        
        contar = contar + 1
    
    if contar >=2:
        # else:
        print('\nEl Cliente no existe en el sistema')
            
        
    input('\nPresiona ENTER para continuar\n')


def _obtener_nombre_campo(campo_nombre):

    while True:
        campo = str.capitalize(input('Por favor Ingresar {}: '.format(campo_nombre)))
        if campo.isdigit():
            print('!Este campo solo acepta texto¡')
        elif len(campo) == 0:
            print('!Este campo no debe estar vacio¡')
        else:
            break

    return campo

def _obtener_dicionario_cliente():
    
    diccionario = {
                'nombre': _obtener_nombre_campo('nombre'),
                'compañia': _obtener_nombre_campo('compañia'),
                'email': _obtener_nombre_campo('email'),
                'cargo': _obtener_nombre_campo('cargo')
            }
    return diccionario

# ******************** #
# Interfaz de USuario #
# ****************** #

def presentacion():
    while True:
        print('*****************************')
        print('* SISTEMA BUSQUEDA CLIENTES *')
        print('*****************************')
        print('')
        print('[C]rear Cliente')
        print('[L]istar Clientes')
        print('[A]ctualizar Cliente')
        print('[E]Liminar Cliente')
        print('[B]uscar Cliente')
        print('[S]alir')
        
        opcion = input('Por favor eliga una opción: ')
        print('')
        opcion = opcion.upper()
        
        if opcion in ['C', 'L', 'A', 'E', 'B', 'S']:
            return opcion
        else:
            input('!ALERTA¡ \nACABAS DE INGRESAR UN VALOR NO VALIDO\nPresiona ENTER para continuar\n')


# ******************** #
# Inicio del Programa #
# ****************** #
if __name__ == '__main__':
    
    _inicializar_clientes_archivo()
        
    while True:

        op = presentacion()
        
        # ****************
        # Crear Clientes *
        # ****************
        if op == 'C':
            
            cliente = _obtener_dicionario_cliente()
            crear_usuario(cliente)
        
        # *****************
        # Listar Clientes *
        # *****************
        elif op == 'L':

            listar_usuario()

        # *********************
        # Actualizar Clientes *
        # *********************
        elif op == 'A':
            
            while True:
                index_actualizar =input('Ingresa el Codigo del Cliente: ')
                if index_actualizar.isalpha():
                    print('!Este campo solo acepta un número¡')
                elif len(index_actualizar) == 0:
                    print('!Este campo no debe estar vacio¡')
                else:
                    index_actualizar = int(index_actualizar)
                    break
            
            print('Por favor actualiza la información')
            cliente_actualizar = _obtener_dicionario_cliente()
            actualizar_cliente(index_actualizar, cliente_actualizar)

        # *******************
        # Eliminar Clientes *
        # *******************
        
        elif op == 'E':#Eliminar Clientes
            
            while True:
                index_eliminar =input('Ingresa el Indice del Cliente: ')
                if index_eliminar.isalpha():
                    print('!Este campo solo acepta un número¡')
                elif len(index_eliminar) == 0:
                    print('!Este campo no debe estar vacio¡')
                else:
                    index_eliminar = int(index_eliminar)
                    break
            
            eliminar_usuario(index_eliminar)

        # *********************
        # Buscar Clientes *
        # *********************
        
        elif op == 'B':#Buscar Clientes
            
            nombre_cliente = _obtener_nombre_campo('nombre a buscar')
            buscar_usuario(nombre_cliente)

        # ******************************
        elif op == 'S':#Salir del programa
            _grabar_clientes_archivo()
            print('Se ha grabado Información y Ha salido del programa correctamente')
            print('!FIN¡')
            break
        else:
            break

    
    