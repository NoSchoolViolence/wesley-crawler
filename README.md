# wesley-crawler
Please use python 3.6 to create virtual environment

To create a virtual environment
	python3.6 -m venv venv


to install required libraries
	pip install -e requirements.txt

to configure the application modify config.py
You can configure the appliation. For example, you can set:
- the query list
	# {query1, query2,.....,queryN}
	SEARCH_TOPIC_LIST={'school+violence','school+shooter','student+violence','teacher+violence+school'}

- save the research result as CSV 
	SAVE_AS_CSV=1

- save the resarch result as JSON
	SAVE_AS_JSON=1
-

to run the crawler run app.py
	python3.6 appy

