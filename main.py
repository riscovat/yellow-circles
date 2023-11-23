import sys
from PyQt5 import uic
from PyQt5.QtGui import QPainter, QPen, QColor, QBrush
from PyQt5.QtCore import Qt
from random import randint

from PyQt5.QtWidgets import QMainWindow, QApplication


class GoodMoodRising(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.pushButton.clicked.connect(self.run)
        self.color = QColor(255, 255, 0)
        self.draw = False

    def run(self):
        self.draw = True
        self.repaint()

    def paintEvent(self, event):
        if self.draw:
            qp = QPainter(self)
            qp.begin(self)
            pen = QBrush(self.color)
            qp.setBrush(pen)
            qp.drawEllipse(150, 50, randint(0, 400), randint(0, 400))
            qp.end()
            self.draw = False


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = GoodMoodRising()
    ex.show()
    sys.exit(app.exec_())
