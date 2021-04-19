# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'draft.ui'
#
# Created by: PyQt5 UI code generator 5.15.3
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(403, 511)
        MainWindow.setMinimumSize(QtCore.QSize(403, 511))
        MainWindow.setMaximumSize(QtCore.QSize(403, 511))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setEnabled(True)
        self.tabWidget.setGeometry(QtCore.QRect(10, 10, 381, 471))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.BrightText, brush)
        self.tabWidget.setPalette(palette)
        font = QtGui.QFont()
        font.setItalic(False)
        font.setUnderline(False)
        font.setStrikeOut(False)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.tabWidget.setFont(font)
        self.tabWidget.setFocusPolicy(QtCore.Qt.NoFocus)
        self.tabWidget.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.tabWidget.setAutoFillBackground(False)
        self.tabWidget.setStyleSheet("QTabBar::tab:selected { \n"
"  background: rgb(178, 232, 219); \n"
"}")
        self.tabWidget.setTabPosition(QtWidgets.QTabWidget.North)
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.tabWidget.setElideMode(QtCore.Qt.ElideLeft)
        self.tabWidget.setUsesScrollButtons(False)
        self.tabWidget.setTabBarAutoHide(False)
        self.tabWidget.setObjectName("tabWidget")
        self.encrypt = QtWidgets.QWidget()
        self.encrypt.setFocusPolicy(QtCore.Qt.TabFocus)
        self.encrypt.setObjectName("encrypt")
        self.enc_lbl_sec_msg = QtWidgets.QLabel(self.encrypt)
        self.enc_lbl_sec_msg.setGeometry(QtCore.QRect(20, 170, 111, 16))
        self.enc_lbl_sec_msg.setObjectName("enc_lbl_sec_msg")
        self.enc_lbl_sec_key = QtWidgets.QLabel(self.encrypt)
        self.enc_lbl_sec_key.setGeometry(QtCore.QRect(20, 250, 81, 16))
        self.enc_lbl_sec_key.setObjectName("enc_lbl_sec_key")
        self.enc_lbl_video = QtWidgets.QLabel(self.encrypt)
        self.enc_lbl_video.setGeometry(QtCore.QRect(20, 320, 91, 16))
        self.enc_lbl_video.setObjectName("enc_lbl_video")
        self.enc_btn_upload = QtWidgets.QPushButton(self.encrypt)
        self.enc_btn_upload.setGeometry(QtCore.QRect(20, 340, 101, 31))
        self.enc_btn_upload.setObjectName("enc_btn_upload")
        self.btn_enc = QtWidgets.QPushButton(self.encrypt)
        self.btn_enc.setGeometry(QtCore.QRect(240, 390, 113, 32))
        self.btn_enc.setObjectName("btn_enc")
        self.enc_lbl_vid_id = QtWidgets.QLabel(self.encrypt)
        self.enc_lbl_vid_id.setGeometry(QtCore.QRect(20, 30, 111, 16))
        self.enc_lbl_vid_id.setObjectName("enc_lbl_vid_id")
        self.enc_lbl_vid_tag = QtWidgets.QLabel(self.encrypt)
        self.enc_lbl_vid_tag.setGeometry(QtCore.QRect(20, 100, 111, 16))
        self.enc_lbl_vid_tag.setObjectName("enc_lbl_vid_tag")
        self.enc_line_vid_id = QtWidgets.QLineEdit(self.encrypt)
        self.enc_line_vid_id.setGeometry(QtCore.QRect(20, 60, 311, 21))
        self.enc_line_vid_id.setObjectName("enc_line_vid_id")
        self.enc_line_vid_tag = QtWidgets.QLineEdit(self.encrypt)
        self.enc_line_vid_tag.setGeometry(QtCore.QRect(20, 130, 311, 21))
        self.enc_line_vid_tag.setObjectName("enc_line_vid_tag")
        self.enc_line_sec_msg = QtWidgets.QLineEdit(self.encrypt)
        self.enc_line_sec_msg.setGeometry(QtCore.QRect(20, 210, 311, 21))
        self.enc_line_sec_msg.setObjectName("enc_line_sec_msg")
        self.enc_line_sec_key = QtWidgets.QLineEdit(self.encrypt)
        self.enc_line_sec_key.setGeometry(QtCore.QRect(20, 280, 311, 21))
        self.enc_line_sec_key.setObjectName("enc_line_sec_key")
        self.tabWidget.addTab(self.encrypt, "")
        self.decrypt = QtWidgets.QWidget()
        self.decrypt.setObjectName("decrypt")
        self.dec_upload = QtWidgets.QPushButton(self.decrypt)
        self.dec_upload.setGeometry(QtCore.QRect(20, 110, 101, 31))
        self.dec_upload.setText("Upload")
        self.dec_upload.setObjectName("dec_upload")
        self.dec_lbl_sec_key = QtWidgets.QLabel(self.decrypt)
        self.dec_lbl_sec_key.setGeometry(QtCore.QRect(20, 20, 81, 16))
        self.dec_lbl_sec_key.setObjectName("dec_lbl_sec_key")
        self.btn_dec = QtWidgets.QPushButton(self.decrypt)
        self.btn_dec.setGeometry(QtCore.QRect(240, 160, 113, 32))
        self.btn_dec.setObjectName("btn_dec")
        self.dec_lbl_video = QtWidgets.QLabel(self.decrypt)
        self.dec_lbl_video.setGeometry(QtCore.QRect(20, 90, 91, 16))
        self.dec_lbl_video.setObjectName("dec_lbl_video")
        self.dec_line_sec_key = QtWidgets.QLineEdit(self.decrypt)
        self.dec_line_sec_key.setGeometry(QtCore.QRect(20, 50, 311, 21))
        self.dec_line_sec_key.setObjectName("dec_line_sec_key")
        self.tabWidget.addTab(self.decrypt, "")
        self.extra = QtWidgets.QWidget()
        self.extra.setEnabled(True)
        self.extra.setObjectName("extra")
        self.ex_btn_open = QtWidgets.QPushButton(self.extra)
        self.ex_btn_open.setGeometry(QtCore.QRect(120, 60, 131, 31))
        self.ex_btn_open.setObjectName("ex_btn_open")
        self.ex_lbl_data_tbl = QtWidgets.QLabel(self.extra)
        self.ex_lbl_data_tbl.setGeometry(QtCore.QRect(150, 30, 71, 16))
        self.ex_lbl_data_tbl.setObjectName("ex_lbl_data_tbl")
        self.ex_btn_start = QtWidgets.QPushButton(self.extra)
        self.ex_btn_start.setGeometry(QtCore.QRect(130, 200, 111, 31))
        self.ex_btn_start.setObjectName("ex_btn_start")
        self.ex_lbl_play_vid = QtWidgets.QLabel(self.extra)
        self.ex_lbl_play_vid.setGeometry(QtCore.QRect(120, 170, 131, 16))
        self.ex_lbl_play_vid.setObjectName("ex_lbl_play_vid")
        self.tabWidget.addTab(self.extra, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Steganator"))
        self.enc_lbl_sec_msg.setText(_translate("MainWindow", "Secret Message"))
        self.enc_lbl_sec_key.setText(_translate("MainWindow", "Secret Key"))
        self.enc_lbl_video.setText(_translate("MainWindow", "Video"))
        self.enc_btn_upload.setText(_translate("MainWindow", "Upload"))
        self.btn_enc.setText(_translate("MainWindow", "Encrypt"))
        self.enc_lbl_vid_id.setText(_translate("MainWindow", "Video ID"))
        self.enc_lbl_vid_tag.setText(_translate("MainWindow", "Video Tag"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.encrypt), _translate("MainWindow", "Encrypt Video"))
        self.dec_lbl_sec_key.setText(_translate("MainWindow", "Secret Key"))
        self.btn_dec.setText(_translate("MainWindow", "Decrypt"))
        self.dec_lbl_video.setText(_translate("MainWindow", "Video"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.decrypt), _translate("MainWindow", "Decrypt Video"))
        self.ex_btn_open.setText(_translate("MainWindow", "Open"))
        self.ex_lbl_data_tbl.setText(_translate("MainWindow", "Data Table"))
        self.ex_btn_start.setText(_translate("MainWindow", "Start"))
        self.ex_lbl_play_vid.setText(_translate("MainWindow", "Play Encrypted Video"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.extra), _translate("MainWindow", "Extra"))