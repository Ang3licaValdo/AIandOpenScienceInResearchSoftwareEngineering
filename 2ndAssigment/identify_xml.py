import os

def identifying_xml(direc):
    content = os.listdir(direc)
    
    xmls = []
    for file in content:
        if os.path.isfile(os.path.join(direc, file)) and file.endswith('.xml'):
            xmls.append("Papers/"+file)

    return xmls

identifying_xml("./Papers")