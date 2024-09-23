# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'widget.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QLayout,
    QLineEdit, QPlainTextEdit, QPushButton, QSizePolicy,
    QWidget)

class Ui_widget(object):
    def setupUi(self, widget):
        if not widget.objectName():
            widget.setObjectName(u"widget")
        widget.resize(800, 400)
        widget.setStyleSheet(u"background-color: rgb(119, 118, 123);")
        self.gridLayoutWidget = QWidget(widget)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(520, 58, 252, 230))
        self.gridLayout_4 = QGridLayout(self.gridLayoutWidget)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setSizeConstraint(QLayout.SizeConstraint.SetFixedSize)
        self.gridLayout_4.setHorizontalSpacing(5)
        self.gridLayout_4.setVerticalSpacing(0)
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.push_7 = QPushButton(self.gridLayoutWidget)
        self.push_7.setObjectName(u"push_7")
        self.push_7.setMinimumSize(QSize(50, 50))
        self.push_7.setStyleSheet(u"font: 400 12pt \"Arial\";\n"
"color: rgb(255, 255, 255)")

        self.gridLayout_4.addWidget(self.push_7, 0, 0, 1, 1)

        self.push_1 = QPushButton(self.gridLayoutWidget)
        self.push_1.setObjectName(u"push_1")
        self.push_1.setMinimumSize(QSize(50, 50))
        self.push_1.setStyleSheet(u"font: 400 12pt \"Arial\";\n"
"color: rgb(255, 255, 255)")

        self.gridLayout_4.addWidget(self.push_1, 2, 0, 1, 1)

        self.push_5 = QPushButton(self.gridLayoutWidget)
        self.push_5.setObjectName(u"push_5")
        self.push_5.setMinimumSize(QSize(50, 50))
        self.push_5.setStyleSheet(u"font: 400 12pt \"Arial\";\n"
"color: rgb(255, 255, 255)")

        self.gridLayout_4.addWidget(self.push_5, 1, 1, 1, 1)

        self.push_4 = QPushButton(self.gridLayoutWidget)
        self.push_4.setObjectName(u"push_4")
        self.push_4.setMinimumSize(QSize(50, 50))
        self.push_4.setStyleSheet(u"font: 400 12pt \"Arial\";\n"
"color: rgb(255, 255, 255)")

        self.gridLayout_4.addWidget(self.push_4, 1, 0, 1, 1)

        self.push_2 = QPushButton(self.gridLayoutWidget)
        self.push_2.setObjectName(u"push_2")
        self.push_2.setMinimumSize(QSize(50, 50))
        self.push_2.setStyleSheet(u"font: 400 12pt \"Arial\";\n"
"color: rgb(255, 255, 255)")

        self.gridLayout_4.addWidget(self.push_2, 2, 1, 1, 1)

        self.push_6 = QPushButton(self.gridLayoutWidget)
        self.push_6.setObjectName(u"push_6")
        self.push_6.setMinimumSize(QSize(50, 50))
        self.push_6.setStyleSheet(u"font: 400 12pt \"Arial\";\n"
"color: rgb(255, 255, 255)")

        self.gridLayout_4.addWidget(self.push_6, 1, 2, 1, 1)

        self.push_8 = QPushButton(self.gridLayoutWidget)
        self.push_8.setObjectName(u"push_8")
        self.push_8.setMinimumSize(QSize(50, 50))
        self.push_8.setStyleSheet(u"font: 400 12pt \"Arial\";\n"
"color: rgb(255, 255, 255)")

        self.gridLayout_4.addWidget(self.push_8, 0, 1, 1, 1)

        self.push_9 = QPushButton(self.gridLayoutWidget)
        self.push_9.setObjectName(u"push_9")
        self.push_9.setMinimumSize(QSize(50, 50))
        self.push_9.setStyleSheet(u"font: 400 12pt \"Arial\";\n"
"color: rgb(255, 255, 255)")

        self.gridLayout_4.addWidget(self.push_9, 0, 2, 1, 1)

        self.push_3 = QPushButton(self.gridLayoutWidget)
        self.push_3.setObjectName(u"push_3")
        self.push_3.setMinimumSize(QSize(50, 50))
        self.push_3.setStyleSheet(u"font: 400 12pt \"Arial\";\n"
"color: rgb(255, 255, 255)")

        self.gridLayout_4.addWidget(self.push_3, 2, 2, 1, 1)

        self.push_dot = QPushButton(self.gridLayoutWidget)
        self.push_dot.setObjectName(u"push_dot")
        self.push_dot.setMinimumSize(QSize(50, 50))
        self.push_dot.setStyleSheet(u"font: 600 13pt \"Arial\";\n"
"color: rgb(255, 255, 255)")

        self.gridLayout_4.addWidget(self.push_dot, 3, 2, 1, 1)

        self.push_0 = QPushButton(self.gridLayoutWidget)
        self.push_0.setObjectName(u"push_0")
        self.push_0.setMinimumSize(QSize(50, 50))
        self.push_0.setStyleSheet(u"font: 400 12pt \"Arial\";\n"
"color: rgb(255, 255, 255)")

        self.gridLayout_4.addWidget(self.push_0, 3, 1, 1, 1)

        self.push_c = QPushButton(self.gridLayoutWidget)
        self.push_c.setObjectName(u"push_c")
        self.push_c.setMinimumSize(QSize(50, 50))
        self.push_c.setStyleSheet(u"font: 600 12pt \"Arial\";\n"
"color: rgb(255, 255, 255)")

        self.gridLayout_4.addWidget(self.push_c, 3, 0, 1, 1)

        self.formLayoutWidget = QWidget(widget)
        self.formLayoutWidget.setObjectName(u"formLayoutWidget")
        self.formLayoutWidget.setGeometry(QRect(30, 51, 471, 151))
        self.gridLayout_3 = QGridLayout(self.formLayoutWidget)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setHorizontalSpacing(6)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gcv = QLineEdit(self.formLayoutWidget)
        self.gcv.setObjectName(u"gcv")
        font = QFont()
        font.setPointSize(12)
        self.gcv.setFont(font)
        self.gcv.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.gridLayout_3.addWidget(self.gcv, 2, 3, 1, 1)

        self.fixCharg = QLineEdit(self.formLayoutWidget)
        self.fixCharg.setObjectName(u"fixCharg")
        self.fixCharg.setFont(font)
        self.fixCharg.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.gridLayout_3.addWidget(self.fixCharg, 4, 1, 1, 1)

        self.curReading = QLineEdit(self.formLayoutWidget)
        self.curReading.setObjectName(u"curReading")
        self.curReading.setFont(font)
        self.curReading.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.curReading.setMaxLength(8)

        self.gridLayout_3.addWidget(self.curReading, 0, 3, 1, 1)

        self.meterRentLabel = QLabel(self.formLayoutWidget)
        self.meterRentLabel.setObjectName(u"meterRentLabel")
        self.meterRentLabel.setStyleSheet(u"font: 400 12pt \"Arial\";\n"
"color: rgb(255, 255, 255)")

        self.gridLayout_3.addWidget(self.meterRentLabel, 4, 2, 1, 1)

        self.meterRent = QLineEdit(self.formLayoutWidget)
        self.meterRent.setObjectName(u"meterRent")
        self.meterRent.setFont(font)
        self.meterRent.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.gridLayout_3.addWidget(self.meterRent, 4, 3, 1, 1)

        self.currentLabel = QLabel(self.formLayoutWidget)
        self.currentLabel.setObjectName(u"currentLabel")
        self.currentLabel.setStyleSheet(u"font: 400 12pt \"Arial\";\n"
"color: rgb(255, 255, 255)")

        self.gridLayout_3.addWidget(self.currentLabel, 0, 2, 1, 1)

        self.factorLabel = QLabel(self.formLayoutWidget)
        self.factorLabel.setObjectName(u"factorLabel")
        self.factorLabel.setStyleSheet(u"font: 400 12pt \"Arial\";\n"
"color: rgb(255, 255, 255)")

        self.gridLayout_3.addWidget(self.factorLabel, 2, 0, 1, 1)

        self.previousLabel = QLabel(self.formLayoutWidget)
        self.previousLabel.setObjectName(u"previousLabel")
        font1 = QFont()
        font1.setFamilies([u"Arial"])
        font1.setPointSize(12)
        font1.setBold(False)
        font1.setItalic(False)
        self.previousLabel.setFont(font1)
        self.previousLabel.setStyleSheet(u"font: 400 12pt \"Arial\";\n"
"color: rgb(255, 255, 255)")

        self.gridLayout_3.addWidget(self.previousLabel, 0, 0, 1, 1)

        self.gCVLabel = QLabel(self.formLayoutWidget)
        self.gCVLabel.setObjectName(u"gCVLabel")
        self.gCVLabel.setStyleSheet(u"font: 400 12pt \"Arial\";\n"
"color: rgb(255, 255, 255)")

        self.gridLayout_3.addWidget(self.gCVLabel, 2, 2, 1, 1)

        self.factor = QLineEdit(self.formLayoutWidget)
        self.factor.setObjectName(u"factor")
        self.factor.setFont(font)
        self.factor.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.gridLayout_3.addWidget(self.factor, 2, 1, 1, 1)

        self.fixChargesLabel = QLabel(self.formLayoutWidget)
        self.fixChargesLabel.setObjectName(u"fixChargesLabel")
        self.fixChargesLabel.setStyleSheet(u"font: 400 12pt \"Arial\";\n"
"color: rgb(255, 255, 255)")

        self.gridLayout_3.addWidget(self.fixChargesLabel, 4, 0, 1, 1)

        self.preReading = QLineEdit(self.formLayoutWidget)
        self.preReading.setObjectName(u"preReading")
        self.preReading.setFont(font)
        self.preReading.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"")
        self.preReading.setInputMethodHints(Qt.InputMethodHint.ImhNone)
        self.preReading.setMaxLength(8)

        self.gridLayout_3.addWidget(self.preReading, 0, 1, 1, 1)

        self.footer = QLabel(widget)
        self.footer.setObjectName(u"footer")
        self.footer.setGeometry(QRect(270, 12, 267, 26))
        self.footer.setMaximumSize(QSize(267, 16777202))
        font2 = QFont()
        font2.setPointSize(16)
        font2.setBold(True)
        self.footer.setFont(font2)
        self.footer.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.pushCalculate = QPushButton(widget)
        self.pushCalculate.setObjectName(u"pushCalculate")
        self.pushCalculate.setGeometry(QRect(30, 210, 471, 41))
        self.pushCalculate.setStyleSheet(u"font: 600 12pt \"Arial\";\n"
"color: rgb(255, 255, 255)")
        self.header = QLabel(widget)
        self.header.setObjectName(u"header")
        self.header.setGeometry(QRect(250, 361, 327, 20))
        self.header.setMaximumSize(QSize(16777202, 16777202))
        font3 = QFont()
        font3.setPointSize(12)
        font3.setBold(True)
        self.header.setFont(font3)
        self.totAmount = QPlainTextEdit(widget)
        self.totAmount.setObjectName(u"totAmount")
        self.totAmount.setGeometry(QRect(30, 260, 471, 81))
        self.totAmount.setStyleSheet(u"color: rgb(246, 245, 244);")
        self.pushOnlineBill = QPushButton(widget)
        self.pushOnlineBill.setObjectName(u"pushOnlineBill")
        self.pushOnlineBill.setGeometry(QRect(600, 300, 121, 41))
        self.pushOnlineBill.setStyleSheet(u"font: 400 12pt \"Arial\";\n"
"color: rgb(255, 255, 255)")

        self.retranslateUi(widget)

        QMetaObject.connectSlotsByName(widget)
    # setupUi

    def retranslateUi(self, widget):
        widget.setWindowTitle(QCoreApplication.translate("widget", u"Form", None))
        self.push_7.setText(QCoreApplication.translate("widget", u"7", None))
