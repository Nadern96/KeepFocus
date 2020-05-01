import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QAction, QDialog, QVBoxLayout, QLabel
from PyQt5 import QtCore, QtGui, QtWidgets 
from gui.MyTab import MyTabWidget
from database.modelsfun import *


class App(QMainWindow):
    def __init__(self):
        super().__init__()
        self.title = 'KeepFocus'
        self.setWindowTitle(self.title)        
        self.tab_widget = MyTabWidget(self)
        self.setCentralWidget(self.tab_widget)

        # add menu bar
        mainMenu = self.menuBar()
        mainMenu.setStyleSheet("color:#017ffc;padding:5px;")
        fileMenu = mainMenu.addMenu('File')

        # exit button
        exitButton = QAction('Exit', self)
        exitButton.setShortcut('Ctrl+Q')
        exitButton.setStatusTip('Exit application')
        exitButton.triggered.connect(self.close)
        # About button
        aboutButton = QAction('About', self)
        aboutButton.setShortcut('Ctrl+B')
        aboutButton.setStatusTip('About application')
        aboutButton.triggered.connect(self.about)

        fileMenu.addAction(aboutButton)
        fileMenu.addAction(exitButton)

        self.showMaximized()
        self.setMinimumSize(700,650)
        self.setContentsMargins(0, 0, 0, 0);
        self.setStyleSheet("background-color:#22282d;")


    def about(self):
        aboutDialog = QDialog(self)
        aboutDialog.setFixedSize(400,200)
        aboutDialog.setWindowTitle("About")
        aboutDialog.setStyleSheet("background:white")

        layout = QVBoxLayout(self)
        label = QLabel(self)
        label.setText(
"""KeepFocus keeps tracking your screen, analyzing what \nyou are doing and giving you feedback on how to do\nbetter and how to be more productive.\n
It does so by taking a screenshot of the screen every\nfixed interval and using image processing technology to\nknow what you are doing and notify you when you lose\ntrack.\n\nCopyright © 2020 all rights reserved for TimeWorries
"""
        )
        layout.addWidget(label);
        aboutDialog.setLayout(layout);
        aboutDialog.show()        

if __name__ == '__main__':
    checkDay()
    QApplication.setStyle("Fusion")
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
