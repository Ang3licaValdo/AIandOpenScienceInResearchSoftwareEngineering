FROM python:3.9

WORKDIR /para_la_prueba 

#copy the requirements from my text file to the container
COPY ./requirements.txt /para_la_prueba/requirements.txt

#Installing the requirements
RUN pip install -r /para_la_prueba/requirements.txt

#copy a directory into another directory in the container
COPY ./Papers /para_la_prueba
COPY link.py /para_la_prueba 

#how to run the python script
CMD ["python" ,"./link.py"]
