First task
==========

The first task is about presenting the most important words found in the
abstarct of each article in a word cloud, for this to happen, thanks to
GROBID we have an xml from each of the pdfs chosen, to find what we need
it’s easy to analyze and xml with the Python library called
BeautifulSoup, to get the text from the ‘abstract’ tag, first i had to
find the tag with the method called ‘find_all’ and afterwards with the
BeautifulSoup constructor and .text we got a string free of xml tags,
then that string is used as a parameter for the method generate(string)
that belongs to the wordcloud python library, that’s the one in charge
of creating the word cloud.

The code that does all of the things above is in a Python file called
‘cloud.py’

For executing the ‘cloud.py’ file:

.. code:: bash

     python cloud.py

As an output you’ll get eleven .png files, ten of them are a cloud with
the keywords of each paper and the one named ‘wordcloud_output.png’
contains the keywords of the ten papers.

Output example:
---------------
|Output example|


.. |Output example| image:: /images/wordcloud_paper1.png
