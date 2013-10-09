# -*- coding: utf-8 -*-
from unfurl import expand_url as eu

def test_bitly():
	assert eu("http://j.mp/Y4seGv") == "http://www.nytimes.com/2013/03/11/world/asia/karzai-accuses-us-and-taliban-of-colluding-in-afghanistan.html?ref=global-home&_r=0"
	assert eu("http://j.mp/13ND7TO") == "http://www.profnetconnect.com/angela_smith/blog/2013/03/07/angie%E2%80%99s_social_media_angels:_givingtuesday"

def test_tco():
	assert eu("http://t.co/bxPFQgZ1AV") == "http://www.nytimes.com/2013/03/14/crosswords/bridge/bridge-spring-north-american-championships.html?partner=rss&emc=rss&_r=0"

def test_arrows():
	assert eu(u"http://➡.ws/kd") == "http://www.theglobeandmail.com/technology/tech-news/crtc-will-rescind-unlimited-use-internet-decision---or-ottawa-will-overturn-it/article565223/"
	assert eu(u"http://➡.ws/wwwwwwwww") == "http://expandurl.appspot.com/"

def test_tinyurl():
	assert eu("http://tinyurl.com/l7953rg") == "http://espnfc.com/blog/_/name/espnfcunited/id/9949?cc=5901"
