# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
##
## Created by: Qt User Interface Compiler version 6.10.2
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QLineEdit, QMainWindow, QPushButton, QSizePolicy,
    QSpacerItem, QTabWidget, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1028, 688)
        MainWindow.setMinimumSize(QSize(700, 500))
        MainWindow.setStyleSheet(u"\n"
"QMainWindow, QWidget#main_widget {\n"
"    background-color: #0f1117;\n"
"    color: #e0e0e0;\n"
"}\n"
"QFrame#ticker_bar {\n"
"    background-color: #161b27;\n"
"    border-bottom: 1px solid #2a3040;\n"
"}\n"
"QLabel#ticker_label {\n"
"    color: #a0aabb;\n"
"    font-size: 11px;\n"
"    padding: 2px 6px;\n"
"}\n"
"QLabel#gold_label {\n"
"    color: #f5c842;\n"
"    font-weight: bold;\n"
"    font-size: 12px;\n"
"    padding: 2px 8px;\n"
"}\n"
"QTabWidget::pane {\n"
"    border: 1px solid #2a3040;\n"
"    background-color: #0f1117;\n"
"}\n"
"QTabBar::tab {\n"
"    background-color: #161b27;\n"
"    color: #7a8ba0;\n"
"    padding: 8px 22px;\n"
"    font-size: 13px;\n"
"    border: 1px solid #2a3040;\n"
"    border-bottom: none;\n"
"    margin-right: 2px;\n"
"}\n"
"QTabBar::tab:selected {\n"
"    background-color: #1e2535;\n"
"    color: #e0e0e0;\n"
"    border-top: 2px solid #4a8cff;\n"
"}\n"
"QTabBar::tab:hover {\n"
"    background-color: #1a2030;\n"
"    color: #c0c8d8;\n"
"}\n"
"QLineEdit#search_input"
                        "_korea,\n"
"QLineEdit#search_input_japan,\n"
"QLineEdit#search_input_us,\n"
"QLineEdit#search_input_europe {\n"
"    background-color: #1a2030;\n"
"    color: #e0e0e0;\n"
"    border: 1px solid #2e3d56;\n"
"    border-radius: 6px;\n"
"    padding: 8px 12px;\n"
"    font-size: 14px;\n"
"    selection-background-color: #2d4a7a;\n"
"}\n"
"QLineEdit#search_input_korea:focus,\n"
"QLineEdit#search_input_japan:focus,\n"
"QLineEdit#search_input_us:focus,\n"
"QLineEdit#search_input_europe:focus {\n"
"    border: 1px solid #4a8cff;\n"
"}\n"
"QPushButton#search_btn_korea,\n"
"QPushButton#search_btn_japan,\n"
"QPushButton#search_btn_us,\n"
"QPushButton#search_btn_europe {\n"
"    background-color: #2d5aac;\n"
"    color: #ffffff;\n"
"    border: none;\n"
"    border-radius: 6px;\n"
"    padding: 8px 20px;\n"
"    font-size: 13px;\n"
"    font-weight: bold;\n"
"}\n"
"QPushButton#search_btn_korea:hover,\n"
"QPushButton#search_btn_japan:hover,\n"
"QPushButton#search_btn_us:hover,\n"
"QPushButton#search_btn_europe:hover {\n"
""
                        "    background-color: #3568c4;\n"
"}\n"
"QPushButton#search_btn_korea:pressed,\n"
"QPushButton#search_btn_japan:pressed,\n"
"QPushButton#search_btn_us:pressed,\n"
"QPushButton#search_btn_europe:pressed {\n"
"    background-color: #1e4088;\n"
"}\n"
"QFrame#result_card_korea,\n"
"QFrame#result_card_japan,\n"
"QFrame#result_card_us,\n"
"QFrame#result_card_europe {\n"
"    background-color: #161b27;\n"
"    border: 1px solid #2a3040;\n"
"    border-radius: 10px;\n"
"    padding: 6px;\n"
"}\n"
"QLabel#res_name   { color: #a8b8cc; font-size: 12px; }\n"
"QLabel#res_ticker { color: #556070; font-size: 11px; }\n"
"QLabel#res_price  { color: #e8eef8; font-size: 28px; font-weight: bold; }\n"
"QLabel#res_change_pos { color: #3ddc84; font-size: 14px; font-weight: bold; }\n"
"QLabel#res_change_neg { color: #ff5f5f; font-size: 14px; font-weight: bold; }\n"
"QLabel#res_change_neu { color: #aaaaaa; font-size: 14px; }\n"
"QLabel#hint_label_korea,\n"
"QLabel#hint_label_japan,\n"
"QLabel#hint_label_us,\n"
"QLabel#hint_label_europ"
                        "e {\n"
"    color: #3a4a60; font-size: 11px; font-style: italic;\n"
"}\n"
"QLabel#status_label { color: #556070; font-size: 11px; }\n"
"QLabel#loading_label { color: #4a8cff; font-size: 13px; }\n"
"QLabel#error_label   { color: #ff5f5f; font-size: 13px; }\n"
"   ")
        self.main_widget = QWidget(MainWindow)
        self.main_widget.setObjectName(u"main_widget")
        self.main_layout = QVBoxLayout(self.main_widget)
        self.main_layout.setSpacing(0)
        self.main_layout.setObjectName(u"main_layout")
        self.main_layout.setContentsMargins(0, 0, 0, 0)
        self.ticker_bar = QFrame(self.main_widget)
        self.ticker_bar.setObjectName(u"ticker_bar")
        self.ticker_bar.setMinimumHeight(48)
        self.ticker_bar.setMaximumHeight(48)
        self.ticker_bar.setFrameShape(QFrame.Shape.NoFrame)
        self.ticker_layout = QHBoxLayout(self.ticker_bar)
        self.ticker_layout.setSpacing(0)
        self.ticker_layout.setObjectName(u"ticker_layout")
        self.ticker_layout.setContentsMargins(14, 4, 14, 4)
        self.gold_label = QLabel(self.ticker_bar)
        self.gold_label.setObjectName(u"gold_label")

        self.ticker_layout.addWidget(self.gold_label)

        self.sep_gold = QLabel(self.ticker_bar)
        self.sep_gold.setObjectName(u"sep_gold")

        self.ticker_layout.addWidget(self.sep_gold)

        self.lbl_usd = QLabel(self.ticker_bar)
        self.lbl_usd.setObjectName(u"lbl_usd")

        self.ticker_layout.addWidget(self.lbl_usd)

        self.fx_label_usd = QLabel(self.ticker_bar)
        self.fx_label_usd.setObjectName(u"fx_label_usd")

        self.ticker_layout.addWidget(self.fx_label_usd)

        self.sep_usd = QLabel(self.ticker_bar)
        self.sep_usd.setObjectName(u"sep_usd")

        self.ticker_layout.addWidget(self.sep_usd)

        self.lbl_jpy = QLabel(self.ticker_bar)
        self.lbl_jpy.setObjectName(u"lbl_jpy")

        self.ticker_layout.addWidget(self.lbl_jpy)

        self.fx_label_jpy = QLabel(self.ticker_bar)
        self.fx_label_jpy.setObjectName(u"fx_label_jpy")

        self.ticker_layout.addWidget(self.fx_label_jpy)

        self.sep_jpy = QLabel(self.ticker_bar)
        self.sep_jpy.setObjectName(u"sep_jpy")

        self.ticker_layout.addWidget(self.sep_jpy)

        self.lbl_eur = QLabel(self.ticker_bar)
        self.lbl_eur.setObjectName(u"lbl_eur")

        self.ticker_layout.addWidget(self.lbl_eur)

        self.fx_label_eur = QLabel(self.ticker_bar)
        self.fx_label_eur.setObjectName(u"fx_label_eur")

        self.ticker_layout.addWidget(self.fx_label_eur)

        self.sep_eur = QLabel(self.ticker_bar)
        self.sep_eur.setObjectName(u"sep_eur")

        self.ticker_layout.addWidget(self.sep_eur)

        self.lbl_cny = QLabel(self.ticker_bar)
        self.lbl_cny.setObjectName(u"lbl_cny")

        self.ticker_layout.addWidget(self.lbl_cny)

        self.fx_label_cny = QLabel(self.ticker_bar)
        self.fx_label_cny.setObjectName(u"fx_label_cny")

        self.ticker_layout.addWidget(self.fx_label_cny)

        self.ticker_spacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.ticker_layout.addItem(self.ticker_spacer)

        self.update_time_label = QLabel(self.ticker_bar)
        self.update_time_label.setObjectName(u"update_time_label")

        self.ticker_layout.addWidget(self.update_time_label)


        self.main_layout.addWidget(self.ticker_bar)

        self.tab_widget = QTabWidget(self.main_widget)
        self.tab_widget.setObjectName(u"tab_widget")
        self.tab_widget.setDocumentMode(True)
        self.tab_korea = QWidget()
        self.tab_korea.setObjectName(u"tab_korea")
        self.layout_korea = QVBoxLayout(self.tab_korea)
        self.layout_korea.setSpacing(16)
        self.layout_korea.setObjectName(u"layout_korea")
        self.layout_korea.setContentsMargins(24, 24, 24, 16)
        self.search_row_korea = QHBoxLayout()
        self.search_row_korea.setSpacing(10)
        self.search_row_korea.setObjectName(u"search_row_korea")
        self.search_input_korea = QLineEdit(self.tab_korea)
        self.search_input_korea.setObjectName(u"search_input_korea")
        self.search_input_korea.setMinimumHeight(38)

        self.search_row_korea.addWidget(self.search_input_korea)

        self.search_btn_korea = QPushButton(self.tab_korea)
        self.search_btn_korea.setObjectName(u"search_btn_korea")
        self.search_btn_korea.setMinimumHeight(38)
        self.search_btn_korea.setMaximumHeight(38)
        self.search_btn_korea.setMinimumWidth(80)
        self.search_btn_korea.setMaximumWidth(80)
        self.search_btn_korea.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.search_row_korea.addWidget(self.search_btn_korea)


        self.layout_korea.addLayout(self.search_row_korea)

        self.hint_label_korea = QLabel(self.tab_korea)
        self.hint_label_korea.setObjectName(u"hint_label_korea")

        self.layout_korea.addWidget(self.hint_label_korea)

        self.result_card_korea = QFrame(self.tab_korea)
        self.result_card_korea.setObjectName(u"result_card_korea")
        self.result_card_korea.setFrameShape(QFrame.Shape.NoFrame)
        self.result_layout_korea = QVBoxLayout(self.result_card_korea)
        self.result_layout_korea.setSpacing(6)
        self.result_layout_korea.setObjectName(u"result_layout_korea")
        self.result_layout_korea.setContentsMargins(20, 16, 20, 16)
        self.placeholder_korea = QLabel(self.result_card_korea)
        self.placeholder_korea.setObjectName(u"placeholder_korea")
        self.placeholder_korea.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.result_layout_korea.addWidget(self.placeholder_korea)


        self.layout_korea.addWidget(self.result_card_korea)

        self.spacer_korea = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.layout_korea.addItem(self.spacer_korea)

        self.tab_widget.addTab(self.tab_korea, "")
        self.tab_japan = QWidget()
        self.tab_japan.setObjectName(u"tab_japan")
        self.layout_japan = QVBoxLayout(self.tab_japan)
        self.layout_japan.setSpacing(16)
        self.layout_japan.setObjectName(u"layout_japan")
        self.layout_japan.setContentsMargins(24, 24, 24, 16)
        self.search_row_japan = QHBoxLayout()
        self.search_row_japan.setSpacing(10)
        self.search_row_japan.setObjectName(u"search_row_japan")
        self.search_input_japan = QLineEdit(self.tab_japan)
        self.search_input_japan.setObjectName(u"search_input_japan")
        self.search_input_japan.setMinimumHeight(38)

        self.search_row_japan.addWidget(self.search_input_japan)

        self.search_btn_japan = QPushButton(self.tab_japan)
        self.search_btn_japan.setObjectName(u"search_btn_japan")
        self.search_btn_japan.setMinimumHeight(38)
        self.search_btn_japan.setMaximumHeight(38)
        self.search_btn_japan.setMinimumWidth(80)
        self.search_btn_japan.setMaximumWidth(80)
        self.search_btn_japan.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.search_row_japan.addWidget(self.search_btn_japan)


        self.layout_japan.addLayout(self.search_row_japan)

        self.hint_label_japan = QLabel(self.tab_japan)
        self.hint_label_japan.setObjectName(u"hint_label_japan")

        self.layout_japan.addWidget(self.hint_label_japan)

        self.result_card_japan = QFrame(self.tab_japan)
        self.result_card_japan.setObjectName(u"result_card_japan")
        self.result_card_japan.setFrameShape(QFrame.Shape.NoFrame)
        self.result_layout_japan = QVBoxLayout(self.result_card_japan)
        self.result_layout_japan.setSpacing(6)
        self.result_layout_japan.setObjectName(u"result_layout_japan")
        self.result_layout_japan.setContentsMargins(20, 16, 20, 16)
        self.placeholder_japan = QLabel(self.result_card_japan)
        self.placeholder_japan.setObjectName(u"placeholder_japan")
        self.placeholder_japan.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.result_layout_japan.addWidget(self.placeholder_japan)


        self.layout_japan.addWidget(self.result_card_japan)

        self.spacer_japan = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.layout_japan.addItem(self.spacer_japan)

        self.tab_widget.addTab(self.tab_japan, "")
        self.tab_us = QWidget()
        self.tab_us.setObjectName(u"tab_us")
        self.layout_us = QVBoxLayout(self.tab_us)
        self.layout_us.setSpacing(16)
        self.layout_us.setObjectName(u"layout_us")
        self.layout_us.setContentsMargins(24, 24, 24, 16)
        self.search_row_us = QHBoxLayout()
        self.search_row_us.setSpacing(10)
        self.search_row_us.setObjectName(u"search_row_us")
        self.search_input_us = QLineEdit(self.tab_us)
        self.search_input_us.setObjectName(u"search_input_us")
        self.search_input_us.setMinimumHeight(38)

        self.search_row_us.addWidget(self.search_input_us)

        self.search_btn_us = QPushButton(self.tab_us)
        self.search_btn_us.setObjectName(u"search_btn_us")
        self.search_btn_us.setMinimumHeight(38)
        self.search_btn_us.setMaximumHeight(38)
        self.search_btn_us.setMinimumWidth(80)
        self.search_btn_us.setMaximumWidth(80)
        self.search_btn_us.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.search_row_us.addWidget(self.search_btn_us)


        self.layout_us.addLayout(self.search_row_us)

        self.hint_label_us = QLabel(self.tab_us)
        self.hint_label_us.setObjectName(u"hint_label_us")

        self.layout_us.addWidget(self.hint_label_us)

        self.result_card_us = QFrame(self.tab_us)
        self.result_card_us.setObjectName(u"result_card_us")
        self.result_card_us.setFrameShape(QFrame.Shape.NoFrame)
        self.result_layout_us = QVBoxLayout(self.result_card_us)
        self.result_layout_us.setSpacing(6)
        self.result_layout_us.setObjectName(u"result_layout_us")
        self.result_layout_us.setContentsMargins(20, 16, 20, 16)
        self.placeholder_us = QLabel(self.result_card_us)
        self.placeholder_us.setObjectName(u"placeholder_us")
        self.placeholder_us.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.result_layout_us.addWidget(self.placeholder_us)


        self.layout_us.addWidget(self.result_card_us)

        self.spacer_us = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.layout_us.addItem(self.spacer_us)

        self.tab_widget.addTab(self.tab_us, "")
        self.tab_europe = QWidget()
        self.tab_europe.setObjectName(u"tab_europe")
        self.layout_europe = QVBoxLayout(self.tab_europe)
        self.layout_europe.setSpacing(16)
        self.layout_europe.setObjectName(u"layout_europe")
        self.layout_europe.setContentsMargins(24, 24, 24, 16)
        self.search_row_europe = QHBoxLayout()
        self.search_row_europe.setSpacing(10)
        self.search_row_europe.setObjectName(u"search_row_europe")
        self.search_input_europe = QLineEdit(self.tab_europe)
        self.search_input_europe.setObjectName(u"search_input_europe")
        self.search_input_europe.setMinimumHeight(38)

        self.search_row_europe.addWidget(self.search_input_europe)

        self.search_btn_europe = QPushButton(self.tab_europe)
        self.search_btn_europe.setObjectName(u"search_btn_europe")
        self.search_btn_europe.setMinimumHeight(38)
        self.search_btn_europe.setMaximumHeight(38)
        self.search_btn_europe.setMinimumWidth(80)
        self.search_btn_europe.setMaximumWidth(80)
        self.search_btn_europe.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.search_row_europe.addWidget(self.search_btn_europe)


        self.layout_europe.addLayout(self.search_row_europe)

        self.hint_label_europe = QLabel(self.tab_europe)
        self.hint_label_europe.setObjectName(u"hint_label_europe")

        self.layout_europe.addWidget(self.hint_label_europe)

        self.result_card_europe = QFrame(self.tab_europe)
        self.result_card_europe.setObjectName(u"result_card_europe")
        self.result_card_europe.setFrameShape(QFrame.Shape.NoFrame)
        self.result_layout_europe = QVBoxLayout(self.result_card_europe)
        self.result_layout_europe.setSpacing(6)
        self.result_layout_europe.setObjectName(u"result_layout_europe")
        self.result_layout_europe.setContentsMargins(20, 16, 20, 16)
        self.placeholder_europe = QLabel(self.result_card_europe)
        self.placeholder_europe.setObjectName(u"placeholder_europe")
        self.placeholder_europe.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.result_layout_europe.addWidget(self.placeholder_europe)


        self.layout_europe.addWidget(self.result_card_europe)

        self.spacer_europe = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.layout_europe.addItem(self.spacer_europe)

        self.tab_widget.addTab(self.tab_europe, "")

        self.main_layout.addWidget(self.tab_widget)

        MainWindow.setCentralWidget(self.main_widget)

        self.retranslateUi(MainWindow)

        self.tab_widget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Gold & Stock Monitor", None))
        self.gold_label.setText(QCoreApplication.translate("MainWindow", u"\uc21c\uae08  \ub85c\ub529 \uc911...", None))
        self.sep_gold.setObjectName(QCoreApplication.translate("MainWindow", u"ticker_label", None))
        self.sep_gold.setStyleSheet(QCoreApplication.translate("MainWindow", u"color: #2a3040;", None))
        self.sep_gold.setText(QCoreApplication.translate("MainWindow", u"  \u2502  ", None))
        self.lbl_usd.setObjectName(QCoreApplication.translate("MainWindow", u"ticker_label", None))
        self.lbl_usd.setText(QCoreApplication.translate("MainWindow", u"\ub2ec\ub7ec  ", None))
        self.fx_label_usd.setObjectName(QCoreApplication.translate("MainWindow", u"ticker_label", None))
        self.fx_label_usd.setText(QCoreApplication.translate("MainWindow", u"--", None))
        self.sep_usd.setObjectName(QCoreApplication.translate("MainWindow", u"ticker_label", None))
        self.sep_usd.setStyleSheet(QCoreApplication.translate("MainWindow", u"color: #2a3040;", None))
        self.sep_usd.setText(QCoreApplication.translate("MainWindow", u"  \u2502  ", None))
        self.lbl_jpy.setObjectName(QCoreApplication.translate("MainWindow", u"ticker_label", None))
        self.lbl_jpy.setText(QCoreApplication.translate("MainWindow", u"\uc5d4  ", None))
        self.fx_label_jpy.setObjectName(QCoreApplication.translate("MainWindow", u"ticker_label", None))
        self.fx_label_jpy.setText(QCoreApplication.translate("MainWindow", u"--", None))
        self.sep_jpy.setObjectName(QCoreApplication.translate("MainWindow", u"ticker_label", None))
        self.sep_jpy.setStyleSheet(QCoreApplication.translate("MainWindow", u"color: #2a3040;", None))
        self.sep_jpy.setText(QCoreApplication.translate("MainWindow", u"  \u2502  ", None))
        self.lbl_eur.setObjectName(QCoreApplication.translate("MainWindow", u"ticker_label", None))
        self.lbl_eur.setText(QCoreApplication.translate("MainWindow", u"\uc720\ub85c  ", None))
        self.fx_label_eur.setObjectName(QCoreApplication.translate("MainWindow", u"ticker_label", None))
        self.fx_label_eur.setText(QCoreApplication.translate("MainWindow", u"--", None))
        self.sep_eur.setObjectName(QCoreApplication.translate("MainWindow", u"ticker_label", None))
        self.sep_eur.setStyleSheet(QCoreApplication.translate("MainWindow", u"color: #2a3040;", None))
        self.sep_eur.setText(QCoreApplication.translate("MainWindow", u"  \u2502  ", None))
        self.lbl_cny.setObjectName(QCoreApplication.translate("MainWindow", u"ticker_label", None))
        self.lbl_cny.setText(QCoreApplication.translate("MainWindow", u"\uc704\uc548  ", None))
        self.fx_label_cny.setObjectName(QCoreApplication.translate("MainWindow", u"ticker_label", None))
        self.fx_label_cny.setText(QCoreApplication.translate("MainWindow", u"--", None))
        self.update_time_label.setObjectName(QCoreApplication.translate("MainWindow", u"status_label", None))
        self.update_time_label.setText("")
        self.tab_korea.setStyleSheet(QCoreApplication.translate("MainWindow", u"background-color: #0f1117;", None))
        self.search_input_korea.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\uc885\ubaa9 \ucf54\ub4dc \ub610\ub294 \ud2f0\ucee4 \uc785\ub825 \ud6c4 \uac80\uc0c9...", None))
        self.search_btn_korea.setText(QCoreApplication.translate("MainWindow", u"\uac80\uc0c9", None))
        self.hint_label_korea.setText(QCoreApplication.translate("MainWindow", u"\uc608) 005930 (\uc0bc\uc131\uc804\uc790), 035720 (\uce74\uce74\uc624)", None))
        self.placeholder_korea.setObjectName(QCoreApplication.translate("MainWindow", u"status_label", None))
        self.placeholder_korea.setText(QCoreApplication.translate("MainWindow", u"\uc885\ubaa9 \ucf54\ub4dc\ub97c \uc785\ub825\ud558\uace0 \uac80\uc0c9\ud558\uc138\uc694.", None))
        self.tab_widget.setTabText(self.tab_widget.indexOf(self.tab_korea), QCoreApplication.translate("MainWindow", u"\ud55c\uad6d", None))
        self.tab_japan.setStyleSheet(QCoreApplication.translate("MainWindow", u"background-color: #0f1117;", None))
        self.search_input_japan.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\uc885\ubaa9 \ucf54\ub4dc \ub610\ub294 \ud2f0\ucee4 \uc785\ub825 \ud6c4 \uac80\uc0c9...", None))
        self.search_btn_japan.setText(QCoreApplication.translate("MainWindow", u"\uac80\uc0c9", None))
        self.hint_label_japan.setText(QCoreApplication.translate("MainWindow", u"\uc608) 7203 (Toyota), 6758 (Sony)", None))
        self.placeholder_japan.setObjectName(QCoreApplication.translate("MainWindow", u"status_label", None))
        self.placeholder_japan.setText(QCoreApplication.translate("MainWindow", u"\uc885\ubaa9 \ucf54\ub4dc\ub97c \uc785\ub825\ud558\uace0 \uac80\uc0c9\ud558\uc138\uc694.", None))
        self.tab_widget.setTabText(self.tab_widget.indexOf(self.tab_japan), QCoreApplication.translate("MainWindow", u"\uc77c\ubcf8", None))
        self.tab_us.setStyleSheet(QCoreApplication.translate("MainWindow", u"background-color: #0f1117;", None))
        self.search_input_us.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\uc885\ubaa9 \ucf54\ub4dc \ub610\ub294 \ud2f0\ucee4 \uc785\ub825 \ud6c4 \uac80\uc0c9...", None))
        self.search_btn_us.setText(QCoreApplication.translate("MainWindow", u"\uac80\uc0c9", None))
        self.hint_label_us.setText(QCoreApplication.translate("MainWindow", u"\uc608) AAPL (Apple), TSLA (Tesla), MSFT (Microsoft)", None))
        self.placeholder_us.setObjectName(QCoreApplication.translate("MainWindow", u"status_label", None))
        self.placeholder_us.setText(QCoreApplication.translate("MainWindow", u"\uc885\ubaa9 \ucf54\ub4dc\ub97c \uc785\ub825\ud558\uace0 \uac80\uc0c9\ud558\uc138\uc694.", None))
        self.tab_widget.setTabText(self.tab_widget.indexOf(self.tab_us), QCoreApplication.translate("MainWindow", u"\ubbf8\uad6d", None))
        self.tab_europe.setStyleSheet(QCoreApplication.translate("MainWindow", u"background-color: #0f1117;", None))
        self.search_input_europe.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\uc885\ubaa9 \ucf54\ub4dc \ub610\ub294 \ud2f0\ucee4 \uc785\ub825 \ud6c4 \uac80\uc0c9...", None))
        self.search_btn_europe.setText(QCoreApplication.translate("MainWindow", u"\uac80\uc0c9", None))
        self.hint_label_europe.setText(QCoreApplication.translate("MainWindow", u"\uc608) BMW.DE (BMW), SAP.DE (SAP), MC.PA (LVMH)", None))
        self.placeholder_europe.setObjectName(QCoreApplication.translate("MainWindow", u"status_label", None))
        self.placeholder_europe.setText(QCoreApplication.translate("MainWindow", u"\uc885\ubaa9 \ucf54\ub4dc\ub97c \uc785\ub825\ud558\uace0 \uac80\uc0c9\ud558\uc138\uc694.", None))
        self.tab_widget.setTabText(self.tab_widget.indexOf(self.tab_europe), QCoreApplication.translate("MainWindow", u"\uc720\ub7fd", None))
    # retranslateUi

