from PyQt6.QtCore import QDate, pyqtSignal
from PyQt6.QtWidgets import QWidget, QApplication, QPushButton
from PyQt6.uic import loadUi
import sys
import os
import pathlib
#from QCustomWidgets.utils import addFonts

package_path = pathlib.Path(__file__).parent.parent
ui_path = package_path.joinpath('assets/ui/date_picker.ui')
css_path = package_path.joinpath('assets/css/date_picker.css')
class QDatePickerWidget(QWidget):
    dateChanged = pyqtSignal()
    today = QDate.currentDate()
    year = today.year()
    month = today.month()
    month_text = ""
    day = today.day()
    def __init__(self):
        super().__init__()
        self.setupUi()
        self.setupSignal()
    def setupUi(self):
        #addFonts()
        self.ui = loadUi(ui_path, self)
        self.setStyleSheet(open(css_path).read())
        buttons = self.ui.button_container.findChildren(QPushButton)
        self.month_dict = {id + 1: button for id, button in enumerate(buttons)}
        self.ui.retTodayButton.setText(f'{self.day:2d} {self.month_dict[self.month].text()} {self.year}')
        button = self.month_dict[self.month]
        button.setChecked(True)
        self.month_text = button.text()
        self.updateDate()
    def setupSignal(self):
        for button in self.month_dict:
            button = self.month_dict[button]
            button.pressed.connect(lambda btn=button: self.selectMonth(btn))

        self.ui.decYearButton.clicked.connect(self.decreaseYear)
        self.ui.incYearButton.clicked.connect(self.increaseYear)
        self.ui.retTodayButton.clicked.connect(self.retToday)

    @staticmethod
    def date_change_emit(function):
        def wrapper(*args):
            if function.__name__ == 'selectMonth':
                function(args[0], args[1])
            else:
                function(args[0])
            args[0].updateDate()
            args[0].dateChanged.emit()
        return wrapper

    @date_change_emit
    def selectMonth(self, button):
        self.month_text ,self.month= button.text(), button.objectName()[1:]
        button.setChecked(True)
        for btn in self.month_dict.values():
            btn_name = btn.objectName()[1:]
            if self.month != int(btn_name):
                btn.setChecked(False)

    @date_change_emit
    def decreaseYear(self):
        self.year -= 1

    @date_change_emit
    def increaseYear(self):
        self.year += 1

    def getDate(self):
        return {"year":self.year,"month_id": self.month,"month_text": self.month_text}

    def retToday(self):
        self.year = self.today.year()
        self.month = self.today.month()
        btn = self.month_dict[self.month]
        self.selectMonth(btn)
        btn.setChecked(True)

    def updateDate(self):
        self.ui.date_info.setText(str(self.year))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = QDatePickerWidget()
    w.show()
    app.exec()