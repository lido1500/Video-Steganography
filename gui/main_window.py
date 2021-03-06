# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'draft.ui'
#
# Created by: PyQt5 UI code generator 5.15.3
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.
import os
from subprocess import call, STDOUT

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog

import execute
from db.get_postgres_con import insert, get_values_video_details
from aes.aes_enc import AESCipher
from gui.datatable_window import TableView


class Ui_MainWindow(QtWidgets.QMainWindow):

    def __init__(self, username):
        super(Ui_MainWindow, self).__init__()

        self.username = username
        self.setObjectName("MainWindow")
        self.resize(403, 511)
        self.setMinimumSize(QtCore.QSize(403, 511))
        self.setMaximumSize(QtCore.QSize(403, 511))

        self.centralwidget = QtWidgets.QWidget(self)
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
        self.enc_btn_upload.clicked.connect(self.enc_getValues)

        self.btn_enc = QtWidgets.QPushButton(self.encrypt)
        self.btn_enc.setGeometry(QtCore.QRect(240, 390, 113, 32))
        self.btn_enc.setObjectName("btn_enc")
        self.btn_enc.clicked.connect(self.enc_btn_handler)

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

        # Adding Tab to Tab Widget
        self.tabWidget.addTab(self.encrypt, "")

        # Decrypt Tab Setting Up
        self.decrypt = QtWidgets.QWidget()
        self.decrypt.setObjectName("decrypt")
        self.dec_upload = QtWidgets.QPushButton(self.decrypt)
        self.dec_upload.setGeometry(QtCore.QRect(20, 110, 101, 31))
        self.dec_upload.setText("Upload")
        self.dec_upload.setObjectName("dec_upload")

        # Controller Calls function when clicked
        self.dec_upload.clicked.connect(self.dec_getValues)

        self.dec_lbl_sec_key = QtWidgets.QLabel(self.decrypt)
        self.dec_lbl_sec_key.setGeometry(QtCore.QRect(20, 20, 81, 16))
        self.dec_lbl_sec_key.setObjectName("dec_lbl_sec_key")

        self.btn_dec = QtWidgets.QPushButton(self.decrypt)
        self.btn_dec.setGeometry(QtCore.QRect(240, 160, 113, 32))
        self.btn_dec.setObjectName("btn_dec")

        # Controller Calls function when clicked
        self.btn_dec.clicked.connect(self.dec_btn_handler)

        self.dec_lbl_video = QtWidgets.QLabel(self.decrypt)
        self.dec_lbl_video.setGeometry(QtCore.QRect(20, 90, 91, 16))
        self.dec_lbl_video.setObjectName("dec_lbl_video")
        self.dec_line_sec_key = QtWidgets.QLineEdit(self.decrypt)
        self.dec_line_sec_key.setGeometry(QtCore.QRect(20, 50, 311, 21))
        self.dec_line_sec_key.setObjectName("dec_line_sec_key")

        # Adding Tab to Tab Widget
        self.tabWidget.addTab(self.decrypt, "")

        # Others Tab Setting Up
        self.extra = QtWidgets.QWidget()
        self.extra.setEnabled(True)
        self.extra.setObjectName("extra")
        self.ex_btn_open = QtWidgets.QPushButton(self.extra)
        self.ex_btn_open.setGeometry(QtCore.QRect(120, 60, 131, 31))
        self.ex_btn_open.setObjectName("ex_btn_open")
        self.ex_btn_open.clicked.connect(self.ex_btn_open_handler)

        self.ex_lbl_data_tbl = QtWidgets.QLabel(self.extra)
        self.ex_lbl_data_tbl.setGeometry(QtCore.QRect(150, 30, 71, 16))
        self.ex_lbl_data_tbl.setObjectName("ex_lbl_data_tbl")
        self.ex_btn_start = QtWidgets.QPushButton(self.extra)
        self.ex_btn_start.setGeometry(QtCore.QRect(130, 200, 111, 31))
        self.ex_btn_start.setObjectName("ex_btn_start")
        self.ex_btn_start.clicked.connect(self.ex_btn_start_handler)

        self.ex_lbl_play_vid = QtWidgets.QLabel(self.extra)
        self.ex_lbl_play_vid.setGeometry(QtCore.QRect(120, 170, 131, 16))
        self.ex_lbl_play_vid.setObjectName("ex_lbl_play_vid")

        self.tabWidget.addTab(self.extra, "")

        self.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(self)
        self.statusbar.setObjectName("statusbar")
        self.setStatusBar(self.statusbar)

        # Uncomment to force 2nd tab to appear first
        # self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(self)

        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Ui_MainWindow", "Steganator"))
        self.enc_lbl_sec_msg.setText(_translate("Ui_MainWindow", "Secret Message"))
        self.enc_lbl_sec_key.setText(_translate("Ui_MainWindow", "Secret Key"))
        self.enc_lbl_video.setText(_translate("Ui_MainWindow", "Video"))
        self.enc_btn_upload.setText(_translate("Ui_MainWindow", "Upload"))
        self.btn_enc.setText(_translate("Ui_MainWindow", "Encrypt"))
        self.enc_lbl_vid_id.setText(_translate("Ui_MainWindow", "Video ID"))
        self.enc_lbl_vid_tag.setText(_translate("Ui_MainWindow", "Video Tag"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.encrypt), _translate("Ui_MainWindow", "Encrypt Video"))
        self.dec_lbl_sec_key.setText(_translate("Ui_MainWindow", "Secret Key"))
        self.btn_dec.setText(_translate("Ui_MainWindow", "Decrypt"))
        self.dec_lbl_video.setText(_translate("Ui_MainWindow", "Video"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.decrypt), _translate("Ui_MainWindow", "Decrypt Video"))
        self.ex_btn_open.setText(_translate("Ui_MainWindow", "Open"))
        self.ex_lbl_data_tbl.setText(_translate("Ui_MainWindow", "Data Table"))
        self.ex_btn_start.setText(_translate("Ui_MainWindow", "Start"))
        self.ex_lbl_play_vid.setText(_translate("Ui_MainWindow", "Play Encrypted Video"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.extra), _translate("Ui_MainWindow", "Extra"))

    # Method to open File Browser and get file path
    def open_dialog_box(self):
        filename = QFileDialog.getOpenFileName()
        f_path = filename[0]
        return f_path

    # Get Values from Enc Tab
    def enc_getValues(self):
        self.vid_id = self.enc_line_vid_id.text()
        self.vid_tag = self.enc_line_vid_tag.text()
        self.sec_msg = self.enc_line_sec_msg.text()
        self.sec_key = self.enc_line_sec_key.text()
        self.path = self.open_dialog_box()
        pass

    def enc_btn_handler(self):
        sec_msg_h = self.sec_msg
        sec_key_h = self.sec_key
        vid_id_h = self.vid_id
        vid_tag_h = self.vid_tag
        aes = AESCipher(key=sec_key_h)
        final_sec_msg_h = aes.encrypt(plain_text=sec_msg_h)
        path_h = self.path

        execute.main(input_string=final_sec_msg_h, f_name=path_h)

        insert(username=self.username, vid_id=vid_id_h, vid_tag=vid_tag_h, sec_key=sec_key_h, sec_msg=sec_msg_h)

    # Get Values from Dec Tab
    def dec_getValues(self):
        self.dec_sec_key = self.dec_line_sec_key.text()
        self.dec_path = self.open_dialog_box()
        pass

    def dec_btn_handler(self):
        dec_sec_key_h = self.dec_sec_key
        dec_path_h = self.dec_path

        dec_sec_msg_list = execute.decode_string(video=dec_path_h)

        dec_str = ""
        for i in dec_sec_msg_list:
            dec_str = dec_str + i

        aes = AESCipher(key=dec_sec_key_h)
        final_dec_sec_msg_h = aes.decrypt(encrypted_text=dec_str)

        self.w1 = QtWidgets.QMessageBox()
        self.w1.setIcon(QtWidgets.QMessageBox.Information)
        pop_up_msg = 'Secret: ' + final_dec_sec_msg_h
        self.w1.setText(pop_up_msg)
        self.w1.show()

    def ex_btn_open_handler(self):
        vid_details_list = get_values_video_details(self.username)

        final_vid_details_list = []
        for item in vid_details_list:
            item_list = list(item)
            item_list.pop(0)
            item_list.pop(4)
            final_vid_details_list.append(tuple(item_list))

        vid_details_dict_key_list = ['vid_id', 'vid_tag', 'sec_key', 'sec_msg']

        final_vid_details_dict = []

        for val in final_vid_details_list:
            vid_details_dict = dict(zip(vid_details_dict_key_list, val))
            final_vid_details_dict.append(vid_details_dict)
        table_view = TableView(final_vid_details_dict)
        table_view.show()
        # Stops from window shutting down
        self.table_view = table_view

    def ex_btn_start_handler(self):
        self.vid_path = self.open_dialog_box()
        call(["ffplay", self.vid_path], stdout=open(os.devnull, "w"),
             stderr=STDOUT)


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
