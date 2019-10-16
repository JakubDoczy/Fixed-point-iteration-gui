import sys
from PyQt5.QtWidgets import QDialog, QApplication, QMessageBox
from PyQt5 import QtCore, QtTest
from PyQt5.Qt import QMutex
from frontend import Ui_Dialog

import numpy as np


class AppWindow(QDialog):
    @staticmethod
    def error_window(txt='Unknown Error!'):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Critical)
        msg.setText("Error")
        msg.setInformativeText(txt)
        msg.setWindowTitle("Error")
        msg.exec_()

    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.canvasMutex = QMutex()  # protects canvas (probably redundant since I don't use workers)
        self.timer = QtCore.QTimer()

        self.timer.timeout.connect(self.draw_step)

        # connect actions
        self.ui.drawPushButton.clicked.connect(self.redraw_background)
        self.ui.startPushButton.clicked.connect(self.start_presentation)
        self.ui.stopPushButton.clicked.connect(self.timer.stop)
        self.ui.stepPushButton.clicked.connect(self.on_step_pushed)
        self.ui.functionEdit.textChanged.connect(self.set_redraw_needed)
        self.ui.x0DoubleSpinBox.valueChanged.connect(self.set_redraw_needed)
        self.ui.leftIntervalSpinBox.valueChanged.connect(self.set_redraw_needed)
        self.ui.rightIntervalSpinBox.valueChanged.connect(self.set_redraw_needed)
        self.ui.xyCheckBox.clicked.connect(self.set_redraw_needed)

        self.eps = 1e-15
        self.itTBD = 0
        self.xx = None  # x axes - linspace from left
        self.gx = None  # lambda function g(x)
        self.xc = None  # current value of x
        self.redraw = True  # indicates that old values are no longer valid!

        self.show()

    def set_redraw_needed(self):
        self.redraw = True

    def start_presentation(self):
        if not self.redraw_background():
            return

        self.itTBD = self.ui.iterationSpinBox.value()
        self.timer.start(int(self.ui.delaySpinBox.value() * 1000))

    def on_step_pushed(self):
        if self.redraw and not self.redraw_background():
            return

        self.itTBD = 1
        self.draw_step()

    # should only be called by draw_step()
    def reset_drawing(self):
        self.timer.stop()
        self.itTBD = 0
        self.canvasMutex.unlock()

    # draws one iteration on graph
    def draw_step(self):
        if self.canvasMutex.tryLock():
            if self.itTBD < 1:
                self.reset_drawing()
                return

            nxc = self.gx(self.xc)  # value of g(x_{n+1})

            if abs(self.xc - nxc) < self.eps:
                print('I am unable to reach better precision so I\'ll stop.')
                self.reset_drawing()
                return

            if nxc < self.ui.leftIntervalSpinBox.value() or nxc > self.ui.rightIntervalSpinBox.value():
                self.error_window('Out of interval!')
                self.reset_drawing()
                return

            # self.gx(nxc) may reach value out of interval but only on y-axis
            # I could also remember its value so I don't have to compute it in next iteration
            # but it is so cheap that I don't care
            self.ui.myMplCanvas.axes.plot([self.xc, nxc, nxc], [nxc, nxc, self.gx(nxc)], r'r--', linewidth=0.75)
            self.ui.myMplCanvas.draw()

            self.xc = nxc
            self.itTBD -= 1
            self.ui.xValueLabel.setText('Current value of x is: %.6f' % self.xc)
            self.canvasMutex.unlock()

    def redraw_background(self):
        self.gx = lambda x: eval(self.ui.functionEdit.text())
        self.xc = self.ui.x0DoubleSpinBox.value()
        li = self.ui.leftIntervalSpinBox.value()
        ri = self.ui.rightIntervalSpinBox.value()

        if li >= ri or self.xc < li or self.xc > ri:
            self.error_window('Invalid interval!')
            return False

        self.xx = np.linspace(self.ui.leftIntervalSpinBox.value(), self.ui.rightIntervalSpinBox.value(), 10000)

        try:
            yy = self.gx(self.xx)
        except SyntaxError:
            self.error_window('Unable to parse g(x)!')
            return False

        if self.canvasMutex.tryLock():
            self.ui.myMplCanvas.clear()
            self.ui.myMplCanvas.axes.plot(self.xx, yy, label='g(x)')

            if self.ui.xyCheckBox.isChecked():
                self.ui.myMplCanvas.axes.plot(self.xx, self.xx, label='y = x')

            self.ui.myMplCanvas.draw()
            self.redraw = False
            self.canvasMutex.unlock()

        return True


# main!
if __name__ == '__main__':
    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)
    app = QApplication(sys.argv)
    w = AppWindow()
    w.show()
    sys.exit(app.exec_())
