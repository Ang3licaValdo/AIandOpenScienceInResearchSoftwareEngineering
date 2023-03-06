[![DOI](https://zenodo.org/badge/596545346.svg)](https://zenodo.org/badge/latestdoi/596545346)

# AI and Open Science In Research Software Engineering subject repository with deliverables 

This repository has been created with the purpose of uploading all the deliverables of the subject called "AI and Open Science In Research Software Engineering".

The assigment consists of analysing each paper and doing what's asked of me in the following steps, using Python as the language of choice.

- Draw a keyword cloud based on the abstract information.
- Create a visualization showing the number of figures per article.
- Create a list of links found in each paper. 

The explanation of how I solved the three tasks mentioned above is in the file called **"rationale.md"**

**DISCLAIMER: YOU CAN RUN THIS SOFTWARE USING A VIRTUAL ENVIROMENT OR DOCKER, THE INSTRUCTIONS FOR RUNNING IT WITH DOCKER CAN BE FOUND ALMOST AT THE BOTTOM OF THIS READ ME FILE FROM THE 'How to execute this project with docker' SUBTITLE, ALSO YOU CAN CHECK IT OUT WITH EXAMPLES ON THIS DOCUMENTATION LINK: https://aiandopenscienceinresearchsoftwareengineering.readthedocs.io/en/latest/run_docker.html**


## Requirements
- Having Python installed. 
- Installing pip
- Python library: BeautifulSoup
- Python parser: lxml 
- Install Image
- Installing Numpy
- Installing Docker
- Docker compose

## How to run the three python scripts with a virtual enviroment

First of all, you need to have pip installed. Pip is a package manager for installing and managing Python software packages


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
5. You'll need to install the next libraries inside the virtual enviroment, so after you see the parenthesis in your console with the name of your enviroment, just type the commands shown for each of the libraries required listed next, or to make this step easier and faster just type the next command in your terminal (you should be inside the '2ndAssigment' directory):

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
3. Now if you are not inside the '2ndAssigment' directory in your terminal already, change directories until you are inside the './AIandOpenScienceInResearchSoftwareEngineering-main/**2ndAssigment**' directory and run the next command:
```bash
  python request_grobid.py
```
This runs a Python script that'll connect to the GROBID server using the Python client given by GROBID, and downloads all of the XML of the pdfs inside the 'Papers' directory, it might take a few minutes.
**NOTE:** if the grobid server it's taking long just stop the container and start it again by running the prior command once more.

4. Chech the 'Papers' directory to make sure that all of the xmls are there and stop the docker container, after that, you can run each of the python scripts for each task, mentioned next:

## How to run the Python file of the first task

Execute the 'cloud.py' file inside the '2ndAssigment' directory on your terminal, running the next command:
```bash
  python cloud.py
```

As an output you'll get eleven .png files, ten of them are a cloud with the keywords of each paper and the one named 'wordcloud_paper_all_papers.png' contains the keywords of the ten papers.

## How to run the Python file of the second task

Execute the 'visualization.py' file inside the '2ndAssigment' directory on your terminal, run the next command:
```bash
  python visualization.py
```

As an output you'll get a png file called 'graph_figures.png'.

## How to run the Python file of the third task

Execute the 'link.py' file inside the '2ndAssigment' directory on your terminal, run the next command:
```bash
  python link.py
```

As an output you'll get a .txt file called 'links.txt', that'll contain the link found in each pdf.


**You'll find all of the prior outputs in a directory inside '2ndAssigment' called 'output_files'.**


# How to execute this project with docker

First you have to make sure that you have your xmls ready to execute the Python scripts in a Docker container, for this, follow the next steps:

## How to get your xmls from your own pdfs 

**NOTE:** If you already executed this project without docker, please still follow the next instructions and run the commands in the proper directories indicated next.

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

2. Now copy and paste your pdfs into the directory called 'Papers', that you'll find inside the directory called 'compose', which location is: './AIandOpenScienceInResearchSoftwareEngineering-main/Docker/compose'.
 
3. Now in your terminal, make sure that you are inside the directory 'compose' which location is: './AIandOpenScienceInResearchSoftwareEngineering-main/Docker/compose', and run the next command:
```bash
  python request_grobid.py
```
This runs a Python script that'll connect to the GROBID server using the Grobid Python client library, and downloads all of the XML of the pdfs inside the 'Papers' directory, this might take a few minutes, if it takes too long stop the Grobid container, start it again and execute request_grobid.py again.

## Now run the Python scripts with Docker compose

For this project Docker compose was the easiest way of containerizing my Python files, because it allows for all of the three separate Python files to run at the same time and also adding a bind mount which is used to retrieve the output files that each file creates and store them in a directory in the host machine so the user can see the output since containers don't have a graphic enviroment.

For it to run in your computer, follow the next steps:

**IMPORTANT:** Make sure that you have docker compose downloaded on your machine so you can execute this project using containers.

1. Open your console and change directories until you are inside the directory named 'Docker' and then change directories once more to the directory inside 'Docker' called 'compose' ('./AIandOpenScienceInResearchSoftwareEngineering-main/Docker/compose)'.
```bash
  cd Docker/compose
```
2. Once you are inside the 'compose' directory, run the next command on your terminal:
```bash
  docker-compose up --build
```
3. After you've run the prior command all of the output files from each of the Python files should be found on the directory called 'result_files' that can be found inside the directory 'compose'.

4. Now, type the next command:
```bash
  docker-compose down
```

And that's it! Now you have all of the output files in your computer :)

## Tests
The unittests used to make this project worked succesfully can be found inside the '2ndAssigment' directory.

## Workflow diagram
![title](Images/workflow_diagram.png)

## Documentation
You can check out this software's documentation on the next link:

http://aiandopenscienceinresearchsoftwareengineering.readthedocs.io/



