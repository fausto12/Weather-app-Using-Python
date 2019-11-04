# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Updated_weather.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import requests

API = ""


class Ui_Weather(object):
    def setupUi(self, Weather):
        Weather.setObjectName("Weather")
        Weather.resize(800, 600)
        Weather.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        Weather.setFocusPolicy(QtCore.Qt.ClickFocus)
        Weather.setWindowTitle("Weather")
        Weather.setAutoFillBackground(False)
        Weather.setStyleSheet("QMainWindow#MainWindow {\n"
                              "    \n"
                              "    \n"
                              "    background-color: white;\n"
                              "}")
        Weather.setWindowFilePath("")
        Weather.setAnimated(False)
        Weather.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.centralwidget = QtWidgets.QWidget(Weather)
        self.centralwidget.setObjectName("centralwidget")
        self.zipcodeInput = QtWidgets.QLineEdit(self.centralwidget)
        self.zipcodeInput.setGeometry(QtCore.QRect(290, 30, 211, 51))
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.zipcodeInput.sizePolicy().hasHeightForWidth())
        self.zipcodeInput.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("MS UI Gothic")
        font.setPointSize(16)
        self.zipcodeInput.setFont(font)
        self.zipcodeInput.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.zipcodeInput.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.zipcodeInput.setToolTip("")
        self.zipcodeInput.setStatusTip("")
        self.zipcodeInput.setWhatsThis("")
        self.zipcodeInput.setAccessibleName("")
        self.zipcodeInput.setAccessibleDescription("")
        self.zipcodeInput.setStyleSheet("QLineEdit#zipcodeInput {\n"
                                        "    background:transparent;\n"
                                        "    border: 1px solid black;\n"
                                        "    border-radius: 20px;\n"
                                        "}")
        self.zipcodeInput.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.zipcodeInput.setInputMask("")
        self.zipcodeInput.setText("")
        self.zipcodeInput.setMaxLength(5)
        self.zipcodeInput.setFrame(False)
        self.zipcodeInput.setAlignment(QtCore.Qt.AlignCenter)
        self.zipcodeInput.setPlaceholderText("Zip Code...")
        self.zipcodeInput.setObjectName("zipcodeInput")
        self.weatherImage = QtWidgets.QLabel(self.centralwidget)
        self.weatherImage.setGeometry(QtCore.QRect(60, 120, 301, 271))
        self.weatherImage.setToolTip("")
        self.weatherImage.setText("")
        self.weatherImage.setPixmap(QtGui.QPixmap(
            "weather_images/rain.png"))
        self.weatherImage.setScaledContents(True)
        self.weatherImage.setObjectName("weatherImage")
        self.cityDisplay = QtWidgets.QLineEdit(self.centralwidget)
        self.cityDisplay.setGeometry(QtCore.QRect(470, 110, 291, 71))
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.cityDisplay.sizePolicy().hasHeightForWidth())
        self.cityDisplay.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.cityDisplay.setFont(font)
        self.cityDisplay.setCursor(QtGui.QCursor(QtCore.Qt.CrossCursor))
        self.cityDisplay.setToolTip("")
        self.cityDisplay.setStatusTip("")
        self.cityDisplay.setWhatsThis("")
        self.cityDisplay.setAccessibleName("")
        self.cityDisplay.setAccessibleDescription("")
        self.cityDisplay.setStyleSheet("QLineEdit#cityDisplay {\n"
                                       "    \n"
                                       "    background:transparent;\n"
                                       "\n"
                                       "}")
        self.cityDisplay.setInputMask("")
        self.cityDisplay.setText("")
        self.cityDisplay.setFrame(False)
        self.cityDisplay.setAlignment(QtCore.Qt.AlignCenter)
        self.cityDisplay.setReadOnly(True)
        self.cityDisplay.setPlaceholderText("")
        self.cityDisplay.setObjectName("cityDisplay")
        self.descriptionDisplay = QtWidgets.QLineEdit(self.centralwidget)
        self.descriptionDisplay.setGeometry(QtCore.QRect(470, 220, 291, 51))
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.descriptionDisplay.sizePolicy().hasHeightForWidth())
        self.descriptionDisplay.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("MS UI Gothic")
        font.setPointSize(14)
        self.descriptionDisplay.setFont(font)
        self.descriptionDisplay.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.descriptionDisplay.setToolTip("")
        self.descriptionDisplay.setStatusTip("")
        self.descriptionDisplay.setWhatsThis("")
        self.descriptionDisplay.setAccessibleName("")
        self.descriptionDisplay.setAccessibleDescription("")
        self.descriptionDisplay.setStyleSheet("QLineEdit#descriptionDisplay{\n"
                                              "    border:none;\n"
                                              "    background:transparent;\n"
                                              "}")
        self.descriptionDisplay.setInputMask("")
        self.descriptionDisplay.setText("")
        self.descriptionDisplay.setFrame(False)
        self.descriptionDisplay.setAlignment(QtCore.Qt.AlignCenter)
        self.descriptionDisplay.setReadOnly(True)
        self.descriptionDisplay.setPlaceholderText("")
        self.descriptionDisplay.setObjectName("descriptionDisplay")
        self.tempDisplay = QtWidgets.QLineEdit(self.centralwidget)
        self.tempDisplay.setGeometry(QtCore.QRect(470, 300, 291, 51))
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.tempDisplay.sizePolicy().hasHeightForWidth())
        self.tempDisplay.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("MS UI Gothic")
        font.setPointSize(14)
        self.tempDisplay.setFont(font)
        self.tempDisplay.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.tempDisplay.setToolTip("")
        self.tempDisplay.setStatusTip("")
        self.tempDisplay.setWhatsThis("")
        self.tempDisplay.setAccessibleName("")
        self.tempDisplay.setAccessibleDescription("")
        self.tempDisplay.setStyleSheet("QLineEdit#tempDisplay{\n"
                                       "     background:transparent;\n"
                                       "}")
        self.tempDisplay.setInputMask("")
        self.tempDisplay.setText("")
        self.tempDisplay.setFrame(False)
        self.tempDisplay.setAlignment(QtCore.Qt.AlignCenter)
        self.tempDisplay.setReadOnly(True)
        self.tempDisplay.setPlaceholderText("")
        self.tempDisplay.setObjectName("tempDisplay")
        Weather.setCentralWidget(self.centralwidget)

        self.retranslateUi(Weather)
        QtCore.QMetaObject.connectSlotsByName(Weather)
        # gets the user input when the "Enter" key is pressed.
        self.zipcodeInput.returnPressed.connect(self.getInput)

    def retranslateUi(self, Weather):
        pass

    def getInput(self):
        zipcodeValue = self.zipcodeInput.text()
        API = "bec728d68fa54dd3a813df9e47d550a3"
        url = "http://api.openweathermap.org/data/2.5/weather?zip={},us&appid={}&units=imperial".format(
            zipcodeValue, API)
        res = requests.get(url)

        data = res.json()

        city = data['name']
        description = data['weather'][0]['description']
        temperature = data['main']['temp']

        self.cityDisplay.setText(city)
        self.descriptionDisplay.setText(description)
        self.tempDisplay.setText(str(temperature))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Weather = QtWidgets.QMainWindow()
    ui = Ui_Weather()
    ui.setupUi(Weather)
    Weather.show()
    sys.exit(app.exec_())