#if QT_CONFIG(shortcut)
        self.push_7.setShortcut(QCoreApplication.translate("widget", u"7", None))
#endif // QT_CONFIG(shortcut)
        self.push_1.setText(QCoreApplication.translate("widget", u"1", None))
#if QT_CONFIG(shortcut)
        self.push_1.setShortcut(QCoreApplication.translate("widget", u"1", None))
#endif // QT_CONFIG(shortcut)
        self.push_5.setText(QCoreApplication.translate("widget", u"5", None))
#if QT_CONFIG(shortcut)
        self.push_5.setShortcut(QCoreApplication.translate("widget", u"5", None))
#endif // QT_CONFIG(shortcut)
        self.push_4.setText(QCoreApplication.translate("widget", u"4", None))
#if QT_CONFIG(shortcut)
        self.push_4.setShortcut(QCoreApplication.translate("widget", u"4", None))
#endif // QT_CONFIG(shortcut)
        self.push_2.setText(QCoreApplication.translate("widget", u"2", None))
#if QT_CONFIG(shortcut)
        self.push_2.setShortcut(QCoreApplication.translate("widget", u"2", None))
#endif // QT_CONFIG(shortcut)
        self.push_6.setText(QCoreApplication.translate("widget", u"6", None))
#if QT_CONFIG(shortcut)
        self.push_6.setShortcut(QCoreApplication.translate("widget", u"6", None))
