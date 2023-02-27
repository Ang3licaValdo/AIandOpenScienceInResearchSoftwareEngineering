
# Second assigment 

This is the file that'll be used to describe the making of the second assigment of the subject mentioned on the README file, which consists in programming the next three points using Python:

1. Draw a keyword cloud based on the abstract information.
2. Create a visualization showing the number of figures per article.
3. Create a list of links found in each paper.

To complete this task GROBID is used to obtain the xml files of each pdf that is being analyzed for the assigment.


## Where to find the Python files

There is one python file for each of the three tasks mentioned above. Each of these files can be found inside the folder called '2ndAssigment'.

## Requirements
- Having Python installed. 
- Installing pip
- Python library: BeautifulSoup
- Python parser: lxml 
- Install Image
- Installing Numpy
- Installing Docker

## How to run the three python scripts with a virtual enviroment

Fist of all, you need to have pip installed. Pip is a package manager for installing and managing Python software packages


```bash
  sudo apt install python3-pip
```

Then you will like to create a virtual enviroment to run the scripts, for this, follow the next steps:
1. After you've downloaded the contents of this repository, open your terminal and change directories until you are located inside the '2ndAssigment' directory (you'll need to find the 'AIandOpenScienceInResearchSoftwareEngineering-main' directory wherever you dowloaded this repository first because the '2ndAssigment' directory is inside of it).
2. type the next command to install virtual enviroments:
```bash
  python3 -m pip install --user virtualenv
```
3. Set up the virtual enviroment (give it any name you like, in this next command the name is 'test'):
```bash
  python3 -m venv test
```
4. Activate your enviroment:
```bash
  source test/bin/activate
```
5. You'll need to install the next libraries inside the virtual enviroment, so after you see the parenthesis in your console with the name of your enviroment, just type the commands shown for each of the libraries requiered listed next, or to make this step easier and faster just type the next command in your terminal (you should be inside the '2ndAssigment' directory):

```bash
  pip install -r requirements.txt
```
If you want to install one by one, run the next commands:
- Installing BeautifulSoup

```bash
  pip install beautifulsoup4
```
  
- **Installing lxml**

```bash
  pip install lxml
```

- **Installing Image**

```bash
  pip install image
```
- **Installing NumPy**

```bash
  pip install numpy
```
- **Installing WordCloud**
```bash
  pip install wordcloud
```
## How to get your xmls from your own pdfs 
1. Make sure you have GROBID server running, you can do this using Docker (make sure you have it installed), and the run the next commands in another terminal:
- Pull the GROBID image: 
```bash
  docker pull lfoppiano/grobid:0.7.2
```
- Run the image:
```bash
  docker run -t --rm -p 8070:8070 lfoppiano/grobid:0.7.2
```
The web service will be running in http://localhost:8070/

2. Now copy and paste your pdfs inside the directory called 'Papers' that's inside the directory '2ndAssigment' that you downloaded when downloading this repository.
3. Now change directories in your terminal until you are inside the './AIandOpenScienceInResearchSoftwareEngineering-main/**2ndAssigment**' directory and run the next command:
```bash
  python request_grobid.py
```
This runs a Python script that'll connect to the GROBID server and download all of the XML of the pdfs inside the 'Papers' directory, it maight take a few minutes.
**NOTE: if the grobid server it's taking long just stop the container and start it again, and the run the prior command once more.

4. Chech the 'Papers' directory to make sure that all of the xmls are there and stop the docker container, after that, you can run each of the python scripts for each task, mentioned next:

## First task

The first task is about presenting the most important words found in the abstarct of each article in a word cloud, for this to happen, thanks to GROBID we have an xml from each of the pdfs chosen, to find what we need it's easy to analyze and xml with the Python library called BeautifulSoup, to get the text from the 'abstract' tag, first i had to find the tag with the method called 'find_all' and afterwards with the BeautifulSoup constructor and .text we got a string free of xml tags, then that string is used as a parameter for the method generate(string) that belongs to the wordcloud python library, that's the one in charge of creating the word cloud.

The code that does all of the things above is in a Python file called 'cloud.py' 

