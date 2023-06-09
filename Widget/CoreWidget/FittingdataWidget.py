import PyQt5.QtWidgets as QtWidgets
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import *
from Utilities.Helper import settings
from PyQt5 import QtGui
from PyQt5.QtCore import *



class FittingdataWidget(QWidget):

    """
    This class is a TextEdit with a few extra features,
    can be integrated into LabGui as a message box,which
    can be use for warning and display calculate result
    """

    fitting_jud = pyqtSignal(object)


    def __init__(self, parent=None):
        super(FittingdataWidget, self).__init__(parent)

        self.Fitting = QCheckBox('Gaussian Fitting',self)
        self.Fitting.stateChanged.connect(lambda: self.change_cal(self.Fitting))

        self.fLayout = QtWidgets.QVBoxLayout()
        self.fLayout.addWidget(self.Fitting)
        # self.fLayout.setStretchFactor(self.flurence, 2)


        self.Layout1 = QtWidgets.QHBoxLayout()
        self.label1 = QtWidgets.QLabel('HAmpli')
        # self.label1.setFont(QFont("Roman times", 9))
        self.slabel1 = QtWidgets.QLabel(str('NA'))
        # self.slabel1.setFont(QFont("Roman times", 9))
        self.Layout1.addWidget(self.label1)
        self.Layout1.addWidget(self.slabel1)


        self.Layout2 = QtWidgets.QHBoxLayout()
        self.label2 = QtWidgets.QLabel('Hpos')
        # self.label2.setFont(QFont("Roman times", 9))
        self.slabel2 = QtWidgets.QLabel(str('NA'))
        # self.slabel2.setFont(QFont("Roman times", 9))
        self.Layout2.addWidget(self.label2)
        self.Layout2.addWidget(self.slabel2)
        
        self.Layout3 = QtWidgets.QHBoxLayout()
        self.label3 = QtWidgets.QLabel('HWaist')
        # self.label3.setFont(QFont("Roman times", 9))
        self.slabel3 = QtWidgets.QLabel(str('NA'))
        # self.slabel3.setFont(QFont("Roman times", 9))
        self.Layout3.addWidget(self.label3)
        self.Layout3.addWidget(self.slabel3)

        self.Layout4 = QtWidgets.QHBoxLayout()
        self.label4 = QtWidgets.QLabel('VAmpli')
        # self.label4.setFont(QFont("Roman times", 9))
        self.slabel4 = QtWidgets.QLabel(str('NA'))
        # self.slabel4.setFont(QFont("Roman times", 9))
        self.Layout4.addWidget(self.label4)
        self.Layout4.addWidget(self.slabel4)

        self.Layout5 = QtWidgets.QHBoxLayout()
        self.label5 = QtWidgets.QLabel('Vpos')
        # self.label5.setFont(QFont("Roman times", 9))
        self.slabel5 = QtWidgets.QLabel(str('NA'))
        # self.slabel5.setFont(QFont("Roman times", 9))
        self.Layout5.addWidget(self.label5)
        self.Layout5.addWidget(self.slabel5)

        self.Layout6 = QtWidgets.QHBoxLayout()
        self.label6 = QtWidgets.QLabel('VWaist')
        # self.label6.setFont(QFont("Roman times", 9))
        self.slabel6 = QtWidgets.QLabel(str('NA'))
        # self.slabel6.setFont(QFont("Roman times", 9))
        self.Layout6.addWidget(self.label6)
        self.Layout6.addWidget(self.slabel6)

        self.Layout7 = QtWidgets.QHBoxLayout()
        self.label7 = QtWidgets.QLabel('#(Fitting)')
        # self.label7.setFont(QFont("Roman times", 9))
        self.slabel7 = QtWidgets.QLabel(str('NA'))
        # self.slabel7.setFont(QFont("Roman times", 9))
        self.Layout7.addWidget(self.label7)
        self.Layout7.addWidget(self.slabel7)

        self.fLayout.addLayout(self.Layout1)
        self.fLayout.addLayout(self.Layout2)
        self.fLayout.addLayout(self.Layout3)
        self.fLayout.addLayout(self.Layout4)
        self.fLayout.addLayout(self.Layout5)
        self.fLayout.addLayout(self.Layout6)
        self.fLayout.addLayout(self.Layout7)
        self.setLayout(self.fLayout)
        self.setFont(QFont("Roman times", 10))

        screen = QtGui.QDesktopWidget().screenGeometry()
        self.setFixedWidth(screen.width()*13/100)

    def change_cal(self,mode):
        if mode.isChecked():
            if settings.widget_params["Analyse Data Setting"]["roiStatus"]:
                settings.widget_params["Fitting Setting"]["mode"] = 1
                self.fitting_jud.emit(1)
            else:
                mode.setCheckState(0)
                print("please add roi first.")
        else:
            # if settings.widget_params["Analyse Data Setting"]["roiStatus"]:
            settings.widget_params["Fitting Setting"]["mode"] = 0
            self.fitting_jud.emit(1)
                # mode.setCheckState(0)
                # print("please add roi first.")

    def change_label(self, dict):
        self.slabel1.setText(str('%.2f' % abs(dict['data1'])))
        self.slabel2.setText(str('%.1f' % abs(dict['data2']))+'px')
        self.slabel3.setText(str('%.1f' % abs(dict['data3']))+'px/'+str('%.1f'% abs(dict['data8']))+'mm')
        self.slabel4.setText(str('%.2f' % abs(dict['data4'])))
        self.slabel5.setText(str('%.1f' % abs(dict['data5']))+'px')
        self.slabel6.setText(str('%.1f' % abs(dict['data6']))+'px/'+str('%.1f'% abs(dict['data9']))+'mm')
        self.slabel7.setText(str('%.2e' % abs(dict['data7'])))

