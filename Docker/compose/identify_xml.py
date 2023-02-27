import os

def identifying_xml(directorio):
    contenido = os.listdir(directorio)
    xmls = []
    for fichero in contenido:
        if os.path.isfile(os.path.join(directorio, fichero)) and fichero.endswith('.xml'):
            xmls.append(fichero)
    #print(xmls)
    return xmls

