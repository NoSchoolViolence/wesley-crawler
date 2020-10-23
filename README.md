# wesley-crawler
Please use python 3.6 to create virtual environment

To create a virtual environment
	<br>
	<strong><em>python3.6 -m venv venv</em> </strong>


to install required libraries
	<br>
	<strong><em>pip install -e requirements.txt</em></strong>

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
	<br>
	<strong><em>python3.6 appy</em></strong>

