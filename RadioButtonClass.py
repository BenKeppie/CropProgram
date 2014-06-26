from PyQt4.QtGui import *

class RadioButtonWidget(QWidget):
    """This class creates a rodio button"""

    def __init__(self, label, instruction, button_list):
        super().__init__()

        self.title_label=QLabel(label)
        self.radio_group_box=QGroupBox(instruction)
        self.radio_button_group=QButtonGroup()

        self.radio_button_list=[]
        for each in button_list:
            self.radio_button_list.append(QRadioButton(each))

        #set default radio button value
        self.radio_button_list[0].setChecked(True)

        #create layout
        self.radio_button_layout=QVBoxLayout()
        #add button to layout
        counter=1
        for each in self.radio_button_list:
            self.radio_button_layout.addWidget(each)
            self.radio_button_group.addButton(each)
            self.radio_button_group.setId(each,counter)
            counter+=1

        #add layout to group box
        self.radio_group_box.setLayout(self.radio_button_layout)

        #create a layout for whole widget
        self.main_layout=QVBoxLayout()
        self.main_layout.addWidget(self.title_label)
        self.main_layout.addWidget(self.radio_group_box)

        #set layout for particular widget
        self.setLayout(self.main_layout)

    #method for button access
    def selected_button(self):
        return self.radio_button_group.checkedId()

        
