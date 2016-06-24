
import re, urllib, urllib2, urlparse

#from resources.lib.libraries import cleantitle
#from resources.lib.libraries import client
#from resources.lib import resolvers

class source:
	def __init__(self):
		self.base_link = 'http://kissanime.to'
		self.link_1 = 'http://kissanime.to'
		self.search_link = ''
		self.episode_link = ''
		self.headers = {}

	def  get_show(self, imdb, tvdb, tvshowtitle, year):
		try:
			query = ''
			result = ''
			links =[self.link_1, self.link_2]
			
			for base_link in links
				result = client.source(urlparse.urljoin(base_link, query), headers=self.headers)





