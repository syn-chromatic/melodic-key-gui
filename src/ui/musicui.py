# Form implementation generated from reading ui file 'MusicalKey.ui'
#
# Created by: PyQt6 UI code generator 6.4.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(480, 256)
        MainWindow.setAcceptDrops(True)
        MainWindow.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(30, 30, 30);\n"
"")
        MainWindow.setTabShape(QtWidgets.QTabWidget.TabShape.Rounded)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalSlider = QtWidgets.QSlider(self.centralwidget)
        self.horizontalSlider.setGeometry(QtCore.QRect(129, 62, 171, 21))
        self.horizontalSlider.setStyleSheet("")
        self.horizontalSlider.setTracking(True)
        self.horizontalSlider.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.highPassDial = QtWidgets.QDial(self.centralwidget)
        self.highPassDial.setGeometry(QtCore.QRect(160, 90, 50, 64))
        self.highPassDial.setMinimum(1)
        self.highPassDial.setMaximum(20000)
        self.highPassDial.setSingleStep(50)
        self.highPassDial.setPageStep(50)
        self.highPassDial.setWrapping(False)
        self.highPassDial.setNotchTarget(1.0)
        self.highPassDial.setNotchesVisible(True)
        self.highPassDial.setObjectName("highPassDial")
        self.lowPassDial = QtWidgets.QDial(self.centralwidget)
        self.lowPassDial.setGeometry(QtCore.QRect(220, 90, 50, 64))
        self.lowPassDial.setMinimum(1)
        self.lowPassDial.setMaximum(20000)
        self.lowPassDial.setSingleStep(50)
        self.lowPassDial.setPageStep(50)
        self.lowPassDial.setWrapping(False)
        self.lowPassDial.setNotchTarget(1.0)
        self.lowPassDial.setNotchesVisible(True)
        self.lowPassDial.setObjectName("lowPassDial")
        self.playButton = QtWidgets.QPushButton(self.centralwidget)
        self.playButton.setEnabled(False)
        self.playButton.setGeometry(QtCore.QRect(30, 60, 41, 21))
        self.playButton.setStyleSheet("QPushButton {background-color: rgb(45, 150, 50);} \n"
"QPushButton:disabled{color: rgb(70, 70, 70);background-color: rgb(160, 160, 160);}\n"
"")
        self.playButton.setObjectName("playButton")
        self.pauseButton = QtWidgets.QPushButton(self.centralwidget)
        self.pauseButton.setEnabled(False)
        self.pauseButton.setGeometry(QtCore.QRect(70, 60, 41, 21))
        self.pauseButton.setStyleSheet("QPushButton {color: rgb(0, 0, 0); background-color: rgb(210, 210, 210);} \n"
"QPushButton:disabled{color: rgb(70, 70, 70);background-color: rgb(160, 160, 160);}\n"
"")
        self.pauseButton.setObjectName("pauseButton")
        self.highPassLabel = QtWidgets.QLabel(self.centralwidget)
        self.highPassLabel.setGeometry(QtCore.QRect(150, 150, 71, 20))
        self.highPassLabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.highPassLabel.setObjectName("highPassLabel")
        self.highPassCheckbox = QtWidgets.QPushButton(self.centralwidget)
        self.highPassCheckbox.setEnabled(True)
        self.highPassCheckbox.setGeometry(QtCore.QRect(320, 60, 111, 21))
        self.highPassCheckbox.setStyleSheet("QPushButton {color:rgb(0, 0, 0);} \n"
"QPushButton {color: rgb(120, 10, 10); background:rgb(210, 210, 210);} \n"
"QPushButton:checked{color: rgb(20, 140, 50); background:rgb(50, 50, 50);}\n"
"QPushButton:disabled{color: rgb(70, 70, 70);background-color: rgb(160, 160, 160); border-style: None;}")
        self.highPassCheckbox.setCheckable(True)
        self.highPassCheckbox.setChecked(False)
        self.highPassCheckbox.setObjectName("highPassCheckbox")
        self.lowPassCheckbox = QtWidgets.QPushButton(self.centralwidget)
        self.lowPassCheckbox.setGeometry(QtCore.QRect(320, 80, 111, 21))
        self.lowPassCheckbox.setStyleSheet("QPushButton {color:rgb(0, 0, 0);} \n"
"QPushButton {color: rgb(120, 10, 10); background:rgb(210, 210, 210);} \n"
"QPushButton:checked{color: rgb(20, 140, 50); background:rgb(50, 50, 50);}\n"
"QPushButton:disabled{color: rgb(70, 70, 70);background-color: rgb(160, 160, 160); border-style: None;}")
        self.lowPassCheckbox.setCheckable(True)
        self.lowPassCheckbox.setObjectName("lowPassCheckbox")
        self.instrumentFilterCheckbox = QtWidgets.QPushButton(self.centralwidget)
        self.instrumentFilterCheckbox.setGeometry(QtCore.QRect(320, 100, 111, 21))
        self.instrumentFilterCheckbox.setStyleSheet("QPushButton {color:rgb(0, 0, 0);} \n"
"QPushButton {color: rgb(120, 10, 10); background:rgb(210, 210, 210);} \n"
"QPushButton:checked{color: rgb(20, 140, 50); background:rgb(50, 50, 50);}\n"
"QPushButton:disabled{color: rgb(70, 70, 70);background-color: rgb(160, 160, 160); border-style: None;}")
        self.instrumentFilterCheckbox.setCheckable(True)
        self.instrumentFilterCheckbox.setObjectName("instrumentFilterCheckbox")
        self.recordButton = QtWidgets.QPushButton(self.centralwidget)
        self.recordButton.setEnabled(True)
        self.recordButton.setGeometry(QtCore.QRect(330, 11, 51, 21))
        self.recordButton.setStyleSheet("QPushButton {background-color: rgb(45, 150, 50);} \n"
"QPushButton:disabled{color: rgb(70, 70, 70);background-color: rgb(160, 160, 160);}\n"
"")
        self.recordButton.setObjectName("recordButton")
        self.lowPassLabel = QtWidgets.QLabel(self.centralwidget)
        self.lowPassLabel.setGeometry(QtCore.QRect(220, 150, 51, 20))
        self.lowPassLabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lowPassLabel.setObjectName("lowPassLabel")
        self.startProcessingButton = QtWidgets.QPushButton(self.centralwidget)
        self.startProcessingButton.setEnabled(True)
        self.startProcessingButton.setGeometry(QtCore.QRect(300, 170, 151, 21))
        self.startProcessingButton.setStyleSheet("QPushButton {color: rgb(0, 0, 0); background-color: rgb(210, 210, 210);} \n"
"QPushButton:disabled{color: rgb(70, 70, 70);background-color: rgb(160, 160, 160);}")
        self.startProcessingButton.setCheckable(False)
        self.startProcessingButton.setAutoDefault(False)
        self.startProcessingButton.setDefault(False)
        self.startProcessingButton.setFlat(False)
        self.startProcessingButton.setObjectName("startProcessingButton")
        self.currentDuration = QtWidgets.QLabel(self.centralwidget)
        self.currentDuration.setGeometry(QtCore.QRect(140, 40, 71, 20))
        self.currentDuration.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.currentDuration.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.currentDuration.setObjectName("currentDuration")
        self.entireDuration = QtWidgets.QLabel(self.centralwidget)
        self.entireDuration.setGeometry(QtCore.QRect(220, 40, 71, 20))
        self.entireDuration.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.entireDuration.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.entireDuration.setWordWrap(False)
        self.entireDuration.setObjectName("entireDuration")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(200, 40, 31, 20))
        self.label_5.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.label_5.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.devicesList = QtWidgets.QComboBox(self.centralwidget)
        self.devicesList.setGeometry(QtCore.QRect(110, 10, 211, 21))
        self.devicesList.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(45, 45, 45);\n"
