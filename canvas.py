# -*- coding: utf-8 -*-

import PyQt5
from PyQt5 import QtGui, QtCore, QtWidgets
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5 import NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure
from matplotlib.widgets import SpanSelector

from numpy import arange

fluid_lims=False #can change vertical limits interactively?

def alert(self,text,title="Calib. util.",loud=False):
    if loud:
        mess=QtCore.QT_TR_NOOP(text)
        QtGui.QMessageBox.information(self, self.tr(title), mess)
    else:
        print(text)

def extend_alert(self,text,title="Results",extras=[],details=[]):
    box=QtGui.QMessageBox(QtGui.QMessageBox.Information,title,text)
    if len(extras) > 0: box.setInformativeText("\n".join(extras))
    if len(details) > 0: box.setDetailedText("\n".join(details))
    box.exec_()
    return box

#--------------------------------------------

class MyMplCanvas(FigureCanvas):
    """Ultimately, this is a QWidget (as well as a FigureCanvasAgg, etc.)."""
    def compute_initial_figure(self):
        return
    
    def __init__(self, parent=None, width=6, height=4, dpi=100, polar=False):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111,polar=polar)
        self.compute_initial_figure()
        FigureCanvas.__init__(self, fig)
        #try:
            #self.setParent(parent)
            #FigureCanvas.setSizePolicy(self,
            #        QtGui.QSizePolicy.Expanding,
            #        QtGui.QSizePolicy.Expanding)
            #FigureCanvas.updateGeometry(self)
        #except:
        #    print("simple graphics - beware")
        self.figure.subplots_adjust(left=0.08,right=0.96)

    def clear(self,reset=True):
        self.figure.clf()
        if reset:
            self.axes=self.figure.gca()
            self.draw()
            
    def change_sizes(self,labsize=8):
        '''modify font sizes'''
        self.axes.xaxis.label.set_fontsize(labsize)
        for lab in self.axes.xaxis.get_ticklabels():
            lab.set_fontsize(labsize)
        self.axes.yaxis.label.set_fontsize(labsize)
        for lab in self.axes.yaxis.get_ticklabels():
            lab.set_fontsize(labsize)

            
class MyNavigationToolbar(NavigationToolbar) :
    span=None
    hZoom=True
    
    def __init__(self , canvas , parent , direction = 'h' ) :
        self.canvas = canvas
        QtWidgets.QWidget.__init__( self, parent )

        if direction=='h' :    self.layout = PyQt5.QtWidgets.QHBoxLayout
        else : self.layout = PyQt5.QtWidgets.QVBoxLayout
        NavigationToolbar.__init__( self, canvas, parent )
        
    def zoomToggle(self):
        #self.toolbar.zoom() #this implements the classic zoom
        if self.hZoom:
            self.hZoom = False
            if self.span: self.span.visible = False
        else:
            self.hZoom = True
            if self.span: self.span.visible = True


def checkItem(text,confunc,context,init=False):
    '''creating a checkbox with annotation
    '''
    ch_wid=QtGui.QCheckBox(context.tr(text))
    context.connect(ch_wid, QtCore.SIGNAL("clicked()"), confunc)
    mee_box=QtGui.QWidgetAction(context)
    mee_box.setDefaultWidget(ch_wid)
    ch_wid.setChecked(init)
    return mee_box

