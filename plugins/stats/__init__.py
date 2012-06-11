#!/usr/bin/python
# -*- coding: utf-8 -*-


from plugin import *
import random
import re
import urllib2, urllib, uuid
import json
from urllib2 import urlopen
from xml.dom import minidom

class statsPlugin(Plugin):
    
    @register("de-DE", ".*wie.*viele.*aktive.*verbindungen.*")
    def currently(self, speech, language, matchedRegex):
        if language == 'de-DE':
            self.say("Zurzeit {0} verbindungen".format(self.numberOfConnections()))
        self.complete_request()
          
