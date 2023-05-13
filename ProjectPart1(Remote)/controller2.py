from PyQt5.QtWidgets import *
from view import *
from lab import *
QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)
QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)



class Controller(QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)
        self.ChanDown.clicked.connect(lambda: Television.channel_down)
        self.ChanUp.clicked.connect(lambda: Television.channel_up)
        self.VolUp.clicked.connect(lambda: Television.volume_up)
        self.VolDown.clicked.connect(lambda: Television.volume_down)
        self.power.clicked.connect(lambda: Television.power)
        self.Mute.clicked.connect(lambda: Television.mute)
        self.tv = Television()
        self.newvar = str(self.tv)
        self.volume = self.newvar
        self.volumedisplay.setText(self.volume)




