import pandas as pd
import config
import os
import json
from json import JSONEncoder
import logging
import logging.config

log = logging.getLogger('debugLogger')

class FileManager():
	def save_as_csv(self, web_list,web_list_content_clean, topic=None):
		log.info("save_as_csv --> "+topic)
		df = pd.DataFrame({"URLs":web_list, "Content":web_list_content_clean})
		if not topic:
			topic ="Dummy"
		file_name=os.getcwd()+"/files/"+topic.replace("+", "_") + "_google.csv"
		df.to_csv(file_name)
		return file_name

	class SearchItem:
		def __init__(self, url, content):
			self.url=url
			self.content=content

	class SearchResponse:
		def __init__(self, items):
			self.items=items

	class SearchResponseEncoder(JSONEncoder):
		def default(self, o):
			return o.__dict__

	def save_as_json(self, web_list,web_list_content, topic=None):
		items=[]

		for i in range(len(web_list)):
			item = self.SearchItem(web_list[i], web_list_content[i])
			items.append(item)

		data = self.SearchResponse(items)
		file_name=topic.replace("+", "_")
		file_name=file_name.replace(" ","_")
		file_name=os.getcwd()+"/files/"+file_name + "_google.json"
		with open(file_name, 'w') as outfile:
			json.dump(data, outfile, indent=4, cls=self.SearchResponseEncoder)
		log.info(" Search Result saved as json --> "+file_name + "_google.json")
		return file_name