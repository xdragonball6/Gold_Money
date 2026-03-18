# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'login_dialogukADWQ.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *


class Ui_LoginDialog(object):
    def setupUi(self, LoginDialog):
        if not LoginDialog.objectName():
            LoginDialog.setObjectName(u"LoginDialog")
        LoginDialog.resize(400, 300)
        self.verticalLayout = QVBoxLayout(LoginDialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.top_widget = QWidget(LoginDialog)
        self.top_widget.setObjectName(u"top_widget")
        self.top_widget.setMaximumSize(QSize(16777215, 40))
        self.top_horizontal = QHBoxLayout(self.top_widget)
        self.top_horizontal.setSpacing(5)
        self.top_horizontal.setObjectName(u"top_horizontal")
        self.top_horizontal.setContentsMargins(9, 5, 9, 5)
        self.title_label = QLabel(self.top_widget)
        self.title_label.setObjectName(u"title_label")

        self.top_horizontal.addWidget(self.title_label)

        self.exit_btn = QPushButton(self.top_widget)
        self.exit_btn.setObjectName(u"exit_btn")
        sizePolicy = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.exit_btn.sizePolicy().hasHeightForWidth())
        self.exit_btn.setSizePolicy(sizePolicy)
        self.exit_btn.setMaximumSize(QSize(30, 16777215))
        self.exit_btn.setStyleSheet(u"font: 9pt \"fontello\";border: 0;")
        self.exit_btn.setAutoDefault(False)
        self.exit_btn.setFlat(True)

        self.top_horizontal.addWidget(self.exit_btn)


        self.verticalLayout.addWidget(self.top_widget)

        self.item_frame = QFrame(LoginDialog)
        self.item_frame.setObjectName(u"item_frame")
        self.item_frame.setFrameShape(QFrame.NoFrame)
        self.verticalLayout_2 = QVBoxLayout(self.item_frame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(18, -1, 18, -1)
        self.id_edit = QLineEdit(self.item_frame)
        self.id_edit.setObjectName(u"id_edit")
        self.id_edit.setMinimumSize(QSize(0, 35))

        self.verticalLayout_2.addWidget(self.id_edit)

        self.pw_edit = QLineEdit(self.item_frame)
        self.pw_edit.setObjectName(u"pw_edit")
        self.pw_edit.setMinimumSize(QSize(0, 35))
        self.pw_edit.setEchoMode(QLineEdit.Normal)

        self.verticalLayout_2.addWidget(self.pw_edit)

        self.login_btn = QPushButton(self.item_frame)
        self.login_btn.setObjectName(u"login_btn")
        self.login_btn.setMinimumSize(QSize(0, 40))

        self.verticalLayout_2.addWidget(self.login_btn)


        self.verticalLayout.addWidget(self.item_frame)


        self.retranslateUi(LoginDialog)

        QMetaObject.connectSlotsByName(LoginDialog)
    # setupUi

    def retranslateUi(self, LoginDialog):
        LoginDialog.setWindowTitle(QCoreApplication.translate("LoginDialog", u"Dialog", None))
        self.title_label.setText(QCoreApplication.translate("LoginDialog", u"\ub85c\uadf8\uc778", None))
        self.exit_btn.setText(QCoreApplication.translate("LoginDialog", u"\uee0f", None))
        self.id_edit.setPlaceholderText(QCoreApplication.translate("LoginDialog", u"ID", None))
        self.pw_edit.setText("")
        self.pw_edit.setPlaceholderText(QCoreApplication.translate("LoginDialog", u"PW", None))
        self.login_btn.setText(QCoreApplication.translate("LoginDialog", u" \ub85c\uadf8\uc778", None))
    # retranslateUi

