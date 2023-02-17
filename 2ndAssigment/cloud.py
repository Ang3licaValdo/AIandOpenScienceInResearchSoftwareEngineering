from bs4 import BeautifulSoup
from wordcloud import WordCloud, STOPWORDS
import numpy as np
from PIL import Image

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

def createWordcloud(cloudText):
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
    wc.to_file('wordcloud_paper' + str(i) + '.png')


concat = ""
data = ""
concat_ind = ""

i = 1

list_of_xml = ['Papers/1Report.xml','Papers/2Report.xml','Papers/3Report.xml','Papers/4Report.xml','Papers/5Report.xml','Papers/6Report.xml','Papers/7Report.xml','Papers/8Report.xml','Papers/10Report.xml','Papers/11Report.xml']


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
            createWordcloud(concat_def)

            i = i+1

    concat_ind = ""   

#For removing xml tags:
concat_definite = BeautifulSoup(concat, "lxml").text

#creating a wordcloud of all of the pdf abstracts
createWordcloud(concat_definite)
