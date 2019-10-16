# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'app.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from canvas import MyMplCanvas, MyNavigationToolbar
from PyQt5.QtWidgets import QApplication

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(941, 553)
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")

        self.myMplCanvas = MyMplCanvas(Dialog)
        self.myMplCanvas.setObjectName(_fromUtf8("matplotlib widget"))
        self.gridLayout.addWidget(self.myMplCanvas, 1, 0, 5, 1)
        self.myNavigationToolbar = MyNavigationToolbar(self.myMplCanvas, self.myMplCanvas)
        self.myNavigationToolbar.setObjectName("navigation toolbar")
        self.gridLayout.addWidget(self.myNavigationToolbar, 6, 0, 1, 1)

        self.groupBox = QtWidgets.QGroupBox(Dialog)
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gxLabel = QtWidgets.QLabel(self.groupBox)
        self.gxLabel.setObjectName("gxLabel")
        self.gridLayout_2.addWidget(self.gxLabel, 0, 0, 1, 1)
        self.rightIntervalSpinBox = QtWidgets.QDoubleSpinBox(self.groupBox)
        self.rightIntervalSpinBox.setMinimum(-999.99)
        self.rightIntervalSpinBox.setMaximum(9999.99)
        self.rightIntervalSpinBox.setProperty("value", 3.0)
        self.rightIntervalSpinBox.setObjectName("rightIntervalSpinBox")
        self.gridLayout_2.addWidget(self.rightIntervalSpinBox, 2, 3, 1, 1)
        self.xyCheckBox = QtWidgets.QCheckBox(self.groupBox)
        self.xyCheckBox.setChecked(True)
        self.xyCheckBox.setObjectName("xyCheckBox")
        self.gridLayout_2.addWidget(self.xyCheckBox, 3, 0, 1, 2)
        self.leftIntervalSpinBox = QtWidgets.QDoubleSpinBox(self.groupBox)
        self.leftIntervalSpinBox.setMinimum(-999.99)
        self.leftIntervalSpinBox.setMaximum(9999.99)
        self.leftIntervalSpinBox.setProperty("value", 1.0)
        self.leftIntervalSpinBox.setObjectName("leftIntervalSpinBox")
        self.gridLayout_2.addWidget(self.leftIntervalSpinBox, 2, 1, 1, 1)
        self.delaySpinBox = QtWidgets.QDoubleSpinBox(self.groupBox)
        self.delaySpinBox.setProperty("value", 0.5)
        self.delaySpinBox.setObjectName("delaySpinBox")
        self.gridLayout_2.addWidget(self.delaySpinBox, 5, 1, 1, 1)
        self.itLabel = QtWidgets.QLabel(self.groupBox)
        self.itLabel.setObjectName("itLabel")
        self.gridLayout_2.addWidget(self.itLabel, 4, 0, 1, 1)
        self.delayLabel = QtWidgets.QLabel(self.groupBox)
        self.delayLabel.setObjectName("delayLabel")
        self.gridLayout_2.addWidget(self.delayLabel, 5, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 2, 0, 1, 1)
        self.x0DoubleSpinBox = QtWidgets.QDoubleSpinBox(self.groupBox)
        self.x0DoubleSpinBox.setDecimals(2)
        self.x0DoubleSpinBox.setMinimum(-100000000000.0)
        self.x0DoubleSpinBox.setMaximum(99999999999.99)
        self.x0DoubleSpinBox.setProperty("value", 2.0)
        self.x0DoubleSpinBox.setObjectName("x0DoubleSpinBox")
        self.gridLayout_2.addWidget(self.x0DoubleSpinBox, 1, 1, 1, 3)
        self.functionEdit = QtWidgets.QLineEdit(self.groupBox)
        self.functionEdit.setObjectName("functionEdit")
        self.gridLayout_2.addWidget(self.functionEdit, 0, 1, 1, 3)
        self.iterationSpinBox = QtWidgets.QSpinBox(self.groupBox)
        self.iterationSpinBox.setMinimum(1)
        self.iterationSpinBox.setValue(3)
        self.iterationSpinBox.setMaximum(999999)
        self.iterationSpinBox.setObjectName("iteartionSpinBox")
        self.gridLayout_2.addWidget(self.iterationSpinBox, 4, 1, 1, 1)
        self.x0Label = QtWidgets.QLabel(self.groupBox)
        self.x0Label.setObjectName("x0Label")
        self.gridLayout_2.addWidget(self.x0Label, 1, 0, 1, 1)
        self.startPushButton = QtWidgets.QPushButton(self.groupBox)
        self.startPushButton.setObjectName("startPushButton")
        self.gridLayout_2.addWidget(self.startPushButton, 8, 0, 1, 2)
        self.drawPushButton = QtWidgets.QPushButton(self.groupBox)
        self.drawPushButton.setObjectName("drawPushButton")
        self.gridLayout_2.addWidget(self.drawPushButton, 9, 3, 1, 1)
        self.stepPushButton = QtWidgets.QPushButton(self.groupBox)
        self.stepPushButton.setObjectName("stepPushButton")
        self.gridLayout_2.addWidget(self.stepPushButton, 8, 3, 1, 1)
        self.stopPushButton = QtWidgets.QPushButton(self.groupBox)
        self.stopPushButton.setObjectName("stopPushButton")
        self.gridLayout_2.addWidget(self.stopPushButton, 9, 0, 1, 2)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem, 10, 0, 1, 1)
        self.xValueLabel = QtWidgets.QLabel(self.groupBox)
        self.xValueLabel.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.xValueLabel, 11, 0, 1, 4)
        self.gridLayout.addWidget(self.groupBox, 2, 2, 3, 1, QtCore.Qt.AlignTop)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        Dialog.setTabOrder(self.functionEdit, self.x0DoubleSpinBox)
        Dialog.setTabOrder(self.x0DoubleSpinBox, self.leftIntervalSpinBox)
        Dialog.setTabOrder(self.leftIntervalSpinBox, self.rightIntervalSpinBox)
        Dialog.setTabOrder(self.rightIntervalSpinBox, self.xyCheckBox)
        Dialog.setTabOrder(self.xyCheckBox, self.iterationSpinBox)
        Dialog.setTabOrder(self.iterationSpinBox, self.delaySpinBox)
        Dialog.setTabOrder(self.delaySpinBox, self.startPushButton)
        Dialog.setTabOrder(self.startPushButton, self.stepPushButton)
        Dialog.setTabOrder(self.stepPushButton, self.stopPushButton)
        Dialog.setTabOrder(self.stopPushButton, self.drawPushButton)
        Dialog.setTabOrder(self.drawPushButton, self.myNavigationToolbar)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Fixed point method visualization"))
        self.gxLabel.setText(_translate("Dialog", "g(x)="))
        self.xyCheckBox.setText(_translate("Dialog", "Show x = y"))
        self.itLabel.setText(_translate("Dialog", "Max iterations"))
        self.delayLabel.setText(_translate("Dialog", "Delay"))
        self.label.setText(_translate("Dialog", "I ="))
        self.functionEdit.setText(_translate("Dialog", "x -( (x ** 2 - 3)/2)"))
        self.x0Label.setText(_translate("Dialog", "x0"))
        self.startPushButton.setText(_translate("Dialog", "Start"))
        self.drawPushButton.setText(_translate("Dialog", "Draw"))
        self.stepPushButton.setText(_translate("Dialog", "Step"))
        self.stopPushButton.setText(_translate("Dialog", "Stop"))
        self.xValueLabel.setText(_translate("Dialog", "Current value of x is:"))


# use this only for 'resarch'
if __name__ == '__main__':
    from PyQt5.QtWidgets import QApplication, QWidget
    import sys
    app = QApplication(sys.argv)
    ex = Ui_Dialog()
    ex.show()
    sys.exit(app.exec_())
