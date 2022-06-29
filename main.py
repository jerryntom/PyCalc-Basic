from PyQt5 import QtCore, QtGui, QtWidgets
from math import sqrt
from platform import system
from ctypes import windll
import os
import sys

if system() == "Windows":
    myappid = u'jerryntom.python.pycalc.29062022v1'
    windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)
else:
    pass

def resource_path(relative_path):
        try:
            base_path = sys._MEIPASS
        except Exception:
            base_path = os.path.abspath(".")
        
        return os.path.join(base_path, relative_path)


class Ui_Calculator:
    def __init__(self):
        self.styleSheet = """
            QToolTip {
                font-size: 25pt;
            }
            
            QLabel {
                text-align: left;
            }
            """
        self.calculatorHistory = ["0"]
        self.pastResult = ""
        self.pastCalculation = ""
        self.afterCalculation = ""
        self.beforeCalculation = ""    
        self.value = "0"

        self.centralwidget = QtWidgets.QWidget(Calculator)
        self.font = QtGui.QFont()
        self.numberField = QtWidgets.QLabel(self.centralwidget)
        self.errorLabel = QtWidgets.QLabel(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(Calculator)

        self.percentButton = self.buttonObject(10, 100, 111, 41, '%', self.percents)
        self.clearEntryButton = self.buttonObject(130, 100, 111, 41, 'CE', self.clearEntry)
        self.clearButton= self.buttonObject(250, 100, 111, 41, 'C', self.clear)
        self.backButton = self.buttonObject(370, 100, 111, 41, 'Back', self.back)
        self.squaredButton = self.buttonObject(130, 150, 111, 41, 'x²', self.squared)
        self.fractionButton = self.buttonObject(10, 150, 111, 41, '1/x', self.fraction)
        self.divideButton = self.buttonObject(370, 150, 111, 41, '/', self.mathButton)
        self.rootSecButton = self.buttonObject(250, 150, 111, 41, '²√x', self.squareRoot)
        self.eightButton = self.buttonObject(130, 200, 111, 41, '8', self.numberButton)
        self.sevenButton = self.buttonObject(10, 200, 111, 41, '7', self.numberButton)
        self.multiplyButton = self.buttonObject(370, 200, 111, 41, '*', self.mathButton)
        self.nineButton = self.buttonObject(250, 200, 111, 41, '9', self.numberButton)
        self.fiveButton = self.buttonObject(130, 250, 111, 41, '5', self.numberButton)
        self.fourButton = self.buttonObject(10, 250, 111, 41, '4', self.numberButton)
        self.substractButton = self.buttonObject(370, 250, 111, 41, '-', self.mathButton)
        self.sixButton = self.buttonObject(250, 250, 111, 41, '6', self.numberButton)
        self.twoButton = self.buttonObject(130, 300, 111, 41, '2', self.numberButton)
        self.oneButton = self.buttonObject(10, 300, 111, 41, '1', self.numberButton)
        self.addButton = self.buttonObject(370, 300, 111, 41, '+', self.mathButton)
        self.threeButton = self.buttonObject(250, 300, 111, 41, '3', self.numberButton)
        self.zeroButton = self.buttonObject(130, 350, 111, 41, '0', self.numberButton)
        self.plusMinusButton = self.buttonObject(10, 350, 111, 41, '+/-', self.plusMinus)
        self.calculateButton = self.buttonObject(370, 350, 111, 41, '=', self.calculate)
        self.commaButton = self.buttonObject(250, 350, 111, 41, '.', self.mathButton)

    def setupUi(self, Calculator): 
        """
        Creates GUI and its main compononents.

        Args:
            Calculator (object): QtWidgets.QMainWindow() 

        Returns:
            None 
        """
        Calculator.setObjectName("Calculator")
        Calculator.setMaximumSize(494, 421)
        Calculator.setMinimumSize(494, 421)
        Calculator.setWindowOpacity(0.96)
        Calculator.setTabShape(QtWidgets.QTabWidget.Triangular)
        Calculator.setWindowIcon(QtGui.QIcon(resource_path('images/logo.ico')))
        Calculator.setWindowTitle("PyCalc Basic")

        self.centralwidget.setObjectName("centralwidget")

        self.font.setFamily("Segoe UI Light")
        self.font.setPointSize(36)
        self.font.setBold(False)

        self.numberField.setGeometry(QtCore.QRect(10, 10, 471, 81))
        self.numberField.setFont(self.font)
        self.numberField.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing)
        self.numberField.setObjectName("label")
        self.numberField.setToolTip('0')
        self.numberField.setText('0')

        self.font.setPointSize(16)

        self.errorLabel.setGeometry(QtCore.QRect(10, -50, 471, 81))
        self.errorLabel.setFont(self.font)
        self.errorLabel.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing)
        self.errorLabel.setObjectName("errorLabel")
        
        self.statusbar.setObjectName("statusbar")
        Calculator.setCentralWidget(self.centralwidget)
        Calculator.setStatusBar(self.statusbar)

        QtCore.QMetaObject.connectSlotsByName(Calculator)

        self.value = self.numberField.text()

    def buttonObject(self, xCord, yCord, width, height, name, function):
        """
        Template for buttons. 
        Defines button and assigns function to it.

        Args:
            xCord (int): x cordinate of position
            yCord (int): y cordinate of position
            width (int): width of button
            height (int): height of button
            name (string): name / symbol of button 
            function (NoneType): function assigned to button 

        Returns:
            self.pushButton (object): pushButton object 
        """
        self.font.setFamily("Segoe UI Light")
        self.font.setPointSize(18)
        self.font.setBold(False)
        
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(xCord, yCord, width, height))
        self.pushButton.setFont(self.font)
        self.pushButton.setObjectName(name)
        self.pushButton.setText(name)

        try:
            if name in ('/', '*', '-', '+', '.'):
                self.pushButton.clicked.connect(lambda: self.mathButton(name))
            elif int(name) in range(0, 10):
                self.pushButton.clicked.connect(lambda: self.numberButton(name))
        except ValueError:
            self.pushButton.clicked.connect(function)

        return self.pushButton

    def percents(self):
        """
        Calculates certain percentage of previous number.
        For example 10 + 10% is 10 + 1.

        Returns:
            None 
        """
        percent = ''
        pastNumber = ''
        
        try: 
            for i in range(len(self.value) - 1, -1, -1):
                if self.value[i] in ('-', '+', '*', '/'):
                    break
                else:
                    percent += self.value[i]
            
            for i in range(len(self.value)-len(percent) - 2, -1, -1):
                if self.value[i] in ('-', '+', '*', '/'):
                    break 
                else:
                    pastNumber += self.value[i]

            self.value = self.value[0:len(self.value)-len(percent)]
            percent = float(percent[::-1])
            percent = str(percent/100)
            pastNumber = pastNumber[::-1]

            result = float(percent) * float(pastNumber) 
            result = self.roundNumber(result)

            if result == "":
                raise ValueError

            self.value += result 
            self.numberField.setText(self.value)
            self.numberField.setToolTip(self.value)
        except ValueError:
            self.exceptErrors("Calculated value is too small",
            "Calculated value is too small")
        except Exception as e:
            self.exceptErrors(e, "Error occured - percent function") 
        

    def clearEntry(self):
        """
        Reverts to previous expression 

        Returns:
            None 
        """
        if len(self.calculatorHistory) == 1:
            self.value = '0'
        elif len(self.calculatorHistory) > 1:
            self.calculatorHistory.pop()
            self.value = self.calculatorHistory[len(self.calculatorHistory)-1]

        self.numberField.setText(self.value)
        self.numberField.setToolTip(self.value)
    
    def clear(self):
        """
        Clears entire history of mathematical expressions 

        Returns:
            None 
        """
        self.value = '0'
        self.numberField.setText(self.value)
        self.numberField.setToolTip(self.value)
        self.calculatorHistory = ['0']

    def back(self):
        """
        Deletes one character from current expression.

        Returns:
            None 
        """
        try:
            if len(str(self.value)) == 1:
                self.value = '0'
            else:
                self.value = self.value[0:len(self.value)-1]
                
            self.numberField.setText(self.value)
            self.numberField.setToolTip(self.value)
        except Exception as e:
            self.exceptErrors(e, "Error occured - back function")
            self.clear()

    def fraction(self):
        """
        Calculates 1/x fraction where x is a current number. 
        Can be used if there's only a number not expression.

        Returns:
            None 
        """
        try:    
            if self.value == self.afterCalculation:
                self.value = self.beforeCalculation
                self.beforeCalculation = self.afterCalculation
            else:
                if len(self.value) >= 10: 
                    self.exceptErrors("Size limit - 10", 
                    "Size limit - 10")
                    return None

                self.beforeCalculation = self.value 
                self.pastCalculation = "fraction"
                self.value = self.roundNumber(1 / float(self.value))
                    
            self.numberField.setText(self.value)
            self.numberField.setToolTip(self.value)
            self.afterCalculation = self.value
            self.calculatorHistory.append(self.value)
            self.checkSizeLimit()
        except ZeroDivisionError as e:
            self.exceptErrors(e, "ZeroDivisionError - fraction function")
        except Exception as e:
            self.exceptErrors(e, "Error occured - fraction function")

    def squared(self):
        """
        Squares a number. Can be used if there's only a number not expression.

        Returns:
            None 
        """
        try:
            self.value = float(self.value)
            self.value = self.roundNumber(pow(self.value, 2))
            self.calculatorHistory.append(self.value)
            self.numberField.setText(self.value)
            self.numberField.setToolTip(self.value)
            self.checkSizeLimit()
        except Exception as e:
            self.exceptErrors(e, "Error occured - expSec function")

    def squareRoot(self):
        """
        Calculates square root of any number. 
        Can be used if there's only a number not expression.

        Returns:
            None 
        """        
        try:
            self.value = self.roundNumber(sqrt(float(self.value)))
            self.calculatorHistory.append(self.value)
            self.numberField.setText(self.value)
            self.numberField.setToolTip(self.value)
            self.checkSizeLimit()
        except Exception as e:
            self.exceptErrors(e, "Error occured - rootSec function")
     
    def calculate(self):
        """
        Mathematical expression handler. 
        Calculates entire expressions and shows result. 

        Returns: 
            None
        """
        try:
            if self.value == self.pastResult:
                self.value += self.pastCalculation
            else:
                self.pastCalculation = ''
                
                for i in range(len(self.value)-1, -1, -1):
                    if self.value[i] in ('-', '+', '*', '/'): 
                        self.pastCalculation += self.value[i]
                        break 
                    else:
                        self.pastCalculation += self.value[i]

                self.pastCalculation = self.pastCalculation[::-1]

            self.value = eval(self.value)
            self.value = self.roundNumber(self.value)
                
            if float(self.value) % 1 == 0 and '.' in self.value: 
                self.value = self.value[0:len(self.value)-2]
            
            self.calculatorHistory.append(self.value)
            self.numberField.setText(self.value)
            self.pastResult = self.value 
            self.numberField.setToolTip(self.value)
            self.checkSizeLimit()
        except Exception as e:
            if "/" in self.pastCalculation:
                self.clear()

            self.exceptErrors(e, "Can't calculate")

    def plusMinus(self):
        """
        Changes positive number to negative and vice versa.
        Can be used if there's only a number not expression.

        Returns: 
            None
        """ 
        try:         
            if float(self.value) % 1 == 0:
                self.value = str(-(float(self.value)))
                self.value = self.value[0:len(self.value)-2]
            elif float(self.value) % 1 != 0:
                self.value = str(-(float(self.value)))

            if self.value == '-0':
                self.value = '0'

            self.calculatorHistory.append(self.value)
            self.numberField.setText(self.value)
            self.numberField.setToolTip(self.value)
        except Exception as e:
            self.exceptErrors(e, "Can't convert it by plusMinus function")

    def clearErrors(self):
        """
        Clear error label in certain time after showing error info. 

        Returns: 
            None
        """
        self.errorLabel.setText('')

    def checkSizeLimit(self):
        """
        Result size limit handler. 
        Checks if result exceeds size rule. 

        Returns:
            None
        """
        if len(self.value) >= 64: 
            self.exceptErrors("Size limit 64", "Size limit - 64")
            self.clearEntry()
    
    def exceptErrors(self, errorLog, errorCom):
        """
        Error handler - shows error in IDE console and 
        passes info to communicate user.

        Args:
            errorLog (string): log info 
            errorCom (string): info for user passed to error label 

        Returns: 
            None
        """
        print(errorLog)
        self.errorLabel.setText(errorCom)
        QtCore.QTimer.singleShot(2000, self.clearErrors)

    def mathButton(self, symbol):
        """
        Mathematical button handler - basic functioning.

        Args:
            symbol (string): symbol of mathematical button

        Returns:
            None
        """
        self.value += symbol
        self.numberField.setText(self.value)   
        self.numberField.setToolTip(self.value) 

    def numberButton(self, number):
        """
        Number button handler - basic functioning.

        Args:
            number (int or float): raw number

        Returns:
            None
        """
        if number == '0' and self.value != '0':
            self.value += '0'
        else:
            if self.value == '0':
                self.value = number
            else:
                self.value += number
                        
        self.numberField.setText(self.value)  
        self.numberField.setToolTip(self.value)

    def roundNumber(self, number):         
        """
        Rounds number to 10 decimal places.

        Args:
            number (int or float): raw number

        Returns:
            result (str): rounded number
        """
        if number % 1 == 0:
            result = str(int(number))
        elif number % 1 != 0:
            result = format(number, ".10f")

            if "%" in self.pastCalculation:
                result = round(number, 10)
            elif "/" in self.pastCalculation:
                result = round(number, 4)
            elif ('.00000' in str(result) or '.99999' in str(result))  and self.pastCalculation != "fraction":
                result = format(number, ".0f")
        
            result = str(result).rstrip('0')

        return result 

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Calculator = QtWidgets.QMainWindow()
    ui = Ui_Calculator()
    app.setStyleSheet(ui.styleSheet)
    ui.setupUi(Calculator)
    Calculator.show()
    sys.exit(app.exec_())
