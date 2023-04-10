from pymongo import MongoClient
from datetime import datetime

# Conexión a la base de datos
client = MongoClient()
db = client['gastos']

# Colección de gastos
gastos = db['gastos']

# Función para agregar un gasto a la base de datos
def agregar_gasto():
    descripcion = input('Ingrese una descripción del gasto: ')
    monto = float(input('Ingrese el monto del gasto: '))
    fecha = input('Ingrese la fecha del gasto en formato dd/mm/aaaa: ')
    fecha_datetime = datetime.strptime(fecha, '%d/%m/%Y')
    gasto = {'descripcion': descripcion, 'monto': monto, 'fecha': fecha_datetime}
    gastos.insert_one(gasto)
    print('Gasto agregado con éxito')

# Función para ver el gasto total
def ver_gasto_total():
    total = 0
    for gasto in gastos.find():
        total += gasto['monto']
    print(f'El gasto total es: {total}')

# Función para ver los gastos de un mes específico
def gasto_por_mes(mes):
    mes_datetime = datetime.strptime(mes, '%m/%Y')
    total = 0
    for gasto in gastos.find({'fecha': {'$gte': mes_datetime, '$lt': mes_datetime.replace(month=mes_datetime.month+1)}}):
        total += gasto['monto']
    print(f'El gasto total para el mes {mes} es: {total}')

# Programa principal
while True:
    print('¿Qué acción desea realizar?')
    print('1. Agregar gasto')
    print('2. Ver gasto total')
    print('3. Ver gastos de un mes')
    opcion = input('Ingrese 1, 2 o 3: ')

    if opcion == '1':
        agregar_gasto()
    elif opcion == '2':
        ver_gasto_total()
    elif opcion == '3':
        mes_ingresado = input('Ingrese un mes con el formato mm/aaaa: ')
        gasto_por_mes(mes_ingresado)
    else:
        print('Opción inválida')
