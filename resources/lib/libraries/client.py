import re, sys, urllib2, HTMLParser

def request(url, close=True, error=False, proxy=None, post=None, headers=None, mobile=False, safe=False, referer=None, cookie=none, output='', timeout='30'):
	try:
		handlers = []
		if not proxy == None:
			handlers += [urllib2.ProxyHandler({'http': '%s' % (proxy)}), urllib2.HTTPHandler]
			opener = urllib2.build_opener(*handler)
			opener = urllib2.install_opener(opener)
		if output == 'cookie' or not close == True:
			import cookielib
			cookies = cookielib.LWPCookieJar()
			handlers += [urllib2.HTTPHandler(), urllib2.HTTPSHandler(), urllib2.HTTPCookieProcessor(cookies)]
			opener = urllib2.build_opener(*handlers)
			opener = urllib2.install_opener(opener)
		try:
			if sys.version_info < (2, 7, 9): raise Exception()
			import ssl;
			ssl_context = ssl.create_default_context()
			ssl_context.check_hostname = False
			ssl_context.verify_mode = ssl.CERT_NONE
			handlers += [urllib2.HTTPSHandler(context=ssl_context)]
			opener = urllib2.build_opener(*handlers)
			opener = urllib2.install_opener(opener)
		except:
			pass

		try: headers.update(headers)
		except: headers = {}
		
		if 'User-Agent' in headers:
			pass


