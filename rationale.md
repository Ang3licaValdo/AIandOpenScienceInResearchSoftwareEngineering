
# How I solved each of the three tasks

This is the file that'll be used to describe how i decided to approach each of the next three tasks: 

1. Draw a keyword cloud based on the abstract information.
2. Create a visualization showing the number of figures per article.
3. Create a list of links found in each paper.

To complete this task GROBID is used to obtain the xml files of each pdf that is being analyzed for the assigment.

## First task

The first task is about presenting the most important words found in the abstract of each article in a word cloud, for this to happen, thanks to GROBID we have an xml from each of the pdfs chosen, to find what we need it's easy to analyze an xml with the Python library called BeautifulSoup, to get the text from the 'abstract' tag, first i had to find the tag with the method called 'find_all' and afterwards with the BeautifulSoup constructor and .text got a string free of xml tags, then that string is used as a parameter for the method generate(string) that belongs to the wordcloud python library, that's the one in charge of creating the word cloud.

The code that does all of the things above is in a Python file called 'cloud.py' 

As an output you'll get eleven .png files, ten of them are a cloud with the keywords of each paper and the one named 'wordcloud_paper_all_papers.png' contains the keywords of the ten papers.

## Second task

For this task we have to represent in some way how many figures there are in each paper, for that i used a bar graph which data comes from finding all of the 'figure' tags with the method 'find_all' from BeautifulSoup and then counting the number of tags per paper and appending that number to a list. You'll get the bar graph as soon as you execute the Python file called 'visualization.py' as a png.

As an output you'll get a png file called 'graph_figures.png'.

## Third task

For this task we have list the links encountered in each paper, i did it by first checking the xml and observing how GROBID identified the links, cause some of them were found inside paragraphs, others were DOI and others were identified with the tag 'ptr' which belong to the references that have links where the information came from, after realizing this, i used the method 'find_all' from the BeautifulSoup library and obtained the attribute of the tag which contained the url or simply the text in case of the DOI and all of it was written into a text file.

The code to obtain the .txt that contains the links to each paper is called 'link.py'.

As an output you'll get a .txt file called 'links.txt', that'll contain the link found in each pdf.


**You'll find all of the prior outputs in a directory inside '2ndAssigment' called 'output_files'.**

