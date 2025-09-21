import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QRadioButton, QButtonGroup


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(700, 300, 500, 500)
        self.setWindowTitle("Radio Button Example")

        # Create radio buttons
        self.radio1 = QRadioButton("Visa", self)
        self.radio2 = QRadioButton("MasterCard", self)
        self.radio3 = QRadioButton("Gift Card", self)
        self.radio4 = QRadioButton("In Store", self)
        self.radio5 = QRadioButton("Online", self)
        self.button_group1 = QButtonGroup(self)
        self.button_group2 = QButtonGroup(self)
        # self.initUI()

        # Position them
        self.radio1.move(50, 50)
        self.radio2.move(50, 100)
        self.radio3.move(50, 150)
        self.radio4.move(50, 200)
        self.radio5.move(50, 250)

        # Group them so only one can be selected
        self.group = QButtonGroup(self)
        self.group.addButton(self.radio1)
        self.group.addButton(self.radio2)
        self.group.addButton(self.radio3)
        self.group.addButton(self.radio4)
        self.group.addButton(self.radio5)


        # Default selection
        self.radio1.setChecked(True)
        self.button_group1.addButton(self.radio1)
        self.button_group1.addButton(self.radio2)
        self.button_group1.addButton(self.radio3)
        self.button_group2.addButton(self.radio4)
        self.button_group2.addButton(self.radio5)

        self.radio1.toggled.connect(self.radio_button_changed)
        self.radio2.toggled.connect(self.radio_button_changed)
        self.radio3.toggled.connect(self.radio_button_changed)
        self.radio4.toggled.connect(self.radio_button_changed)
        self.radio5.toggled.connect(self.radio_button_changed)

    def radio_button_changed(self):
        radio_button = self.sender()     # THE SENDER METHOD IS GOING TO RETURN THE WIDGET THAT SENT THE SIGNAL
        if radio_button.isChecked():
            print(f"{radio_button.text()} is selected")
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
