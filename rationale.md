
# Second assigment 

This is the file that'll be used to describe the making of the second assigment of the subject, mentioned on the README file, which consists in propogramming the next three points with Python:

1. Draw a keyword cloud based on the abstract information.
2. Create a visualization showing the number of figures per article.
3. Create a list of links found in each paper.

## Where to find the Python files

Each of these files can be found in the folder called '2nd assigment python'.

## Requirements
- Having Python installed. 
- Installing pip
- Python library: BeautifulSoup
- Python parser: lxml 
- Install Image
- Installing Numpy

## Installing the Requirements

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
  pip install beautifulsoup4
```

### Installing Image

```bash
  pip install image
```
### Installing NumPy

```bash
  pip install numpy
```

## First task

The first task is about finding the keywords of each one of the papers and pressenting them in a keyword cloud, the code that does this is in a Python file called 'cloud.py' 

For executing the 'cloud.py' file:
```bash
  python cloud.py
```

As an output you'll get eleven .png files, ten of them are a cloud with the keywords of each paper and the one named 'wordcloud_output.png' contains the keywords of the ten papers.

## Second task

For this task we have to represent in some way how many figures there are in each paper, for that i used a bar graph, that you'll get when you execute the Python file called 'visualization.py 

For executing the 'visualization.py' file:
```bash
  python visualization.py
```

As an output you'll get a bar graph, each bar represents how many figures there are in each article.

## Third task

For this task we have list the links encountered in each paper, this is done by the file called 'link.py' 

For executing the 'link.py' file:
```bash
  python link.py
```

As an output you'll get a .txt file that'll contain the link found in each pdf.


