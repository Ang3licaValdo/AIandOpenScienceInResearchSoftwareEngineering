from bs4 import BeautifulSoup
from wordcloud import WordCloud, STOPWORDS
import numpy as np
from PIL import Image
import identify_xml

def verifyXML(XMLName):
    if '.xml' in XMLName:
        return 1
    else:
        return "not an XML file"

def openXML(xmlName):
    if verifyXML(xmlName) == 1:
        with open(list_of_xml[paper], 'r') as f:
            data =  f.read()
        return data

def createWordcloud(cloudText,i):
    #FOR THE WORDCLOUD OF EACH PAPER

    #frequent words that dont need to be included
    stopwords = STOPWORDS
    stopwords.add("et")
    stopwords.add("al")
    #image for the cloud shape
    mask = np.array(Image.open("cloud_image.webp"))

    #object for the wordcloud
    wc = WordCloud(background_color='white',stopwords=stopwords,height = 600,width=400, mask=mask)

    #generating the wordcloud
    wc.generate(cloudText)

    #creating an image of the wordcloud
    wc.to_file('files/wordcloud_paper' + i + '.png')


concat = ""
data = ""
concat_ind = ""

i = 1

#list_of_xml = ['1Report.xml','2Report.xml','3Report.xml','4Report.xml','5Report.xml','6Report.xml','7Report.xml','8Report.xml','10Report.xml','11Report.xml']
list_of_xml = identify_xml.identifying_xml("./")

for paper in range(len(list_of_xml)):
    
    #Storing the returned information
    parser_data = BeautifulSoup(openXML(list_of_xml[paper]), "xml")

    #Finding all instaces of the indicated tag

    find_tag = parser_data.find_all('abstract')

    #For that is going to concatenate all of the paragraphs
    for paragraph in range(len(find_tag)):
        concat = concat + str(find_tag[paragraph])

        concat_ind = concat_ind + str(find_tag[paragraph])
        concat_def = BeautifulSoup(concat_ind, "lxml").text

        if paragraph+1 == len(find_tag):
            #creating the wordcloud for each paper
            createWordcloud(concat_def,str(i))

            i = i+1

    concat_ind = ""   

#For removing xml tags:
concat_definite = BeautifulSoup(concat, "lxml").text

#creating a wordcloud of all of the pdf abstracts
createWordcloud(concat_definite, "_all_papers")
