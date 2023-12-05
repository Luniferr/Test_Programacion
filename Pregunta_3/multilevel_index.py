"""Función que toma el listado `objects` y genera un diccionario nuevo que agrupa los datos en función de los valores de las llaves solicitadas en result"""

def multilevel_index(documents, keys):
    """Construye y devuelve un índice multinivel a partir de una lista de documentos y llaves específicas"""
    index = {}  

    for doc in documents: 
        actual_index = index  

        for key in keys:  
            value = doc[key]  
            if value not in actual_index:
                actual_index[value] = {} 
            actual_index = actual_index[value]  

        if "data" not in actual_index:
            actual_index["data"] = []  
        actual_index["data"].append(doc)  

    return index  


objects = [
    {
        "age": 12,
        "name": "Mateo",
        "last_name": "González",
    }, 
    {
        "age": 25,
        "name": "Arturo",
        "last_name": "González",
    }, 
    {
        "age": 12,
        "name": "Julián",
        "last_name": "Fernández",
    },
]

result = multilevel_index(objects, ["age", "last_name"])
print(result)
