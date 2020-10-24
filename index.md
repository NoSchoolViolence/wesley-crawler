## Welcome to Wesley's Crawler GitHub Pages

## What is Wesley?
Wesley is the engine being developed to ingest enormous amounts of text, process the unstructured data, extract the information, store it in an structured manner, and analyze the data in various efforts to prevent & reduce violence in schools. 

This repository serves as the centralized location for uploading code (usually Jupyter Notebooks) for creating new features in Wesley. A Trello board cataloging the features that are pending, in progress, and completed can be accessed here: https://trello.com/b/8nLD3i32/wesley.
### What is Wesly Crawler?
<TBD>
You can use the [wesley-crawler](https://github.com/ramazansicakyuz/wesley-crawler/edit/gh-pages/index.md) to make searches with the predefined queries and fetch the all of the URLs and clean text of the content of the websites and PDFs.

### Important
Please use python 3.6 to create virtual environment

To create a virtual environment
  `python3.6 -m venv venv`

### Prepare environment
to install required libraries
  `pip install -e requirements.txt`

### Configure Application
to configure the application modify config.py You can configure the appliation. For example, you can set:

- the query list 
    `SEARCH_TOPIC_LIST={'school+violence','school+shooter','student+violence','teacher+violence+school'}`
- save the research result as 
    `CSV SAVE_AS_CSV=1`
- save the resarch result as 
    `JSON SAVE_AS_JSON=1`
    
### RUN the Crawler
to run the crawler run app.py
  `python3.6 appy`
  

