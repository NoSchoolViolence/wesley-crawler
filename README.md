## Welcome to Wesley's Crawler GitHub Page

## What is Wesley?
Wesley is the engine being developed to ingest enormous amounts of text, process the unstructured data, extract the information, store it in an structured manner, and analyze the data in various efforts to prevent & reduce violence in schools. 

This repository serves as the centralized location for uploading code (usually Jupyter Notebooks) for creating new features in Wesley. A Trello board cataloging the features that are pending, in progress, and completed can be accessed here: https://trello.com/b/8nLD3i32/wesley.
### What is Wesly Crawler?

<TBD>

You can use the [wesley-crawler](https://github.com/ramazansicakyuz/wesley-crawler/edit/gh-pages/index.md) to make searches with the predefined queries and fetch the all of the URLs and clean text of the content of the websites and PDFs.

### Important
Please use python 3.x to create virtual environment

### Prepare environment
To create a virtual environment
  `python3 -m venv venv`

Acivate virtual environment
  `source venv/bin/activate`

Install required libraries
  `pip install -r requirements.txt`

### Configure Application
to configure the application modify config.py You can configure the appliation. For example, you can set:

- the query list 
    `SEARCH_TOPIC_LIST={'school+violence','school+shooter','student+violence','teacher+violence+school'}`
- save the research result as 
    `CSV SAVE_AS_CSV=1`
- save the resarch result as 
    `JSON SAVE_AS_JSON=1`
 If you want to upload your dataset formatted as CSV and/or JSON to box.com - Cloud File Storage - you can create a custom application on Box.com 
 and use your account or you can ask to _Ramazan_.
 
 to configure Box.com integration update boxconfig.py and set the following attributes:
 - `CLIENT_ID='USE_YOUR_CLIENT_ID'`
 - `CLIENT_SECRET='USE_YOUR_OWN_SECRET'`
 - `ACCESS_TOKEN='USE_YOUR_TOKEN'`
 
### RUN the Crawler
to run the crawler run app.py
  `python3.6 appy`

