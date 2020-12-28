import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon
from ui import Ui_MainWindow
from currency_converter import CurrencyConverter

class CurrencyConv(QtWidgets.QMainWindow):
    def __init__(self):
        super(CurrencyConv, self).__init__()   
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.init_UI()

    def init_UI(self):
        self.setWindowTitle('Currency Converter')
        self.setWindowIcon(QIcon('exchange.png'))

        self.ui.input_currency.setPlaceholderText('Amount')
        self.ui.input_amount.setPlaceholderText('From:')
        self.ui.output_currency.setPlaceholderText('To:')
        self.ui.output_amount.setPlaceholderText('Total')
        self.ui.pushButton.clicked.connect(self.conventer)

    def conventer(self):
        c = CurrencyConverter()
        input_currency = self.ui.input_amount.text()
        output_currency = self.ui.output_currency.text()
        input_amount = int(self.ui.input_currency.text())

        output_amount = round(c.convert(input_amount, '%s' % (input_currency), '%s' % (output_currency)), 2)

        self.ui.output_amount.setText(str(output_amount))

app = QtWidgets.QApplication([])
application = CurrencyConv()
application.show()

sys.exit(app.exec())