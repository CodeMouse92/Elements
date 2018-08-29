from PySide2.QtWidgets import QAction, qApp
from PySide2.QtGui import QIcon


class Actions(object):

    @staticmethod
    def build(window):
        actions = dict()

        # Quit
        actions["quit"] = Actions.createAction("Quit", action=qApp.quit,
                                               desc="Quit the application",
                                               shortcut="Ctrl+Q",
                                               icon="application-exit",
                                               window=window)

        return actions

    @staticmethod
    def createAction(name, action, window, desc=None, shortcut=None, icon=None):
        if icon:
            act = QAction(QIcon.fromTheme(icon), name, window)
        else:
            act = QAction(name, window)

        act.triggered.connect(action)

        if shortcut:
            act.setShortcut(shortcut)
        if desc:
            act.setToolTip(desc)
            act.setStatusTip(desc)

        return act
