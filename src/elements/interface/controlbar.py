"""
ControlBar [Elements]
The music playback bar.
"""
from elements.interface.common.fonts import Font_Heading1, Font_Heading2

from PySide2.QtCore import Qt, QSize
from PySide2.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, QPushButton, QLabel, QSlider, QDial, QSizePolicy
from PySide2.QtGui import QIcon, QPixmap

class ControlBar(QHBoxLayout):

    def __init__(self):
        super().__init__()
        self.imgCover = QLabel()

        self.buildButtons()
        self.buildInfo()
        self.buildCoverImage()

    def buildCoverImage(self):
        self.addWidget(self.imgCover)
        self.setCoverImage()

    def buildInfo(self):
        vboxInfo = QVBoxLayout()
        w_vboxInfo = QWidget()

        vboxInfo.setSpacing(1)
        vboxInfo.setContentsMargins(1, 1, 1, 1)

        lblPrimary = QLabel()
        lblPrimary.setText("Track Title")
        lblPrimary.setAlignment(Qt.AlignCenter)
        lblPrimary.setFont(Font_Heading1)

        lblSecondary = QLabel()
        lblSecondary.setText("Artist or Album Name")
        lblSecondary.setAlignment(Qt.AlignCenter)
        lblSecondary.setFont(Font_Heading2)

        vboxInfo.addWidget(lblPrimary)
        vboxInfo.addWidget(lblSecondary)

        w_vboxInfo.setLayout(vboxInfo)
        w_vboxInfo.setMinimumSize(100, 0)

        self.addWidget(w_vboxInfo)

    def buildButtons(self):
        btnPlay = QPushButton()
        btnPlay.setIcon(QIcon.fromTheme("media-playback-start"))
        btnPlay.setIconSize(QSize(20, 20))
        btnPlay.playState = False
        btnPlay.setObjectName("btnPlay")
        btnPlay.clicked.connect(self.callPlay)
        self.addWidget(btnPlay)

        btnStop = QPushButton()
        btnStop.setIcon(QIcon.fromTheme("media-playback-stop"))
        btnStop.setIconSize(QSize(20, 20))
        btnStop.setObjectName("btnStop")
        btnStop.clicked.connect(self.callStop)
        self.addWidget(btnStop)

        btnPrev = QPushButton()
        btnPrev.setIcon(QIcon.fromTheme("media-skip-backward"))
        btnPrev.setIconSize(QSize(20, 20))
        btnPrev.setObjectName("btnPrev")
        btnPrev.clicked.connect(self.callPrev)
        self.addWidget(btnPrev)

        sliderSeek = QSlider(Qt.Horizontal)
        sliderSeek.setMinimumSize(100, 0)
        self.addWidget(sliderSeek)

        btnNext = QPushButton()
        btnNext.setIcon(QIcon.fromTheme("media-skip-forward"))
        btnNext.setIconSize(QSize(20, 20))
        btnNext.setObjectName("btnNext")
        btnNext.clicked.connect(self.callNext)
        self.addWidget(btnNext)

    def callPlay(self, pressed):
        button = self.parentWidget().findChild(QPushButton, "btnPlay")
        if button.playState:
            button.setIcon(QIcon.fromTheme("media-playback-start"))
            button.playState = False
        else:
            button.setIcon(QIcon.fromTheme("media-playback-pause"))
            button.playState = True

    def callStop(self, pressed):
        button = self.parentWidget().findChild(QPushButton, "btnPlay")
        button.setIcon(QIcon.fromTheme("media-playback-start"))
        button.playState = False

    def callPrev(self, pressed):
        pass

    def callNext(self, pressed):
        pass

    def setCoverImage(self, path=None):
        # Define a new pixmap
        pixmap = QPixmap()

        # Attempt to load from the path. If it fails or no path is specified, load fallback.
        if not (path and pixmap.load(path)):
            path = 'icons/ui/elements_nocover.png'
            pixmap.load(path)

        # Scale the pixmap to 50x50
        pixmap = pixmap.scaled(50, 50)

        # Load the pixmap on the control bar
        self.imgCover.setPixmap(pixmap)