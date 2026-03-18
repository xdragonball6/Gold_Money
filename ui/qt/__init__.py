import os
import sys
from PySide6.QtGui import QMovie, QPixmap
from PySide6.QtCore import Qt, QSize
from PySide6.QtWidgets import QWidget, QDialog

from .loading import Ui_LoadingWidget
from .login_dialog import Ui_LoginDialog
from .main_window import Ui_MainWindow

sys.path.append(os.path.abspath(os.path.dirname(__file__)))

class LoadingWidget(QWidget, Ui_LoadingWidget):
    def __init__(self, *args, **kwargs):
        super(LoadingWidget, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.gif = QMovie(u':/loading/loading.gif')
        self.gif.setScaledSize(QSize(120, 120))
        self.loading_label.setMovie(self.gif)
        self.hide()

    def end(self):
        self.hide()
        self.gif.stop()
        self.status_label.setText('')

    def start(self):
        self.resize(self.parent().size())
        self.loading_label.resize(self.size())
        self.layer_frame.resize(self.size())
        self.gif.start()
        self.show()


class LoginDialog(QDialog, Ui_LoginDialog):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)
        self.loading = LoadingWidget(self.item_frame)