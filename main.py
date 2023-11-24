import sys
import random
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton
from PyQt5.QtGui import QPainter, QBrush, QColor


class Balls(QMainWindow):
    def __init__(self):
        super().__init__()
        self.do_paint = False
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 600, 600)
        self.setWindowTitle('Координаты')
        self.button = QPushButton(self)
        self.button.move(300, 550)
        self.button.clicked.connect(self.paint)

    def paint(self):
        self.do_paint = True
        self.update()

    def paintEvent(self, event):
        if self.do_paint:
            self.qp = QPainter()
            self.qp.begin(self)
            self.circle()
            self.qp.end()

    def circle(self):
        self.random = random.randint(1, 600)
        self.qp.setBrush(QColor(random.randint(1, 255), random.randint(1, 255), random.randint(1, 255)))
        self.qp.drawEllipse(random.randint(1, 600), random.randint(1, 600), self.random, self.random)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Balls()
    ex.show()
    sys.exit(app.exec_())