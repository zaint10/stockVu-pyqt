import datetime,time,threading
import handler as hd
from PyQt5 import QtCore, QtGui, QtWidgets
from multiprocessing import Process
import gui_2

TIME_LIMIT = 100





class Ui_vMainWindow(QtWidgets.QMainWindow):


    YYYMMDD= ''
    DDMMYYYY=''
    system=None
    ready_to_analyze=False
    completed=False
    count = 0


    def setupUi(self, vMainWindow):

        vMainWindow.setObjectName("vMainWindow")
        vMainWindow.resize(800, 600)
        vMainWindow.setMinimumSize(QtCore.QSize(800, 600))
        vMainWindow.setMaximumSize(QtCore.QSize(800, 600))
        vMainWindow.setStyleSheet("background-color:rgb(40, 40, 40);\n"
                                  "\n"
                                  "font: 75 12pt \"Candara Light\";\n"
                                  "\n"
                                  "color: rgb(255, 255, 255);\n"
                                  "\n"
                                  "\n"
                                  "alternate-background-color: #aa0000;\n"
                                  "\n"
                                  "\n"
                                  "")
        vMainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)

        self.centralwidget = QtWidgets.QWidget(vMainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.v_wcalendar = QtWidgets.QCalendarWidget(self.centralwidget)
        self.v_wcalendar.setGeometry(QtCore.QRect(200, 0, 381, 251))
        self.v_wcalendar.setStyleSheet("color: rgb(170, 0, 0);\n"
                                       "selection-background-color: rgb(85, 85, 127);\n"
                                       "background-color: rgb(0, 0, 0);\n"
                                       "color: rgb(255, 255, 255);\n"
                                       "selection-color: rgb(0, 0, 0);\n"
                                       "font-size: 18px")
        self.v_wcalendar.setInputMethodHints(QtCore.Qt.ImhNone)
        self.v_wcalendar.setFirstDayOfWeek(QtCore.Qt.Sunday)
        self.v_wcalendar.setGridVisible(True)
        self.v_wcalendar.setSelectionMode(QtWidgets.QCalendarWidget.SingleSelection)
        self.v_wcalendar.setVerticalHeaderFormat(QtWidgets.QCalendarWidget.NoVerticalHeader)
        self.v_wcalendar.setObjectName("v_wcalendar")
        self.vet_date = QtWidgets.QLineEdit(self.centralwidget)
        self.vet_date.setGeometry(QtCore.QRect(390, 260, 133, 20))
        self.vet_date.setText("")
        self.vet_date.setMaxLength(50)
        self.vet_date.setFrame(True)
        self.vet_date.setAlignment(QtCore.Qt.AlignCenter)
        self.vet_date.setReadOnly(True)
        self.vet_date.setObjectName("vet_date")
        self.vlabel_date = QtWidgets.QLabel(self.centralwidget)
        self.vlabel_date.setGeometry(QtCore.QRect(290, 260, 94, 20))
        font = QtGui.QFont()
        font.setFamily("Candara Light")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.vlabel_date.setFont(font)
        self.vlabel_date.setFrameShadow(QtWidgets.QFrame.Plain)
        self.vlabel_date.setTextFormat(QtCore.Qt.RichText)
        self.vlabel_date.setAlignment(QtCore.Qt.AlignCenter)
        self.vlabel_date.setObjectName("vlabel_date")
        self.vLabelstatus = QtWidgets.QLabel(self.centralwidget)
        self.vLabelstatus.setGeometry(QtCore.QRect(200, 370, 381, 41))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.vLabelstatus.setFont(font)
        self.vLabelstatus.setStyleSheet("QLabel {\n"
                                        "background: #aa0000;\n"
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
                                        "color: #FFF;\n"
                                        "\n"
                                        "}\n"
                                        "")
        self.vLabelstatus.setFrameShape(QtWidgets.QFrame.Panel)
        self.vLabelstatus.setFrameShadow(QtWidgets.QFrame.Raised)
        self.vLabelstatus.setTextFormat(QtCore.Qt.RichText)
        self.vLabelstatus.setAlignment(QtCore.Qt.AlignCenter)
        self.vLabelstatus.setObjectName("vLabelstatus")
        self.vbtn_fetch = QtWidgets.QPushButton(self.centralwidget)
        self.vbtn_fetch.setGeometry(QtCore.QRect(460, 290, 75, 23))
        self.vbtn_fetch.setAutoFillBackground(False)
        self.vbtn_fetch.setStyleSheet("QPushButton{\n"
                                      "  width: 180px;\n"
                                      "  padding: 4px 0;\n"
                                      "    color:#fff;\n"
                                      "  background-color: #aa0000;\n"
                                      "  position: relative;\n"
                                      "  left: 30%;\n"
                                      "  top: 30%;\n"
                                      "\n"
                                      "  \n"
                                      " \n"
                                      "}\n"
                                      "QPushButton:hover {\n"
                                      "    background-color:#000000;\n"
                                      "}\n"
                                      "")
        self.vbtn_fetch.setObjectName("vbtn_fetch")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 184, 561))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.verticalLayout.setContentsMargins(1, 1, 1, 1)
        self.verticalLayout.setObjectName("verticalLayout")
        self.vtb_dashBoard = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Candara Light")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.vtb_dashBoard.setFont(font)
        self.vtb_dashBoard.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.vtb_dashBoard.setStyleSheet("QPushButton{\n"
                                         "  width: 180px;\n"
                                         "  padding: 4px 0;\n"
                                         "  background-color: #ff8113;\n"
                                         "  position: relative;\n"
                                         "  left: 30%;\n"
                                         "  top: 30%;\n"
                                         "  \n"
                                         " \n"
                                         "}\n"
                                         "QPushButton:hover!pressed{\n"
                                         "background-color: rgb(224, 255, 0);\n"
                                         "}\n"
                                         "QPushButton{\n"
                                         "font-family: \'Roboto\'; \n"
                                         "text-align: center; text-transform: uppercase;\n"
                                         "color: #000;\n"
                                         "}\n"
                                         "")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../PycharmProjects/STOCKVU/Images/home.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.vtb_dashBoard.setIcon(icon)
        self.vtb_dashBoard.setFlat(False)
        self.vtb_dashBoard.setObjectName("vtb_dashBoard")
        self.verticalLayout.addWidget(self.vtb_dashBoard)
        self.vbtn_showResults = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.vbtn_showResults.setEnabled(False)
        font = QtGui.QFont()
        font.setFamily("Candara Light")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.vbtn_showResults.setFont(font)
        self.vbtn_showResults.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.vbtn_showResults.setStyleSheet("QPushButton{\n"
                                            "  width: 180px;\n"
                                            "  padding: 4px 0;\n"
                                            "  background-color: #5555ff;\n"
                                            "  position: absolute;\n"
                                            "  left: 50%;\n"
                                            "  top: 50%;\n"
                                            "  transform: translateX(-50%) \n"
                                            " \n"
                                            "}\n"
                                            "QPushButton:hover!pressed{\n"
                                            "background-color: rgb(224, 255, 0);\n"
                                            "}\n"
                                            "QPushButton{\n"
                                            "font-family: \'Roboto\'; \n"
                                            "text-align: center; text-transform: uppercase;\n"
                                            "color: #000;\n"
                                            "\n"
                                            "}\n"
                                            "")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../PycharmProjects/STOCKVU/Images/results.png"), QtGui.QIcon.Normal,
                        QtGui.QIcon.Off)
        self.vbtn_showResults.setIcon(icon1)
        self.vbtn_showResults.setFlat(False)
        self.vbtn_showResults.setObjectName("vbtn_showResults")
        self.verticalLayout.addWidget(self.vbtn_showResults)
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(600, 0, 201, 551))
        self.frame.setStyleSheet("padding-left:5px;\n"
                                 "background-color: rgb(24, 24, 24);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.frame)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(0, 0, 216, 561))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.v_rightLayour = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.v_rightLayour.setSizeConstraint(QtWidgets.QLayout.SetMinAndMaxSize)
        self.v_rightLayour.setContentsMargins(2, 10, 2, 5)
        self.v_rightLayour.setSpacing(0)
        self.v_rightLayour.setObjectName("v_rightLayour")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setObjectName("label")
        self.v_rightLayour.addWidget(self.label)
        self.pushButton_2 = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Candara Light")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("QPushButton{\n"
                                        "  width: 180px;\n"
                                        " \n"
                                        "  background-color: #ff8113;\n"
                                        "  position: relative;\n"
                                        "  left: 30%;\n"
                                        "  top: 30%;\n"
                                        "padding:5px 0;\n"
                                        "background-color: rgb(40, 40, 40);\n"
                                        "margin:10px;\n"
                                        "  \n"
                                        " \n"
                                        "}\n"
                                        "")
        self.pushButton_2.setObjectName("pushButton_2")
        self.v_rightLayour.addWidget(self.pushButton_2)
        self.pushButton_3 = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.pushButton_3.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_3.sizePolicy().hasHeightForWidth())
        self.pushButton_3.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Candara Light")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet("QPushButton{\n"
                                        "  width: 180px;\n"
                                        " \n"
                                        "  background-color: #ff8113;\n"
                                        "  position: relative;\n"
                                        "  left: 30%;\n"
                                        "  top: 30%;\n"
                                        "padding:5px 0;\n"
                                        "background-color: rgb(40, 40, 40);\n"
                                        "margin:10px;\n"
                                        "  \n"
                                        " \n"
                                        "}\n"
                                        "")
        self.pushButton_3.setCheckable(False)
        self.pushButton_3.setAutoRepeat(False)
        self.pushButton_3.setAutoDefault(False)
        self.pushButton_3.setDefault(False)
        self.pushButton_3.setFlat(False)
        self.pushButton_3.setObjectName("pushButton_3")
        self.v_rightLayour.addWidget(self.pushButton_3)
        self.vprogressBar = QtWidgets.QProgressBar(self.verticalLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.vprogressBar.sizePolicy().hasHeightForWidth())
        self.vprogressBar.setSizePolicy(sizePolicy)
        self.vprogressBar.setMaximumSize(QtCore.QSize(200, 20))
        self.vprogressBar.setStyleSheet("color: rgb(0, 0, 0);\n"
                                        "margin-left:5px;\n"
                                        "margin-right:5px")
        self.vprogressBar.setProperty("value", 0)
        self.vprogressBar.setAlignment(QtCore.Qt.AlignCenter)
        self.vprogressBar.setOrientation(QtCore.Qt.Horizontal)
        self.vprogressBar.setObjectName("vprogressBar")
        self.v_rightLayour.addWidget(self.vprogressBar)
        vMainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(vMainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 25))
        self.menubar.setObjectName("menubar")
        vMainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(vMainWindow)
        self.statusbar.setObjectName("statusbar")
        vMainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(vMainWindow)
        QtCore.QMetaObject.connectSlotsByName(vMainWindow)

    def retranslateUi(self, vMainWindow):
        _translate = QtCore.QCoreApplication.translate
        vMainWindow.setWindowTitle(_translate("vMainWindow", "StockVU"))
        self.vet_date.setPlaceholderText(_translate("vMainWindow", "YYYYMMDD"))
        self.vlabel_date.setText(_translate("vMainWindow", "Selected Date"))
        self.vLabelstatus.setText(_translate("vMainWindow", "STATUS"))
        self.vbtn_fetch.setText(_translate("vMainWindow", "Fetch File"))
        self.vtb_dashBoard.setText(_translate("vMainWindow", "Dash Board"))
        self.vbtn_showResults.setText(_translate("vMainWindow", "View Results"))
        self.label.setText(_translate("vMainWindow", "Analysis"))
        self.pushButton_2.setText(_translate("vMainWindow", "Run All in One"))
        self.pushButton_3.setText(_translate("vMainWindow", "Set Tier Constraints"))

        self.clickEvents()
        self.wtierSetter = gui_2.Second(self)


    def clickEvents(self):
        self.v_wcalendar.clicked.connect(lambda: self.showDate())
        self.vbtn_fetch.clicked.connect(lambda:hd.DirectoyHandler().fetch_file(self) )
        self.pushButton_2.clicked.connect(lambda : self.runAnalysis())
        self.pushButton_3.clicked.connect(lambda : self.showTierWindow())

    def showTierWindow(self):

        self.wtierSetter.setWindowFlags(QtCore.Qt.Window  | QtCore.Qt.WindowStaysOnTopHint)
        self.wtierSetter.show()
    def runAnalysis(self):
        if self.ready_to_analyze:

            Process(target=hd.AppWindow.startt(self)).start()
            Process(target=self.updateProgressBaru()).start()


        else:
            self.updateStatus('!!File is not Selected!!')

    @QtCore.pyqtSlot()
    def showDate(self):
        obj_date=datetime.datetime.strptime(self.v_wcalendar.selectedDate().toString(), '%a %b %d %Y')
        self.DDMMYYYY=obj_date.strftime('%d-%m-%Y')
        self.YYYMMDD=obj_date.strftime('%Y%m%d')

        self.vet_date.setText(self.DDMMYYYY)
        self.updateStatus("Date Selected")



    def updateStatus(self,msg,isComplete=False):
        self.vLabelstatus.setText(msg)
        if isComplete:
            self.vLabelstatus.setStyleSheet("QLabel {\n"
                                            "background: #4CAF50;\n"
                                            "  width: 180px;\n"
                                            "  padding: 4px 0;\n"
                                            "  \n"
                                            "  position: absolute;\n"
                                            "  left: 50%;\n"
                                            "  top: 50%;\n"
                                            "}\n"
                                            "\n"
                                            "QLabel{\n"
                                            "font-family: \'Roboto\'; \n"
                                            "text-align: center; \n"
                                            "color: #FFF;\n"
                                            "\n"
                                            "}\n"
                                            "")

    def updateProgressBar(self,val):
        if val<100:
            self.vprogressBar.setValue(val)

    def updateProgressBaru(self):
        while self.count < TIME_LIMIT:
            self.count += 5
            time.sleep(.10)
            self.vprogressBar.setValue(self.count)

    def showError(self,msg,title):
        QtWidgets.QMessageBox.critical(self, title, msg, QtWidgets.QMessageBox.Ok)
        self.vprogressBar.setValue(45)








