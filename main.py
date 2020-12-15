import sys
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import os
import ntpath
from moviepy.editor import *
import pafy
import shutil

class MyWindow(QWidget):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.setGeometry(158, 158, 754, 554)
        self.setMaximumWidth(754)
        self.setMaximumHeight(554)
        self.setMinimumWidth(754)
        self.setMinimumHeight(554)
        self.setWindowTitle("ConDo")
        self.setWindowIcon(QtGui.QIcon('music.png'))
        self.initUI()
        self.setStyleSheet("""
                            QPushButton {
                                border-radius: 15px;
                                border: 1px solid green;
                                background-color: lightgrey;
                            }

                            QPushButton:hover {
                                background-color: white;
                            }

                            QLineEdit {
                                border-radius: 7px;
                                border: 1px solid green;
                                background-color: lightgrey;
                            }

                            QLineEdit:hover {
                                background-color: white;
                            }

                            QLineEdit:focus {
                                background-color: white;
                            }
                            """)

    def initUI(self):
        self.label = QtWidgets.QLabel(self)
        self.label.setText("")
        self.label.move(754 // 2 - 21, 554 // 3 + 554 // 3)
        self.label.setFont(QFont("Bahnschrift", 17))
        self.label.resize(1000, 45)

        self.l = QtWidgets.QLabel(self)
        self.l.setText("Welcome to ConDo")
        self.l.move(754 // 2 - 105, 554 // 3)
        self.l.setFont(QFont("Bahnschrift", 17))
        self.l.resize(10000, 27)

        self.btn1 = QtWidgets.QPushButton(self)
        self.btn1.setText("Convert")
        self.btn1.setGeometry(754 // 3 - 77, 554 // 2 - 37, 154, 75)
        self.btn1.clicked.connect(self.convert)
        self.btn1.setFont(QFont("Bahnschrift", 17))

        self.btn2 = QtWidgets.QPushButton(self)
        self.btn2.setText("Download")
        self.btn2.setGeometry(754 // 3 + 754 // 3 - 77, 554 // 2 - 37, 154, 75)
        self.btn2.clicked.connect(self.download)
        self.btn2.setFont(QFont("Bahnschrift", 17))

        self.btn3 = QtWidgets.QPushButton(self)
        self.btn3.setText("mp3")
        self.btn3.setGeometry(10000000, 554 // 2 - 37, 154, 75)
        self.btn3.clicked.connect(self.convertmp3)
        self.btn3.setFont(QFont("Bahnschrift", 17))

        self.btn4 = QtWidgets.QPushButton(self)
        self.btn4.setText("wav")
        self.btn4.setGeometry(10000000, 554 // 2 - 37, 154, 75)
        self.btn4.clicked.connect(self.convertwav)
        self.btn4.setFont(QFont("Bahnschrift", 17))

        self.btnB = QtWidgets.QPushButton(self)
        self.btnB.setText("Main page")
        self.btnB.setGeometry(7540 - 97, 554 - 47, 97, 47)
        self.btnB.clicked.connect(self.mainPage)
        self.btnB.setFont(QFont("Bahnschrift", 11))

        self.btnD = QtWidgets.QPushButton(self)
        self.btnD.setText("Download Video")
        self.btnD.setGeometry(7540 // 3 + 754 // 3 - 77, 554 // 2 - 37, 154, 75)
        self.btnD.clicked.connect(self.download_vid)
        self.btnD.setFont(QFont("Bahnschrift", 11))

        self.textbox = QLineEdit(self)
        self.textbox.move(200000, 20)
        self.textbox.resize(310, 40)
        self.textbox.setFont(QFont("Bahnschrift", 11))

    def convert(self):
        self.btnB.setGeometry(754 - 97, 554 - 47, 97, 47)
        self.label.setText("")
        self.btn1.setGeometry(10000000, 554 // 2 - 37, 154, 75)
        self.btn2.setGeometry(10000000, 554 // 2 - 37, 154, 75)
        self.btn3.setGeometry(754 // 3 - 77, 554 // 2 - 37, 154, 75)
        self.btn4.setGeometry(754 // 3 + 754 // 3 - 77, 554 // 2 - 37, 154, 75)
        self.l.move(754 // 2 - 65, 554 // 3)
        self.l.setText("Convert to")

    def download(self):
        self.btnB.setGeometry(754 - 97, 554 - 47, 97, 47)
        self.textbox.move(754 // 2 - 155, 554 // 2 - 69)
        self.btn1.setGeometry(1000, 554 // 2 - 37, 154, 75)
        self.btn2.move(7540 // 2 - 77, 554 // 2)
        self.btnD.move(754 // 2 - 77, 554 // 2)
        self.label.move(754 // 2 - 187, 554 // 3 + 554 // 3)
        self.label.setFont(QFont("Bahnschrift", 11))
        self.label.setText("Download will start when you press the button")
        self.l.move(754 // 2 - 277, 554 // 3 + 554 // 3 + 27)
        self.l.setFont(QFont("Bahnschrift", 11))
        self.l.setText('Please do not close this app until you recieve a "Downloaded" message')

    def download_vid(self):
        try:
            self.btnB.setGeometry(754 - 97, 554 - 47, 97, 47)
            self.label.move(754 // 2 - 145, 554 // 3 + 554 // 3)
            url = self.textbox.text()
            video = pafy.new(url)
            best = video.getbest()
            best.download()
            shutil.move("{}.mp4".format(video.title), "{}.mp4".format(video.title))
            self.l.move(754 // 2 - 27, 554 // 3 + 554 // 3 + 27)
            self.l.setText("Video saved to Converter\media as .mp4 and format")
            self.label.move(754 // 2 - 79, 554 // 3 + 554 // 3)
            self.label.setFont(QFont("Bahnschrift", 17))
            self.label.setText("Downloaded")
        except ValueError:
            self.label.move(754 // 2 - 183, 554 // 3 + 554 // 3)
            self.label.setFont(QFont("Bahnschrift", 11))
            self.label.setText("Please fill the text area correct and try again")

    def convertmp3(self):
        try:
            self.btnB.setGeometry(754 - 97, 554 - 47, 97, 47)
            fname = QFileDialog.getOpenFileName(self, 'Open file', 'C:/', "Video files (*.mp4 *.webm)")
            videoPath = fname[0]
            pixmap = QPixmap(videoPath)
            video = VideoFileClip(os.path.join(videoPath))
            base = os.path.splitext(ntpath.basename(videoPath))[0]
            video.audio.write_audiofile(os.path.join("media/{}.mp3".format(base)))
            self.l.move(754 // 2 - 69, 554 // 3)
            self.l.setText("Converted to")
            self.label.move(754 // 2 - 173, 554 // 3 + 554 // 3)
            self.label.setText("File path: ConverterApp\media")
        except IOError:
            self.label.move(754 // 2 - 207, 554 // 3 + 554 // 3)
            self.label.setFont(QFont("Bahnschrift", 17))
            self.label.setText("Please select a file and try again")

    def convertwav(self):
        try:
            self.btnB.setGeometry(754 - 97, 554 - 47, 97, 47)
            fname = QFileDialog.getOpenFileName(self, 'Open file', 'C:/', "Video files (*.mp4 *.webm)")
            videoPath = fname[0]
            pixmap = QPixmap(videoPath)
            video = VideoFileClip(os.path.join(videoPath))
            base = os.path.splitext(ntpath.basename(videoPath))[0]
            video.audio.write_audiofile(os.path.join("media", "{}.wav".format(base)))
            self.l.move(754 // 2 - 69, 554 // 3)
            self.l.setText("Converted to")
            self.label.move(754 // 2 - 173, 554 // 3 + 554 // 3)
            self.label.setText("File path: Converter/media/")
        except IOError:
            self.label.move(754 // 2 - 207, 554 // 3 + 554 // 3)
            self.label.setFont(QFont("Bahnschrift", 17))
            self.label.setText("Please select a file and try again")

    def mainPage(self):
        self.label.setText("")
        self.label.move(754 // 2 - 21, 554 // 3 + 554 // 3)
        self.label.setFont(QFont("Bahnschrift", 17))

        self.l.setText("Welcome to ConDo")
        self.l.move(754 // 2 - 105, 554 // 3)
        self.l.setFont(QFont("Bahnschrift", 17))
        self.l.resize(1000, 27)

        self.btn1.setText("Convert")
        self.btn1.setGeometry(754 // 3 - 77, 554 // 2 - 37, 154, 75)
        self.btn1.clicked.connect(self.convert)
        self.btn1.setFont(QFont("Bahnschrift", 17))

        self.btn2.setText("Download")
        self.btn2.setGeometry(754 // 3 + 754 // 3 - 77, 554 // 2 - 37, 154, 75)
        self.btn2.clicked.connect(self.download)
        self.btn2.setFont(QFont("Bahnschrift", 17))

        self.btn3.setText("mp3")
        self.btn3.setGeometry(10000000, 554 // 2 - 37, 154, 75)
        self.btn3.clicked.connect(self.convertmp3)
        self.btn3.setFont(QFont("Bahnschrift", 17))

        self.btn4.setText("wav")
        self.btn4.setGeometry(10000000, 554 // 2 - 37, 154, 75)
        self.btn4.clicked.connect(self.convertwav)
        self.btn4.setFont(QFont("Bahnschrift", 17))

        self.btnD.setText("Download Video")
        self.btnD.setGeometry(7540 // 3 + 754 // 3 - 77, 554 // 2 - 37, 154, 75)
        self.btnD.clicked.connect(self.download_vid)
        self.btnD.setFont(QFont("Bahnschrift", 11))

        self.btnB.setText("Main page")
        self.btnB.setGeometry(7540 - 97, 554 - 47, 97, 47)
        self.btnB.clicked.connect(self.mainPage)
        self.btnB.setFont(QFont("Bahnschrift", 11))

        self.textbox.move(200000, 20)
        self.textbox.resize(310, 40)

def window():
    app = QApplication(sys.argv)
    win = MyWindow()
    win.show()
    sys.exit(app.exec_())

window()