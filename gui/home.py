from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
import sys


class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.b1 = QtWidgets.QPushButton(self)
        self.label = QtWidgets.QLabel(self)
        self.w1 = QtWidgets.QLabel("Window 1")
        self.w2 = QtWidgets.QLabel("Window 2")
        self.initUI()
        self.setGeometry(200, 200, 300, 300)
        self.setWindowTitle("Encryption")

    def initUI(self):
        self.label.setText("My First Label")
        self.label.move(60, 60)

        self.b1.setText("Click Me")
        self.b1.clicked.connect(self.clicked)

    def clicked(self):
        self.label.setText("You Pressed the button")
        self.w1.show()
        self.w2.show()
        self.update()

    def update(self):
        self.label.adjustSize()


def window():
    app = QApplication(sys.argv)
    win = MyWindow()
    win.show()
    sys.exit(app.exec())


def testwin():
    w1 = QLabel("Window 1")
    w2 = QLabel("Window 2")
    w1.show()
    w2.show()


if __name__ == '__main__':
    window()
    # testwin()
