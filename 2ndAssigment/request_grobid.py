from grobid_client.grobid_client import GrobidClient
import identify_xml
import shutil
import os

#downloading the XML files from GROBID
client = GrobidClient(config_path="./config.json")
client.process("processFulltextDocument", "./Papers", n=2)

#Getting the xml
copy_xml = identify_xml.identifying_xml("./Papers")
