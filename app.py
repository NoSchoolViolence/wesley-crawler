import os
import time
import config
from crawler import Crawler
from cleaner import Cleaner
from filemanager import FileManager
from search import GoogleSearch
import logging
import logging.config
#from pathlib import Path
from pathlib3x import Path

class Application():
	def __init__(self):
		self.__crawler = Crawler()
		self.__cleaner = Cleaner()
		self.__file_manager = FileManager()
		self.__search_engine= GoogleSearch(config.SEARCH_TOPIC, config.MAX_ITEM, config.NUMBER_OF_RESULTS_PER_PAGE,config.PAUSE_BTW_REQUEST)

	def setQuery(self, keyword):
		self.__search_engine.setKeyword(keyword)

	def run(self, query):
		log.info("Application started.")
		web_list = self.__search_engine.search(query)
		log.debug("Search is done."+str(len(web_list))+" URL was found.")
		if web_list:
			web_list_content_clean = self.__crawler.get_text_from_list_of_urls(web_list, verbose = True)
			log.info("Search contents are downloaded.")

		if  web_list_content_clean:
			web_list_content_clean = self.__cleaner.clean_content(web_list_content_clean)
			log.info("Content was cleaned.")

		return web_list, web_list_content_clean

	def save_as_csv(self, web_list, web_list_content_clean, topic=None):
		if not topic:
			topic=config.SEARCH_TOPIC

		self.__file_manager.save_as_csv(web_list, web_list_content_clean,topic)

	def save_as_json(self, web_list, web_list_content_clean, topic=None):
		if not topic:
			topic=config.SEARCH_TOPIC
		self.__file_manager.save_as_json(web_list, web_list_content_clean,topic)

	def verify_require_folders(self):
		try:
			Path(os.getcwd() + '/tmp/').mkdir(parents=True, exist_ok=True)
			Path(os.getcwd() + '/files/').mkdir(parents=True, exist_ok=True)
			Path(os.getcwd() + '/log/').mkdir(parents=True, exist_ok=True)
		except FileNotFoundError as e:
			log.error("Error:/log creation ", exc_info=True)
		except NotImplementedError as e:
			log.error("Error:/log creation ", exc_info=True)

	def remove_tmp_folders(self):
		try:
			#Path(os.getcwd() + '/tmp/').unlink(missing_ok=True)
			# Path(os.getcwd() + '/tmp/').rmdir()
			Path(os.getcwd() + '/tmp/').rmtree(ignore_errors=True)
			# self.rm_rf(Path(os.getcwd() + '/tmp/'))
		except FileNotFoundError as e:
			log.error("Error:/tmp creation ", exc_info=True)
		except NotImplementedError as e:
			log.error("Error:/tmp creation ", exc_info=True)

	def rm_rf(self, pth: Path):
		for child in pth.iterdir():
			if child.is_file():
				child.unlink()
			else:
				self.rm_rf(child)
		pth.rmdir()

def main():
	start_time = time.time()
	app = Application()
	app.verify_require_folders()
	queries = config.SEARCH_TOPIC_LIST
	for query in queries:
		log.info(f"Query for search is {query}")
		app.setQuery(query)

		web_list, web_list_content_clean = app.run(query)
		finish_time = time.time()
		run_time = round(finish_time - start_time)
		log.info(f"Application Running time = {run_time // 60} mins and {run_time % 60} sec over {len(web_list)} urls")

		if config.SAVE_AS_CSV == 1:
			app.save_as_csv(web_list, web_list_content_clean, query)
			log.info('Result is saved as csv format for'+query)
		if config.SAVE_AS_JSON == 1:
			app.save_as_json(web_list, web_list_content_clean, query)
			log.info('Result is saved as json for'+query)
	if config.REMOVE_TMP_DIR==1:
		app.remove_tmp_folders()

	log.info("Mission Completed!")

if __name__ == '__main__':
	logging.config.fileConfig('logging.ini', disable_existing_loggers=False)
	log = logging.getLogger('debugLogger')
	main()