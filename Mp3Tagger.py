#!/usr/bin/python
#-*-coding: utf-8 -*-

import string
import re
from ID3 import *

class Mp3Tagger(object):
    def __init__(self):
        pass
    def setFile(self,filename):
        self.objID3 = ID3(filename)
        self.options = {}
    def getTags(self):
        return self.objID3.as_dict()
    def setTitle(self, title):
        self.options['TITLE'] = title
    def setArtist(self, artist):
        self.options['ARTIST'] = artist
    def setAlbum(self, album):
        self.options['ALBUM'] = album
    def setYear(self, year):
        self.options['YEAR'] = str(year)
    def setComment(self, comment):
        self.options['COMMENT'] = comment
    def setGenre(self, genre):
        self.options['GENRE'] = genre
    def setTracknumber(self, number):
        self.options['TRACKNUMBER'] = str(number)
    def delete(self):
        self.objID3.delete()
    def save(self):
        needsWrite = 0

        if len(self.options.keys()) > 0:
            needsWrite = 1

        for k, v in self.options.items():
            if k == 'GENRE' and re.match("\d+$", v):
                self.objID3[k] = string.atoi(v)
            else:
                self.objID3[k] = v
        if needsWrite:
            self.objID3.write()

if __name__ == '__main__':
    file = '/tmp/KalwiRemi-Kiss.mp3'
    mt = Mp3Tagger()
    mt.setFile(file)
    print(mt.getTags())
    mt.setAlbum('jakiś inny')
    mt.save()
    print(mt.getTags())