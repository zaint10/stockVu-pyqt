from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog
from multiprocessing import Process
import csv
import handler as hd

ready_to_generate = False
guideline_loaded = False


class Second(QtWidgets.QMainWindow):
    array = []
    header = []
    global ready_to_generate
    global guideline_loaded

    def __init__(self, parent=None):
        super(Second, self).__init__(parent)
        self.setupUi(self)

    def openFileDialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        guideline_fileName, _ = QFileDialog.getOpenFileName(self, "QFileDialog.getExistingDirectory()", "",
                                                            "All Files (*);;CSV File(*.csv)", options=options)
        return guideline_fileName

    @QtCore.pyqtSlot()
    def loadguidelines(self):
        self.tableWidget.setRowCount(0)
        f = self.openFileDialog()
        if f != '':
            with open(f, 'r') as file:

                reader = csv.reader(file, delimiter=",")
                self.header = [name for name in next(reader)]
                for row, rowData in enumerate(reader):

                    self.tableWidget.insertRow(row)
                    for col, colData in enumerate(rowData):
                        self.tableWidget.setItem(row, col, QtWidgets.QTableWidgetItem(colData))

            file.close()
            self.guideline_loaded = True
            self.vlbl_load.setText('Guideline Loaded')


    def generateTiers(self):
        if not self.guideline_loaded:
            msg = 'No Guidline is loaded. Please load the guidelines.'
            QtWidgets.QMessageBox.warning(self, 'Invalid Guidelines', msg, QtWidgets.QMessageBox.Ok)
            return

        for row in range(self.tableWidget.rowCount()):
            temp,val = [],0
            for col in range(1, self.tableWidget.columnCount()):
                val = self.tableWidget.item(row, col).text()
                if not val.isdigit():
                    msg = 'The Guidline have not set Properly. Some cells contain n/a values'
                    QtWidgets.QMessageBox.warning(self, 'Invalid Guidelines', msg, QtWidgets.QMessageBox.Ok)
                    self.ready_to_generate = False
                    break
                else:
                    temp = temp + [int(val)]
            else:
                temp = temp + [int(val)]

                self.array.append(temp)
                self.ready_to_generate = True
                continue
            break
        print(self.array[0][7])
        if self.ready_to_generate:
            Process(target=hd.AppWindow.generateT(self.array, self)).start()

    def showMesssage(self, msg, **args):
        QtWidgets.QMessageBox.information(self, 'Files successfully created', msg, QtWidgets.QMessageBox.Ok)
    def showError(self,msg,title):
        QtWidgets.QMessageBox.critical(self, title, msg, QtWidgets.QMessageBox.Ok)

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.NonModal)
        MainWindow.resize(792, 378)
        MainWindow.setMinimumSize(QtCore.QSize(0, 0))
        MainWindow.setMaximumSize(QtCore.QSize(16666666, 16666666))
        MainWindow.setStyleSheet("")
        MainWindow.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("")
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(10, 10, 761, 351))
        self.frame.setStyleSheet("background-color:rgb(72, 72, 72);\n"
                                 "background-color: rgb(10, 170, 76);\n"
                                 "font: 75 8pt \"MS Sans Serif\";\n"
                                 "\n"
                                 "\n"
                                 "color: rgb(255, 255, 255);\n"
                                 "\n"
                                 "\n"
                                 "\n"
                                 "\n"
                                 "\n"
                                 "")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.tableWidget = QtWidgets.QTableWidget(self.frame)
        self.tableWidget.setGeometry(QtCore.QRect(0, 0, 781, 241))
        self.tableWidget.setStyleSheet("background-color: rgb(144, 144, 144);\n"
                                       "background-color: rgb(85, 170, 127);\n"
                                       "font: 75 12pt \"Calibri\";\n"
                                       "selection-background-color: rgb(170, 32, 4);\n"
                                       "\n"
                                       "color: rgb(0, 0, 0);")
        self.tableWidget.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.tableWidget.setLineWidth(3)
        self.tableWidget.setAlternatingRowColors(True)
        self.tableWidget.setGridStyle(QtCore.Qt.DashDotDotLine)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(8)
        self.tableWidget.setRowCount(4)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        item.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsUserCheckable)
        self.tableWidget.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 7, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        item.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsUserCheckable)
        self.tableWidget.setItem(1, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        item.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsUserCheckable)
        self.tableWidget.setItem(2, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        item.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsUserCheckable)
        self.tableWidget.setItem(3, 0, item)
        self.vbtn_generateTiers = QtWidgets.QPushButton(self.frame)
        self.vbtn_generateTiers.setEnabled(True)
        self.vbtn_generateTiers.setGeometry(QtCore.QRect(640, 240, 141, 51))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.vbtn_generateTiers.sizePolicy().hasHeightForWidth())
        self.vbtn_generateTiers.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.vbtn_generateTiers.setFont(font)
        self.vbtn_generateTiers.setStyleSheet("QPushButton{\n"
                                              "  width: 180px;\n"
                                              "\n"
                                              "  position: relative;\n"
                                              "  left: 30%;\n"
                                              "  top: 30%;\n"
                                              "padding:5px 0;\n"
                                              "background-color: rgb(40, 40, 40);\n"
                                              "margin:10px;\n"
                                              "  \n"
                                              " \n"
                                              "}\n"
                                              "QPushButtonl:clicked{\n"
                                              "background-color: #00aa00;\n"
                                              "}")
        self.vbtn_generateTiers.setCheckable(False)
        self.vbtn_generateTiers.setAutoRepeat(False)
        self.vbtn_generateTiers.setAutoDefault(False)
        self.vbtn_generateTiers.setDefault(False)
        self.vbtn_generateTiers.setFlat(False)
        self.vbtn_generateTiers.setObjectName("vbtn_generateTiers")
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setGeometry(QtCore.QRect(210, 260, 281, 61))
        self.pushButton.setStyleSheet("QPushButton {\n"
                                      "background: #000;\n"
                                      "  width: 180px;\n"
                                      "  padding: 4px 0;\n"
                                      "  \n"
                                      "  position: absolute;\n"
                                      "  left: 50%;\n"
                                      "  top: 50%;\n"
                                      "  transform: translateX(-50%) \n"
                                      " \n"
                                      "}\n"
                                      "QPushButton:hover{\n"
                                      "background-color: #005500;\n"
                                      "}\n"
                                      "QPushButton{\n"
                                      "font-family: \'Roboto\'; \n"
                                      "text-align: center; text-transform: uppercase;\n"
                                      "color: #FFF;\n"
                                      " user-select: none;\n"
                                      "\n"
                                      "}\n"
                                      "")
        self.pushButton.setObjectName("pushButton")
        self.vlbl_load = QtWidgets.QLabel(self.frame)
        self.vlbl_load.setGeometry(QtCore.QRect(270, 190, 201, 20))
        self.vlbl_load.setStyleSheet("QLabel {\n"
                                     "background: #fff;\n"
                                     "  width: 180px;\n"
                                     "  padding: 4px 0;\n"
                                     "  \n"
                                     "  position: absolute;\n"
                                     "  left: 50%;\n"
                                     "  top: 50%;\n"
                                     "  transform: translateX(-50%) \n"
                                     " \n"
                                     "}\n"
                                     "\n"
                                     "QLabel{\n"
                                     "font-family: \'Roboto\'; \n"
                                     "text-align: center; text-transform: uppercase;\n"
                                     "color: #000;\n"
                                     " user-select: none;\n"
                                     "\n"
                                     "}\n"
                                     "")
        self.vlbl_load.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.vlbl_load.setAlignment(QtCore.Qt.AlignCenter)
        self.vlbl_load.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.vlbl_load.setObjectName("vlbl_load")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Tiers guidelines"))
        item = self.tableWidget.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "0"))
        item = self.tableWidget.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", "1"))
        item = self.tableWidget.verticalHeaderItem(2)
        item.setText(_translate("MainWindow", "2"))
        item = self.tableWidget.verticalHeaderItem(3)
        item.setText(_translate("MainWindow", "3"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Tiers"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Worst 1D%"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Worst 2D%"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Worst 5D%"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Since Inception"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Last 12 Months"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "Last 6 Months"))
        item = self.tableWidget.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "Since Start yr"))
        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        item = self.tableWidget.item(0, 1)
        item.setText(_translate("MainWindow", "2"))
        item = self.tableWidget.item(0, 2)
        item.setText(_translate("MainWindow", "3"))
        item = self.tableWidget.item(0, 3)
        item.setText(_translate("MainWindow", "n/a"))
        item = self.tableWidget.item(0, 4)
        item.setText(_translate("MainWindow", "5"))
        item = self.tableWidget.item(0, 5)
        item.setText(_translate("MainWindow", "5"))
        item = self.tableWidget.item(0, 6)
        item.setText(_translate("MainWindow", "5"))
        item = self.tableWidget.item(0, 7)
        item.setText(_translate("MainWindow", "5"))
        self.tableWidget.setSortingEnabled(__sortingEnabled)
        self.vbtn_generateTiers.setText(_translate("MainWindow", "Load (*csv) File"))
        self.pushButton.setText(_translate("MainWindow", "Generate Tiers"))
        self.vlbl_load.setText(_translate("MainWindow", "Nothing Loaded"))

        self.tableWidget.setRowCount(0)
        self.vbtn_generateTiers.clicked.connect(self.loadguidelines)
        self.pushButton.clicked.connect(self.generateTiers)
