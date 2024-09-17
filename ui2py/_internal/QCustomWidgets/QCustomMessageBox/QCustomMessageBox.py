from PyQt6.QtWidgets import QApplication, QLabel, QDialog, QDialogButtonBox
import sys
from PyQt6.QtGui import QIcon,QPixmap
from PyQt6.QtCore import Qt,QPoint
from PyQt6.uic import loadUi
import os
import convertor_resource
import pathlib
#from QCustomWidgets.utils import addFonts

package_path = pathlib.Path(__file__).parent.parent
ui_path = package_path.joinpath('assets/ui/dialog.ui')
css_path = package_path.joinpath('assets/css/dialog.css')

class QCustomMessageBox(QDialog):
    def __init__(self):
        super().__init__()
        #addFonts()
        self.setWindowFlag(Qt.WindowType.FramelessWindowHint)
        self.ui = loadUi(ui_path, self)
        self.ui.setStyleSheet(open(css_path).read())
        ##################################################################
        self.titleLabel = self.ui.findChild(QLabel,"dialog_title")
        self.messageLabel = self.ui.findChild(QLabel,"message_label")
        self.iconLabel = self.ui.findChild(QLabel,"message_icon")
        ##################################################################
        self.icon_size = 80
        self.tfMode = Qt.TransformationMode.SmoothTransformation
        self.aspMode = Qt.AspectRatioMode.KeepAspectRatio
        ##################################################################
        Qbtn = QDialogButtonBox.StandardButton.Ok
        self.ui.buttonBox.setStandardButtons(Qbtn)
        self.ui.buttonBox.button(QDialogButtonBox.StandardButton.Ok).setText("Tamam")
        self.btn =self.ui.buttonBox.button(QDialogButtonBox.StandardButton.Ok)
        ##################################################################


    def setTitle(self, title):
        self.titleLabel.setText(title)

    def setIcon(self, icon):
        self.iconLabel.setPixmap(QPixmap(icon).scaled(self.icon_size, self.icon_size,
                                                  aspectRatioMode=self.aspMode,
                                                  transformMode=self.tfMode))
    def setText(self, text):
        self.messageLabel.setText(text)


    def setStyle(self, mode="info"):
        color='black'
        b_color='white'
        match mode:
            case 'info':
                color="black"
                btn_color='#A1C4FF'
                b_color = '#2FB8EE'
            case 'success':
                color = "black"
                btn_color='white'
                b_color = '#1CA45D'
            case 'warning':
                color = "black"
                btn_color='black'
                b_color='#E5C91B'

            case 'error':
                color = "white"
                btn_color='white'
                b_color='#F14652'

            case 'question':
                color = "white"
                btn_color='gray'
        try:
            Qbtn = QDialogButtonBox.StandardButton.Ok
            self.ui.buttonBox.setStandardButtons(Qbtn)
            self.ui.buttonBox.button(QDialogButtonBox.StandardButton.Ok).setText("Tamam")
            self.btn = self.ui.buttonBox.button(QDialogButtonBox.StandardButton.Ok)
        except Exception as e:
            print(e)

        self.ui.content_wrapper.setStyleSheet(f"QWidget{{background-color:{btn_color};}}")
        self.btn.setStyleSheet(f"background-color:{b_color};color:{color}")
        self.messageLabel.setStyleSheet(f"color:{color}")
    def info(self, message):
        self.setStyle(mode='info')
        self.setTitle("Bilgilendirme")
        self.setText(message)
        self.setIcon(':/myicons/alerts/info-icon.png')

    def error(self, message):
        self.setStyle(mode='error')
        self.ui.content_wrapper.setStyleSheet("QWidget{background-color:#FF9A9A;}")
        self.setTitle("Hata")
        self.setText(message)
        self.setIcon(':/myicons/alerts/cancel-icon.png')

    def success(self, message):
        self.setStyle(mode='success')
        self.ui.content_wrapper.setStyleSheet("QWidget{background-color:#20C997;}")
        self.setTitle("Bilgilendirme")
        self.setText(message)
        self.setIcon(':/myicons/alerts/check-mark-icon.png')

    def warning(self, message):
        self.setStyle(mode='warning')
        self.ui.content_wrapper.setStyleSheet("QWidget{background-color:#FEE69A;}")
        self.setTitle("Uyarı")
        self.setText(message)
        self.setIcon(':/myicons/alerts/icons8-danger-94.png')


    def question(self,message):
        self.setStyle(mode='question')
        Qbtn = QDialogButtonBox.StandardButton.Yes|QDialogButtonBox.StandardButton.No
        self.ui.buttonBox.setStandardButtons(Qbtn)
        self.ui.buttonBox.button(QDialogButtonBox.StandardButton.Yes).setText("Evet")
        self.ui.buttonBox.button(QDialogButtonBox.StandardButton.Yes).setStyleSheet("background-color: #20C997;")
        self.ui.buttonBox.button(QDialogButtonBox.StandardButton.No).setText("Hayır")
        self.ui.buttonBox.button(QDialogButtonBox.StandardButton.No).setStyleSheet("background-color: #FF9A9A;")
        self.setTitle("Soru")
        self.setText(message)
        self.setIcon(":/myicons/alerts/icons8-question.png")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    for i,text in zip(('question','info', 'error', 'warning','success'),('ssssssssssssssssssssssssssssssssssssssssssssssssssssssssss','asfasf','s','s','s')):
        w = QCustomMessageBox()
        w.__getattribute__(i)(text)
        w.exec()

    sys.exit(app.exec())