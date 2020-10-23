import re
import unicodedata
import config
from bs4 import BeautifulSoup
import logging
import logging.config

log = logging.getLogger('debugLogger')

class Cleaner():

	def __init(self, web_list_content=None):
		if not web_list_content:
			self.__web_list_content = web_list_content
	
	def set_web_list_content(self, web_list_content):
		self.__web_list_content = web_list_content

	def clean_content(self, html_content_list):
		web_list_content_clean = []
		if html_content_list:
			web_list_content_clean = [self.__clean_text(text) for text in html_content_list]

		return web_list_content_clean

	def __clean_text(self, html_content):
		log.info("__clean_text.....")
		try:
			soup = BeautifulSoup(html_content, "html.parser")  # create a new bs4 object from the html data loaded
			for script in soup(["script", "style"]):  # remove all javascript and stylesheet code
				script.extract()
			# get text
			text = soup.get_text()
			# break into lines and remove leading and trailing space on each
			lines = (line.strip() for line in text.splitlines())
			# break multi-headlines into a line each
			chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
			# drop blank lines
			text = '\n'.join(chunk for chunk in chunks if chunk)
		except Exception as e:
			text = html_content
			log.error("Error on cleaning", exc_info=True)
		return text