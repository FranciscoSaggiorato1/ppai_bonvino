# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'interfazDiseño.ui'
##
## Created by: Qt User Interface Compiler version 6.7.1
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QHeaderView, QLabel,
    QLayout, QMainWindow, QMenuBar, QPushButton,
    QSizePolicy, QSpacerItem, QStackedWidget, QStatusBar,
    QTabWidget, QTableWidget, QTableWidgetItem, QVBoxLayout,
    QWidget)
import recursos_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        font = QFont()
        font.setKerning(False)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet(u"background-color: rgb(86, 7, 12);")
        MainWindow.setTabShape(QTabWidget.Rounded)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.pushButton = QPushButton(self.page)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(310, 470, 161, 61))
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        self.pushButton.setStyleSheet(u"QPushButton {\n"
"border: 2px solid black;\n"
"border-radius: 9px;\n"
"color: white;\n"
"}\n"
"QPushButton:hover {\n"
"    background: rgba(99, 7, 7, 0.8)\n"
"}\n"
"QPushButton:pressed {\n"
"    background: rgba(99, 7, 7, 0.8)\n"
"}")
        self.label = QLabel(self.page)
        self.label.setObjectName(u"label")
        self.label.setEnabled(False)
        self.label.setGeometry(QRect(-30, -20, 861, 474))
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMouseTracking(True)
        self.label.setScaledContents(True)
        self.label.setAlignment(Qt.AlignCenter)
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.page_2.setStyleSheet(u"")
        self.verticalLayoutPage2 = QVBoxLayout(self.page_2)
        self.verticalLayoutPage2.setObjectName(u"verticalLayoutPage2")
        self.verticalLayoutPage2.setSizeConstraint(QLayout.SetMinimumSize)
        self.verticalSpacerTop = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayoutPage2.addItem(self.verticalSpacerTop)

        self.label_2 = QLabel(self.page_2)
        self.label_2.setObjectName(u"label_2")
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setStyleSheet(u"\n"
"            color: rgb(86, 7, 12);\n"
"            background-color: rgb(255, 255, 240);\n"
"            font-family: \"montserrat\", Times, serif;\n"
"            font-size: 16px;\n"
"            font-weight: bold;\n"
"            border-radius: 5px;\n"
"            padding: 10px;\n"
"           ")
        self.label_2.setAlignment(Qt.AlignCenter)

        self.verticalLayoutPage2.addWidget(self.label_2)

        self.tableWidget = QTableWidget(self.page_2)
        self.tableWidget.setObjectName(u"tableWidget")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(50)
        sizePolicy1.setVerticalStretch(50)
        sizePolicy1.setHeightForWidth(self.tableWidget.sizePolicy().hasHeightForWidth())
        self.tableWidget.setSizePolicy(sizePolicy1)
        self.tableWidget.setStyleSheet(u"\n"
"            background-color: rgb(69, 5, 9);\n"
"            color: rgb(255, 255, 240);\n"
"            QHeaderView::section {\n"
"              color: rgb(255, 255, 240);\n"
"              background-color: rgb(255, 255, 240);\n"
"            }\n"
"            QTableWidgetItem::setData(Qt::BackgroundRole,Qt::grey)\n"
"           ")
        self.tableWidget.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.tableWidget.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.verticalLayoutPage2.addWidget(self.tableWidget)

        self.verticalSpacerBottom = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayoutPage2.addItem(self.verticalSpacerBottom)

        self.pushButtonVolverBodega = QPushButton(self.page_2)
        self.pushButtonVolverBodega.setObjectName(u"pushButtonVolverBodega")
        self.pushButtonVolverBodega.setStyleSheet(u"QPushButton {\n"
"border: 2px solid black;\n"
"border-radius: 9px;\n"
"color: white;\n"
"}\n"
"QPushButton:hover {\n"
"    background: rgba(99, 7, 7, 0.8)\n"
"}\n"
"QPushButton:pressed {\n"
"    background: rgba(99, 7, 7, 0.8)\n"
"}")

        self.verticalLayoutPage2.addWidget(self.pushButtonVolverBodega)

        self.stackedWidget.addWidget(self.page_2)
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.page_3.setStyleSheet(u"")
        self.verticalLayoutPage3 = QVBoxLayout(self.page_3)
        self.verticalLayoutPage3.setObjectName(u"verticalLayoutPage3")
        self.verticalLayoutPage3.setSizeConstraint(QLayout.SetMinimumSize)
        self.verticalSpacerTop1 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayoutPage3.addItem(self.verticalSpacerTop1)

        self.label_3 = QLabel(self.page_3)
        self.label_3.setObjectName(u"label_3")
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setStyleSheet(u"\n"
"            color: rgb(86, 7, 12);\n"
"            background-color: rgb(255, 255, 240);\n"
"            font-family: \"montserrat\", Times, serif;\n"
"            font-size: 16px;\n"
"            font-weight: bold;\n"
"            border-radius: 5px;\n"
"            padding: 10px;\n"
"           ")
        self.label_3.setAlignment(Qt.AlignCenter)

        self.verticalLayoutPage3.addWidget(self.label_3)

        self.tableVino = QTableWidget(self.page_3)
        self.tableVino.setObjectName(u"tableVino")
        sizePolicy1.setHeightForWidth(self.tableVino.sizePolicy().hasHeightForWidth())
        self.tableVino.setSizePolicy(sizePolicy1)
        self.tableVino.setStyleSheet(u"\n"
"            background-color: rgb(69, 5, 9);\n"
"            color: rgb(255, 255, 240);\n"
"            QHeaderView::section {\n"
"              color: rgb(255, 255, 240);\n"
"              background-color: rgb(255, 255, 240);\n"
"            }\n"
"            QTableWidgetItem::setData(Qt::BackgroundRole,Qt::grey)\n"
"           ")
        self.tableVino.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.tableVino.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.verticalLayoutPage3.addWidget(self.tableVino)

        self.verticalSpacerBottom1 = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayoutPage3.addItem(self.verticalSpacerBottom1)

        self.pushButtonVolver = QPushButton(self.page_3)
        self.pushButtonVolver.setObjectName(u"pushButtonVolver")
        self.pushButtonVolver.setStyleSheet(u"QPushButton {\n"
"border: 2px solid black;\n"
"border-radius: 9px;\n"
"color: white;\n"
"}\n"
"QPushButton:hover {\n"
"    background: rgba(99, 7, 7, 0.8)\n"
"}\n"
"QPushButton:pressed {\n"
"    background: rgba(99, 7, 7, 0.8)\n"
"}")

        self.verticalLayoutPage3.addWidget(self.pushButtonVolver)

        self.stackedWidget.addWidget(self.page_3)

        self.horizontalLayout.addWidget(self.stackedWidget)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Importar actualizacion vinos", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><img src=\":/logo/logo.jpg\"/></p></body></html>", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Seleccione las bodegas que desea actualizar", None))
        self.pushButtonVolverBodega.setText(QCoreApplication.translate("MainWindow", u"Volver al inicio", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Vinos actualizados y/o creados", None))
        self.pushButtonVolver.setText(QCoreApplication.translate("MainWindow", u"Volver al inicio", None))
    # retranslateUi

