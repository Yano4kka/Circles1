import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPainter, QColor
from random import *
from PyQt5 import uic


class WordTrick(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.trick_button.clicked.connect(self.draw_flag)
        self.do = False

    def paintEvent(self, event):
        if self.do:
            qp = QPainter()
            qp.begin(self)
            x, y = 50, 60
            h = randint(0, 100)
            w = h
            qp.setBrush(QColor(255, 247, 34))
            qp.drawEllipse(x, y, w, h)
            qp.end()

    def draw_flag(self):
        self.update()
        self.do = True


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = WordTrick()
    ex.show()
    sys.exit(app.exec())