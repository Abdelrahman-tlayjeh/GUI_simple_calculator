from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def __init__(self):
        self.inputs_on_scr = ""
        self.inputs_to_calc = ""
        self.max_length = 25
        self.operator = ["+", "-", "*", "/", "**"]
        self.screen_fontSize = 16

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(487, 570)
#pushButton design
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
#screen
        self.lcd_screen = QtWidgets.QTextBrowser(self.centralwidget)
        self.lcd_screen.setGeometry(QtCore.QRect(30, 20, 421, 91))
        self.lcd_screen.setObjectName("lcd_screen")
        self.lcd_screen.setFontPointSize(16)     
#button 0
        self.nb0 = QtWidgets.QPushButton(self.centralwidget)
        self.nb0.setGeometry(QtCore.QRect(30, 400, 61, 61))
        self.nb0.setFont(font)
        self.nb0.setObjectName("nb0")
        #On Click function
        self.nb0.clicked.connect(lambda: self.add_char("0", "0"))
#button 1
        self.nb1 = QtWidgets.QPushButton(self.centralwidget)
        self.nb1.setGeometry(QtCore.QRect(30, 310, 61, 61))
        self.nb1.setFont(font)
        self.nb1.setObjectName("nb1")
        #On Click function
        self.nb1.clicked.connect(lambda: self.add_char("1", "1"))
#button 2
        self.nb2 = QtWidgets.QPushButton(self.centralwidget)
        self.nb2.setGeometry(QtCore.QRect(120, 310, 61, 61))
        self.nb2.setFont(font)
        self.nb2.setObjectName("nb2")
        #On Click function
        self.nb2.clicked.connect(lambda: self.add_char("2", "2"))
#button 3
        self.nb3 = QtWidgets.QPushButton(self.centralwidget)
        self.nb3.setGeometry(QtCore.QRect(210, 310, 61, 61))
        self.nb3.setFont(font)
        self.nb3.setObjectName("nb3")
        #On Click function
        self.nb3.clicked.connect(lambda: self.add_char("3", "3"))
#button 4
        self.nb4 = QtWidgets.QPushButton(self.centralwidget)
        self.nb4.setGeometry(QtCore.QRect(30, 220, 61, 61))
        self.nb4.setFont(font)
        self.nb4.setObjectName("nb4")
        #On Click function
        self.nb4.clicked.connect(lambda: self.add_char("4", "4"))
#button 5
        self.nb5 = QtWidgets.QPushButton(self.centralwidget)
        self.nb5.setGeometry(QtCore.QRect(120, 220, 61, 61))
        self.nb5.setFont(font)
        self.nb5.setObjectName("nb5")
        #On Click function
        self.nb5.clicked.connect(lambda: self.add_char("5", "5"))
#button 6
        self.nb6 = QtWidgets.QPushButton(self.centralwidget)
        self.nb6.setGeometry(QtCore.QRect(210, 220, 61, 61))
        self.nb6.setFont(font)
        self.nb6.setObjectName("nb6")
        #On Click function
        self.nb6.clicked.connect(lambda: self.add_char("6", "6"))
#button 7
        self.nb7 = QtWidgets.QPushButton(self.centralwidget)
        self.nb7.setGeometry(QtCore.QRect(30, 130, 61, 61))    
        self.nb7.setFont(font)
        self.nb7.setObjectName("nb7")
        #On Click function
        self.nb7.clicked.connect(lambda: self.add_char("7", "7"))
#button 8
        self.nb8 = QtWidgets.QPushButton(self.centralwidget)
        self.nb8.setGeometry(QtCore.QRect(120, 130, 61, 61))
        self.nb8.setFont(font)
        self.nb8.setObjectName("nb8")
        #On Click function
        self.nb8.clicked.connect(lambda: self.add_char("8", "8"))
#button 9        
        self.nb9 = QtWidgets.QPushButton(self.centralwidget)
        self.nb9.setGeometry(QtCore.QRect(210, 130, 61, 61))
        self.nb9.setFont(font)
        self.nb9.setObjectName("nb9")
        #On Click function
        self.nb9.clicked.connect(lambda: self.add_char("9", "9"))
#button .
        self.dot = QtWidgets.QPushButton(self.centralwidget)
        self.dot.setGeometry(QtCore.QRect(120, 400, 61, 61))
        self.dot.setFont(font)
        self.dot.setObjectName("dot")
        #On Click function
        self.dot.clicked.connect(lambda: self.add_char(".", "."))
#button ^
        self.pwr = QtWidgets.QPushButton(self.centralwidget)
        self.pwr.setGeometry(QtCore.QRect(210, 400, 61, 61))
        self.pwr.setFont(font)
        self.pwr.setObjectName("pwr")
        #On Click function
        self.pwr.clicked.connect(lambda: self.add_char("^", "**"))
#button +
        self.add = QtWidgets.QPushButton(self.centralwidget)
        self.add.setGeometry(QtCore.QRect(300, 310, 61, 61))
        self.add.setFont(font)
        self.add.setObjectName("add")
        #On Click function
        self.add.clicked.connect(lambda: self.add_char("+", "+"))
#button -
        self.min = QtWidgets.QPushButton(self.centralwidget)
        self.min.setGeometry(QtCore.QRect(390, 310, 61, 61))
        self.min.setFont(font)
        self.min.setObjectName("min")
        #On Click function
        self.min.clicked.connect(lambda: self.add_char("-", "-"))
