from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QListView
import sys


class Form(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('ui.ui', self)
        self.push.clicked.connect(self.map)

    def map(self):
        print(self.lineEdit.text())
        print(self.lineEdit_2.text())
        print(self.lineEdit_3.text())
        print(self.lineEdit_4.text())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Form()
    ex.show()
    sys.exit(app.exec())
