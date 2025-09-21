# PyQt5 introduction

import sys
from cProfile import label

# from PyQt5.QtGui.QIcon import pixmap # Error here
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtGui import QIcon, QFont, QPixmap
from PyQt5.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My cool first GUI")
        self.setGeometry(700, 300, 500, 500)
        self.setWindowIcon(QIcon("MuxarramPython.jpg"))

        label = QLabel(self)
        label.setGeometry(0, 0, 250, 250)

        pixmap = QPixmap("MuxarramPython.jpg")
        label.setPixmap(pixmap)

        label.setScaledContents(True)

        label.setGeometry((self.width() - label.width()) // 2,   #This is how to add an image to your PuQt5 application
                         (self.height() - label.height()) // 2,
                          label.width(),
                          label.height())

        label = QLabel("Hello", self)
        label.setFont(QFont("Arial", 40))
        label.setGeometry(0, 0, 500, 100)
        label.setStyleSheet("color: #292929;"
                            "background-color: #6fdcf7;"
                            "font-weight: bold;"
                            "font-style: italic;"
                            "text-decoration: underline;")

        label.setAlignment(Qt.AlignTop)  # VERTICALLY TOP
        label.setAlignment(Qt.AlignBottom)  # VERTICALLY BOTTOM
        label.setAlignment(Qt.AlignVCenter)  # VERTICALLY CENTER

        label.setAlignment(Qt.AlignRight) # HORIZONTALLY RIGHT
        label.setAlignment(Qt.AlignCenter) # HORIZONTALLY CENTER
        label.setAlignment(Qt.AlignLeft) # HORIZONTALLY LEFT

        label.setAlignment(Qt.AlignHCenter | Qt.AlignTop) #CENTER & TOP
        label.setAlignment(Qt.AlignHCenter | Qt.AlignBottom) #CENTER & BOTTOM
        label.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter) #H-CENTER & V-CENTER
        label.setAlignment(Qt.AlignCenter) #H-CENTER & V-CENTER


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()