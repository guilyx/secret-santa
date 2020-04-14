import sys
import random
from PySide2 import QtCore, QtWidgets, QtGui


class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.__setWindow()
        self.setMaximumHeight(600)
        self.setMaximumWidth(800)

        self.statusBars = dict()
        self.progressBars = dict()
        self.buttons = dict()
        self.labels = dict()
        self.groupBoxes = dict()
        self.sliders = dict()
        self.entries = dict()

        self.defaultFont = QtGui.QFont('Helvetica', 11, QtGui.QFont.Normal)

        self.__createGroupBox('Secret Santa App', self,
                              fontSize=20, fontOption=QtGui.QFont.Bold)
        self.groupBoxes['Secret Santa App'].setAlignment(
            QtCore.Qt.AlignHCenter)
        self.groupBoxes['Secret Santa App'].setGeometry(20, 20, 760, 560)

        self.__firstMenu()

    def __clearLayout(self, layout):
        for i in reversed(range(layout.count())):
            layout.itemAt(i).widget().setParent(None)

    def __firstMenu(self):
        self.mainLayout = QtWidgets.QVBoxLayout()
        self.mainLayout.setContentsMargins(20, 20, 20, 20)

        self.__createProgressBar('Progress', 3)
        self.__setButtons()
        self.__setSanta()

        introText = "Author : Erwin Lejeune\nDate of Creation : 14/04/2020\nLicense: MIT"
        self.__createLabel(introText, QtCore.Qt.AlignJustify)
        self.labels[introText].setWordWrap(True)

        self.groupBoxes['Secret Santa App'].setLayout(self.mainLayout)
        self.mainLayout.addWidget(self.labels[introText])
        self.mainLayout.addLayout(self.applicationLayout)
        self.mainLayout.addWidget(self.groupBoxes['Options'])
        self.mainLayout.addWidget(self.groupBoxes['Progress'])

        self.buttons['Run'].clicked.connect(self.__run)
        self.buttons['Exit'].clicked.connect(self.__exitUI)
        self.buttons['About'].clicked.connect(self.__aboutBox)

    def __setSanta(self):
        self.applicationLayout = QtWidgets.QHBoxLayout()
        self.__createGroupBox('Gmail IDs', self.groupBoxes['Secret Santa App'])
        self.__createGroupBox('Pool Size', self.groupBoxes['Secret Santa App'])

        self.__createSlider('Pool Size')
        self.__createTextEntry('Gmail IDs')
        self.__createTextEntry(
            'Password', echoMode=QtWidgets.QLineEdit.Password)
            
        self.nparticipantsLayout = QtWidgets.QHBoxLayout()
        self.nparticipantsLayout.addWidget(self.labels['Pool Size'])
        self.nparticipantsLayout.addWidget(self.sliders['Pool Size'])
        self.groupBoxes['Pool Size'].setLayout(self.nparticipantsLayout)

        self.nameEntriesLayout = QtWidgets.QVBoxLayout()
        self.nameEntriesLayout.addWidget(self.entries['Gmail IDs'])
        self.nameEntriesLayout.addWidget(self.entries['Password'])
        self.groupBoxes['Gmail IDs'].setLayout(self.nameEntriesLayout)

        self.applicationLayout.addWidget(self.groupBoxes['Gmail IDs'])
        self.applicationLayout.addWidget(self.groupBoxes['Pool Size'])

    def __run(self):
        if (self.entries['Gmail IDs'].text() is not '') and (self.entries['Password'].text() is not ''):
            QtWidgets.QMessageBox.information(
                self.buttons['Run'], 'Information', 'You can now enter the names and emails of your list.')
        else:
            QtWidgets.QMessageBox.critical(
                self.buttons['Run'], 'Error', 'You need to enter your gmail ids !')

    def __createSlider(self, label):
        self.sliders[label] = QtWidgets.QSlider()
        self.sliders[label].setOrientation(QtCore.Qt.Horizontal)
        self.sliders[label].setTickInterval(1)
        self.sliders[label].setMinimum(3)
        self.sliders[label].setMaximum(100)
        self.labels[label] = QtWidgets.QLabel('3')

        self.sliders[label].valueChanged.connect(self.sliderSignalValue)

    def sliderSignalValue(self):
        size = self.sliders['Pool Size'].value()
        self.labels['Pool Size'].setText(str(size))

    def __createTextEntry(self, label, echoMode=None, maxlength=80):
        self.entries[label] = QtWidgets.QLineEdit()
        self.entries[label].setText(label)
        self.entries[label].setMaxLength(maxlength)
        if echoMode:
            self.entries[label].setEchoMode(echoMode)

    def __setWindow(self):
        self.setWindowTitle('Secret Santapp')
        self.setWindowIcon(QtGui.QIcon('icon.png'))
        self.resize(800, 600)
        self.__centerWindow()

    def __createButton(self, label):
        self.buttons[label] = QtWidgets.QPushButton(label)
        self.buttons[label].setMaximumWidth(120)
        self.buttons[label].setMinimumWidth(80)
        self.buttons[label].setMinimumHeight(40)
        self.buttons[label].setMaximumWidth(50)
        self.buttons[label].setFont(self.defaultFont)

    def __createLabel(self, label, align=None, font='Helvetica', fontSize=11, fontOption=None):
        if align == None:
            self.labels[label] = QtWidgets.QLabel(label)
            if fontOption:
                self.labels[label].setFont(
                    QtGui.QFont(font, fontSize, fontOption))
            else:
                self.labels[label].setFont(QtGui.QFont(
                    font, fontSize, QtGui.QFont.Normal))
        else:
            self.labels[label] = QtWidgets.QLabel(label)
            if fontOption:
                self.labels[label].setFont(
                    QtGui.QFont(font, fontSize, fontOption))
            else:
                self.labels[label].setFont(QtGui.QFont(
                    font, fontSize, QtGui.QFont.Normal))
            self.labels[label].setAlignment(align)

    def __createGroupBox(self, label, parent, font='Helvetica', fontSize=11, fontOption=None):
        self.groupBoxes[label] = QtWidgets.QGroupBox(label, parent)
        if fontOption == None:
            self.groupBoxes[label].setFont(QtGui.QFont(font, fontSize))
        else:
            self.groupBoxes[label].setFont(
                QtGui.QFont(font, fontSize, fontOption))

    def __createProgressBar(self, label, value):
        # Create label
        self.__createGroupBox('Progress', self.groupBoxes['Secret Santa App'])

        progressLayout = QtWidgets.QHBoxLayout()

        # Create Progress Bar widget
        self.progressBars[label] = QtWidgets.QProgressBar()
        self.progressBars[label].setFont(self.defaultFont)
        self.progressBars[label].setMinimum(0)
        self.progressBars[label].setMaximum(100)

        # Attach Progress to new Status
        self.statusBars[label] = QtWidgets.QStatusBar()
        self.progressBars[label].setValue(value)  # function here
        self.statusBars[label].addWidget(self.progressBars[label], 1)

        progressLayout.addWidget(self.statusBars[label])

        self.groupBoxes['Progress'].setLayout(progressLayout)

    def __createStatusBar(self, message, time_ms):
        self.statusBars[message] = QtWidgets.QStatusBar()
        self.statusBars[message].showMessage(message, time_ms)

    def __centerWindow(self):
        qRect = self.frameGeometry()
        centerPoint = QtWidgets.QDesktopWidget().availableGeometry().center()
        qRect.moveCenter(centerPoint)
        self.move(qRect.topLeft())

    def __setButtons(self):
        self.__createGroupBox('Options', self.groupBoxes['Secret Santa App'])
        buttonsLayout = QtWidgets.QHBoxLayout()

        self.__createButton('Run')
        self.__createButton('Exit')
        self.__createButton('About')

        buttonsLayout.addWidget(self.buttons['Run'])
        buttonsLayout.addWidget(self.buttons['About'])
        buttonsLayout.addWidget(self.buttons['Exit'])

        self.groupBoxes['Options'].setLayout(buttonsLayout)

    def __aboutBox(self):
        QtWidgets.QMessageBox.about(self.buttons['About'], "About Secret Santapp",
                                    "Secret Santa is a desktop Gmail IDs running with PySide2 allowing you to create a pool for your Secret Santa !")

    def __exitUI(self):
        userinfo = QtWidgets.QMessageBox.question(
            self, "Confirmation", "Are you sure ?", QtWidgets.QMessageBox.No | QtWidgets.QMessageBox.Yes)
        if userinfo == QtWidgets.QMessageBox.Yes:
            app.quit()
        elif userinfo == QtWidgets.QMessageBox.No:
            pass


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    widget = MyWidget()
    widget.show()

    sys.exit(app.exec_())
