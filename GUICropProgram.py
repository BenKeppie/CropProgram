import sys
from PyQt4.QtGui import *
from PyQt4.QtCore import *

class MainWindow(QMainWindow):
    """The main window for my application"""
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Hello World")
        self.create_layout()

    def create_layout(self):
        self.text_box=QLineEdit()
        self.button=QPushButton("Submit")
        self.label=QLabel("Please enter your name")

        self.layout=QVBoxLayout()
        self.layout.addWidget(self.text_box)
        self.layout.addWidget(self.button)
        self.layout.addWidget(self.label)

        self.widget=QWidget()
        self.widget.setLayout(self.layout)
        self.setCentralWidget(self.widget)

        self.button.clicked.connect(self.display_name)

    def display_name(self):
        name=self.text_box.text()
        self.label.setText("Hello {0}!".format(name))
                                    




if __name__ == "__main__":
    application=QApplication(sys.argv)
    window=MainWindow()
    window.show()
    window.raise_()
    application.exec_()
