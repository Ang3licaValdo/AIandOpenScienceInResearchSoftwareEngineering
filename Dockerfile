FROM python:3.9

# WORKDIR /code

# COPY ./requirements.txt /code/requirements.txt

ADD visualization.py .
COPY ./Papers ./Papers

# RUN pip install -r /code/requirements.txt

#COPY ./link.py /code/2ndAssigment

RUN pip3 install beautifulsoup4
RUN pip3 install lxml
RUN pip3 install image
RUN pip3 install numpy 
RUN pip3 install wordcloud


CMD ["python","-u" ,"./visualization.py"]