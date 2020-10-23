from googlesearch import search
import logging
import logging.config

log = logging.getLogger('debugLogger')

class GoogleSearch:
	def __init__(self,keyword, max_num_result=None, number_of_results_per_page=None, pause_btw_request=None):
		self.keyword = keyword
		if max_num_result:
			self.max_num_result=max_num_result
		else:
			self.max_num_result=100
		if number_of_results_per_page:
			self.number_of_results_per_page=number_of_results_per_page
		else:
			self.number_of_results_per_page=10
		if pause_btw_request:
			self.pause_btw_request=pause_btw_request
		else:
			self.pause_btw_request=0.5
	def setKeyword(self, keyword):
		self.keyword=keyword

	def search(self, query):

		if not query:
			query=self.keyword

		count = 0

		web_list=[]
		try :
			response = search(query=query, tld='co.in', lang='en', num=self.number_of_results_per_page, stop=self.max_num_result, pause=self.pause_btw_request)
			for item in response:
				count +=1
				if not item:
					item = ""
				web_list.append(item)
				log.debug(str(count)+" : "+ str(item))
		except ImportError as ie:
			log.error("No Module named 'google' Found:"+str(ie), exc_info=True)
		return web_list

# if __name__=='__main__':
# 	gs = GoogleSearch("school violence")
# 	gs.search()