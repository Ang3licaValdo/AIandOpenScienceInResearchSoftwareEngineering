How to execute this project with docker
========================================

Docker allows to create containers for applications, so they can be run in any computer without having issues with libraries and dependencies.
Since this project consists of three different Python scripts, it is good practice to have them each in a different container. Docker offers an option so you can run different applications at the same time, it's called Docker compose, to use it, you have to create a docker-compose.yml file and declare each application, its location in the file system and whatever else you want to add, like volumes.

For this project Docker compose was the easiest way of containerizing my Python files, because it allows for all of them to run at the same time and also adding a bind mount which is used to retrieve the output files that each file creates and stroing them in a directory in the host machine so the user can see the output since containers don't have a graphic enviroment.

For it to run in your computer, follow the next steps:

**IMPORTANT:** Make sure that you have docker compose downloaded on your machine so you can execute this project using containers.

1. Download the directory called Docker from this respository.
2. Open your console and change directories until you are inside the docker directory and then change directories once more to the directory inside 'Docker' called 'compose'.
.. code:: bash
        cd Docker
        cd compose

3. Once you are inside the 'compose' directory, run the next command on your terminal:
.. code:: bash
        docker-compose up --build

4. After you've run the prior command all of the output files from each of the Python files should be found on the directory called 'result_files' that can be found inside the directory 'compose'.

5. Now type the next command:
.. code:: bash
        docker-compose down

And that's it! Now you have all of the output files in your computer :)
