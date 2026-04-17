import sys
from PyQt6.QtWidgets import QApplication, QWidget
from PyQt6 import uic
import pandas as pd
from dialog import Ui_Dialog



class AppDemo(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)  

if __name__ == '__main__':
    app =   QApplication([])
    demo = AppDemo()
    demo.show()
    app.exec()
