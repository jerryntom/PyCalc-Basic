from PyQt5 import QtCore, QtGui, QtWidgets
from math import sqrt

class Ui_Calculator:
    # declarations of variables   
    def __init__(self):     
        self.styleSheet = """
            QToolTip {
                font-size: 25pt;
            }
            """
        self.calcHistory = ["0"]
        self.pastResult = ""
        self.pastCalculation = ""
        self.aftFrac = ""
        self.befFrac = ""    
        self.value = "0"

        self.centralwidget = QtWidgets.QWidget(Calculator)
        self.font = QtGui.QFont()
        self.numberField = QtWidgets.QLabel(self.centralwidget)
        self.errorLabel = QtWidgets.QLabel(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(Calculator)

        # buttons 
        self.percentBut = self.buttonObject(10, 100, 111, 41, '%', self.percentClicked)
        self.clearEntryBut = self.buttonObject(130, 100, 111, 41, 'CE', self.clearEntry)
        self.clearBut= self.buttonObject(250, 100, 111, 41, 'C', self.clear)
        self.backBut = self.buttonObject(370, 100, 111, 41, 'back', self.back)
        self.expSecBut = self.buttonObject(130, 150, 111, 41, 'x²', self.expSec)
        self.fractionBut = self.buttonObject(10, 150, 111, 41, '1/x', self.fraction)
        self.divideBut = self.buttonObject(370, 150, 111, 41, '/', self.mathSymbol)
        self.rootSecBut = self.buttonObject(250, 150, 111, 41, '²√x', self.rootSec)
        self.eightBut = self.buttonObject(130, 200, 111, 41, '8', self.numbers)
        self.sevenBut = self.buttonObject(10, 200, 111, 41, '7', self.numbers)
        self.multiplyBut = self.buttonObject(370, 200, 111, 41, '*', self.mathSymbol)
        self.nineBut = self.buttonObject(250, 200, 111, 41, '9', self.numbers)
        self.fiveBut = self.buttonObject(130, 250, 111, 41, '5', self.numbers)
        self.fourBut = self.buttonObject(10, 250, 111, 41, '4', self.numbers)
        self.substractBut = self.buttonObject(370, 250, 111, 41, '-', self.mathSymbol)
        self.sixBut = self.buttonObject(250, 250, 111, 41, '6', self.numbers)
        self.twoBut = self.buttonObject(130, 300, 111, 41, '2', self.numbers)
        self.oneBut = self.buttonObject(10, 300, 111, 41, '1', self.numbers)
        self.addBut = self.buttonObject(370, 300, 111, 41, '+', self.mathSymbol)
        self.threeBut = self.buttonObject(250, 300, 111, 41, '3', self.numbers)
        self.zeroBut = self.buttonObject(130, 350, 111, 41, '0', self.numbers)
        self.plusMinusBut = self.buttonObject(10, 350, 111, 41, '+/-', self.plusMinus)
        self.calculateBut = self.buttonObject(370, 350, 111, 41, '=', self.calculate)
        self.dotBut = self.buttonObject(250, 350, 111, 41, '.', self.mathSymbol)

    #construction of window and its components
    def setupUi(self, Calculator): 
        Calculator.setObjectName("Calculator")
        Calculator.setMaximumSize(494, 421)
        Calculator.setMinimumSize(494, 421)
        Calculator.setWindowOpacity(0.96)
        Calculator.setTabShape(QtWidgets.QTabWidget.Triangular)
        Calculator.setWindowIcon(QtGui.QIcon('logo.ico'))

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

    # template for buttons 
    def buttonObject(self, xCord, yCord, width, height, name, function):
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
                self.pushButton.clicked.connect(lambda: self.mathSymbol(name))
            elif int(name) in range(0, 10):
                self.pushButton.clicked.connect(lambda: self.numbers(name))
        except ValueError:
            self.pushButton.clicked.connect(function)

        return self.pushButton

    # calculating part of number by percents 
    def percentClicked(self):
        percent = ''
        pastNumber = ''
        errorCheck = True 
        
        try: 
            for i in range(len(self.value)-1, -1, -1):
                if self.value[i] in ('-', '+', '*', '/'):
                    break
                else:
                    percent += self.value[i]
            
            for i in range(len(self.value)-len(percent)-2, -1, -1):
                if self.value[i] in ('-', '+', '*', '/'):
                    break 
                else:
                    pastNumber += self.value[i]

            self.value = self.value[0:len(self.value)-len(percent)]
            percent = float(percent[::-1])
            percent = str(percent/100)
            pastNumber = pastNumber[::-1]
            result = float(percent) * float(pastNumber) 

            self.value += self.betterRound(result)
            self.numberField.setText(self.value)
            self.numberField.setToolTip(self.value)
            
            print(self.value)
            print(percent, pastNumber)
        except Exception as e:
            self.exceptErrors(e, "Error occured - percent function") 

    # revert to past expression
    def clearEntry(self):
        if len(self.calcHistory) == 1:
            self.value = '0'
        elif len(self.calcHistory) > 1:
            self.calcHistory.pop()
            self.value = self.calcHistory[len(self.calcHistory)-1]

        self.numberField.setText(self.value)
        self.numberField.setToolTip(self.value)
        print(self.value)
    
    # delete entire expression and calcHistory
    def clear(self):
        self.value = '0'
        self.numberField.setText(self.value)
        self.numberField.setToolTip(self.value)
        self.calcHistory = ['0']
        print(self.value)

    # delete one character from expression
    def back(self):
        if len(self.value) == 1:
            self.value = '0'
        else:
            self.value = self.value[0:len(self.value)-1]
            
        self.numberField.setText(self.value)
        self.numberField.setToolTip(self.value)
        print(self.value)

    # calculating fraction of numbers - 1/x
    def fraction(self):
        try:    
            if self.value == self.aftFrac:
                self.value = self.befFrac
                self.befFrac = self.aftFrac
            else:
                if len(self.value) >= 12: 
                    self.exceptErrors('Too big number', "Too big number - fraction function")
                    return None

                self.befFrac = self.value 
                self.value = self.betterRound(1 / float(self.value))
                    
            self.numberField.setText(self.value)
            self.numberField.setToolTip(self.value)
            self.aftFrac = self.value
            self.calcHistory.append(self.value)
            self.checkLongNumber()
            print(self.value)
        except ZeroDivisionError as e:
            self.exceptErrors(e, "ZeroDivisionError - fraction function")
        except Exception as e:
            self.exceptErrors(e, "Error occured - fraction function")

    # calculating second degree's power
    def expSec(self):
        try:
            self.value = float(self.value)
            self.value = self.betterRound(pow(self.value, 2))
            self.calcHistory.append(self.value)
            self.numberField.setText(self.value)
            self.numberField.setToolTip(self.value)
            self.checkLongNumber()
            print(self.value)
        except Exception as e:
            self.exceptErrors(e, "Error occured - expSec function")

    # calculating square root
    def rootSec(self):
        try:
            self.value = self.betterRound(sqrt(float(self.value)))
            self.calcHistory.append(self.value)
            self.numberField.setText(self.value)
            self.numberField.setToolTip(self.value)
            self.checkLongNumber()
            print(self.value)
        except Exception as e:
            self.exceptErrors(e, "Error occured - rootSec function")
    
    # calculating entire expressions from self.value 
    def calculate(self):
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
            self.value = self.betterRound(float(self.value))
                
            if float(self.value) % 1 == 0 and '.' in self.value: 
                self.value = self.value[0:len(self.value)-2]
            
            self.calcHistory.append(self.value)
            self.numberField.setText(self.value)
            self.pastResult = self.value 
            self.numberField.setToolTip(self.value)
            self.checkLongNumber()
            print(self.value)
        except Exception as e:
            self.exceptErrors(e, "Syntax error - can't calculate")

    # changing + to - and the other way
    def plusMinus(self):
        try:         
            if float(self.value) % 1 == 0:
                self.value = str(-(float(self.value)))
                self.value = self.value[0:len(self.value)-2]
            elif float(self.value) % 1 != 0:
                self.value = str(-(float(self.value)))

            if self.value == '-0':
                self.value = '0'

            self.calcHistory.append(self.value)
            self.numberField.setText(self.value)
            self.numberField.setToolTip(self.value)
            print(self.value)
        except Exception as e:
            self.exceptErrors(e, "Can't convert it by plusMinus function")

    # connected to QTimer - exceptErrors for hiding error label
    def clearErrors(self):
        self.errorLabel.setText('')

    # checking if number has 64 chars or more
    def checkLongNumber(self):
        if len(self.value) >= 64: 
            self.errorLabel.setText('SizeLimit: 64')
            QtCore.QTimer.singleShot(2000, self.clearErrors)
            self.value = '0'
            self.numberField.setText(self.value)
            self.numberField.setToolTip(self.value)
    
    # passing errors to error label 
    def exceptErrors(self, errorLog, errorCom):
        print(errorLog)
        self.errorLabel.setText(errorCom)
        QtCore.QTimer.singleShot(2000, self.clearErrors)

    # making buttons with math symbols better
    def mathSymbol(self, symbol):
        self.value += symbol
        self.numberField.setText(self.value)   
        self.numberField.setToolTip(self.value) 
        print(self.value)

    # making numeric button better
    def numbers(self, number):
        if number == '0' and self.value != '0':
            self.value += '0'
        else:
            if self.value == '0':
                self.value = number
            else:
                self.value += number
                        
        self.numberField.setText(self.value)  
        self.numberField.setToolTip(self.value)
        print(self.value)

    # rounding numbers to 10 decimal places
    def betterRound(self, number):         
        if number % 1 == 0:
            result = str(int(number))
        elif number % 1 != 0:
            result = format(number, ".10f")
            
            if '.00000' in str(result) or '.99999' in str(result):
                result = format(number, ".0f")
        
        result = str(result).rstrip('0')

        return result 

# app execution
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Calculator = QtWidgets.QMainWindow()
    ui = Ui_Calculator()
    app.setStyleSheet(ui.styleSheet)
    ui.setupUi(Calculator)
    Calculator.show()
    sys.exit(app.exec_())
