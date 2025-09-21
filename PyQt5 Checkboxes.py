# PyQt5 Checkboxes
import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QCheckBox


class SecondWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(700, 300, 500, 500)
        self.setWindowTitle("Checkbox Example")

        self.checkbox = QCheckBox("Do you like food?", self)
        self.initUI()

    def initUI(self):
        self.checkbox.setGeometry(50, 50, 400, 100)
        self.checkbox.setStyleSheet("font-size: 30px;"
            "font-family: Arial;")
        self.checkbox.setChecked(False)
        self.checkbox.stateChanged.connect(self.checkbox_changed)

    def checkbox_changed(self, state):
        # print(state)
        if state == Qt.Checked: # 2
            print("You like food")
        else:
            print("You DO NOT like food")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = SecondWindow()
    window.show()
    sys.exit(app.exec_())
