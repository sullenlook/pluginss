import urllib2
import json

from plugin import *
class chucknorrisjoke(Plugin):

	@register ("de-DE", ".*Chuck.*norris.*witz.*")
	def st_chucknorris(self, speech, language):
		if language == 'de-DE':
			req = urllib2.Request("http://api.icndb.com/jokes/random")
		full_json = urllib2.urlopen(req).read()
		load = json.loads(full_json)
		store = load['value']['joke']
		store = store.replace('&quot;','\"')
		self.say(store)
		self.complete_request()