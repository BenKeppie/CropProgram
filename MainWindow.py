import sys

from PyQt4.QtCore import *
from PyQt4.QtGui import *

from PotatoClass import *
from WheatClass import *

from RadioButtonClass import *

class CropWindow(QMainWindow):
    """This class creates a main window to observe the growth of a simulation"""

    def __init__(self):
        super().__init__() #calls super class
        self.setWindowTitle("Crop Simulator")
        self.create_select_crop_layout()

    def create_select_crop_layout(self):
        #initial layout of window (selecting crop type)
        self.crop_radio_buttons=RadioButtonWidget("Crop Simulation","Please select a crop", ("Wheat", "Potato"))
        self.instantiate_button=QPushButton("Create Crop")

        #layout to hold widgets
        self.initial_layout=QVBoxLayout()
        self.initial_layout.addWidget(self.crop_radio_buttons)
        self.initial_layout.addWidget(self.instantiate_button)

        self.select_crop_widget=QWidget()
        self.select_crop_widget.setLayout(self.initial_layout)

        self.setCentralWidget(self.select_crop_widget)

        self.instantiate_button.clicked.connect(self.instantiate_crop)

    def instantiate_crop(self):
        crop_type=self.crop_radio_buttons.selected_button() #Get radio button value
        if crop_type==1:
            self.simulated_crop=Wheat()
        elif crop_type==2:
            self.simulated_crop=Potato()
        print(self.simulated_crop)


if __name__ == "__main__":
    crop_simulation=QApplication(sys.argv) #monitors events
    crop_window=CropWindow() #Creates instance of class
    crop_window.show() #show instance
    crop_window.raise_() #raise instance to top of window stack
    crop_simulation.exec_() #Monitors
