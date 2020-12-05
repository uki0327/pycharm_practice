import sys

from PyQt5.QtWidgets import QApplication, QWidget, QTextEdit, QVBoxLayout


class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.te = QTextEdit()

        for i in range(9):
            for j in range(9):
                a = i + 1
                b = j + 1
                self.te.append(a + ' x ' + b + ' = ' + a * b + '\n')

        self.te.move(20, 20)

        layout = QVBoxLayout()
        layout.addWidget(self.te)

        self.setWindowTitle('구구단')
        self.setGeometry(100, 100, 900, 300)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
