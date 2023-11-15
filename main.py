from PyQt5 import QtCore, QtGui, QtWidgets
from math import sqrt
import os
import sys


def relative_path_to_absolute(relative_path):
    try:
        # scenario for PyInstaller executable
        base_path = sys.MEIPASS
    except Exception as e:
        # base_path is a current working directory
        base_path = os.path.abspath(".")
        print(e)

    return os.path.join(base_path, relative_path)


class CalculatorApp:
    """
    CalculatorApp is a class representing a basic calculator application
    with a graphical user interface (GUI) implemented using PyQt5.

    This class provides functionality for performing mathematical calculations,
    handling user interactions, and displaying the results in the GUI.
    """
    def __init__(self):
        self.basic_style_sheet = """
            QToolTip {
                font-size: 25pt;
            }
            
            QLabel {
                text-align: left;
            }
            """
        self.calculator_history = ["0"]
        self.prev_calculation = ""
        self.past_calculation = ""
        self.after_calculation = ""
        self.before_calculation = ""
        self.expression_field_value = "0"

        # elements of gui
        self.central_widget = QtWidgets.QWidget(Calculator)
        self.font = QtGui.QFont()
        self.expression_field_label = QtWidgets.QLabel(self.central_widget)
        self.error_label = QtWidgets.QLabel(self.central_widget)
        self.status_bar = QtWidgets.QStatusBar(Calculator)

        # buttons
        self.calculate_fraction_of_previous_number_button = \
            self.button_object(10, 100, 111, 41, '%', self.calculate_fraction_of_previous_number)
        self.revert_to_previous_result_button = \
            self.button_object(130, 100, 111, 41, 'CE', self.revert_to_previous_result)
        self.clear_calculator_memory_button = self.button_object(250, 100, 111, 41, 'C', self.clear_calculator_memory)
        self.clear_character_button = self.button_object(370, 100, 111, 41, 'Back', self.clear_character)
        self.square_number_button = self.button_object(130, 150, 111, 41, 'x²', self.square_number)
        self.number_to_inverse_button = self.button_object(10, 150, 111, 41, '1/x', self.number_to_inverse)
        self.divide_button = self.button_object(370, 150, 111, 41, '/', self.math_operation_button)
        self.square_root_button = self.button_object(250, 150, 111, 41, '²√x', self.square_root)
        self.eight_button = self.button_object(130, 200, 111, 41, '8', self.digit_button)
        self.seven_button = self.button_object(10, 200, 111, 41, '7', self.digit_button)
        self.multiply_button = self.button_object(370, 200, 111, 41, '*', self.math_operation_button)
        self.nine_button = self.button_object(250, 200, 111, 41, '9', self.digit_button)
        self.five_button = self.button_object(130, 250, 111, 41, '5', self.digit_button)
        self.four_button = self.button_object(10, 250, 111, 41, '4', self.digit_button)
        self.subtract_button = self.button_object(370, 250, 111, 41, '-', self.math_operation_button)
        self.six_button = self.button_object(250, 250, 111, 41, '6', self.digit_button)
        self.two_button = self.button_object(130, 300, 111, 41, '2', self.digit_button)
        self.one_button = self.button_object(10, 300, 111, 41, '1', self.digit_button)
        self.add_button = self.button_object(370, 300, 111, 41, '+', self.math_operation_button)
        self.three_button = self.button_object(250, 300, 111, 41, '3', self.digit_button)
        self.zero_button = self.button_object(130, 350, 111, 41, '0', self.digit_button)
        self.negate_number_button = self.button_object(10, 350, 111, 41, '+/-', self.negate_number)
        self.evaluate_expression_button = self.button_object(370, 350, 111, 41, '=', self.evaluate_expression)
        self.comma_button = self.button_object(250, 350, 111, 41, '.', self.math_operation_button)
        self.push_button = None

    def set_key_press_event(self, event):
        """
        Waits for key press to catch event

        :param event: calculator app event
        :return: None
        """
        key_press = event.key()

        if key_press == QtCore.Qt.Key_0:
            self.digit_button('0')
        elif key_press == QtCore.Qt.Key_1:
            self.digit_button('1')
        elif key_press == QtCore.Qt.Key_2:
            self.digit_button('2')
        elif key_press == QtCore.Qt.Key_3:
            self.digit_button('3')
        elif key_press == QtCore.Qt.Key_4:
            self.digit_button('4')
        elif key_press == QtCore.Qt.Key_5:
            self.digit_button('5')
        elif key_press == QtCore.Qt.Key_6:
            self.digit_button('6')
        elif key_press == QtCore.Qt.Key_7:
            self.digit_button('7')
        elif key_press == QtCore.Qt.Key_8:
            self.digit_button('8')
        elif key_press == QtCore.Qt.Key_9:
            self.digit_button('9')
        elif key_press == QtCore.Qt.Key_Return:
            self.evaluate_expression()
        elif key_press == QtCore.Qt.Key_Backspace:
            self.clear_character()
        elif key_press == QtCore.Qt.Key_Plus:
            self.math_operation_button('+')
        elif key_press == QtCore.Qt.Key_Minus:
            self.math_operation_button('-')
        elif key_press == QtCore.Qt.Key_Asterisk:
            self.math_operation_button('*')
        elif key_press == QtCore.Qt.Key_Slash:
            self.math_operation_button('/')
        elif key_press == QtCore.Qt.Key_Period:
            self.math_operation_button('.')

    def set_user_interface(self, calculator_window_instance):
        """
        Creates GUI and its main components.

        :param calculator_window_instance: QtWidgets.QMainWindow()
        :return: None
        """
        # properties of main window
        calculator_window_instance.setObjectName("Calculator")
        calculator_window_instance.setMaximumSize(494, 421)
        calculator_window_instance.setMinimumSize(494, 421)
        calculator_window_instance.setWindowOpacity(0.96)
        calculator_window_instance.setWindowIcon(QtGui.QIcon(relative_path_to_absolute('images/logo.ico')))
        calculator_window_instance.setWindowTitle("PyCalc Basic")
        calculator_window_instance.keyPressEvent = self.set_key_press_event

        self.central_widget.setObjectName("centralwidget")

        self.font.setFamily("Segoe UI Light")
        self.font.setPointSize(36)
        self.font.setBold(False)

        # properties of expression field
        self.expression_field_label.setGeometry(QtCore.QRect(10, 10, 471, 81))
        self.expression_field_label.setFont(self.font)
        self.expression_field_label.setAlignment(QtCore.Qt.AlignBottom | QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing)
        self.expression_field_label.setObjectName("qlineedit")
        self.expression_field_label.setToolTip('0')
        self.expression_field_label.setText('0')

        self.font.setPointSize(16)

        # properties of error label
        self.error_label.setGeometry(QtCore.QRect(10, -50, 471, 81))
        self.error_label.setFont(self.font)
        self.error_label.setAlignment(QtCore.Qt.AlignBottom | QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing)
        self.error_label.setObjectName("errorLabel")

        # properties of status bar
        self.status_bar.setObjectName("statusbar")
        calculator_window_instance.setCentralWidget(self.central_widget)
        calculator_window_instance.setStatusBar(self.status_bar)

        QtCore.QMetaObject.connectSlotsByName(calculator_window_instance)

        self.expression_field_value = self.expression_field_label.text()

        return calculator_window_instance

    def button_object(self, x_pos, y_pos, width, height, name, function):
        """
        Template for button. Defines button and assigns function to it.
        :param x_pos: x coordinate of position
        :param y_pos: y coordinate of position
        :param width: width of button
        :param height: height of button
        :param name: name / symbol of button
        :param function: function assigned to button
        :return: self.pushButton(object): QPushButton object
        """
        self.font.setFamily("Segoe UI Light")
        self.font.setPointSize(18)
        self.font.setBold(False)

        self.push_button = QtWidgets.QPushButton(self.central_widget)
        self.push_button.setGeometry(QtCore.QRect(x_pos, y_pos, width, height))
        self.push_button.setFont(self.font)
        self.push_button.setObjectName(name)
        self.push_button.setText(name)

        try:
            if name in ('/', '*', '-', '+', '.'):
                self.push_button.clicked.connect(lambda: self.math_operation_button(name))
            elif int(name) in range(0, 10):
                self.push_button.clicked.connect(lambda: self.digit_button(name))
        except ValueError:
            self.push_button.clicked.connect(function)

        return self.push_button

    def calculate_fraction_of_previous_number(self):
        """
        Calculates certain percentage of previous number inside expression.
        For example 10 + 10% is 10 + 1.

        :return: None
        """
        percent = ''
        previous_number = ''

        try:
            for i in range(len(self.expression_field_value) - 1, -1, -1):
                if self.expression_field_value[i] in ('-', '+', '*', '/'):
                    break
                else:
                    percent += self.expression_field_value[i]

            for i in range(len(self.expression_field_value) - len(percent) - 2, -1, -1):
                if self.expression_field_value[i] in ('-', '+', '*', '/'):
                    break
                else:
                    previous_number += self.expression_field_value[i]

            self.expression_field_value = self.expression_field_value[0:len(self.expression_field_value) - len(percent)]
            percent = float(percent[::-1])
            percent = str(percent / 100)
            previous_number = previous_number[::-1]

            result = float(percent) * float(previous_number)
            result = self.round_number(result)

            if result == "":
                raise ValueError

            self.expression_field_value += result
            self.expression_field_label.setText(self.expression_field_value)
            self.expression_field_label.setToolTip(self.expression_field_value)
        except ValueError:
            self.generate_error_info("Calculated value is too small",
                                     "Calculated value is too small")
        except Exception as error:
            self.generate_error_info(str(error), "Error occurred - percent function")

    def revert_to_previous_result(self):
        """
        Reverts to previous result.

        :return: None
        """
        if len(self.calculator_history) == 1:
            self.expression_field_value = '0'
        elif len(self.calculator_history) > 1:
            self.calculator_history.pop()
            self.expression_field_value = self.calculator_history[len(self.calculator_history) - 1]

        self.expression_field_label.setText(self.expression_field_value)
        self.expression_field_label.setToolTip(self.expression_field_value)

    def clear_calculator_memory(self):
        """
        Clears entire history of mathematical expressions

        :return: None
        """
        self.expression_field_value = '0'
        self.expression_field_label.setText(self.expression_field_value)
        self.expression_field_label.setToolTip(self.expression_field_value)
        self.calculator_history = ['0']

    def clear_character(self):
        """
        Deletes one character from current expression.

        :return: None
        """
        try:
            if len(str(self.expression_field_value)) == 1:
                self.expression_field_value = '0'
            else:
                self.expression_field_value = self.expression_field_value[0:len(self.expression_field_value) - 1]

            self.expression_field_label.setText(self.expression_field_value)
            self.expression_field_label.setToolTip(self.expression_field_value)
        except Exception as error:
            self.generate_error_info(str(error), "Error occurred - clear_character function")
            self.clear_calculator_memory()

    def number_to_inverse(self):
        """
        Calculates 1/x fraction where x is a current number.

        :return: None
        """
        try:
            if self.expression_field_value == self.after_calculation:
                self.expression_field_value = self.before_calculation
                self.before_calculation = self.after_calculation
            else:
                if len(self.expression_field_value) >= 10:
                    self.generate_error_info("Size limit - 10",
                                             "Size limit - 10")
                    return None

                self.before_calculation = self.expression_field_value
                self.past_calculation = 'fraction'
                self.expression_field_value = self.round_number(1 / float(self.expression_field_value))

            self.expression_field_label.setText(self.expression_field_value)
            self.expression_field_label.setToolTip(self.expression_field_value)
            self.after_calculation = self.expression_field_value
            self.calculator_history.append(self.expression_field_value)
            self.is_result_too_big()
        except ZeroDivisionError as error:
            self.generate_error_info(str(error), "ZeroDivisionError - number_to_inverse function")
        except Exception as error:
            self.generate_error_info(str(error), "Error occurred - number_to_inverse function")

    def square_number(self):
        """
        Raises a number to the second power.

        :return: None
        """
        try:
            self.expression_field_value = float(self.expression_field_value)
            self.expression_field_value = self.round_number(pow(self.expression_field_value, 2))
            self.calculator_history.append(self.expression_field_value)
            self.expression_field_label.setText(self.expression_field_value)
            self.expression_field_label.setToolTip(self.expression_field_value)
            self.is_result_too_big()
        except Exception as error:
            self.generate_error_info(str(error), "Error occurred - square_number function")

    def square_root(self):
        """
        Calculates a square root of number.

        :return: None
        """
        try:
            self.expression_field_value = self.round_number(sqrt(float(self.expression_field_value)))
            self.calculator_history.append(self.expression_field_value)
            self.expression_field_label.setText(self.expression_field_value)
            self.expression_field_label.setToolTip(self.expression_field_value)
            self.is_result_too_big()
        except Exception as error:
            self.generate_error_info(str(error), "Error occurred - square_root function")

    def evaluate_expression(self):
        """
        Evaluates a result of valid, mathematical expression.

        :return: None
        """
        try:
            if self.expression_field_value == self.prev_calculation:
                self.expression_field_value += self.past_calculation
            else:
                self.past_calculation = ''

                for i in range(len(self.expression_field_value) - 1, -1, -1):
                    if self.expression_field_value[i] in ('-', '+', '*', '/'):
                        self.past_calculation += self.expression_field_value[i]
                        break
                    else:
                        self.past_calculation += self.expression_field_value[i]

                self.past_calculation = self.past_calculation[::-1]

            self.expression_field_value = eval(self.expression_field_value)
            self.expression_field_value = self.round_number(self.expression_field_value)

            if float(self.expression_field_value) % 1 == 0 and '.' in self.expression_field_value:
                self.expression_field_value = self.expression_field_value[0:len(self.expression_field_value) - 2]

            self.calculator_history.append(self.expression_field_value)
            self.expression_field_label.setText(self.expression_field_value)
            self.prev_calculation = self.expression_field_value
            self.expression_field_label.setToolTip(self.expression_field_value)
            self.is_result_too_big()
        except Exception as error:
            if "/" in self.past_calculation:
                self.clear_calculator_memory()

            self.generate_error_info(str(error), "Can't evaluate an expression - SYNTAX ERROR")

    def negate_number(self):
        """
        Changes positive number to negative and vice versa.

        :return: None
        """
        try:
            if float(self.expression_field_value) % 1 == 0:
                self.expression_field_value = str(-(float(self.expression_field_value)))
                self.expression_field_value = self.expression_field_value[0:len(self.expression_field_value) - 2]
            else:
                self.expression_field_value = str(-(float(self.expression_field_value)))

            if self.expression_field_value == '-0':
                self.expression_field_value = '0'

            self.calculator_history.append(self.expression_field_value)
            self.expression_field_label.setText(self.expression_field_value)
            self.expression_field_label.setToolTip(self.expression_field_value)
        except Exception as error:
            self.generate_error_info(str(error), "Can't convert by negate_number function")

    def is_result_too_big(self):
        """
        Checks if result exceeds size rule.

        :return: None
        """
        if len(self.expression_field_value) >= 64:
            self.generate_error_info("Size limit 64", "Size limit - 64")
            self.revert_to_previous_result()

    def generate_error_info(self, detailed_error_info, short_error_info):
        """
        Error handler - shows error in IDE console and
        passes info to communicate user.

        :param detailed_error_info: log info
        :param short_error_info: info for user passed to error label
        :return: None
        """
        print(detailed_error_info)
        self.error_label.setText(short_error_info)
        QtCore.QTimer.singleShot(2000, lambda: self.error_label.setText(''))

    def math_operation_button(self, math_symbol):
        """
        Mathematical operation handler - basic functioning.

        :param math_symbol: symbol of mathematical button
        :return: None
        """
        self.expression_field_value += math_symbol
        self.expression_field_label.setText(self.expression_field_value)
        self.expression_field_label.setToolTip(self.expression_field_value)

    def digit_button(self, digit):
        """
        Digit button handler - basic functioning.

        :param digit: digit in form of a character
        :return: None
        """
        if digit == '0' and self.expression_field_value != '0':
            self.expression_field_value += '0'
        else:
            if self.expression_field_value == '0':
                self.expression_field_value = digit
            else:
                self.expression_field_value += digit

        self.expression_field_label.setText(str(self.expression_field_value))
        self.expression_field_label.setToolTip(str(self.expression_field_value))

    def round_number(self, number):
        """
        Rounds number maximally 10 decimal places.

        :param number: Number to round
        :return: result (str): rounded number
        """
        if number % 1 == 0:
            result = str(int(number))
        else:
            result = format(number, ".10f")

            if "%" in self.past_calculation:
                result = round(number, 10)
            elif "/" in self.past_calculation:
                result = round(number, 4)
            elif ('.00000' in str(result) or '.99999' in str(result)) and self.past_calculation != "fraction":
                result = format(number, ".0f")

            result = str(result).rstrip('0')

        return result


# block execution from another Python file than main.py
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Calculator = QtWidgets.QMainWindow()
    ui = CalculatorApp()
    app.setStyleSheet(ui.basic_style_sheet)
    ui.set_user_interface(Calculator)
    Calculator.show()
    sys.exit(app.exec_())
