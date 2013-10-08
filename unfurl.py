# -*- coding: utf-8 -*-
import urllib2
import cookielib
from urlparse import urlparse

def expand_url(url):
	#set cookie since many sites *WRONGLY* require you to set a cookie to redirect you to a secure page and back to insecure content
	cookiejar = cookielib.CookieJar()
	opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookiejar))
	parsed = urlparse(url)
	scheme = parsed.scheme
	if not parsed.scheme:
		#URL must begin with a protocol e.g. http:// https:// ftp://
		raise Exception("URL does not contain prorocol e.g http:// or https://")
	domain = parsed.netloc
	#convert to idna
	domain_idna = domain.encode("idna")
	path = parsed.path
	if parsed.query is not '':
		path +="?"+parsed.query
	parsed_url = scheme+"://"+domain_idna+path
	#open url
	opened_url = opener.open(parsed_url)
	resolved_url = opened_url.geturl()
	return resolved_url

if __name__ == "__main__":
   print expand_url("http://j.mp/Y4seGv")
   print expand_url("http://t.co/bxPFQgZ1AV")
   print expand_url(u"http://➡.ws/kd")
   print expand_url(u"http://➡.ws/wwwwwwwww")
   print expand_url("qq")
   print expand_url("http://j.mp/13ND7TO")
