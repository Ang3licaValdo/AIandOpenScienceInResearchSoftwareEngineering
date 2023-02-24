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

Installing the Requirements in a virtual enviroment
---------------------------------------------------

Fist of all, you need to have pip installed. Pip is a package manager
for installing and managing Python software packages

.. code:: bash

     sudo apt install python3-pip

Then you will like to create a virtual enviroment to run the scripts,
for this, follow the next steps: 1. After you’ve downloaded the
‘2ndAssigment’ directory, open your terminal and change directories
until you are located inside the ‘2ndAssigment’ directory. 2. type the
next command to install virtual enviroments:

.. code:: bash

     python3 -m pip install --user virtualenv

3. Set up ithe virtual enviroment (give it any name you like, inn this
   next command the name is ‘test’

.. code:: bash

     python3 -m venv test

4. Activate your enviroment:

.. code:: bash

     source env_3.10/bin/activate

5. As a final step, you’ll need to install the next libraries inside the
   virtual enviroment, so after you see parenthesis in your console with
   the name of your enviroment, just type the commands shown for each of
   the libraries requiered listed next.

-  Installing BeautifulSoup

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
