import urllib2
import cookielib
from urlparse import urlparse
import httplib2 as httplib
import json


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


def expand_url_with_hops(url, hops = [], headers = None):
    expanded = expand_url(url)
    parsed = urlparse(url)
    cookiejar = cookielib.CookieJar()
    h = httplib.Http()
    h.follow_redirects = False
    response, content = h.request(url, 'HEAD', headers)
    if response.has_key('set-cookie'):
        headers = json.dumps({'Cookie': response['set-cookie']})
    if response.status/100 == 3 and response['location']:
        redirected_url = response['location']
        hops.append(redirected_url)
        if expanded == redirected_url:
            return url,hops
        return expand_url_with_hops(redirected_url, hops, headers) # changed to process chains of short urls
    else:
        return url, hops

