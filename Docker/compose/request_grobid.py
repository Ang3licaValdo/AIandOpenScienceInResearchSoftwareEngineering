from grobid_client.grobid_client import GrobidClient
import identify_xml
import shutil
import os

#downloading the XML files from GROBID
client = GrobidClient(config_path="./grobid_client_python/config.json")
client.process("processFulltextDocument", "./Papers", n=2)

#Getting the xml
copy_xml = identify_xml.identifying_xml("./Papers")
#print(copy_xml)

#Copying the xml to each of the directories for every container
for file_xml in copy_xml:
    src = os.path.join("./Papers", file_xml) 
    dst1 = os.path.join("./clouds/Papers", file_xml) 
    dst2 = os.path.join("./links/Papers", file_xml)
    dst3 = os.path.join("./figures/Papers", file_xml)
    shutil.copy(src, dst1)
    shutil.copy(src, dst2)
    shutil.copy(src, dst3)