"selection-background-color: rgb(45, 45, 45);\n"
"\n"
"padding-right: 10px;\n"
"padding-left: 10px;\n"
"padding-top: 5px;\n"
"padding-bottom: 5px;")
        self.devicesList.setObjectName("devicesList")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(20, 11, 91, 21))
        self.label_3.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.stopRecordButton = QtWidgets.QPushButton(self.centralwidget)
        self.stopRecordButton.setEnabled(False)
        self.stopRecordButton.setGeometry(QtCore.QRect(380, 11, 36, 21))
        self.stopRecordButton.setStyleSheet("QPushButton {background-color: rgb(180, 30, 30);} \n"
"QPushButton:disabled{color: rgb(70, 70, 70);background-color: rgb(160, 160, 160);}\n"
"")
        self.stopRecordButton.setObjectName("stopRecordButton")
        self.highPassCurrent = QtWidgets.QLabel(self.centralwidget)
        self.highPassCurrent.setGeometry(QtCore.QRect(160, 170, 51, 20))
        self.highPassCurrent.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.highPassCurrent.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.highPassCurrent.setObjectName("highPassCurrent")
        self.lowPassCurrent = QtWidgets.QLabel(self.centralwidget)
        self.lowPassCurrent.setGeometry(QtCore.QRect(220, 170, 51, 20))
        self.lowPassCurrent.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.lowPassCurrent.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lowPassCurrent.setObjectName("lowPassCurrent")
        self.saveOutputCheckbox = QtWidgets.QPushButton(self.centralwidget)
        self.saveOutputCheckbox.setGeometry(QtCore.QRect(320, 120, 111, 21))
        self.saveOutputCheckbox.setStyleSheet("QPushButton {color:rgb(0, 0, 0);} \n"
"QPushButton {color: rgb(120, 10, 10); background:rgb(210, 210, 210);} \n"
"QPushButton:checked{color: rgb(20, 140, 50); background:rgb(50, 50, 50);}\n"
"QPushButton:disabled{color: rgb(70, 70, 70);background-color: rgb(160, 160, 160); border-style: None;}")
        self.saveOutputCheckbox.setCheckable(True)
        self.saveOutputCheckbox.setObjectName("saveOutputCheckbox")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 480, 21))
        self.menubar.setStyleSheet("QMenuBar::item:selected { background: rgb(50, 50, 50);} QMenuBar::item:pressed {  background: rgb(150, 30, 30);}")
        self.menubar.setObjectName("menubar")
        self.menuAudio_Settings = QtWidgets.QMenu(self.menubar)
        self.menuAudio_Settings.setObjectName("menuAudio_Settings")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionNot_Implemented = QtGui.QAction(MainWindow)
        self.actionNot_Implemented.setObjectName("actionNot_Implemented")
        self.menuAudio_Settings.addAction(self.actionNot_Implemented)
        self.menubar.addAction(self.menuAudio_Settings.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.playButton.setText(_translate("MainWindow", "Play"))
        self.pauseButton.setText(_translate("MainWindow", "Pause"))
        self.highPassLabel.setText(_translate("MainWindow", "High-Pass"))
        self.highPassCheckbox.setText(_translate("MainWindow", "High Pass Filter"))
        self.lowPassCheckbox.setText(_translate("MainWindow", "Low Pass Filter"))
        self.instrumentFilterCheckbox.setText(_translate("MainWindow", "Instrument Filter"))
        self.recordButton.setText(_translate("MainWindow", "Record"))
        self.lowPassLabel.setText(_translate("MainWindow", "Low-Pass"))
        self.startProcessingButton.setText(_translate("MainWindow", "Start Processing"))
        self.currentDuration.setText(_translate("MainWindow", "00:00:00"))
        self.entireDuration.setText(_translate("MainWindow", "00:00:00"))
        self.label_5.setText(_translate("MainWindow", "//"))
        self.label_3.setText(_translate("MainWindow", "Input Device:"))
        self.stopRecordButton.setText(_translate("MainWindow", "Stop"))
        self.highPassCurrent.setText(_translate("MainWindow", "20000"))
        self.lowPassCurrent.setText(_translate("MainWindow", "20000"))
        self.saveOutputCheckbox.setText(_translate("MainWindow", "Save Output File"))
        self.menuAudio_Settings.setTitle(_translate("MainWindow", "Audio Settings"))
        self.actionNot_Implemented.setText(_translate("MainWindow", "Not Implemented"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
