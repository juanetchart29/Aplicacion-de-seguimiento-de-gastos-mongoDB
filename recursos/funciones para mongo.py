from pymongo import MongoClient

# Conectar a la base de datos de MongoDB
client = MongoClient("localhost", 27017)
db = client["mydatabase"]

# Obtener una colección de la base de datos
mycollection = db["mycollection"]

#agrego un nuevo documento a la coleccion
nuevo_documento = {"nombre":"Juan","edad":25}
mycollection.insert_one(nuevo_documento)

#obtener una lista de todos los documentos en la coleccion 
documentos = mycollection.find()
#imprimo todos los componentes de la lista 
for d in documentos:
    print(d)

#actualizar un documento ecistente en la colección
documento_actualizado = {"nombre":"Juan", "edad": 26}
#una vez definido el cambio utilizo replace_one para buscar el documento que quiero cambiar(se cambia todo)
mycollection.replace_one({"nombre":"Juan"},documento_actualizado)
