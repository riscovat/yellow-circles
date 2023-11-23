import sys
from PyQt5.QtGui import QPainter, QColor, QBrush
from random import randint

from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton


class GoodMoodRising(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(400, 400, 400, 400)
        self.button = QPushButton('Кружок', self)
        self.button.move(130, 300)
        self.draw = False
        self.button.clicked.connect(self.run)

    def run(self):
        self.draw = True
        self.repaint()

    def paintEvent(self, event):
        if self.draw:
            qp = QPainter(self)
            qp.begin(self)
            pen = QBrush(QColor(randint(0, 255), randint(0, 255), randint(0, 255)))
            qp.setBrush(pen)
            qp.drawEllipse(150, 50, randint(0, 400), randint(0, 400))
            qp.end()
            self.draw = False


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = GoodMoodRising()
    ex.show()
    sys.exit(app.exec_())

