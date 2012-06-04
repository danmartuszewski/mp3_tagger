#!/usr/bin/python
#-*- coding:utf-8 -*-

#from encodings.string_escape import encode
#from encodings.string_escape import decode
import sys
import string
from PyQt4 import QtCore, QtGui
from Mp3Tagger import Mp3Tagger
from Ui_Mp3Tagger import Ui_Mp3Tagger

class MyTagger(QtGui.QMainWindow):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_Mp3Tagger()
        self.ui.setupUi(self)
        self.ui.lineEditFilepath.setReadOnly(True)

        QtCore.QObject.connect(self.ui.pushButtonFileDialog,
            QtCore.SIGNAL('clicked()'), self._fileDialog)
        QtCore.QObject.connect(self.ui.pushButtonClear,
            QtCore.SIGNAL('clicked()'), self._clear)
        QtCore.QObject.connect(self.ui.pushButtonSave,
            QtCore.SIGNAL('clicked()'), self._save)

    def _fileDialog(self):
        filename = QtGui.QFileDialog.getOpenFileName(self, 'Wybierz plik', '/tmp' '*.mp3')
        self.initialize(filename)

    def initialize(self,path):
        self.ui.lineEditFilepath.setText(QtCore.QString(path))
        self.objTagger = Mp3Tagger()
        self.objTagger.setFile(unicode(path).encode('utf-8'))
        self._setTags()

    def _setTags(self, tags={}):
        if not tags:
            tags = self.objTagger.getTags()
        try:
            title = unicode(tags['TITLE'].decode('utf-8'))
            self.ui.lineEditTitle.setText(QtCore.QString(title))
        except KeyError:
            self.ui.lineEditTitle.setText(QtCore.QString(''))
        try:
            artist = unicode(tags['ARTIST'].decode('utf-8'))
            self.ui.lineEditArtist.setText(QtCore.QString(artist))
        except KeyError:
            self.ui.lineEditArtist.setText(QtCore.QString(''))
        try:
            album = unicode(tags['ALBUM'].decode('utf-8'))
            self.ui.lineEditAlbum.setText(QtCore.QString(album))
        except KeyError:
            self.ui.lineEditAlbum.setText(QtCore.QString(''))
        try:
            self.ui.lineEditYear.setText(QtCore.QString(tags['YEAR']))
        except KeyError:
            self.ui.lineEditYear.setText(QtCore.QString(''))
        try:
            self.ui.lineEditTracknumber.setText(QtCore.QString(tags['TRACKNUMBER']))
        except KeyError:
            self.ui.lineEditTracknumber.setText(QtCore.QString(''))

    def _clear(self):
        self._setTags({'Tip':'Trick'})

    def _save(self):
        self.objTagger.setTitle(unicode(self.ui.lineEditTitle.text()).encode('utf-8'))
        self.objTagger.setArtist(unicode(self.ui.lineEditArtist.text()).encode('utf-8'))
        self.objTagger.setAlbum(unicode(self.ui.lineEditAlbum.text()).encode('utf-8'))
        try:
            self.objTagger.setYear(int(self.ui.lineEditYear.text()))
        except ValueError, TypeError:
            pass
        try:
            self.objTagger.setTracknumber(int(self.ui.lineEditTracknumber.text()))
        except ValueError, TypeError:
            pass
        self.objTagger.save()

        

if __name__ == '__main__':
    file = '/tmp/KalwiRemi-Kiss.mp3'
    app = QtGui.QApplication(sys.argv)
    myApp = MyTagger()
    myApp.show()
    sys.exit(app.exec_())
