from bs4 import BeautifulSoup
#Deefining  lists
list_of_xml = ['Papers/1Report.xml','Papers/2Report.xml','Papers/3Report.xml','Papers/4Report.xml','Papers/5Report.xml','Papers/6Report.xml','Papers/7Report.xml','Papers/8Report.xml','Papers/10Report.xml','Papers/11Report.xml']
list_of_links = []
list_of_words = []

#Defining variables
i = 1
concat = ""

#First for used to obtain info from all of the 10 papers
for paper in range(len(list_of_xml)):
    #Opening the xml file with the data i want to read
    with open(list_of_xml[paper], 'r') as f:
        data =  f.read()

    #Storing the returned information
    parser_data = BeautifulSoup(data, "xml")

    #Finding all instaces of the indicated tag
    find_tag = parser_data.find_all('p')
    #Creating a file where the links encountered will be stored
    f = open ('links.txt','a')
    f.write('Paper ' + str(i)+ ': \n')

    i = i+1

    #For that is going to concatenate all of the paragraphs
    for paragraph in range(len(find_tag)):
        #all of the paragraphs from every paper
        concat = str(find_tag[paragraph])
        #each paragraph without xml tags
        concat_definite = BeautifulSoup(concat, "lxml").text
        #tokenizing the string
        slicing = concat_definite.split()

        #analyzing each token lookin gif there's http in them to find links
        for word in range(len(slicing)):
            if 'http' in slicing[word]:                
                f.write(slicing[word]+'\n')
                list_of_words.append(slicing[word])
                

print("List of words: "+ str(list_of_words)) 
f.close()     

