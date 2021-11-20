import sys

import random

from PyQt5.QtCore import QRect
from PyQt5.QtGui import QPixmap, QImage, QPainter, QColor
from PyQt5.QtWidgets import QApplication, QWidget, QFileDialog
from UI import Ui_Form


class SqPainter(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.paint)
        self.points = []
        self.do_paint = False

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            size = self.size()
            d = random.randint(10, 300)
            w, h = self.width(), self.height()
            x = random.randint(0, w - d)
            y = random.randint(0, h - d - 50)
            print(size)
            self.points.append((x, y, d))
            for x, y, d in self.points:
                color = random.randint(0, 0xffffff)
                qp.setBrush(QColor(color))
                qp.drawEllipse(QRect(x, y, d, d))
            qp.end()
            self.do_paint = False

    def paint(self):
        self.do_paint = True
        self.repaint()
        self.do_paint = False


def except_hook(cls, exception, traceback):
    sys.excepthook(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = SqPainter()
    ex.show()
    sys.excepthook = except_hook
    sys.exit(app.exec_())
