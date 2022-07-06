from Rest.file import openFile
import requests

def sendInsert():
    try:
        data = openFile("Files/Clientes.txt");
        for i in data:
            employee = {"firstname" : i[0], "surname" : i[1],
                        "country" : {"name" : i[2],
                                     "airports" : [{"name": i[4]}]},
                        "likedLanguages": [{"name" : i[3]}]}
            print("Enviando petición...")
            resp = requests.post("http://localhost:8080/employee/apiv1/clientes/add", json=employee)
            print("Petición exitosa")
            print(resp)
            print(resp.json())
    except requests.exceptions.RequestException as e:
        print("Petición fallida: {}".format(e))