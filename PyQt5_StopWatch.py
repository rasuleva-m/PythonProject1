# Import system-specific parameters and functions (needed for QApplication)
import sys

# Import necessary PyQt5 widgets for GUI elements
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel,
                             QPushButton, QVBoxLayout, QHBoxLayout)

# Import QTimer for timed events, QTime for time handling, and Qt for alignment
from PyQt5.QtCore import QTimer, QTime, Qt


# Define StopWatch class that inherits from QWidget (a window widget)
class StopWatch(QWidget):
    def __init__(self):
        super().__init__()  # Initialize QWidget (parent class)

        # Initialize the stopwatch time to 0 hours, 0 minutes, 0 seconds, 0 ms
        self.time = QTime(0, 0, 0, 0)

        # QLabel to display the current stopwatch time (initially 00:00:00.00)
        self.time_label = QLabel("00:00:00.00", self)

        # Create Start, Stop, and Reset buttons
        self.start_button = QPushButton("Start", self)
        self.stop_button = QPushButton("Stop", self)
        self.reset_button = QPushButton("Reset", self)

        # QTimer object to update stopwatch periodically
        self.timer = QTimer(self)

        # Call the function that sets up the UI
        self.initUI()

    def initUI(self):
        # Set the window title
        self.setWindowTitle("Stopwatch")

        # Create a vertical box layout to stack widgets vertically
        vbox = QVBoxLayout()

        # Add the time label (showing time) into the vertical layout
        vbox.addWidget(self.time_label)

        # Set the layout for the main window
        self.setLayout(vbox)

        # Center the text inside the QLabel
        self.time_label.setAlignment(Qt.AlignCenter)

        # Create a horizontal layout for buttons
        hbox = QHBoxLayout()

        # Add buttons (Start, Stop, Reset) horizontally
        hbox.addWidget(self.start_button)
        hbox.addWidget(self.stop_button)
        hbox.addWidget(self.reset_button)

        # Add the horizontal layout into the vertical layout
        vbox.addLayout(hbox)

        # Apply CSS-like styles to buttons and label
        self.setStyleSheet("""
            QPushButton, QLabel{
                padding: 20px;
                font-weight: bold;
                font-family: calibri;
            }

            QPushButton{
                font-size: 50px;
            }

            QLabel{
                font-size: 120px;
                background-color: hsl(200, 100%, 85%);
                border-radius: 20px;
            }
        """)

        # Connect button clicks to their respective functions
        self.start_button.clicked.connect(self.start)  # Start stopwatch
        self.stop_button.clicked.connect(self.stop)  # Stop stopwatch
        self.reset_button.clicked.connect(self.reset)  # Reset stopwatch

        # Connect the timer timeout signal to update_display function
        self.timer.timeout.connect(self.update_display)

    # Start button: begin timer with 10 ms interval
    def start(self):
        self.timer.start(10)

    # Stop button: stop the timer
    def stop(self):
        self.timer.stop()

    # Reset button: stop timer and reset time back to 0
    def reset(self):
        self.timer.stop()
        self.time = QTime(0, 0, 0, 0)  # Reset time object
        self.time_label.setText(self.format_time(self.time))  # Update label

    # Helper function to format time into hh:mm:ss.ms
    def format_time(self, time):
        hours = time.hour()
        minutes = time.minute()
        seconds = time.second()
        milliseconds = time.msec() // 10  # Convert ms to 2-digit (centiseconds)
        return f"{hours:02}:{minutes:02}:{seconds:02}.{milliseconds:02}"

    # Function to increment time by 10 ms and update label
    def update_display(self):
        self.time = self.time.addMSecs(10)  # Add 10 ms
        self.time_label.setText(self.format_time(self.time))  # Refresh display


# Main execution block
if __name__ == '__main__':
    app = QApplication(sys.argv)  # Create the application
    stopwatch = StopWatch()  # Create StopWatch instance
    stopwatch.show()  # Show the window
    sys.exit(app.exec_())  # Run the event loop until exit
