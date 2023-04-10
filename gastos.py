from pymongo import MongoClient
import datetime 

#me conecto a la base de datos (en mi caso local)
client = MongoClient("localhost",27017)
db = client["gastos"]

#creo una coleccion para las transacciones de datos
transactions = db["transactions"]

#Agreagamos una nueva transaccion de gasto a la base de dato
def agregar_gasto(cantidad,descripcion):
    nueva_transaccion = {
        "fecha": datetime.now(),
        "cantidad":cantidad,
        "descripcion": descripcion
    }
    transactions.insert_one(nueva_transaccion)
    print("Gasto agregado con éxito.") 


#Obtener una lista de todas las transacciones de gastos
def obtener_gastos():
    gastos=[]
    for t in transactions.find():
        gastos.append(t)
    return gastos


#una vez definidas las funciones y las variables hacemos un menu para interactuar
sigue = "S"
while sigue == "S":
    print(''' ¿Que accion desea realizar?
        
        1-Agregar gasto
        2-Ver gasto total
        3-Ver gastos de un mes
        ''')
    accion = int(input("Ingrese 1, 2 o 3: "))
    while accion != 1 and accion != 2 and accion != 3:
        accion = int(input("Error, ingrese una accion valida"))
        
    match accion:
        case 1:
            gasto = int(input("ingrese el gasto que desesa ingresar"))
            descripcion = input("ingrese la descripcion del gasto")
            agregar_gasto(gasto,descripcion)
            print("se ha ingresado exitosamente la transaccion")
            
        case 2: 
            print("los gastos totales son:  ")
            gastos = obtener_gastos()
            for g in gastos:
                print(g)
        
                
                
            
     
        
        
