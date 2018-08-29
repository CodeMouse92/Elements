#!/usr/env/python3
# -*- coding: utf-8 -*-

import sys
from PySide2.QtWidgets import QApplication, QToolTip, QPushButton, QMessageBox, QDesktopWidget, \
    QMainWindow, QMenu, qApp, QAction, QHBoxLayout, QVBoxLayout, QWidget, QGridLayout
from PySide2.QtGui import QIcon, QFont

class AppWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        # Define members, as always
        self.statusbar = None
        self.toolbar = None

        self.initUI()

        # The number of times the button was clicked
        self.clicks = 0

    def initUI(self):
        # Define font
        QToolTip.setFont(QFont('SansSerif', 10))

        # Creates window tooltip
        self.setToolTip("This is a <b>QWidget</b> widget")

        # Create status bar
        self.statusbar = self.statusBar()
        self.statusbar.showMessage("Ready")

        # Create a menu (self-defined function)
        self.buildMenuBar()

        # Create a toolbar (self-defined function)
        self.buildToolbar()

        # Add button
        #btn = QPushButton("Click Me!", self)
        #btn.clicked.connect(self.buttonClick)
        #btn.setToolTip("Quit the application")
        #btn.resize(btn.sizeHint())
        #btn.move(50,50)

        decrementButton = QPushButton("-")
        decrementButton.resize(decrementButton.sizeHint())
        decrementButton.setToolTip("Decrement the count.")
        decrementButton.clicked.connect(self.decrement)

        incrementButton = QPushButton("+")
        incrementButton.setToolTip("Increment the count.")
        incrementButton.clicked.connect(self.increment)

        hbox = QHBoxLayout()
        hbox.addStretch(1)
        hbox.addWidget(decrementButton)
        hbox.addWidget(incrementButton)

        vbox = QVBoxLayout()
        vbox.addStretch(1)
        vbox.addLayout(hbox)

        # Sets up the primary layout box.
        # We MUST do it this way with the central widget in a QMainWindow,
        # because Layouts != Widgets. It's a special case.
        central = QWidget()
        central.setLayout(vbox)
        self.setCentralWidget(central)

        # Define window size and properties
        self.setGeometry(300, 300, 300, 220)
        self.setWindowTitle("Elements")
        self.setWindowIcon(QIcon('icons/app/elements_icon.png'))

        # Center the window on the screen
        self.center()

        # Show the window itself
        self.show()

    def contextMenuEvent(self, event):
        cmenu = QMenu(self)

        newAct = cmenu.addAction("New")
        opnAct = cmenu.addAction("Open")
        quitAct = cmenu.addAction("Quit")
        action = cmenu.exec_(self.mapToGlobal(event.pos()))

        if action == quitAct:
            qApp.quit()

    def buildToolbar(self):
        addAct = QAction(QIcon.fromTheme("list-add"), "Add", self)
        addAct.setShortcut("Ctrl+=")
        addAct.triggered.connect(self.increment)

        exitAct = QAction(QIcon.fromTheme("application-exit"), "Exit", self)
        exitAct.setShortcut("Ctrl+Q")
        exitAct.triggered.connect(qApp.quit)

        self.toolbar = self.addToolBar("Actions")
        self.toolbar.addAction(addAct)
        self.toolbar.addAction(exitAct)

    def buildMenuBar(self):
        menuBar = self.menuBar()

        #exitAct = QAction(QIcon('exit.png'), "&Exit", self)
        exitAct = QAction(QIcon.fromTheme("application-exit"), "&Exit", self)
        exitAct.setShortcut("Ctrl+Q")
        exitAct.setStatusTip("Exit application")
        exitAct.triggered.connect(qApp.quit)

        impMenu = QMenu("Import", self)
        imtAct = QAction("Import mail", self)
        impMenu.addAction(imtAct)

        fileMenu = menuBar.addMenu("&File")
        fileMenu.addMenu(impMenu)
        fileMenu.addAction(exitAct)

        viewStatAct = QAction("View statusbar", self, checkable=True)
        viewStatAct.setStatusTip("View statusbar")
        viewStatAct.setChecked(True)
        viewStatAct.triggered.connect(self.toggleStatus)

        viewMenu = menuBar.addMenu("&View")
        viewMenu.addAction(viewStatAct)

    def toggleStatus(self, state):
        if state:
            self.statusbar.show()
        else:
            self.statusbar.hide()

    def increment(self):
        self.clicks += 1
        self.statusbar.showMessage(str(self.clicks))

    def decrement(self):
        self.clicks -= 1
        self.statusbar.showMessage(str(self.clicks))

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def closeEvent(self, event):

        reply = QMessageBox.question(self, "Hey There!",
                                     "Are you sure you want to quit?",
                                     QMessageBox.Yes | QMessageBox.No,
                                     QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()


if __name__ == "__main__":
    app = QApplication(sys.argv)

    w = AppWindow()

    sys.exit(app.exec_())