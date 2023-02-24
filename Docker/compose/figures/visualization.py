from bs4 import BeautifulSoup
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS
import numpy as np
from PIL import Image

number_of_figures_per_article = []

list_of_xml = ['1Report.xml','2Report.xml','3Report.xml','4Report.xml','5Report.xml','6Report.xml','7Report.xml','8Report.xml','10Report.xml','11Report.xml']


for paper in range(len(list_of_xml)):
    #Opening the file with the data i want to read
    with open(list_of_xml[paper], 'r') as f:
        data =  f.read()

    #Storing the returned information
    parser_data = BeautifulSoup(data, "xml")

    #Finding all instaces of the indicated tag

    find_tag = parser_data.find_all('figure')

    #Saving into a list the number of figures encountered in each Paper
    number_of_figures_per_article.append(len(find_tag))

article_names = ["Paper 1", "Paper 2", "Paper 3", "Paper 4", "Paper 5", "Paper 6", "Paper 7", "Paper 8", "Paper 9" , "Paper 10"]
# Creating graph and axis
fig, ax = plt.subplots()
# Creating the bar graph
bar_colors = ['#eeefff', '#6495ED', '#008B8B', '#FFB90F', '#CAFF70','#00CED1', '#F08080', '#FFEC8B', '#FFAEB9', '#FFA500']
ax.bar(article_names, number_of_figures_per_article, color=bar_colors)

ax.set_ylabel('Number of figures per paper')
ax.set_title('Number of figures in each paper.')

#saving the graph
plt.savefig('files/graph_figures.png')


