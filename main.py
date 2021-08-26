# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets
from math import sqrt

class Ui_Calculator(object):    
    styleSheet = """
    QToolTip {
        font-size: 25pt;
    }
    """
    
    def buttonObject(self, xCord, yCord, width, height, name, function):
        self.font = QtGui.QFont()
        self.font.setFamily("Segoe UI Light")
        self.font.setPointSize(18)
        self.font.setBold(False)
        
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(xCord, yCord, width, height))
        self.pushButton.setFont(self.font)
        self.pushButton.setObjectName(name)
        self.pushButton.clicked.connect(function)
        
        return self.pushButton

    def setupUi(self, Calculator):
        Calculator.setObjectName("Calculator")
        Calculator.setMaximumSize(494, 421)
        Calculator.setMinimumSize(494, 421)
        Calculator.setWindowOpacity(0.96)
        Calculator.setTabShape(QtWidgets.QTabWidget.Triangular)
        Calculator.setWindowIcon(QtGui.QIcon('logo.ico'))

        self.centralwidget = QtWidgets.QWidget(Calculator)
        self.centralwidget.setObjectName("centralwidget")

        self.pushButton_1 = self.buttonObject(10, 100, 111, 41, 'pushButton_1', self.percentClicked)
        self.pushButton_2 = self.buttonObject(130, 100, 111, 41, 'pushButton_2', self.clearEntry)
        self.pushButton_3 = self.buttonObject(250, 100, 111, 41, 'pushButton_3', self.clear)
        self.pushButton_4 = self.buttonObject(370, 100, 111, 41, 'pushButton_4', self.back)
        self.pushButton_5 = self.buttonObject(130, 150, 111, 41, 'pushButton_5', self.expSec)
        self.pushButton_6 = self.buttonObject(10, 150, 111, 41, 'pushButton_6', self.fraction)
        self.pushButton_7 = self.buttonObject(370, 150, 111, 41, 'pushButton_7', self.divide)
        self.pushButton_8 = self.buttonObject(250, 150, 111, 41, 'pushButton_8', self.rootSec)
        self.pushButton_9 = self.buttonObject(130, 200, 111, 41, 'pushButton_9', self.eightClicked)
        self.pushButton_10 = self.buttonObject(10, 200, 111, 41, 'pushButton_10', self.sevenClicked)
        self.pushButton_11 = self.buttonObject(370, 200, 111, 41, 'pushButton_11', self.multiply)
        self.pushButton_12 = self.buttonObject(250, 200, 111, 41, 'pushButton_12', self.nineClicked)
        self.pushButton_13 = self.buttonObject(130, 250, 111, 41, 'pushButton_13', self.fiveClicked)
        self.pushButton_14 = self.buttonObject(10, 250, 111, 41, 'pushButton_14', self.fourClicked)
        self.pushButton_15 = self.buttonObject(370, 250, 111, 41, 'pushButton_15', self.minus)
        self.pushButton_16 = self.buttonObject(250, 250, 111, 41, 'pushButton_16', self.sixClicked)
        self.pushButton_17 = self.buttonObject(130, 300, 111, 41, 'pushButton_17', self.twoClicked)
        self.pushButton_18 = self.buttonObject(10, 300, 111, 41, 'pushButton_18', self.oneClicked)
        self.pushButton_19 = self.buttonObject(370, 300, 111, 41, 'pushButton_19', self.plus)
        self.pushButton_20 = self.buttonObject(250, 300, 111, 41, 'pushButton_20', self.threeClicked)
        self.pushButton_21 = self.buttonObject(130, 350, 111, 41, 'pushButton_21', self.zeroClicked)
        self.pushButton_22 = self.buttonObject(10, 350, 111, 41, 'pushButton_22', self.plusMinus)
        self.pushButton_23 = self.buttonObject(370, 350, 111, 41, 'pushButton_23', self.calculate)
        self.pushButton_24 = self.buttonObject(250, 350, 111, 41, 'pushButton_24', self.dotClicked)

        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(36)
        font.setBold(False)

        self.numberField = QtWidgets.QLabel(self.centralwidget)
        self.numberField.setGeometry(QtCore.QRect(10, 10, 471, 81))
        self.numberField.setFont(font)
        self.numberField.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing)
        self.numberField.setObjectName("label")
        self.numberField.setToolTip('0')

        font.setPointSize(16)

        self.errorLabel = QtWidgets.QLabel(self.centralwidget)
        self.errorLabel.setGeometry(QtCore.QRect(10, -50, 471, 81))
        self.errorLabel.setFont(font)
        self.errorLabel.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing)
        self.errorLabel.setObjectName("errorLabel")
        
        Calculator.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(Calculator)
        self.statusbar.setObjectName("statusbar")
        Calculator.setStatusBar(self.statusbar)

        self.retranslateUi(Calculator)
        QtCore.QMetaObject.connectSlotsByName(Calculator)

        self.value = self.numberField.text()
        self.calcHistory = ['0']
        self.pastResult = ''
        self.aftFract = ''

    def retranslateUi(self, Calculator):
        _translate = QtCore.QCoreApplication.translate
        Calculator.setWindowTitle(_translate("Calculator", "PyCalc Basic"))
        self.pushButton_1.setText(_translate("Calculator", "%"))
        self.pushButton_2.setText(_translate("Calculator", "CE"))
        self.pushButton_3.setText(_translate("Calculator", "C"))
        self.pushButton_4.setText(_translate("Calculator", "Back"))
        self.pushButton_5.setText(_translate("Calculator", "x²"))
        self.pushButton_6.setText(_translate("Calculator", "1/x"))
        self.pushButton_7.setText(_translate("Calculator", "/"))
        self.pushButton_8.setText(_translate("Calculator", "²√x"))
        self.pushButton_9.setText(_translate("Calculator", "8"))
        self.pushButton_10.setText(_translate("Calculator", "7"))
        self.pushButton_11.setText(_translate("Calculator", "*"))
        self.pushButton_12.setText(_translate("Calculator", "9"))
        self.pushButton_13.setText(_translate("Calculator", "5"))
        self.pushButton_14.setText(_translate("Calculator", "4"))
        self.pushButton_15.setText(_translate("Calculator", "-"))
        self.pushButton_16.setText(_translate("Calculator", "6"))
        self.pushButton_17.setText(_translate("Calculator", "2"))
        self.pushButton_18.setText(_translate("Calculator", "1"))
        self.pushButton_19.setText(_translate("Calculator", "+"))
        self.pushButton_20.setText(_translate("Calculator", "3"))
        self.pushButton_21.setText(_translate("Calculator", "0"))
        self.pushButton_22.setText(_translate("Calculator", "+/-"))
        self.pushButton_23.setText(_translate("Calculator", "="))
        self.pushButton_24.setText(_translate("Calculator", "."))
        self.numberField.setText(_translate("Calculator", "0"))
        self.errorLabel.setText(_translate("Calculator", ''))

    def percentClicked(self):
        percent = ''
        pastNumber = ''
        errorCheck = True 
        
        try:
            if self.value == '0':
                self.exceptErrors("number label = '0'", "Can't use percent with 0")
                return None 
            elif self.value[len(self.value)-1] in ('.', '+', '-', '*', '/'):
                self.exceptErrors("Syntax Error(characters)", "Syntax error - percent function")
                return None 
            
            for element in self.value:
                if element in ('+', '-', '*', '/'):
                    errorCheck = False 
                    break 
            
            if errorCheck == True: 
                self.exceptErrors("Syntax Error(characters)", "Syntax error - percent function") 
                return None 

            for i in range(len(self.value)-1, -1, -1):
                if self.value[i] in ('-', '+', '*', '/'):
                    break
                else:
                    percent += self.value[i]

            if percent[::-1][0] == '0' and '.' not in percent[::-1]:
                self.exceptErrors("Percent value", "Wrong percent value")
                return None 
            
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

            if result % 1 != 0:
                result = round(result, 10)
            else:
                result = int(result)

            self.value += str(result)
            self.numberField.setText(self.value)
            self.numberField.setToolTip(self.value)
            
            print(self.value)
            print(percent, pastNumber)
        except Exception as e:
            self.exceptErrors(e, "Error occured - percent function")

    def clearEntry(self):
        if len(self.calcHistory) == 1:
            self.value = '0'
        elif len(self.calcHistory) > 1:
            self.calcHistory.pop()
            self.value = self.calcHistory[len(self.calcHistory)-1]

        self.numberField.setText(self.value)
        self.numberField.setToolTip(self.value)
        print(self.value)
        
    def clear(self):
        self.value = '0'
        self.numberField.setText(self.value)
        self.numberField.setToolTip(self.value)
        self.calcHistory = ['0']
        print(self.value)

    def back(self):
        if self.value == '0': 
            return None
        elif len(self.value) == 1:
            self.value = '0'
        else:
            self.value = self.value[0:len(self.value)-1]
            
        self.numberField.setText(self.value)
        self.numberField.setToolTip(self.value)
        print(self.value)

    def fraction(self):
        try:    
            if self.value[len(self.value)-1] == '.':
                self.exceptErrors('Syntax Error - dot in wrong position', "Syntax error - fraction function")
                return None 
                            
            if self.value == self.aftFract:
                self.value = self.befFract
                self.befFract = self.aftFract
            else:
                self.befFract = self.value 
                self.value = 1 / float(self.value)

                if float(self.value) % 1 != 0:
                    self.value = str(round(self.value, 10))
                else: 
                    self.value = str(int(self.value))
                    
            self.numberField.setText(self.value)
            self.numberField.setToolTip(self.value)
            self.aftFract = self.value
            self.calcHistory.append(self.value)
            self.checkLongNumber()
            print(self.value)
        except ZeroDivisionError as e:
            self.exceptErrors(e, "ZeroDivisionError - fraction function")
        except Exception as e:
            self.exceptErrors(e, "Error occured - fraction function")

    def expSec(self):
        try:
            if self.value[len(self.value)-1] in ('+', '-', '*', '/'):
                self.exceptErrors("Syntax Error(characters)", "Syntax error - expSec function")
                return None 

            self.value = float(self.value)
            self.value = pow(self.value, 2)
            
            if self.value % 1 == 0:
                self.value = str(int(self.value))
            else:
                self.value = round(self.value, 10)
                self.value = str(self.value)

            self.calcHistory.append(self.value)
            self.numberField.setText(self.value)
            self.numberField.setToolTip(self.value)
            self.checkLongNumber()
            print(self.value)
        except Exception as e:
            self.exceptErrors(e, "Error occured - expSec function")

    def rootSec(self):
        try:
            if self.value[len(self.value)-1] in ('+', '-', '*', '/'):
                self.exceptErrors("Syntax Error(characters)", "Syntax error - rootSec function")
                return None 

            self.value = sqrt(float(self.value))

            if self.value % 1 != 0:
                self.value = str(round(self.value, 10))
            else:
                self.value = str(int(self.value))
            
            self.calcHistory.append(self.value)

            print(self.value)
            self.numberField.setText(self.value)
            self.numberField.setToolTip(self.value)
            self.checkLongNumber()
        except Exception as e:
            self.exceptErrors(e, "Error occured - rootSec function")
    
    def divide(self):
        self.value += '/'
        self.numberField.setText(self.value)   
        self.numberField.setToolTip(self.value)
        print(self.value)

    def multiply(self):
        self.value += '*'
        self.numberField.setText(self.value)
        self.numberField.setToolTip(self.value)
        print(self.value)
        
    def minus(self):
        self.value += '-'
        self.numberField.setText(self.value)    
        self.numberField.setToolTip(self.value)
        print(self.value)

    def plus(self):
        self.value += '+'
        self.numberField.setText(self.value) 
        self.numberField.setToolTip(self.value)
        print(self.value)

    def calculate(self):
        try:
            if self.value == self.pastResult:
                self.value += self.pastCalculation
            else:
                self.pastCalculation = ''
                charCheck = False

                for element in self.value:
                    if element in ('-', '+', '*', '/'):
                        charCheck = True
                        break
                    
                if charCheck == False:
                    return None

                for i in range(len(self.value)-1, -1, -1):
                    if self.value[i] in ('-', '+', '*', '/'): 
                        self.pastCalculation += self.value[i]
                        break 
                    else:
                        self.pastCalculation += self.value[i]

                self.pastCalculation = self.pastCalculation[::-1]

            self.value = eval(self.value)
            self.value = str(round(self.value, 10))
                
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

    def zeroClicked(self):
        if self.value == '0':
            return None 
        else:
            self.value += '0'
            self.numberField.setText(self.value)      
            self.numberField.setToolTip(self.value)
            print(self.value)

    def oneClicked(self):
        if self.value == '0':
            self.value = '1'
        else:
            self.value += '1'
                     
        self.numberField.setText(self.value)  
        self.numberField.setToolTip(self.value)
        print(self.value)

    def twoClicked(self):
        if self.value == '0':
            self.value = '2'
        else:
            self.value += '2'
        
        self.numberField.setText(self.value)     
        self.numberField.setToolTip(self.value) 
        print(self.value)

    def threeClicked(self):
        if self.value == '0':
            self.value = '3'
        else:
            self.value += '3'
        
        self.numberField.setText(self.value)
        self.numberField.setToolTip(self.value)
        print(self.value)

    def fourClicked(self):
        if self.value == '0':
            self.value = '4'
        else:
            self.value += '4'
        
        self.numberField.setText(self.value)   
        self.numberField.setToolTip(self.value)
        print(self.value)

    def fiveClicked(self):
        if self.value == '0':
            self.value = '5'
        else:
            self.value += '5'
        
        self.numberField.setText(self.value)   
        self.numberField.setToolTip(self.value)
        print(self.value)

    def sixClicked(self):
        if self.value == '0':
            self.value = '6'
        else:
            self.value += '6'
        
        self.numberField.setText(self.value)   
        self.numberField.setToolTip(self.value)
        print(self.value)

    def sevenClicked(self):
        if self.value == '0':
            self.value = '7'
        else:
            self.value += '7'
        
        self.numberField.setText(self.value)      
        self.numberField.setToolTip(self.value)
        print(self.value)


    def eightClicked(self):
        if self.value == '0':
            self.value = '8'
        else:
            self.value += '8'
        
        self.numberField.setText(self.value)  
        self.numberField.setToolTip(self.value)
        print(self.value)

    def nineClicked(self):
        if self.value == '0':
            self.value = '9'
        else:
            self.value += '9'
        
        self.numberField.setText(self.value)   
        self.numberField.setToolTip(self.value)
        print(self.value)

    def plusMinus(self):
        try:
            if self.value == '0':
                return None         
            elif float(self.value) % 1 == 0:
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

    def dotClicked(self):
        self.value += '.'
        self.numberField.setText(self.value)
        self.numberField.setToolTip(self.value)
        print(self.value)

    def clearErrors(self):
        self.errorLabel.setText('')

    def checkLongNumber(self):
        if len(self.value) >= 64: 
            self.errorLabel.setText('SizeLimit: 64')
            QtCore.QTimer.singleShot(2000, self.clearErrors)
            self.value = '0'
            self.numberField.setText(self.value)
            self.numberField.setToolTip(self.value)
        else:
            return None
    
    def exceptErrors(self, errorLog, errorCom):
        print(errorLog)
        self.errorLabel.setText(errorCom)
        QtCore.QTimer.singleShot(2000, self.clearErrors)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Calculator = QtWidgets.QMainWindow()
    ui = Ui_Calculator()
    app.setStyleSheet(ui.styleSheet)
    ui.setupUi(Calculator)
    Calculator.show()
    sys.exit(app.exec_())
