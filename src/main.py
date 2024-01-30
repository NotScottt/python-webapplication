import os
import sys
from PyQt5 import QtGui
from PyQt5.QtCore import *
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtWidgets import QApplication

path = f"file:///{os.getcwd()}/web/index.html".replace("\\", "/")

app = QApplication(sys.argv)

web = QWebEngineView()
web.setWindowTitle("Test")
web.setWindowIcon(QtGui.QIcon('assets/Stonks.ico'))

web.load(QUrl(path))
web.show()

sys.exit(app.exec_())