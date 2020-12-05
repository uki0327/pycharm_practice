import sys
import time
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPainter, QPen, QColor
from PyQt5.QtWidgets import QWidget, QApplication
import numpy as np


class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 400, 300)
        self.setWindowTitle('DrawPoints')
        self.show()

    def paintEvent(self, e):
        qp = QPainter()
        qp.begin(self)
        self.draw_point(qp)
        qp.end()

    def draw_point(self, qp):
        pen = QPen()
        colors = ['#d83c5f','#3cd88f','#AA5ce3',
                  '#df4a26','#ae85f6','#f7a82e',
                  '#406cf3','#e9f229','#29acf2']
        for i in range(1000):
            pen.setWidth(np.random.randint(1,15))
            pen.setColor(QColor(np.random.choice(colors)))
            qp.setPen(pen)
            rand_x = 100*np.random.randn()
            rand_y = 100*np.random.randn()
            qp.drawPoint(self.width() / 2 + rand_x, self.height() /2 + rand_y)
            ## time.sleep(1)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