#endif // QT_CONFIG(shortcut)
        self.push_8.setText(QCoreApplication.translate("widget", u"8", None))
#if QT_CONFIG(shortcut)
        self.push_8.setShortcut(QCoreApplication.translate("widget", u"8", None))
#endif // QT_CONFIG(shortcut)
        self.push_9.setText(QCoreApplication.translate("widget", u"9", None))
#if QT_CONFIG(shortcut)
        self.push_9.setShortcut(QCoreApplication.translate("widget", u"9", None))
#endif // QT_CONFIG(shortcut)
        self.push_3.setText(QCoreApplication.translate("widget", u"3", None))
#if QT_CONFIG(shortcut)
        self.push_3.setShortcut(QCoreApplication.translate("widget", u"3", None))
#endif // QT_CONFIG(shortcut)
        self.push_dot.setText(QCoreApplication.translate("widget", u".", None))
#if QT_CONFIG(shortcut)
        self.push_dot.setShortcut(QCoreApplication.translate("widget", u".", None))
#endif // QT_CONFIG(shortcut)
        self.push_0.setText(QCoreApplication.translate("widget", u"0", None))
#if QT_CONFIG(shortcut)
        self.push_0.setShortcut(QCoreApplication.translate("widget", u"0", None))
#endif // QT_CONFIG(shortcut)
        self.push_c.setText(QCoreApplication.translate("widget", u"C", None))
