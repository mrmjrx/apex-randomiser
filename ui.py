# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from main import get_loadouts
import keyboard


class Ui_MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setObjectName("MainWindow")
        self.resize(800, 700)
        self.setWindowTitle("Apex Randomiser")
        font = QtGui.QFont()
        font.setFamily("JetBrains Mono Light")
        font.setPointSize(16)
        self.setFont(font)
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.loadout1_title = QtWidgets.QLabel(self.centralwidget)
        self.loadout1_title.setGeometry(QtCore.QRect(20, 20, 620, 21))
        font = QtGui.QFont()
        font.setFamily("JetBrains Mono ExtraLight")
        font.setPointSize(16)
        self.loadout1_title.setFont(font)
        self.loadout1_title.setObjectName("loadout1_title")
        self.loadout1_weapons = QtWidgets.QLabel(self.centralwidget)
        self.loadout1_weapons.setGeometry(QtCore.QRect(20, 40, 760, 30))
        font = QtGui.QFont()
        font.setFamily("JetBrains Mono ExtraBold")
        font.setPointSize(20)
        self.loadout1_weapons.setFont(font)
        self.loadout1_weapons.setAlignment(QtCore.Qt.AlignCenter)
        self.loadout1_weapons.setObjectName("loadout1_weapons")
        self.loadout1_stats = QtWidgets.QLabel(self.centralwidget)
        self.loadout1_stats.setGeometry(QtCore.QRect(20, 80, 760, 20))
        self.loadout1_stats.setAlignment(QtCore.Qt.AlignCenter)
        self.loadout1_stats.setObjectName("loadout1_stats")
        self.loadout1_weapon1 = QtWidgets.QLabel(self.centralwidget)
        self.loadout1_weapon1.setGeometry(QtCore.QRect(100, 110, 300, 200))
        self.loadout1_weapon1.setText("")
        self.loadout1_weapon1.setAlignment(QtCore.Qt.AlignCenter)
        self.loadout1_weapon1.setObjectName("loadout1_weapon1")
        self.loadout1_weapon2 = QtWidgets.QLabel(self.centralwidget)
        self.loadout1_weapon2.setGeometry(QtCore.QRect(400, 110, 300, 200))
        self.loadout1_weapon2.setText("")
        self.loadout1_weapon2.setAlignment(QtCore.Qt.AlignCenter)
        self.loadout1_weapon2.setObjectName("loadout1_weapon2")

        self.loadout2_stats = QtWidgets.QLabel(self.centralwidget)
        self.loadout2_stats.setGeometry(QtCore.QRect(20, 380, 760, 20))
        self.loadout2_stats.setAlignment(QtCore.Qt.AlignCenter)
        self.loadout2_stats.setObjectName("loadout2_stats")
        self.loadout2_title = QtWidgets.QLabel(self.centralwidget)
        self.loadout2_title.setGeometry(QtCore.QRect(20, 320, 620, 21))
        font = QtGui.QFont()
        font.setFamily("JetBrains Mono ExtraLight")
        font.setPointSize(16)
        self.loadout2_title.setFont(font)
        self.loadout2_title.setObjectName("loadout2_title")
        self.loadout2_weapons = QtWidgets.QLabel(self.centralwidget)
        self.loadout2_weapons.setGeometry(QtCore.QRect(20, 340, 760, 30))
        font = QtGui.QFont()
        font.setFamily("JetBrains Mono ExtraBold")
        font.setPointSize(20)
        self.loadout2_weapons.setFont(font)
        self.loadout2_weapons.setAlignment(QtCore.Qt.AlignCenter)
        self.loadout2_weapons.setObjectName("loadout2_weapons")
        self.loadout2_weapon1 = QtWidgets.QLabel(self.centralwidget)
        self.loadout2_weapon1.setGeometry(QtCore.QRect(100, 410, 300, 200))
        self.loadout2_weapon1.setText("")
        self.loadout2_weapon1.setPixmap(QtGui.QPixmap("../images/Bocek Compound Bow.png"))
        self.loadout2_weapon1.setAlignment(QtCore.Qt.AlignCenter)
        self.loadout2_weapon1.setObjectName("loadout2_weapon1")
        self.loadout2_weapon2 = QtWidgets.QLabel(self.centralwidget)
        self.loadout2_weapon2.setGeometry(QtCore.QRect(400, 410, 300, 200))
        self.loadout2_weapon2.setText("")
        self.loadout2_weapon2.setPixmap(QtGui.QPixmap("../images/Bocek Compound Bow.png"))
        self.loadout2_weapon2.setAlignment(QtCore.Qt.AlignCenter)
        self.loadout2_weapon2.setObjectName("loadout2_weapon2")

        self.regenerate_button = QtWidgets.QPushButton(self.centralwidget)
        self.regenerate_button.setGeometry(QtCore.QRect(20, 610, 760, 80))
        font = QtGui.QFont()
        font.setFamily("JetBrains Mono Light")
        font.setPointSize(28)
        self.regenerate_button.setFont(font)
        self.regenerate_button.setObjectName("regenerate_button")
        self.regenerate_button.setText("Regenerate Loadouts (Up Arrow)")
        self.regenerate_button.clicked.connect(self.regen_loadouts)
        self.setCentralWidget(self.centralwidget)

        self.regen_loadouts()
        QtCore.QMetaObject.connectSlotsByName(self)

    def regen_loadouts(self):
        loadouts = get_loadouts()
        tier_dict = {1: "D", 2: "C", 3: "B", 4: "A", 5: "S"}
        self.loadout1_title.setText("Loadout #1")
        self.loadout1_weapons.setText(f"{loadouts[0][0].weapon} | {loadouts[0][1].weapon}")
        self.loadout1_stats.setText(f"DPS: {loadouts[0][0].dps} - {tier_dict[loadouts[0][0].rank_num]} Tier | "
                                    f"DPS: {loadouts[0][1].dps} - {tier_dict[loadouts[0][1].rank_num]} Tier")
        self.loadout1_weapon1.setPixmap(QtGui.QPixmap(f"images/{loadouts[0][0].weapon}.png"))
        self.loadout1_weapon2.setPixmap(QtGui.QPixmap(f"images/{loadouts[0][1].weapon}.png"))
        self.loadout2_title.setText("Loadout #2")
        self.loadout2_weapons.setText(f"{loadouts[1][0].weapon} | {loadouts[1][1].weapon}")
        self.loadout2_stats.setText(f"DPS: {loadouts[1][0].dps} - {tier_dict[loadouts[1][0].rank_num]} Tier | "
                                    f"DPS: {loadouts[1][1].dps} - {tier_dict[loadouts[1][1].rank_num]} Tier")
        self.loadout2_weapon1.setPixmap(QtGui.QPixmap(f"images/{loadouts[1][0].weapon}.png"))
        self.loadout2_weapon2.setPixmap(QtGui.QPixmap(f"images/{loadouts[1][1].weapon}.png"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = Ui_MainWindow()

    keyboard.add_hotkey("up", ui.regen_loadouts)

    ui.show()
    sys.exit(app.exec_())