#button X
        self.mul = QtWidgets.QPushButton(self.centralwidget)
        self.mul.setGeometry(QtCore.QRect(300, 220, 61, 61))
        self.mul.setFont(font)
        self.mul.setObjectName("mul")
        #On Click function
        self.mul.clicked.connect(lambda: self.add_char("x", "*"))
#button /
        self.div = QtWidgets.QPushButton(self.centralwidget)
        self.div.setGeometry(QtCore.QRect(390, 220, 61, 61))
        self.div.setFont(font)
        self.div.setObjectName("div")
        #On Click function
        self.div.clicked.connect(lambda: self.add_char("÷", "/"))
#button delete    
        self.delete = QtWidgets.QPushButton(self.centralwidget)
        self.delete.setGeometry(QtCore.QRect(300, 130, 61, 61))
        self.delete.setFont(font)
        self.delete.setObjectName("del")
        #On Click function
        self.delete.clicked.connect(self.del_char)
#button AC
        self.ac = QtWidgets.QPushButton(self.centralwidget)
        self.ac.setGeometry(QtCore.QRect(390, 130, 61, 61))
        self.ac.setFont(font)
        self.ac.setObjectName("ac")
        #On Click function
        self.ac.clicked.connect(self.clear_all)
#button =
        self.eql = QtWidgets.QPushButton(self.centralwidget)
        self.eql.setGeometry(QtCore.QRect(300, 400, 151, 61))
        self.eql.setFont(font)
        self.eql.setObjectName("eql")
        #On Click function
        self.eql.clicked.connect(self.get_result)
#label
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(6, 510, 411, 41))
        font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
#bar/status bar
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 487, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

#Functions-------------------------------------------------------------------------------->
    def update_display(self):
        self.lcd_screen.clear()
        self.lcd_screen.append(self.inputs_on_scr)
        #for debugging---------------------------------------------->
        #print(f"Back-End expression: {self.inputs_to_calc}")
        #print(f"Front-End expression: {self.inputs_on_scr}")

    def add_char(self, char_on_scr, math_char):
        if len(self.inputs_on_scr) <= self.max_length:
            #change font size and max length of screen
            if len(self.inputs_on_scr) == self.max_length:
                #decrease the font size when the first line of screen is full
                if self.screen_fontSize > 10:
                    self.max_length += 1
                    self.screen_fontSize -= 1
                    self.lcd_screen.setFontPointSize(self.screen_fontSize)
                #allow screen to display up to 2 lines of numbers
                if self.screen_fontSize == 10:
                    self.max_length = 89
            #avoid add zero at beginning
            if self.inputs_on_scr == "0":
                self.inputs_on_scr = ""
                self.inputs_to_calc = ""  
            #avoid add zero after operator
            if not(self.inputs_on_scr == ""):    
                if self.inputs_to_calc[-1] == "0" and self.inputs_to_calc[-2] in self.operator:
                    #allow add zero before point "."
                    if not(math_char == "."):
                        self.inputs_on_scr = self.inputs_on_scr[ :-1]
                        self.inputs_to_calc = self.inputs_to_calc[ :-1]
            #adding character and update the screen
            self.inputs_on_scr += char_on_scr
            self.inputs_to_calc += math_char
            self.update_display()

    def del_char(self):     
        if len(self.inputs_on_scr) > 0:
           self.inputs_on_scr = self.inputs_on_scr[ :-1]
           self.inputs_to_calc = self.inputs_to_calc[ :-1]
           self.update_display()

    def clear_all(self):        
        self.inputs_on_scr = ""
        self.inputs_to_calc = ""
        self.update_display()

    def get_result(self):       
        try:
            self.inputs_on_scr = str(eval(self.inputs_to_calc))
            self.inputs_to_calc = self.inputs_on_scr    #allow reuse the result number
            self.update_display()
        except ZeroDivisionError:
            zero_err_msg = "Cannot divide by Zero‬."
            self.inputs_on_scr = ""
            self.inputs_to_calc = ""
            self.lcd_screen.clear()
            self.lcd_screen.append(zero_err_msg)
        except:
            err_msg = "Error!"
            self.inputs_on_scr = ""
            self.inputs_to_calc = ""
            self.lcd_screen.clear()
            self.lcd_screen.append(err_msg)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Simple Calculator"))
        self.nb7.setText(_translate("MainWindow", "7"))
        self.nb8.setText(_translate("MainWindow", "8"))
        self.nb9.setText(_translate("MainWindow", "9"))
        self.delete.setText(_translate("MainWindow", "del"))
        self.ac.setText(_translate("MainWindow", "AC"))
        self.nb4.setText(_translate("MainWindow", "4"))
        self.nb5.setText(_translate("MainWindow", "5"))
        self.nb6.setText(_translate("MainWindow", "6"))
        self.mul.setText(_translate("MainWindow", "x"))
        self.div.setText(_translate("MainWindow", "÷"))
        self.nb1.setText(_translate("MainWindow", "1"))
        self.nb2.setText(_translate("MainWindow", "2"))
        self.nb3.setText(_translate("MainWindow", "3"))
        self.add.setText(_translate("MainWindow", "+"))
        self.min.setText(_translate("MainWindow", "-"))
        self.nb0.setText(_translate("MainWindow", "0"))
        self.dot.setText(_translate("MainWindow", "."))
        self.pwr.setText(_translate("MainWindow", "^"))
        self.eql.setText(_translate("MainWindow", "="))
        self.label.setText(_translate("MainWindow", "By Abdelrahman Tlayjeh."))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
