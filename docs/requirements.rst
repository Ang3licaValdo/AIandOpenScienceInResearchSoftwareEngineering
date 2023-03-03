Requirements
============

The requirements for running the Python scripts
-----------------------------------------------

-  Having Python installed.
-  Installing pip
-  Python library: BeautifulSoup
-  Python parser: lxml
-  Install Image
-  Installing Numpy

How to run the three python scripts with a virtual enviroment
-------------------------------------------------------------

Fist of all, you need to have pip installed. Pip is a package manager
for installing and managing Python software packages

.. code:: bash

     sudo apt install python3-pip

Then you will like to create a virtual enviroment to run the scripts,
for this, follow the next steps: 

1. After you’ve downloaded the contents
of this repository, open your terminal and change directories until you
are located inside the ‘2ndAssigment’ directory (you’ll need to find the
‘AIandOpenScienceInResearchSoftwareEngineering-main’ directory wherever
you dowloaded this repository first because the ‘2ndAssigment’ directory
is inside of it). 

2. type the next command to install virtual enviroments:

.. code:: bash

     python3 -m pip install --user virtualenv

3. Set up the virtual enviroment (give it any name you like, in this next command the name is ‘test’):

.. code:: bash

     python3 -m venv test

4. Activate your enviroment:

.. code:: bash

     source test/bin/activate

5. You’ll need to install the next libraries inside the virtual
   enviroment, so after you see the parenthesis in your console with the
   name of your enviroment, just type the commands shown for each of the
   libraries requiered listed next, or to make this step easier and
   faster just type the next command in your terminal (you should be
   inside the ‘2ndAssigment’ directory):

.. code:: bash

     pip install -r requirements.txt

If you want to install one by one, run the next commands: - Installing
BeautifulSoup

.. code:: bash

     pip install beautifulsoup4

-  **Installing lxml**

.. code:: bash

     pip install lxml

-  **Installing Image**

.. code:: bash

     pip install image

-  **Installing NumPy**

.. code:: bash

     pip install numpy

-  **Installing WordCloud**

.. code:: bash

     pip install wordcloud

How to get your xmls from your own pdfs
---------------------------------------

1. Make sure you have GROBID server running, you can do this using
   Docker (make sure you have it installed), and the run the next
   commands in another terminal:

-  Pull the GROBID image:

.. code:: bash

     docker pull lfoppiano/grobid:0.7.2

-  Run the image:

.. code:: bash

     docker run -t --rm -p 8070:8070 lfoppiano/grobid:0.7.2

The web service will be running in http://localhost:8070/

Your terminal will likely look like the one on the next figure when the GROBID server is running:

|On your terminal it can look like this when GROBID server is running:|


.. |On your terminal it can look like this when GROBID server is running:| image:: /images/grobid.png

2. Now copy and paste your pdfs inside the directory called ‘Papers’
   that’s inside the directory ‘2ndAssigment’ that you downloaded when
   downloading this repository.
3. Now if you are not inside the ‘2ndAssigment’ directory in your
   terminal already, change directories until you are inside the
   ‘./AIandOpenScienceInResearchSoftwareEngineering-main/**2ndAssigment**’
   directory and run the next command:

.. code:: bash

     python request_grobid.py

This runs a Python script that’ll connect to the GROBID server and
download all of the XML of the pdfs inside the ‘Papers’ directory, it
maight take a few minutes. **NOTE:** if the grobid server it’s taking
long just stop the container and start it again by running the prior
command once more.

4. Chech the ‘Papers’ directory to make sure that all of the xmls are
   there and stop the docker container, after that, you can run each of
   the python scripts for each task, mentioned next:
