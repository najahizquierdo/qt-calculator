# This Python file uses the following encoding: utf-8
import sys
from PySide2.QtUiTools import QUiLoader #allows us to import .ui files
from PySide2.QtWidgets import QApplication, QLineEdit, QPushButton
from PySide2.QtCore import QFile, QObject

class Calculator(QObject):
    #class constructor
    def __init__(self, ui_file, parent=None):

        #call parent QObject constructor
        super(Calculator, self).__init__(parent)

        #load the UI file into Python
         ui_file = QFile(ui_file)
        ui_file.open(QFile.ReadOnly)
        loader = QUiLoader()
        self.window = loader.load(ui_file)
        ui_file.close()
        
        #always remember to close files
        ui_file.close()

        #add event listener to the 7 button
        oneButton = self.window.findChild(QPushButton, 'oneButton')
        oneButton.clicked.connect(self.one_button_clicked)

        twoButton = self.window.findChild(QPushButton, 'twoButton')
        twoButton.clicked.connect(self.two_button_clicked)

        threeButton = self.window.findChild(QPushButton, 'threeButton')
        threeButton.clicked.connect(self.three_button_clicked)
        
        fourButton = self.window.findChild(QPushButton, 'fourButton')
        fourButton.clicked.connect(self.four_button_clicked)

        fiveButton = self.window.findChild(QPushButton, 'fiveButton')
        fiveButton.clicked.connect(self.five_button_clicked)

        sixButton = self.window.findChild(QPushButton, 'sixButton')
        sixButton.clicked.connect(self.six_button_clicked)
        
        sevenButton = self.window.findChild(QPushButton, 'sevenButton')
        sevenButton.clicked.connect(self.seven_button_clicked)

        eightButton = self.window.findChild(QPushButton, 'eightButton')
        eightButton.clicked.connect(self.eight_button_clicked)

        nineButton = self.window.findChild(QPushButton, 'nineButton')
        nineButton.clicked.connect(self.nine_button_clicked)

        zeroButton = self.window.findChild(QPushButton, 'zeroButton')
        zeroButton.clicked.connect(self.zero_button_clicked)

        addButton = self.window.findChild(QPushButton, 'addButton')
        addButton.clicked.connect(self.add_button_clicked)

        subtractButton = self.window.findChild(QPushButton, 'subtractButton')
        subtractButton.clicked.connect(self.subtract_button_clicked)

        multiplyButton = self.window.findChild(QPushButton, 'multiplyButton')
        multiplyButton.clicked.connect(self.multiply_button_clicked)

        equalButton = self.window.findChild(QPushButton, 'equalButton')
        equalButton.clicked.connect(self.equal_button_clicked)
        #show window to user
        self.window.show()

    def one_button_clicked(self):
        oneButton = self.window.findChild(QPushButton, 'oneButton')
        accumulator = self.window.findChild(QLineEdit, 'accumulatorText')
        accumulator.setText(accumulator.toPlainText() + oneButton.text())
    def two_button_clicked(self):
        twoButton = self.window.findChild(QPushButton, 'twoButton')
        accumulator = self.window.findChild(QLineEdit, 'accumulatorText')
        accumulator.setText(accumulator.toPlainText() + twoButton.text())
    def three_button_clicked(self):
        threeButton = self.window.findChild(QPushButton, 'threeButton')
        accumulator = self.window.findChild(QLineEdit, 'accumulatorText')
        accumulator.setText(accumulator.toPlainText() + threeButton.text())
    def four_button_clicked(self):
        fourButton = self.window.findChild(QPushButton, 'fourButton')
        accumulator = self.window.findChild(QLineEdit, 'accumulatorText')
        accumulator.setText(accumulator.toPlainText() + fourButton.text())
    def five_button_clicked(self):
        fiveButton = self.window.findChild(QPushButton, 'fiveButton')
        accumulator = self.window.findChild(QLineEdit, 'accumulatorText')
        accumulator.setText(fiveButton.text())
    def six_button_clicked(self):
        sixButton = self.window.findChild(QPushButton, 'sixButton')
        accumulator = self.window.findChild(QLineEdit, 'accumulatorText')
        accumulator.setText(accumulator.toPlainText() + sixButton.text())
    def seven_button_clicked(self):
        sevenButton = self.window.findChild(QPushButton, 'sevenButton')
        accumulator = self.window.findChild(QLineEdit, 'accumulatorText')
        accumulator.setText(accumulator.toPlainText() + sevenButton.text())
    def eight_button_clicked(self):
        eightButton = self.window.findChild(QPushButton, 'eightButton')
        accumulator = self.window.findChild(QLineEdit, 'accumulatorText')
        accumulator.setText(accumulator.toPlainText() + eightButton.text())
    def nine_button_clicked(self):
        nineButton = self.window.findChild(QPushButton, 'nineButton')
        accumulator = self.window.findChild(QLineEdit, 'accumulatorText')
        accumulator.setText(accumulator.toPlainText() + nineButton.text())
    def ten_button_clicked(self):
        tenButton = self.window.findChild(QPushButton, 'tenButton')
        accumulator = self.window.findChild(QLineEdit, 'accumulatorText')
        accumulator.setText(accumulator.toPlainText() + tenButton.text())

    def add_button_clicked(self):
        addButton = self.window.findChild(QPushButton, 'addButton')
        accumulator = self.window.findChild(QLineEdit, 'accumulatorText')
        accumulator.setText(addButton.text())
    def subtract_button_clicked(self):
        subtractButton = self.window.findChild(QPushButton, 'subtractButton')
        accumulator = self.window.findChild(QLineEdit, 'accumulatorText')
        accumulator.setText(subtractButton.text())
    def division_button_clicked(self):
        divisionButton = self.window.findChild(QPushButton, 'divisionButton')
        accumulator = self.window.findChild(QLineEdit, 'accumulatorText')
        accumulator.setText(divisionButton.text())
    def multiply_button_clicked(self):
        multiplyButton = self.window.findChild(QPushButton, 'multiplyButton')
        accumulator = self.window.findChild(QLineEdit, 'accumulatorText')
        accumulator.setText(multiplyButton.text())
    def equal_button_clicked(self):
        equalButton = self.window.findChild(QPushButton, 'equalButton')
        accumulator = self.window.findChild(QLineEdit, 'accumulatorText')
        accumulator.setText(equalButton.text())
           
        

if __name__ == '__main__':
    app = QApplication(sys.argv)
    calculator = Calculator('calculator.ui')
    calculator.window.show()
    sys.exit(app.exec_())