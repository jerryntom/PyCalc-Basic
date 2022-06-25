from PyQt5 import QtCore, QtGui, QtWidgets
from math import sqrt


class Ui_Calculator:
    def __init__(self):
        self.styleSheet = """
            QToolTip {
                font-size: 25pt;
            }
            """
        self.calcHistory = ["0"]
        self.pastResult = ""
        self.pastCalculation = ""
        self.afterCalculation = ""
        self.beforeCalc = ""    
        self.value = "0"

        self.centralwidget = QtWidgets.QWidget(Calculator)
        self.font = QtGui.QFont()
        self.numberField = QtWidgets.QLabel(self.centralwidget)
        self.errorLabel = QtWidgets.QLabel(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(Calculator)

        self.percentBut = self.buttonObject(10, 100, 111, 41, '%', self.percentClicked)
        self.clearEntryBut = self.buttonObject(130, 100, 111, 41, 'CE', self.clearEntry)
        self.clearBut= self.buttonObject(250, 100, 111, 41, 'C', self.clear)
        self.backBut = self.buttonObject(370, 100, 111, 41, 'Back', self.back)
        self.expSecBut = self.buttonObject(130, 150, 111, 41, 'x²', self.squared)
        self.fractionBut = self.buttonObject(10, 150, 111, 41, '1/x', self.oneTenth)
        self.divideBut = self.buttonObject(370, 150, 111, 41, '/', self.mathButton)
        self.rootSecBut = self.buttonObject(250, 150, 111, 41, '²√x', self.squareRoot)
        self.eightBut = self.buttonObject(130, 200, 111, 41, '8', self.numberButton)
        self.sevenBut = self.buttonObject(10, 200, 111, 41, '7', self.numberButton)
        self.multiplyBut = self.buttonObject(370, 200, 111, 41, '*', self.mathButton)
        self.nineBut = self.buttonObject(250, 200, 111, 41, '9', self.numberButton)
        self.fiveBut = self.buttonObject(130, 250, 111, 41, '5', self.numberButton)
        self.fourBut = self.buttonObject(10, 250, 111, 41, '4', self.numberButton)
        self.substractBut = self.buttonObject(370, 250, 111, 41, '-', self.mathButton)
        self.sixBut = self.buttonObject(250, 250, 111, 41, '6', self.numberButton)
        self.twoBut = self.buttonObject(130, 300, 111, 41, '2', self.numberButton)
        self.oneBut = self.buttonObject(10, 300, 111, 41, '1', self.numberButton)
        self.addBut = self.buttonObject(370, 300, 111, 41, '+', self.mathButton)
        self.threeBut = self.buttonObject(250, 300, 111, 41, '3', self.numberButton)
        self.zeroBut = self.buttonObject(130, 350, 111, 41, '0', self.numberButton)
        self.plusMinusBut = self.buttonObject(10, 350, 111, 41, '+/-', self.plusMinus)
        self.calculateBut = self.buttonObject(370, 350, 111, 41, '=', self.calculate)
        self.dotBut = self.buttonObject(250, 350, 111, 41, '.', self.mathButton)

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
        Calculator.setWindowIcon(QtGui.QIcon('logo.ico'))
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

    def percentClicked(self):
        """
        Calculates certain percentage of previous number.
        For example 10 + 10% is 10 + 1.

        Returns:
            None 
        """
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

    def clearEntry(self):
        """
        Reverts to previous expression 

        Returns:
            None 
        """
        if len(self.calcHistory) == 1:
            self.value = '0'
        elif len(self.calcHistory) > 1:
            self.calcHistory.pop()
            self.value = self.calcHistory[len(self.calcHistory)-1]

        self.numberField.setText(self.value)
        self.numberField.setToolTip(self.value)
        print(self.value)
    
    def clear(self):
        """
        Clears entire history of mathematical expressions 

        Returns:
            None 
        """
        self.value = '0'
        self.numberField.setText(self.value)
        self.numberField.setToolTip(self.value)
        self.calcHistory = ['0']
        print(self.value)

    def back(self):
        """
        Deletes one character from current expression.

        Returns:
            None 
        """
        if len(self.value) == 1:
            self.value = '0'
        else:
            self.value = self.value[0:len(self.value)-1]
            
        self.numberField.setText(self.value)
        self.numberField.setToolTip(self.value)
        print(self.value)

    def oneTenth(self):
        """
        Calculates 1/10 fraction of number. 
        Can be used if there's only a number not expression.

        Returns:
            None 
        """
        try:    
            if self.value == self.afterCalculation:
                self.value = self.beforeCalc
                self.beforeCalc = self.afterCalculation
            else:
                if len(self.value) >= 12: 
                    self.exceptErrors('Too big number - size limit 12', 
                    "Too big number - fraction function, size limit")
                    return None

                self.beforeCalc = self.value 
                self.value = self.betterRound(1 / float(self.value))
                    
            self.numberField.setText(self.value)
            self.numberField.setToolTip(self.value)
            self.afterCalculation = self.value
            self.calcHistory.append(self.value)
            self.checkLongNumber()
            print(self.value)
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
            self.value = self.betterRound(pow(self.value, 2))
            self.calcHistory.append(self.value)
            self.numberField.setText(self.value)
            self.numberField.setToolTip(self.value)
            self.checkLongNumber()
            print(self.value)
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
            self.value = self.betterRound(sqrt(float(self.value)))
            self.calcHistory.append(self.value)
            self.numberField.setText(self.value)
            self.numberField.setToolTip(self.value)
            self.checkLongNumber()
            print(self.value)
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

    def plusMinus(self):
        """
        Changes positive number to negative and vice versa.

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

            self.calcHistory.append(self.value)
            self.numberField.setText(self.value)
            self.numberField.setToolTip(self.value)
            print(self.value)
        except Exception as e:
            self.exceptErrors(e, "Can't convert it by plusMinus function")

    def clearErrors(self):
        """
        Clear error label in certain time after showing error info. 

        Returns: 
            None
        """
        self.errorLabel.setText('')

    def checkLongNumber(self):
        """
        Result size limit handler. Checks if result exceeds size rule. 

        Returns:
            None
        """
        if len(self.value) >= 64: 
            self.errorLabel.setText('SizeLimit: 64')
            QtCore.QTimer.singleShot(2000, self.clearErrors)
            self.value = '0'
            self.numberField.setText(self.value)
            self.numberField.setToolTip(self.value)
    
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
        print(self.value)

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
        print(self.value)

    def betterRound(self, number):         
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

            if '.00000' in str(result) or '.99999' in str(result):
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
