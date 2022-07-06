import os

def openFile(path):
    try:
        file = open(path)
        dataSet = []
        for linea in file:
            data = linea.strip().split(",")
            dataSet.append(data)
        file.close()
        print("Archivo encontrado")
        return dataSet
    except IOError as e:
        print("No se encontro el archivo {}".format(e))