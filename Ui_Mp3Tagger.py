# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Mp3Tagger.ui'
#
# Created: Sun Sep 26 23:38:59 2010
#      by: PyQt4 UI code generator 4.7.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_Mp3Tagger(object):
    def setupUi(self, Mp3Tagger):
        Mp3Tagger.setObjectName("Mp3Tagger")
        Mp3Tagger.resize(836, 664)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../../../../../media/sda3/pobrane/mp3.gif"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Mp3Tagger.setWindowIcon(icon)
        self.centralwidget = QtGui.QWidget(Mp3Tagger)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setSpacing(20)
        self.horizontalLayout.setSizeConstraint(QtGui.QLayout.SetDefaultConstraint)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.horizontalLayout.addItem(spacerItem)
        self.label = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.lineEditFilepath = QtGui.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEditFilepath.setFont(font)
        self.lineEditFilepath.setObjectName("lineEditFilepath")
        self.horizontalLayout.addWidget(self.lineEditFilepath)
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.horizontalLayout.addItem(spacerItem1)
        self.pushButtonFileDialog = QtGui.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.pushButtonFileDialog.setFont(font)
        self.pushButtonFileDialog.setObjectName("pushButtonFileDialog")
        self.horizontalLayout.addWidget(self.pushButtonFileDialog)
        spacerItem2 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.horizontalLayout.addItem(spacerItem2)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setSpacing(20)
        self.horizontalLayout_2.setSizeConstraint(QtGui.QLayout.SetDefaultConstraint)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem3 = QtGui.QSpacerItem(17, 75, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.horizontalLayout_2.addItem(spacerItem3)
        self.label_2 = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        spacerItem4 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.horizontalLayout_2.addItem(spacerItem4)
        self.lineEditTitle = QtGui.QLineEdit(self.centralwidget)
        self.lineEditTitle.setEnabled(True)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEditTitle.sizePolicy().hasHeightForWidth())
        self.lineEditTitle.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEditTitle.setFont(font)
        self.lineEditTitle.setObjectName("lineEditTitle")
        self.horizontalLayout_2.addWidget(self.lineEditTitle)
        spacerItem5 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.horizontalLayout_2.addItem(spacerItem5)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setSpacing(20)
        self.horizontalLayout_4.setSizeConstraint(QtGui.QLayout.SetDefaultConstraint)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem6 = QtGui.QSpacerItem(17, 75, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.horizontalLayout_4.addItem(spacerItem6)
        self.label_4 = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_4.addWidget(self.label_4)
        spacerItem7 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.horizontalLayout_4.addItem(spacerItem7)
        self.lineEditArtist = QtGui.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEditArtist.setFont(font)
        self.lineEditArtist.setObjectName("lineEditArtist")
        self.horizontalLayout_4.addWidget(self.lineEditArtist)
        spacerItem8 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.horizontalLayout_4.addItem(spacerItem8)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setSpacing(20)
        self.horizontalLayout_5.setSizeConstraint(QtGui.QLayout.SetDefaultConstraint)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        spacerItem9 = QtGui.QSpacerItem(17, 75, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.horizontalLayout_5.addItem(spacerItem9)
        self.label_5 = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_5.addWidget(self.label_5)
        spacerItem10 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.horizontalLayout_5.addItem(spacerItem10)
        self.lineEditAlbum = QtGui.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEditAlbum.setFont(font)
        self.lineEditAlbum.setObjectName("lineEditAlbum")
        self.horizontalLayout_5.addWidget(self.lineEditAlbum)
        spacerItem11 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.horizontalLayout_5.addItem(spacerItem11)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setSpacing(20)
        self.horizontalLayout_6.setSizeConstraint(QtGui.QLayout.SetDefaultConstraint)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        spacerItem12 = QtGui.QSpacerItem(17, 75, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.horizontalLayout_6.addItem(spacerItem12)
        self.label_6 = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_6.addWidget(self.label_6)
        spacerItem13 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.horizontalLayout_6.addItem(spacerItem13)
        self.lineEditYear = QtGui.QLineEdit(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEditYear.sizePolicy().hasHeightForWidth())
        self.lineEditYear.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEditYear.setFont(font)
        self.lineEditYear.setObjectName("lineEditYear")
        self.horizontalLayout_6.addWidget(self.lineEditYear)
        spacerItem14 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.horizontalLayout_6.addItem(spacerItem14)
        self.verticalLayout.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_7 = QtGui.QHBoxLayout()
        self.horizontalLayout_7.setSpacing(20)
        self.horizontalLayout_7.setSizeConstraint(QtGui.QLayout.SetDefaultConstraint)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        spacerItem15 = QtGui.QSpacerItem(17, 75, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.horizontalLayout_7.addItem(spacerItem15)
        self.label_7 = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_7.addWidget(self.label_7)
        spacerItem16 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.horizontalLayout_7.addItem(spacerItem16)
        self.lineEditTracknumber = QtGui.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEditTracknumber.setFont(font)
        self.lineEditTracknumber.setObjectName("lineEditTracknumber")
        self.horizontalLayout_7.addWidget(self.lineEditTracknumber)
        spacerItem17 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.horizontalLayout_7.addItem(spacerItem17)
        self.verticalLayout.addLayout(self.horizontalLayout_7)
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.pushButtonSave = QtGui.QPushButton(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButtonSave.sizePolicy().hasHeightForWidth())
        self.pushButtonSave.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButtonSave.setFont(font)
        self.pushButtonSave.setObjectName("pushButtonSave")
        self.gridLayout.addWidget(self.pushButtonSave, 0, 0, 1, 1)
        self.pushButtonClear = QtGui.QPushButton(self.centralwidget)
        self.pushButtonClear.setEnabled(True)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButtonClear.sizePolicy().hasHeightForWidth())
        self.pushButtonClear.setSizePolicy(sizePolicy)
        self.pushButtonClear.setObjectName("pushButtonClear")
        self.gridLayout.addWidget(self.pushButtonClear, 0, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        Mp3Tagger.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(Mp3Tagger)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 836, 23))
        self.menubar.setObjectName("menubar")
        Mp3Tagger.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(Mp3Tagger)
        self.statusbar.setObjectName("statusbar")
        Mp3Tagger.setStatusBar(self.statusbar)

        self.retranslateUi(Mp3Tagger)
        QtCore.QMetaObject.connectSlotsByName(Mp3Tagger)

    def retranslateUi(self, Mp3Tagger):
        Mp3Tagger.setWindowTitle(QtGui.QApplication.translate("Mp3Tagger", "Mp3Tagger", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Mp3Tagger", "Edytowany plik:", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonFileDialog.setText(QtGui.QApplication.translate("Mp3Tagger", "Wybierz plik", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("Mp3Tagger", "Tytuł:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("Mp3Tagger", "Artysta:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("Mp3Tagger", "Album:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("Mp3Tagger", "Rok:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setText(QtGui.QApplication.translate("Mp3Tagger", "Numer ścieżki:", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonSave.setText(QtGui.QApplication.translate("Mp3Tagger", "Zapisz zmiany", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonClear.setText(QtGui.QApplication.translate("Mp3Tagger", "Wyczyść metadane", None, QtGui.QApplication.UnicodeUTF8))

import icons_rc
