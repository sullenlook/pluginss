#!/usr/bin/python
# -*- coding: utf-8 -*-

# iJokes.py
# Based off of iJokes AssistantExtensions Plugin :)
#by Salman Burhan

from random import randint
from plugin import *
import os, random



class iJokes(Plugin):

    @register("en-US",".*Tell me a joke.*")
    def st_iJokes(self, speech, language):
        if language == 'en-US':
            filename = "./plugins/iJokes/iJokes.txt"
            file = open(filename, 'r')

            file_size = os.stat(filename)[6]

            file.seek((file.tell()+random.randint(0, file_size-1))%file_size)
    
            file.readline()

            line = file.readline()
    
            self.say(line) 
             
        self.complete_request()


