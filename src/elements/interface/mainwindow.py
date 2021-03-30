"""
MainWindow [Elements]
The main application window.

Author(s): Jason C. McDonald
"""

from PySide2.QtWidgets import QMainWindow, QPushButton, QVBoxLayout, QWidget
from PySide2.QtGui import QIcon
from elements.interface.actions import Actions
from elements.interface.controlbar import ControlBar


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.barMenu = self.menuBar()
        self.actions = Actions.build(self)

        self.initUI()

    def initUI(self):
        # Define window size and properties
        self.setGeometry(300, 300, 300, 220)
        self.setWindowTitle("Elements")
        self.setWindowIcon(QIcon('icons/app/elements_icon.png'))

        central = QVBoxLayout()
        central.addStretch(1)
        centralWidget = QWidget()
        centralWidget.setLayout(central)
        self.setCentralWidget(centralWidget)

        controlBar = ControlBar()
        central.addLayout(controlBar)

        self.buildMenuBar()

        # Show the window itself
        self.show()

    def buildMenuBar(self):
        # File Menu
        menuFile = self.barMenu.addMenu("&File")
        menuFile.addAction(self.actions["quit"])
