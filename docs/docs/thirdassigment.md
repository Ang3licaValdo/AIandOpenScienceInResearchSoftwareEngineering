# Third task

For this task we have list the links encountered in each paper, i did it by first checking the xml and observing how **GROBID** identified the links, cause some of them were found inside paragraph, others were DOI and others were identified with the tag 'ptr' which belong to the references that have links where the information came from, after realizing this, i used the method 'find_all' from the BeautifulSoup library and obtained the attribute of the tag which contained the url or simply the text in case of the DOI and all of it was written into a file.

The code to obtain the .txt that contains the links to each paper is called 'link.py' 

For executing the 'link.py' file:
```bash
  python link.py
```

As an output you'll get a .txt file that'll contain the link found in each pdf.

##Output example:
![Output example](/images/links.png)