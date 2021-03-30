"""
MainApp [Elements]
The main GUI application.

Author(s): Jason C. McDonald
"""

import sys
from PySide2.QtWidgets import QApplication
from elements.interface.mainwindow import MainWindow


class MainApp(object):

    def __init__(self):
        self.app = QApplication(sys.argv)
        self.w = MainWindow()
        sys.exit(self.app.exec_())