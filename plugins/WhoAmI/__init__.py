#!/usr/bin/python
# -*- coding: utf-8 -*-
# Code by Javik
# Update by @SullenLook

import re
import uuid

from plugin import *

from siriObjects.baseObjects import *
from siriObjects.uiObjects import *
from siriObjects.systemObjects import *
from siriObjects.contactObjects import *

class meCard(Plugin):
	
	@register("de-DE", "(Wer bin ich.*)|(Wie ist mein name.*)")
	def mePerson(self, speech, language):
		
		self.say("Du bist {0}, das ist, was du mir gesagt hast. anyway.".format(self.user_name()))		
		
		person_search = PersonSearch(self.refId)
		person_search.scope = PersonSearch.ScopeLocalValue
		person_search.me = "true"        
		person_return = self.getResponseForRequest(person_search)
		person_ = person_return["properties"]["results"]
		mecard = PersonSnippet(persons=person_)
		view = AddViews(self.refId, dialogPhase="Completion")		
		view.views = [mecard]
		self.sendRequestWithoutAnswer(view)
		self.complete_request()