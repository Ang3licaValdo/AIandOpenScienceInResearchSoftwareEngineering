How to execute this project with docker
=======================================

First you have to make sure that you have your xmls ready to execute the
Python scripts in a Docker container, for this, follow the next steps:

.. _how-to-get-your-xmls-from-your-own-pdfs-1:

How to get your xmls from your own pdfs
---------------------------------------

**NOTE:** If you already executed this project without docker, please
still follow the next instructions and run the commands in the proper
directories indicated next.

1. Make sure you have GROBID server running, you can do this using
   Docker make sure you have it installed and the run the next commands
   in your terminal:

-  Pull the GROBID image:

.. code:: bash

     docker pull lfoppiano/grobid:0.7.2

-  Run the image:

.. code:: bash

     docker run -t --rm -p 8070:8070 lfoppiano/grobid:0.7.2

The web service will be running in http://localhost:8070/

2. Now copy and paste your pdfs into the directory called ‘Papers’, that
   you’ll find inside the directory called ‘compose’, which location is:
   ‘./AIandOpenScienceInResearchSoftwareEngineering-main/Docker/compose’
   if you are inside the directory that was downloaded when downloading
   this repository.
   
   The next image shows a flow for you to identify where the Papers directory is in an easier way:
   
|docker:|


.. |docker:| image:: /images/docker_paper.png

3. Now in your terminal, make sure that you are inside the directory
   ‘compose’ which location is:
   ‘./AIandOpenScienceInResearchSoftwareEngineering-main/Docker/compose’,
   and run the next command:

.. code:: bash

     python request_grobid.py
     
     
|terminalseven:|


.. |terminalseven:| image:: /images/terminal7.png


This runs a Python script that’ll connect to the GROBID server using the Grobid Python client and
download all of the XML of the pdfs inside the ‘Papers’ directory, this
might take a few minutes (if it takes way too long, just delete the container, create it again an rerun the python script).

Now the Python scripts with Docker compose
----------------------------------------------

Docker allows to create containers for applications, so they can be run
in any computer without having issues with libraries and dependencies.
Since this project consists of three different Python scripts, it is
good practice to have them each in a different container. Docker offers
an option so you can run different applications at the same time, it’s
called Docker compose, to use it, you have to create a
docker-compose.yml file and declare each application, its location in
the file system and whatever else you want to add, like volumes.

For this project Docker compose was the easiest way of containerizing my
Python files, because it allows for all of them to run at the same time
and also adding a bind mount which is used to retrieve the output files
that each file creates and stroing them in a directory in the host
machine so the user can see the output since containers don’t have a
graphic enviroment.

For it to run in your computer, follow the next steps:

**IMPORTANT:** Make sure that you have docker compose downloaded on your
machine so you can execute this project using containers.

1. Open your console and change directories until you are inside the
   directory named ‘Docker’ and then change directories once more to the
   directory inside ‘Docker’ called ‘compose’
   (‘./AIandOpenScienceInResearchSoftwareEngineering-main/Docker/compose)’.

.. code:: bash

     cd Docker/compose
     
For example:
 
 
|terminalfive:|


.. |terminalfive:| image:: /images/terminal5.png
 

2. Once you are inside the ‘compose’ directory, run the next command on
   your terminal:

.. code:: bash

     docker-compose up --build
    
It'll look something like this:

|terminalsix:|


.. |terminalsix:| image:: /images/terminal6.png


And when it's executed succesfully it'll look like this:


|terminalsixtwo:|


.. |terminalsixtwo:| image:: /images/terminal62.png


3. After you’ve run the prior command all of the output files from each
   of the Python files should be found on the directory called
   **‘result_files’** that can be found inside the directory ‘compose’.
   
   The result_files directory will look like this with all of the output files:
   
   
|output:|


.. |output:| image:: /images/output.png

   
4. Now, type the next command:

.. code:: bash

     docker-compose down

And that’s it! Now you have all of the output files in your computer :)