#if QT_CONFIG(shortcut)
        self.push_c.setShortcut(QCoreApplication.translate("widget", u"0", None))
#endif // QT_CONFIG(shortcut)
        self.curReading.setPlaceholderText(QCoreApplication.translate("widget", u"00000000", None))
        self.meterRentLabel.setText(QCoreApplication.translate("widget", u"Meter Rent", None))
        self.currentLabel.setText(QCoreApplication.translate("widget", u"Current", None))
        self.factorLabel.setText(QCoreApplication.translate("widget", u"Factor", None))
        self.previousLabel.setText(QCoreApplication.translate("widget", u"Previous", None))
        self.gCVLabel.setText(QCoreApplication.translate("widget", u"GCV", None))
        self.fixChargesLabel.setText(QCoreApplication.translate("widget", u"Fix Charges", None))
        self.preReading.setInputMask("")
        self.preReading.setPlaceholderText(QCoreApplication.translate("widget", u"00000000", None))
        self.footer.setText(QCoreApplication.translate("widget", u"Gas Bill Calculator (SNGPL)", None))
        self.pushCalculate.setText(QCoreApplication.translate("widget", u"Calculate", None))
        self.header.setText(QCoreApplication.translate("widget", u"<html><head/><body><p><span style=\" color:#ffffff;\">Sui Northern Gas Pipelines Limited (SNGPL)</span></p></body></html>", None))
        self.totAmount.setPlaceholderText(QCoreApplication.translate("widget", u"Amount", None))
        self.pushOnlineBill.setText(QCoreApplication.translate("widget", u"Online Bill", None))
    # retranslateUi

