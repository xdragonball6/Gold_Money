# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'loadingrOfDiY.ui'
##
## Created by: Qt User Interface Compiler version 6.8.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)

class Ui_LoadingWidget(object):
    def setupUi(self, LoadingWidget):
        if not LoadingWidget.objectName():
            LoadingWidget.setObjectName(u"LoadingWidget")
        LoadingWidget.resize(300, 300)
        LoadingWidget.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        LoadingWidget.setStyleSheet(u"background-color: transparent;")
        self.loading_label = QLabel(LoadingWidget)
        self.loading_label.setObjectName(u"loading_label")
        self.loading_label.setGeometry(QRect(0, 0, 300, 300))
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.loading_label.sizePolicy().hasHeightForWidth())
        self.loading_label.setSizePolicy(sizePolicy)
        self.loading_label.setStyleSheet(u"background: rgba(0, 0, 0, 0.5);\n"
"border-bottom-left-radius: 10px;\n"
"border-bottom-right-radius: 10px;")
        self.loading_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.layer_frame = QFrame(LoadingWidget)
        self.layer_frame.setObjectName(u"layer_frame")
        self.layer_frame.setGeometry(QRect(0, 0, 300, 300))
        self.layer_frame.setStyleSheet(u"background-color: transparent;")
        self.layer_frame.setFrameShape(QFrame.Shape.NoFrame)
        self.layer_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.layer_vertical = QVBoxLayout(self.layer_frame)
        self.layer_vertical.setObjectName(u"layer_vertical")
        self.layer_vertical.setContentsMargins(-1, 0, -1, 0)
        self.spacer_1 = QSpacerItem(20, 134, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.layer_vertical.addItem(self.spacer_1)

        self.status_label = QLabel(self.layer_frame)
        self.status_label.setObjectName(u"status_label")
        self.status_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.layer_vertical.addWidget(self.status_label)

        self.spacer_2 = QSpacerItem(20, 133, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.layer_vertical.addItem(self.spacer_2)


        self.retranslateUi(LoadingWidget)

        QMetaObject.connectSlotsByName(LoadingWidget)
    # setupUi

    def retranslateUi(self, LoadingWidget):
        LoadingWidget.setWindowTitle(QCoreApplication.translate("LoadingWidget", u"Form", None))
        self.loading_label.setText("")
        self.status_label.setText("")
    # retranslateUi

