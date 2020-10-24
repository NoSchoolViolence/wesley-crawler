## Welcome to wesley-crawler GitHub Pages

You can use the [editor on GitHub](https://github.com/ramazansicakyuz/wesley-crawler/edit/gh-pages/index.md) to crawle the URLS of response of the query.

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
  

