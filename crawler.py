import fitz
import wget
import os
import re
import numpy as np
import pandas as pd
import requests
import time
from pathlib import Path
# from selenium import webdriver
# import chromedriver_binary  # Adds chromedriver binary to pat
# from selenium.webdriver.common.keys import Keys
# from selenium.common.exceptions import NoSuchElementException
# from selenium.common.exceptions import WebDriverException
import config
import logging
import logging.config

log = logging.getLogger('debugLogger')

class Crawler():

	def __init__(self, search_topic=None):
		if search_topic:
			self.__search_topic=search_topic
		else:
			self.__search_topic='school violence'

	def filter(self, web_list):
		# website pattern for scraping
		counter=0
		pattern_http = re.compile("^https://")
		index_http = [bool(pattern_http.match(el)) for el in web_list]

		pattern_no_youtube = re.compile("^(?!https://www.youtube.com)")
		index_no_youtube = [bool(pattern_no_youtube.match(el)) for el in web_list]

		# intersection
		index = np.array(index_http) * np.array(index_no_youtube)
		web_list = list(np.array(web_list)[index])
		
		log.info(f"\nTotal number of pages : {counter}")
		log.info(f"Total number of urls (after applying filter) : {len(web_list)}")

		return web_list

	def get_text_from_pdf(self, pdf_link):
		# download pdf in the same directory
		## os.system(f"wget -O pdf_file_temp.pdf {pdf_link}")
		log.info("get_text_from_pdf -->")
		doc = None
		temp_file_name='pdf_file_temp'+str(time.time())+'.pdf'
		try:
			# wget.download(pdf_link, out = "pdf_file_temp.pdf")
			wget.download(pdf_link, out = os.getcwd() + '/tmp/'+temp_file_name)
			# extract text from pdf using PyMuPDF
			# doc = fitz.open("pdf_file_temp.pdf")
			doc = fitz.open(os.getcwd() + '/tmp/'+temp_file_name)

			text = ''
			for page in doc:
				text += page.getText()
		except:
			text = ""
		finally:
			if doc:
				# close the file
				doc.close()
				# delete the pdf
				# os.remove(os.getcwd() + '/tmp/'+temp_file_name)
				Path(os.getcwd() + '/tmp/'+temp_file_name).unlink(missing_ok=True)
		return text

	def get_content(self, web_url):
		log.info("get_content of-->" + web_url)
		response = requests.get(web_url,timeout=10)
		return response.text

	def get_text_from_list_of_urls(self, web_list, verbose = False):
		log.info("get_text_from_list_of_urls-->")
		web_list_content = []
		try:
			# go through the url in web_list
			counter = 0
			pattern = re.compile(".*\.pdf$")
			result=""
			length = len(web_list)
			for web_url in web_list:
				counter += 1
				log.debug("Scraping link"+ str(counter)+"/"+str(length))
				# link ends with .pdf
				if bool(pattern.match(web_url)):
					try:
						result = self.get_text_from_pdf(web_url)
					except Exception as e:
						log.error("Error: get_text_from_pdf =" + web_url, exc_info=True)
						result = ""
					web_list_content.append(result)
				else:
					try:
						result = self.get_content(web_url)
					except Exception as e:
						log.error("Error: get_text_from_url ="+web_url, exc_info=True)
						result = ""
					web_list_content.append(result)

			log.debug("Scraping complete\n")
		except Exception as e:
			log.error("Error: get_text_from_url =" + web_url, exc_info=True)
			web_list_content.append("")

		return web_list_content