#!/usr/bin/python
# -*- coding: utf-8 -*-

#RSS of my Blog

import urllib
import xml.dom.minidom
import random
from xml.dom.minidom import Node

from plugin import *


class examplePlugin(Plugin):

	@register("en-US", ".*feed.*")
	@register("de-DE", ".*Blog.*")
	def feed(self, speech, language): 
		html = urllib.urlopen("http://mummmyi.sullenlook.eu").read()
		dom = xml.dom.minidom.parseString(html)	
		Topic=dom.getElementsByTagName('description')
		x = random.randrange(1,10)
		Text= Topic[x].firstChild.data
    		self.say(Text.replace("<br>","&#8217;",""))
    		self.complete_request()

# EOF