For executing the 'cloud.py' file, inside the '2ndAssigment' directory, run:
```bash
  python cloud.py
```

As an output you'll get eleven .png files, ten of them are a cloud with the keywords of each paper and the one named 'wordcloud_output.png' contains the keywords of the ten papers.

## Second task

For this task we have to represent in some way how many figures there are in each paper, for that i used a bar graph which data comes from finding all of the 'figure' tags with the method 'find_all' from BeautifulSoup and then counting the number of tags per paper and appending that number to a list. You'll get the bar graph as soon as you execute the Python file called 'visualization.py' 

For executing the 'visualization.py' file, inside the '2ndAssigment' directory, run:
```bash
  python visualization.py
```

As an output you'll get a bar graph, each bar represents how many figures there are in each article.

## Third task

For this task we have list the links encountered in each paper, i did it by first checking the xml and observing how GROBID identified the links, cause some of them were found inside paragraph, others were DOI and others were identified with the tag 'ptr' which belong to the references that have links where the information came from, after realizing this, i used the method 'find_all' from the BeautifulSoup library and obtained the attribute of the tag which contained the url or simply the text in case of the DOI and all of it was written into a file.

The code to obtain the .txt that contains the links to each paper is called 'link.py' 

For executing the 'link.py' file, inside the '2ndAssigment' directory, run:
```bash
  python link.py
```

As an output you'll get a .txt file that'll contain the link found in each pdf.

You'll find all of the prior outputs in a directory inside '2ndAssigment' called 'output_files'.

# How to execute this project with docker

First you have to make sure that you have your xmls ready to execute they Python scripts in a Docker container, for this, follow the next steps:

## How to get your xmls from your own pdfs 
1. Make sure you have GROBID server running, you can do this using Docker make sure you have it installed and the run the next commands in your terminal:
- Pull the GROBID image: 
```bash
  docker pull lfoppiano/grobid:0.7.2
```
- Run the image:
```bash
  docker run -t --rm -p 8070:8070 lfoppiano/grobid:0.7.2
```
The web service will be running in http://localhost:8070/

2. Now copy and paste your pdfs into the directory called 'Papers', that you'll find inside the directory called 'compose', which location is: './AIandOpenScienceInResearchSoftwareEngineering-main/Docker/compose' if you are inside the directory that was downloaded when downloading this repository.
 
3. Now in your terminal, make sure that you are inside the directory 'compose' which location is: './AIandOpenScienceInResearchSoftwareEngineering-main/Docker/compose', and run the next command:
```bash
  python request_grobid.py
```
This runs a Python script that'll connect to the GROBID server and download all of the XML of the pdfs inside the 'Papers' directory, this might take a few minutes.

## Running the Python scripts with Docker compose
Docker allows to create containers for applications, so they can be run in any computer without having issues with libraries and dependencies.
Since this project consists of three different Python scripts, it is good practice to have them each in a different container. Docker offers an option so you can run different applications at the same time, it's called Docker compose, to use it, you have to create a docker-compose.yml file and declare each application, its location in the file system and whatever else you want to add, like volumes.

For this project Docker compose was the easiest way of containerizing my Python files, because it allows for all of them to run at the same time and also adding a bind mount which is used to retrieve the output files that each file creates and stroing them in a directory in the host machine so the user can see the output since containers don't have a graphic enviroment.

For it to run in your computer, follow the next steps:

**IMPORTANT:** Make sure that you have docker compose downloaded on your machine so you can execute this project using containers.

1. Download the directory called Docker from this respository.
2. Open your console and change directories until you are inside the directory named 'Docker' and then change directories once more to the directory inside 'Docker' called 'compose'.
```bash
  cd Docker/compose
```
3. Once you are inside the 'compose' directory, run the next command on your terminal:
```bash
  docker-compose up --build
```
4. After you've run the prior command all of the output files from each of the Python files should be found on the directory called 'result_files' that can be found inside the directory 'compose'.
5. Now, type the next command:
```bash
  docker-compose down
```

And that's it! Now you have all of the output files in your computer :)
