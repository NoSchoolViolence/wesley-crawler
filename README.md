# wesley-crawler
Please use python 3.6 to create virtual environment

To create a virtual environment
	<b>python3.6 -m venv venv </b>


to install required libraries
	<b>pip install -e requirements.txt</b>

to configure the application modify config.py
You can configure the appliation. For example, you can set:
- the query list
	SEARCH_TOPIC_LIST={'school+violence','school+shooter','student+violence','teacher+violence+school'}

- save the research result as CSV 
	SAVE_AS_CSV=1

- save the resarch result as JSON
	SAVE_AS_JSON=1
-

to run the crawler run app.py
	<b>python3.6 appy</b>

