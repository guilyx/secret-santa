import sys
import random
import time
from PySide2 import QtCore, QtWidgets, QtGui
from lib.santa_gen import Santa


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
        self.list = dict()
        self.layouts = []

        self.firstMenuParsed = False
        self.secondMenuParsed = False

        self.defaultFont = QtGui.QFont('Helvetica', 11, QtGui.QFont.Normal)

        self.__createGroupBox('Secret Santa App', self,
                              fontSize=20, fontOption=QtGui.QFont.Bold)
        self.groupBoxes['Secret Santa App'].setAlignment(
            QtCore.Qt.AlignHCenter)
        self.groupBoxes['Secret Santa App'].setGeometry(20, 20, 760, 560)

        self.__firstMenu()

    def __clearLayout(self, layout):
        for i in reversed(range(layout.count())):
            if layout.itemAt(i).widget() == None:
                continue
            else:
                layout.itemAt(i).widget().setParent(None)

    def __firstMenu(self):
        self.mainLayout = QtWidgets.QVBoxLayout(self)
        self.mainLayout.setContentsMargins(20, 20, 20, 20)

        self.__createProgressBar('Progress', 3)
        self.__setButtons()
        self.__setSanta()

        self.introText = "Author : Erwin Lejeune\nDate of Creation : 14/04/2020\nLicense: MIT"
        self.__createLabel(self.introText, QtCore.Qt.AlignJustify)
        self.labels[self.introText].setWordWrap(True)

        self.groupBoxes['Secret Santa App'].setLayout(self.mainLayout)

        self.mainLayout.addWidget(self.labels[self.introText])
        self.mainLayout.addLayout(self.applicationLayout)
        self.mainLayout.addWidget(self.groupBoxes['Options'])
        self.mainLayout.addWidget(self.groupBoxes['Progress'])

        self.buttons['Next'].clicked.connect(self.__run)
        self.buttons['Exit'].clicked.connect(self.__exitUI)
        self.buttons['About'].clicked.connect(self.__aboutBox)

        self.firstMenuParsed = True
    
    def __backToFirstMenu(self):
        self.__clearLayout(self.mainLayout)
        
        self.__clearLayout(self.applicationLayout)
        self.__clearLayout(self.buttonsLayout)
        self.__clearLayout(self.nameEntriesLayout)
        self.__clearLayout(self.nparticipantsLayout)
        self.__clearLayout(self.progressLayout)
    
        self.__firstMenu()

    def __setSanta(self):
        self.applicationLayout = QtWidgets.QHBoxLayout()
        self.layouts.append(self.applicationLayout)

        self.__createGroupBox('Gmail IDs', self.groupBoxes['Secret Santa App'])
        self.__createGroupBox('Pool Size', self.groupBoxes['Secret Santa App'])

        self.__createSlider('Pool Size')
        self.__createTextEntry('Gmail IDs')
        self.__createTextEntry(
            'Password', echoMode=QtWidgets.QLineEdit.Password)

        self.entryInit = [self.entries['Gmail IDs'].text(),
                          self.entries['Password'].text()]

        self.nparticipantsLayout = QtWidgets.QHBoxLayout()
        self.layouts.append(self.nparticipantsLayout)
        self.nparticipantsLayout.addWidget(self.labels['Pool Size'])
        self.nparticipantsLayout.addWidget(self.sliders['Pool Size'])
        self.groupBoxes['Pool Size'].setLayout(self.nparticipantsLayout)

        self.nameEntriesLayout = QtWidgets.QVBoxLayout()
        self.nameEntriesLayout.addWidget(self.entries['Gmail IDs'])
        self.nameEntriesLayout.addWidget(self.entries['Password'])
        self.groupBoxes['Gmail IDs'].setLayout(self.nameEntriesLayout)

        self.applicationLayout.addWidget(self.groupBoxes['Gmail IDs'])
        self.applicationLayout.addWidget(self.groupBoxes['Pool Size'])

        self.secondMenuParsed = True

    def __run(self):
        if (self.entries['Gmail IDs'].text() == '') or (self.entries['Password'].text() == ''):
            QtWidgets.QMessageBox.critical(
                self.buttons['Next'], 'Error', 'You need to enter your gmail ids !')

        elif (self.entries['Gmail IDs'].text() == self.entryInit[0]) or (self.entries['Password'].text() == self.entryInit[1]):
            QtWidgets.QMessageBox.critical(
                self.buttons['Next'], 'Error', 'You need to enter your gmail ids !')

        else:
            self.buttons['Back'].setEnabled(True)
            self.buttons['Back'].clicked.connect(self.__backToFirstMenu)
            self.gmailId = self.entries['Gmail IDs'].text()
            self.gmailPwd = self.entries['Password'].text()

            QtWidgets.QMessageBox.information(
                self.buttons['Next'], 'Information', 'You can now enter the names and emails of your list.')

            self.nparticipants = self.sliders['Pool Size'].value()

            self.__clearLayout(self.applicationLayout)
            self.__clearLayout(self.nparticipantsLayout)
            self.__clearLayout(self.nameEntriesLayout)

            for o in range(10):
                self.progressBars['Progress'].setValue(
                    self.progressBars['Progress'].value() + random.randint(1, 3))
                time.sleep(0.1)
            self.poolSize = self.sliders['Pool Size'].value()
            self.__layoutSantaList()

    def __layoutSantaList(self):
        self.buttons['Next'].clicked.disconnect()
        self.__createGroupBox('Pool Identifiers',
                              self.groupBoxes['Secret Santa App'])
        self.idLayout = QtWidgets.QGridLayout()

        for i in range(self.poolSize):
            self.__createTextEntry('Name' + str(i))
            self.__createTextEntry('Email' + str(i))
            self.idLayout.addWidget(self.entries['Name' + str(i)], i, 0)
            self.idLayout.addWidget(self.entries['Email' + str(i)], i, 1)

        self.groupBoxes['Pool Identifiers'].setLayout(self.idLayout)
        self.__clearLayout(self.mainLayout)

        self.scrollArea = QtWidgets.QScrollArea()
        #self.scrollArea.setFixedWidth(560)
        self.scrollArea.setWidgetResizable(True)
        #self.scrollArea.setBackgroundRole(QtGui.QPalette.Dark)
        self.scrollArea.setWidget(self.groupBoxes['Pool Identifiers'])

        self.mainLayout.addWidget(self.labels[self.introText])
        #self.mainLayout.addWidget(self.groupBoxes['Pool Identifiers'])
        self.mainLayout.addWidget(self.scrollArea)
        self.buttons['Next'].setText('Run')
        self.buttons['Run'] = self.buttons['Next']
        self.buttons.pop('Next')
        self.mainLayout.addWidget(self.groupBoxes['Options'])
        self.mainLayout.addWidget(self.groupBoxes['Progress'])

        self.buttons['Run'].clicked.connect(self.__generatePool)

    def __generatePool(self):
        self.secretNames = []
        self.secretEmails = dict()
        for i in range(self.nparticipants):
            name = self.entries['Name' + str(i)].text()
            self.secretNames.append(name)
            self.secretEmails[name] = self.entries['Email' + str(i)].text()

        secretSanta = Santa(self.gmailId, self.gmailPwd)

        self.labels['Progress'].setText('Generating random pool...')
        for o in range(10):
            self.progressBars['Progress'].setValue(
                self.progressBars['Progress'].value() + random.randint(1, 3))
            time.sleep(0.1)

        secretSanta.set_number(self.nparticipants)
        secretSanta.set_names(self.secretNames)
        secretSanta.set_emails(self.secretEmails)
        secretSanta.gen_secrets()

        self.labels['Progress'].setText('Sending Emails...')

        for o in range(10):
            self.progressBars['Progress'].setValue(
                self.progressBars['Progress'].value() + random.randint(1, 3))
            time.sleep(0.1)

        secretSanta.send_emails()
        timestamp = time.time()
        secretSanta.flush_emails()

        self.labels['Progress'].setText('Flushing proofs...')

        for o in range(10):
            self.progressBars['Progress'].setValue(
                self.progressBars['Progress'].value() + random.randint(1, 3))
            time.sleep(0.01)

        self.gmailId = None
        self.gmailPwd = None

        self.labels['Progress'].setText('Exiting cleanly...')

        for o in range(10):
            self.progressBars['Progress'].setValue(
                self.progressBars['Progress'].value() + random.randint(1, 3))
            time.sleep(0.01)

        while time.time() - timestamp < 10:
            pass

        self.labels['Progress'].setText('Complete !')

    def __createSlider(self, label):
        self.sliders[label] = QtWidgets.QSlider()
        self.sliders[label].setOrientation(QtCore.Qt.Horizontal)
        self.sliders[label].setTickInterval(1)
        self.sliders[label].setMinimum(3)
        self.sliders[label].setMaximum(30)
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
        self.setWindowIcon(QtGui.QIcon('../res/icon.png'))
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

        self.progressLayout = QtWidgets.QHBoxLayout()

        # Create Progress Bar widget
        self.progressBars[label] = QtWidgets.QProgressBar()
        self.progressBars[label].setFont(self.defaultFont)
        self.progressBars[label].setMinimum(0)
        self.progressBars[label].setMaximum(100)

        # Create label
        self.labels[label] = QtWidgets.QLabel('Configuration...')

        # Attach Progress to new Status
        self.statusBars[label] = QtWidgets.QStatusBar()
        self.progressBars[label].setValue(value)  # function here
        self.statusBars[label].addWidget(self.labels[label], 1)
        self.statusBars[label].addWidget(self.progressBars[label], 2)

        self.progressLayout.addWidget(self.statusBars[label])

        self.groupBoxes['Progress'].setLayout(self.progressLayout)

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
        self.buttonsLayout = QtWidgets.QHBoxLayout()

        self.__createButton('Next')
        self.__createButton('Back')
        self.__createButton('Exit')
        self.__createButton('About')

        self.buttons['Next'].autoDefault()
        self.buttons['Back'].setEnabled(False)
        self.buttonsLayout.addWidget(self.buttons['Next'])
        self.buttonsLayout.addWidget(self.buttons['Back'])
        self.buttonsLayout.addWidget(self.buttons['About'])
        self.buttonsLayout.addWidget(self.buttons['Exit'])

        self.groupBoxes['Options'].setLayout(self.buttonsLayout)

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



app = QtWidgets.QApplication([])
widget = MyWidget()
widget.show()
sys.exit(app.exec_())
