# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'airForceAttr.ui'
#
# Created: Sun Mar 18 13:32:47 2012
#      by: PyQt4 UI code generator 4.7.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_airForceAttr(object):
    def setupUi(self, airForceAttr):
        airForceAttr.setObjectName("airForceAttr")
        airForceAttr.resize(251, 291)
        self.gridLayout = QtGui.QGridLayout(airForceAttr)
        self.gridLayout.setObjectName("gridLayout")
        self.magnitudeLabel = QtGui.QLabel(airForceAttr)
        self.magnitudeLabel.setObjectName("magnitudeLabel")
        self.gridLayout.addWidget(self.magnitudeLabel, 0, 0, 1, 1)
        self.magnitude = QtGui.QDoubleSpinBox(airForceAttr)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.magnitude.sizePolicy().hasHeightForWidth())
        self.magnitude.setSizePolicy(sizePolicy)
        self.magnitude.setMinimum(-999999999.0)
        self.magnitude.setMaximum(999999999.0)
        self.magnitude.setProperty("value", 4.0)
        self.magnitude.setObjectName("magnitude")
        self.gridLayout.addWidget(self.magnitude, 0, 1, 1, 1)
        self.attenuationLabel = QtGui.QLabel(airForceAttr)
        self.attenuationLabel.setObjectName("attenuationLabel")
        self.gridLayout.addWidget(self.attenuationLabel, 1, 0, 1, 1)
        self.attenuation = QtGui.QDoubleSpinBox(airForceAttr)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.attenuation.sizePolicy().hasHeightForWidth())
        self.attenuation.setSizePolicy(sizePolicy)
        self.attenuation.setMinimum(-999999999.0)
        self.attenuation.setMaximum(999999999.0)
        self.attenuation.setProperty("value", 1.0)
        self.attenuation.setObjectName("attenuation")
        self.gridLayout.addWidget(self.attenuation, 1, 1, 1, 1)
        self.directionLabel = QtGui.QLabel(airForceAttr)
        self.directionLabel.setObjectName("directionLabel")
        self.gridLayout.addWidget(self.directionLabel, 2, 0, 1, 1)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 3, 3, 1, 1)
        self.speedLabel = QtGui.QLabel(airForceAttr)
        self.speedLabel.setObjectName("speedLabel")
        self.gridLayout.addWidget(self.speedLabel, 4, 0, 1, 1)
        self.speed = QtGui.QDoubleSpinBox(airForceAttr)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.speed.sizePolicy().hasHeightForWidth())
        self.speed.setSizePolicy(sizePolicy)
        self.speed.setMinimum(-999999999.0)
        self.speed.setMaximum(999999999.0)
        self.speed.setProperty("value", 1.0)
        self.speed.setObjectName("speed")
        self.gridLayout.addWidget(self.speed, 4, 1, 1, 1)
        self.inheritVelocityLabel = QtGui.QLabel(airForceAttr)
        self.inheritVelocityLabel.setObjectName("inheritVelocityLabel")
        self.gridLayout.addWidget(self.inheritVelocityLabel, 5, 0, 1, 1)
        self.inheritVelocity = QtGui.QDoubleSpinBox(airForceAttr)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.inheritVelocity.sizePolicy().hasHeightForWidth())
        self.inheritVelocity.setSizePolicy(sizePolicy)
        self.inheritVelocity.setProperty("value", 1.0)
        self.inheritVelocity.setObjectName("inheritVelocity")
        self.gridLayout.addWidget(self.inheritVelocity, 5, 1, 1, 1)
        self.inheritRotation = QtGui.QCheckBox(airForceAttr)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.inheritRotation.sizePolicy().hasHeightForWidth())
        self.inheritRotation.setSizePolicy(sizePolicy)
        self.inheritRotation.setChecked(False)
        self.inheritRotation.setObjectName("inheritRotation")
        self.gridLayout.addWidget(self.inheritRotation, 6, 0, 1, 2)
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem1, 7, 0, 1, 1)
        self.directionX = QtGui.QDoubleSpinBox(airForceAttr)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.directionX.sizePolicy().hasHeightForWidth())
        self.directionX.setSizePolicy(sizePolicy)
        self.directionX.setMaximum(1.0)
        self.directionX.setSingleStep(0.01)
        self.directionX.setProperty("value", 1.0)
        self.directionX.setObjectName("directionX")
        self.gridLayout.addWidget(self.directionX, 3, 0, 1, 1)
        self.directionZ = QtGui.QDoubleSpinBox(airForceAttr)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.directionZ.sizePolicy().hasHeightForWidth())
        self.directionZ.setSizePolicy(sizePolicy)
        self.directionZ.setMaximum(1.0)
        self.directionZ.setSingleStep(0.01)
        self.directionZ.setObjectName("directionZ")
        self.gridLayout.addWidget(self.directionZ, 3, 2, 1, 1)
        self.directionY = QtGui.QDoubleSpinBox(airForceAttr)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.directionY.sizePolicy().hasHeightForWidth())
        self.directionY.setSizePolicy(sizePolicy)
        self.directionY.setMaximum(1.0)
        self.directionY.setSingleStep(0.01)
        self.directionY.setProperty("value", 0.0)
        self.directionY.setObjectName("directionY")
        self.gridLayout.addWidget(self.directionY, 3, 1, 1, 1)

        self.retranslateUi(airForceAttr)
        QtCore.QMetaObject.connectSlotsByName(airForceAttr)

    def retranslateUi(self, airForceAttr):
        airForceAttr.setWindowTitle(QtGui.QApplication.translate("airForceAttr", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.magnitudeLabel.setText(QtGui.QApplication.translate("airForceAttr", "Magnitude", None, QtGui.QApplication.UnicodeUTF8))
        self.attenuationLabel.setText(QtGui.QApplication.translate("airForceAttr", "Attenuation", None, QtGui.QApplication.UnicodeUTF8))
        self.directionLabel.setText(QtGui.QApplication.translate("airForceAttr", "Direction:", None, QtGui.QApplication.UnicodeUTF8))
        self.speedLabel.setText(QtGui.QApplication.translate("airForceAttr", "Speed", None, QtGui.QApplication.UnicodeUTF8))
        self.inheritVelocityLabel.setText(QtGui.QApplication.translate("airForceAttr", "Inherit Velocity", None, QtGui.QApplication.UnicodeUTF8))
        self.inheritRotation.setText(QtGui.QApplication.translate("airForceAttr", "Inherit Rotation", None, QtGui.QApplication.UnicodeUTF8))

