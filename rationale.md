
# Second assigment 

This is the file that'll be used to describe the making of the second assigment of the subject, mentioned on the README file, which consists in propogramming the next three points with Python:

1. Draw a keyword cloud based on the abstract information.
2. Create a visualization showing the number of figures per article.
3. Create a list of links found in each paper.

To complete this task GROBID was used to obtain the xml file of each pdf that is being analyzed for this assigment, each pdf and each corresponding xml can be found in the 'Papers' folder.

## Where to find the Python files

Each of these files can be found in the folder called '2ndAssigment'.

## Requirements
- Having Python installed. 
- Installing pip
- Python library: BeautifulSoup
- Python parser: lxml 
- Install Image
- Installing Numpy

## Installing the Requirements in a virtual enviroment

Firs of all, you will like to create a virtual enviroment to run the scripts, for this, follow the next steps:
1. After you've downloaded the '2ndAssigment' directory, open your terminal and change directories until you are located inside the '2ndAssigment' directory.
2. type the next command to install virtual enviroments:
```bash
  python3 -m pip install --user virtualenv
```
3. Set up ithe virtual enviroment (give it any name you like, inn this next command the name is 'test'
```bash
  python3 -m venv test
```
4. Activate your enviroment:
```bash
  source env_3.10/bin/activate
```
5. As a final step, you'll need to install the next libraries inside the virtual enviroment, so after you see parenthesis in your console with the name of your enviroment, just type the commands shown for each of the libraries requiered listed next. 


### Installing pip for Linux Python 3

Pip is a package manager for installing and managing Python software packages


```bash
  sudo apt install python3-pip
```

### Installing BeautifulSoup

```bash
  pip install beautifulsoup4
```
  
### Installing lxml

```bash
  pip install lxml
```

### Installing Image

```bash
  pip install image
```
### Installing NumPy

```bash
  pip install numpy
```
### Installing WordCloud
```bash
  pip install wordcloud
```
## First task

The first task is about presenting the most important words found in the abstarct of each article in a word cloud, for this to happen, thanks to GROBID we have an xml from each of the pdfs chosen, to find what we need it's easy to analyze and xml with the Python library called BeautifulSoup, to get the text from the 'abstract' tag, first i had to find the tag with the method called 'find_all' and afterwards with the BeautifulSoup constructor and .text we got a string free of xml tags, then that string is used as a parameter for the method generate(string) that belongs to the wordcloud python library, that's the one in charge of creating the word cloud.

The code that does all of the things above is in a Python file called 'cloud.py' 

For executing the 'cloud.py' file:
```bash
  python cloud.py
```

As an output you'll get eleven .png files, ten of them are a cloud with the keywords of each paper and the one named 'wordcloud_output.png' contains the keywords of the ten papers.

## Second task

For this task we have to represent in some way how many figures there are in each paper, for that i used a bar graph which data comes from finding all of the 'figure' tags with the method 'find_all' from BeautifulSoup and then counting the number of tags per paper and appending that number to a list. You'll get the bar graph aas soons as you execute the Python file called 'visualization.py' 

For executing the 'visualization.py' file:
```bash
  python visualization.py
```

As an output you'll get a bar graph, each bar represents how many figures there are in each article.

## Third task

For this task we have list the links encountered in each paper, i did it by first checking the xml and observing how GROBID identified the links, cause some of them were found inside paragraph, others were DOI and others were identified with the tag 'ptr' which belong to the references that have links where the information came from, after realizing this, i used the method 'find_all' from the BeautifulSoup library and obtained the attribute of the tag which contained the url or simply the text in case of the DOI and all of it was written into a file.

The code to obtain the .txt that contains the links to each paper is called 'link.py' 

For executing the 'link.py' file:
```bash
  python link.py
```

As an output you'll get a .txt file that'll contain the link found in each pdf.

# How to execute this project with docker

Docker allows to create containers for applications, so they can be run in any computer without having issues with libraries and dependencies.
Since this project consists of three different Python scripts, it is good practice to have them each in a different container. Docker offers an option so you can run different applications at the same time, it's called Docker compose, to use it, you have to create a docker-compose.yml file and declare each application, its location in the file system and whatever else you want to add, like volumes.

For this project Docker compose was the easiest way of containerizing my Python files, because it allows for all of them to run at the same time and also adding a bind mount which is used to retrieve the output files that each file creates and stroing them in a directory in the host machine so the user can see the output since containers don't have a graphic enviroment.

For it to run in your computer, follow the next steps:

**IMPORTANT:** Make sure that you have docker compose downloaded on your machine so you can execute this project using containers.

1. Download the directory called Docker from this respository.
2. Open your console and change directories until you are inside the docker directory and then change directories once more to the directory inside 'Docker' called 'compose'.
```bash
  cd Docker
  cd compose
```
3. Once you are inside the 'compose' directory, run the next command on your terminal:
```bash
  docker-compose up --build
```
4. After you've run the prior command all of the output files from each of the Python files should be found on the directory called 'result_files' that can be found inside the directory 'compose'.

And that's it! Now you have all of the output files in your computer :)
