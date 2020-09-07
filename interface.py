# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'interface.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!

import collections
from random import randrange
import numpy as np
from sympy import symbols, Eq, solve, simplify
from sympy.plotting import plot
import sympy as sp
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem, QMessageBox
from scipy.optimize import linprog


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(979, 838)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(360, 10, 211, 81))

        font = QtGui.QFont()
        font.setFamily("Cooper Black")
        font.setPointSize(16)

        self.label.setFont(font)
        self.label.setTextFormat(QtCore.Qt.PlainText)
        self.label.setObjectName("label")

        self.nbrPlayersSpin = QtWidgets.QSpinBox(self.centralwidget)
        self.nbrPlayersSpin.setGeometry(QtCore.QRect(140, 100, 42, 22))
        self.nbrPlayersSpin.setObjectName("nbrPlayersSpin")

        self.btnGeneratePlayers = QtWidgets.QPushButton(self.centralwidget)
        self.btnGeneratePlayers.setGeometry(QtCore.QRect(200, 100, 111, 23))
        self.btnGeneratePlayers.setObjectName("btnGeneratePlayers")
        self.btnGeneratePlayers.clicked.connect(self.generate_players)

        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(30, 100, 91, 21))
        self.label_2.setObjectName("label_2")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(100, 170, 111, 21))
        self.label_4.setObjectName("label_4")

        self.MatrixWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.MatrixWidget.setGeometry(QtCore.QRect(340, 200, 631, 441))
        self.MatrixWidget.setRowCount(100)
        self.MatrixWidget.setColumnCount(100)
        self.MatrixWidget.setObjectName("MatrixWidget")

        self.nbrStrategiesWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.nbrStrategiesWidget.setGeometry(QtCore.QRect(0, 200, 301, 441))
        self.nbrStrategiesWidget.setColumnCount(2)
        self.nbrStrategiesWidget.setObjectName("nbrStrategiesWidget")
        self.nbrStrategiesWidget.setRowCount(0)

        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(10, 170, 71, 21))
        self.label_5.setObjectName("label_5")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(370, 90, 221, 41))
        self.label_3.setObjectName("label_3")

        self.btnGenerateMatrix = QtWidgets.QPushButton(self.centralwidget)
        self.btnGenerateMatrix.setGeometry(QtCore.QRect(620, 100, 111, 23))
        self.btnGenerateMatrix.setObjectName("btnGenerateMatrix")
        self.btnGenerateMatrix.clicked.connect(self.generate_matrix)

        self.btnSetStrategies = QtWidgets.QPushButton(self.centralwidget)
        self.btnSetStrategies.setGeometry(QtCore.QRect(90, 140, 75, 23))
        self.btnSetStrategies.setObjectName("btnSetStrategies")
        self.btnSetStrategies.clicked.connect(self.setting_strategies)

        self.pushButton_str_dom_str = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_str_dom_str.setGeometry(QtCore.QRect(10, 670, 251, 23))
        self.pushButton_str_dom_str.setObjectName("pushButton_str_dom_str")
        self.pushButton_str_dom_str.clicked.connect(self.str_dom_str)

        self.pushButton_fbl_dom_str = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_fbl_dom_str.setGeometry(QtCore.QRect(10, 700, 251, 23))
        self.pushButton_fbl_dom_str.setObjectName("pushButton_fbl_dom_str")
        self.pushButton_fbl_dom_str.clicked.connect(self.fbl_dom_str)

        self.pushButton_elim_succ_str_frt = QtWidgets.QPushButton(
            self.centralwidget)
        self.pushButton_elim_succ_str_frt.setGeometry(
            QtCore.QRect(10, 730, 361, 23))
        self.pushButton_elim_succ_str_frt.setObjectName(
            "pushButton_elim_succ_str_frt")
        self.pushButton_elim_succ_str_frt.clicked.connect(
            self.elim_succ_str_frt)

        self.pushButton_elim_succ_fbl_frt = QtWidgets.QPushButton(
            self.centralwidget)
        self.pushButton_elim_succ_fbl_frt.setGeometry(
            QtCore.QRect(10, 760, 361, 23))
        self.pushButton_elim_succ_fbl_frt.setObjectName(
            "pushButton_elim_succ_fbl_frt")
        self.pushButton_elim_succ_fbl_frt.clicked.connect(
            self.elim_succ_fbl_frt)

        self.pushButton_nash_equi = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_nash_equi.setGeometry(QtCore.QRect(390, 670, 141, 23))
        self.pushButton_nash_equi.setObjectName("pushButton_nash_equi")
        self.pushButton_nash_equi.clicked.connect(self.nash_equi)

        self.pushButton_prof_pareto = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_prof_pareto.setGeometry(
            QtCore.QRect(390, 700, 141, 23))
        self.pushButton_prof_pareto.setObjectName("pushButton_prof_pareto")
        self.pushButton_prof_pareto.clicked.connect(self.prof_pareto)

        self.pushButton_niv_sec = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_niv_sec.setGeometry(QtCore.QRect(390, 730, 141, 23))
        self.pushButton_niv_sec.setObjectName("pushButton_niv_sec")
        self.pushButton_niv_sec.clicked.connect(self.niv_sec)

        self.pushButton_equi_mixte = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_equi_mixte.setGeometry(QtCore.QRect(390, 760, 181, 23))
        self.pushButton_equi_mixte.setObjectName("pushButton_equi_mixte")
        self.pushButton_equi_mixte.clicked.connect(self.equi_mixte)

        self.pushButton_val_null_sum = QtWidgets.QPushButton(
            self.centralwidget)
        self.pushButton_val_null_sum.setGeometry(
            QtCore.QRect(590, 670, 241, 23))
        self.pushButton_val_null_sum.setObjectName("pushButton_val_null_sum")
        self.pushButton_val_null_sum.clicked.connect(self.val_null_sum)

        MainWindow.setCentralWidget(self.centralwidget)

        self.pushButton_setvalues = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_setvalues.setGeometry(QtCore.QRect(370, 170, 75, 23))
        self.pushButton_setvalues.setObjectName("pushButton_setvalues")

        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 979, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")

        MainWindow.setMenuBar(self.menubar)

        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")

        MainWindow.setStatusBar(self.statusbar)

        self.actionAbout = QtWidgets.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.menuFile.addAction(self.actionAbout)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Game Theory Basics"))
        self.btnGeneratePlayers.setText(
            _translate("MainWindow", "Generate Players"))
        self.label_2.setText(_translate("MainWindow", "Number of players"))
        self.label_4.setText(_translate("MainWindow", "Number Of Strategies"))
        self.label_5.setText(_translate("MainWindow", "Players nums"))
        self.label_3.setText(_translate(
            "MainWindow", "must specify nbr of strategies for each player"))
        self.btnGenerateMatrix.setText(
            _translate("MainWindow", "Generate Matrix"))
        self.btnSetStrategies.setText(
            _translate("MainWindow", "Set Strategies"))
        self.pushButton_str_dom_str.setText(_translate(
            "MainWindow", "determiner la stratégie strictement dominante"))
        self.pushButton_fbl_dom_str.setText(_translate(
            "MainWindow", "determiner la stratégie faiblement dominante"))
        self.pushButton_elim_succ_str_frt.setText(_translate(
            "MainWindow", "equilibres d\'élimination successives des stratégies fortement dominees"))
        self.pushButton_elim_succ_fbl_frt.setText(_translate(
            "MainWindow", "equilibres d\'élimination successives des stratégies faiblement dominees"))
        self.pushButton_nash_equi.setText(
            _translate("MainWindow", "équilibres de Nash"))
        self.pushButton_prof_pareto.setText(
            _translate("MainWindow", "profil de pareto"))
        self.pushButton_niv_sec.setText(
            _translate("MainWindow", "niveau de securite "))
        self.pushButton_equi_mixte.setText(_translate(
            "MainWindow", "calculer l’équilibre de Nash mixte"))
        self.pushButton_val_null_sum.setText(_translate(
            "MainWindow", "déterminer la valeur dans un jeu à somme nulle"))
        self.pushButton_setvalues.setText(
            _translate("MainWindow", "set values"))
        self.pushButton_setvalues.clicked.connect(self.set_values)
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.actionAbout.setText(_translate("MainWindow", "About"))

    def show_results(self):
        print("showing results")
        msg = QMessageBox()
        msg.setWindowTitle("resultat ")
        msg.setIcon(QMessageBox.Question)
        msg.setStandardButtons(QMessageBox.Ok)
        msg.setText(self.output)
        msg.exec_()
        # # self.hide()

    def generate_players(self):
        self.output = "nothing yet "
        print("genrating players")
        self.nplayers = self.nbrPlayersSpin.value()
        self.nbrStrategiesWidget.setRowCount(self.nplayers)
        self.nbrStrategiesWidget.setColumnCount(1)
        # filling in
        for i in range(self.nplayers):
            self.nbrStrategiesWidget.setItem(i, 0, QTableWidgetItem(i))
        self.show_results()

    def generate_matrix(self):
        print("generating matrix")
        self.matrix = self.auto_fill_matrix(
            self.nbr_stra, lambda coords: coords[:])
        self.comb = []
        self.showIndexes(self.matrix, self.comb)
        print("modifying the table")
        # if len(self.nbr_stra) > 2:
        self.MatrixWidget.setRowCount(len(self.comb))
        self.MatrixWidget.setColumnCount(2)
        temp_nbr_stra = self.nbr_stra
        for i, sub in enumerate(self.comb):
            self.MatrixWidget.setItem(i, 0, QTableWidgetItem(str(sub[0])))
            self.MatrixWidget.setItem(i, 1, QTableWidgetItem(str(sub[1])))
        # else:
        #     self.MatrixWidget.setRowCount(self.nbr_stra[0])
        #     self.MatrixWidget.setColumnCount(self.nbr_stra[1])
        #     # print(self.matrix)
        #     for i in range(self.nbr_stra[0]):
        #         for j in range(self.nbr_stra[1]):
        #             self.MatrixWidget.setItem(i, j, QTableWidgetItem(
        #                 str(self.matrix[i][j])))

    def setting_strategies(self):
        print("setting strategies")
        self.nbr_stra = []
        for i in range(self.nplayers):
            item = self.nbrStrategiesWidget.item(i, 0)
            print(item)
            print(item.text())
            print(int(item.text()))
            self.nbr_stra.append(int(item.text()))
        print("stra")
        print(self.nbr_stra)

    def fill_matrix(self, dims, callback, n=0, indices=[]):
        dim = dims[n]
        result = []
        for i in range(dim):
            new_indices = indices + [i]
            if n + 1 < len(dims):
                result.append(self.fill_matrix(
                    dims, callback, n + 1, new_indices))
            else:
                el = []
                for x in range(len(dims)):
                    el.append(int(input("gain de joueur"+str(x+1))))
                result.append(callback(el))

        return result

    # recursive auto fill

    def auto_fill_matrix(self, dims, callback, n=0, indices=[]):
        dim = dims[n]
        result = []
        for i in range(dim):
            new_indices = indices + [i]
            if n + 1 < len(dims):
                result.append(self.auto_fill_matrix(
                    dims, callback, n + 1, new_indices))
            else:
                el = []
                for x in range(len(dims)):
                    print("gain de joueur"+str(x+1))
                    el.append(randrange(10))
                result.append(callback(el))

        return result

    # recursive explorer
    def showIndexes(self, l, comb):
        for index in self.getIndexes(l):
            comb.append(index)
            print(index)

    def getIndexes(self, l, index=[]):
        for i, subl in enumerate(l):
            if type(subl) == list:
                yield from self.getIndexes(subl, index+[i])
            else:
                # or just yield (index+[i]) for the index only
                yield [index+[i], subl]

    def set_values(self):
        for i in range(self.MatrixWidget.rowCount()):
            print(self.MatrixWidget.item(i, 0).text())
            self.comb[i][1] = int(self.MatrixWidget.item(i, 1).text())
        for sub in self.comb:
            print(sub)

    def getStrategyValues(self, player, strategy, comb):
        c = []
        # print("player " +str(player+1)+" payoffs of strategy "+str(strategy+1))
        for l in comb:
            if l[0][player] == strategy:
                if l[0][len(l[0])-1] == player:
                    c.append(l[1])  # value (payoff ) of the current index
                    # print(l[1])
                #  print("------")
        return c

    def compareStrictDomianaitingStrategy(self, str1, str2):
        i = 0
        # print("-------------------------------------")
        while i < len(str1):
            # print("s1 = "+str(str1[i])+" s2 = "+str(str2[i]))
            if str1[i] <= str2[i]:  # if strategy 1 is dominante
                break
            i += 1
        # print("------")
        if i >= len(str1):
            return True
        return False

    def compareWeakDominaitingStrategy(self, str1, str2):
        i = 0
        while i < len(str1):
            # print("s1 = "+str(str1[i])+" s2 = "+str(str2[i]))
            if str1[i] < str2[i]:  # if strategy 1 is dominante
                break
            i += 1
        if i == len(str1):
            return True
        return False

    def compareStrictDominaitedStrategy(self, str1, str2):
        i = 0
        while i < len(str1):
            # print("s1 = "+str(str1[i])+" s2 = "+str(str2[i]))
            if str1[i] >= str2[i]:  # if strategy 1 is strictly dominaited
                break
            i += 1
        if i == len(str1):
            return True
        return False

    def compareWeakDominaitedStrategy(self, str1, str2):
        i = 0
        while i < len(str1):
            # print("s1 = "+str(str1[i])+" s2 = "+str(str2[i]))
            if str1[i] > str2[i]:  # if strategy 1 is weakly dominaited
                break
            i += 1
        if i == len(str1):
            return True
        return False

    def str_dom_str(self):
        print("calcule de strategie Strictement dominante")
        comb = self.comb
        nbr_stra = self.nbr_stra
        n_players = self.nplayers
        for player in range(n_players):
            print("checking dominant strategy for player " + str(player+1))
            # Right side
            dom_straR = -1  # supposedly that the first strategy of the current player is the dominante one
            strategy = 0
            # current strategy values
            str1 = self.getStrategyValues(player, strategy, comb)
            strategy2 = strategy+1
            while strategy2 < nbr_stra[player]:
                str2 = self.getStrategyValues(player, strategy2, comb)
                if self.compareStrictDomianaitingStrategy(str2, str1):
                    dom_straR = strategy2
                    # print("dom stra R = " + str(dom_straR))
                    str1 = str2
                elif self.compareStrictDomianaitingStrategy(str1, str2):
                    dom_straR = strategy
                # print("dom stra R = " + str(dom_straR))

                strategy2 += 1
            # Left side
            # left side
            dom_straL = -1  # supposedly that the last strategy of the current player is the dominante one
            strategy = nbr_stra[player]-1
            # current strategy values
            str1 = self.getStrategyValues(player, strategy, comb)
            strategy2 = 0
            while strategy2 < strategy:
                str2 = self.getStrategyValues(player, strategy2, comb)
                if self.compareStrictDomianaitingStrategy(str2, str1):
                    dom_straL = strategy2
                    # print("dom stra L = " + str(dom_straL))
                    str1 = str2
                elif self.compareStrictDomianaitingStrategy(str1, str2):
                    dom_straL = strategy
                    # print("dom stra L = " + str(dom_straL))

                strategy2 += 1
            text = ""
            if dom_straR >= 0 or dom_straL >= 0:
                if dom_straR >= 0 and dom_straL != dom_straR:
                    print("la strategie Strictement dominante pour le joueur " +
                          str(player+1)+" est "+str(dom_straR+1))
                    text = "la strategie Strictement dominante pour le joueur " + \
                        str(player+1) + " est "+str(dom_straR+1)+" "
                if dom_straL >= 0 and dom_straL != dom_straR:
                    print("la strategie Strictement dominante pour le joueur " +
                          str(player+1)+" est "+str(dom_straL+1))
                    text = "la strategie Strictement dominante pour le joueur " + \
                        str(player+1) + " est " + str(dom_straL+1) + " "
            else:
                print(
                    "pas de strategie Strictement dominante pour le joueur " + str(player+1))
                text = "pas de strategie Strictement dominante pour le joueur " + \
                    str(player+1) + " "
            self.output = text
            self.show_results()

    def fbl_dom_str(self):
        print("calcule de strategie faiblement dominante")
        comb = self.comb
        nbr_stra = self.nbr_stra
        n_players = self.nplayers
        for player in range(n_players):
            print("checking weakly dominant strategy for player " + str(player+1))
            # Right side
            dom_straR = -1  # supposedly that the first strategy of the current player is the dominante one
            strategy = 0
            # current strategy values
            str1 = self.getStrategyValues(player, strategy, comb)
            strategy2 = strategy+1
            while strategy2 < nbr_stra[player]:
                str2 = self.getStrategyValues(player, strategy2, comb)
                if self.compareWeakDominaitingStrategy(str2, str1):
                    dom_straR = strategy2
                    # print("dom stra R = " + str(dom_straR))
                    str1 = str2
                elif self.compareWeakDominaitingStrategy(str1, str2):
                    dom_straR = strategy
                    # print("dom stra R = " + str(dom_straR))

                strategy2 += 1
            # Left side
            # left side
            dom_straL = -1  # supposedly that the last strategy of the current player is the dominante one
            strategy = nbr_stra[player]-1
            # current strategy values
            str1 = self.getStrategyValues(player, strategy, comb)
            strategy2 = 0
            while strategy2 < strategy:
                str2 = self.getStrategyValues(player, strategy2, comb)
                if self.compareWeakDominaitingStrategy(str2, str1):
                    dom_straL = strategy2
                    # print("dom stra L = " + str(dom_straL))
                    str1 = str2
                elif self.compareWeakDominaitingStrategy(str1, str2):
                    dom_straL = strategy
                    # print("dom stra L = " + str(dom_straL))

                strategy2 += 1
            text = ""
            if dom_straR >= 0 or dom_straL >= 0:
                if dom_straR >= 0 and dom_straL != dom_straR:
                    print("la strategie Faiblement dominante pour le joueur " +
                          str(player+1)+" est "+str(dom_straR+1))
                    text = "la strategie Faiblement dominante pour le joueur " + \
                        str(player+1)+" est "+str(dom_straR+1) + " "
                if dom_straL >= 0 and dom_straL != dom_straR:
                    print("la strategie Faiblement dominante pour le joueur " +
                          str(player+1)+" est "+str(dom_straL+1))
                    text = "la strategie Faiblement dominante pour le joueur " + \
                        str(player+1)+" est "+str(dom_straL+1) + ""
            else:
                print(
                    "pas de strategie Faiblement dominante pour le joueur " + str(player+1))
                text = "pas de strategie Faiblement dominante pour le joueur " + \
                    str(player+1) + ""
            self.output = text
            self.show_results()

    def getStrictWeakestStrategy(self, tempComb, player, nbr_stra):
        print("checking dominated strategy for player " + str(player+1))
        print("checking strictly dominantated strategy for player " + str(player+1))
        dom_stra = -1
        # Right side
        dom_straR = -1  # supposedly that the first strategy of the current player is the dominante one

        strategy = 0
        # current strategy values
        str1 = self.getStrategyValues(player, strategy, tempComb)
        if len(str1) > 0:
            strategy2 = strategy+1
            while strategy2 < nbr_stra[player]:
                str2 = self.getStrategyValues(player, strategy2, tempComb)
                if len(str2) > 0:
                    if self.compareStrictDominaitedStrategy(str2, str1):
                        dom_straR = strategy2
                        # print("dom stra R = " + str(dom_straR))
                        str1 = str2
                    elif self.compareStrictDominaitedStrategy(str1, str2):
                        dom_straR = strategy
                        # print("dom stra R = " + str(dom_straR))
                else:
                    print("strategy " + str(strategy2) + " was eliminated ")
                strategy2 += 1
        else:
            print("strategy " + str(strategy) + " was eliminated ")
        # Left side
        # left side
        dom_straL = -1  # supposedly that the last strategy of the current player is the dominante one
        strategy = nbr_stra[player]-1
        # current strategy values
        str1 = self.getStrategyValues(player, strategy, tempComb)
        if len(str1) > 0:
            strategy2 = 0
            while strategy2 < strategy:
                str2 = self.getStrategyValues(player, strategy2, tempComb)
                if len(str2) > 0:
                    if self.compareStrictDominaitedStrategy(str2, str1):
                        dom_straL = strategy2
                        # print("dom stra L = " + str(dom_straL))
                        str1 = str2
                    elif self.compareStrictDominaitedStrategy(str1, str2):
                        dom_straL = strategy
                        # print("dom stra L = " + str(dom_straL))
                else:
                    print("strategy " + str(strategy2) + " was eliminated ")
                strategy2 += 1
        else:
            print("strategy " + str(strategy) + " was eliminated ")

        if dom_straR >= 0 or dom_straL >= 0:
            if dom_straR >= 0 and dom_straL != dom_straR:
                print("la strategie Strictement dominee pour le joueur " +
                      str(player+1)+" est "+str(dom_straR+1))
                dom_stra = dom_straR
            if dom_straL >= 0 and dom_straL != dom_straR:
                print("la strategie Strictement dominee pour le joueur " +
                      str(player+1)+" est "+str(dom_straL+1))
                dom_stra = dom_straL
        else:
            print("pas de strategie Strictement dominee pour le joueur " + str(player+1))

        return dom_stra

    def getWeakWeakestStrategy(self, tempComb, player, nbr_stra):
        print("checking dominated strategy for player " + str(player+1))
        print("checking strictly dominantated strategy for player " + str(player+1))
        dom_stra = -1
        # Right side
        dom_straR = -1  # supposedly that the first strategy of the current player is the dominante one
        strategy = 0
        # current strategy values
        str1 = self.getStrategyValues(player, strategy, tempComb)
        if len(str1) > 0:
            strategy2 = strategy+1
            while strategy2 < nbr_stra[player]:
                str2 = self.getStrategyValues(player, strategy2, tempComb)
                if len(str2) > 0:
                    if self.compareWeakDominaitedStrategy(str2, str1):
                        dom_straR = strategy2
                        # print("dom stra R = " + str(dom_straR))
                        str1 = str2
                    elif self.compareWeakDominaitedStrategy(str1, str2):
                        dom_straR = strategy
                        # print("dom stra R = " + str(dom_straR))
                else:
                    print("strategy " + str(strategy2) + " was eliminated ")
                strategy2 += 1
        else:
            print("strategy " + str(strategy) + " was eliminated ")
        # Left side
        # left side
        dom_straL = -1  # supposedly that the last strategy of the current player is the dominante one
        strategy = nbr_stra[player]-1
        # current strategy values
        str1 = self.getStrategyValues(player, strategy, tempComb)
        if len(str1) > 0:
            strategy2 = 0
            while strategy2 < strategy:
                str2 = self.getStrategyValues(player, strategy2, tempComb)
                if len(str2) > 0:
                    if self.compareWeakDominaitedStrategy(str2, str1):
                        dom_straL = strategy2
                        # print("dom stra L = " + str(dom_straL))
                        str1 = str2
                    elif self.compareWeakDominaitedStrategy(str1, str2):
                        dom_straL = strategy
                        # print("dom stra L = " + str(dom_straL))
                else:
                    print("strategy " + str(strategy2) + " was eliminated ")
                strategy2 += 1
        else:
            print("strategy " + str(strategy) + " was eliminated ")

        if dom_straR >= 0 or dom_straL >= 0:
            if dom_straR >= 0 and dom_straL != dom_straR:
                print("la strategie Faiblement dominee pour le joueur " +
                      str(player+1)+" est "+str(dom_straR+1))
                dom_stra = dom_straR
            if dom_straL >= 0 and dom_straL != dom_straR:
                print("la strategie Faiblement dominee pour le joueur " +
                      str(player+1)+" est "+str(dom_straL+1))
                dom_stra = dom_straL
        else:
            print("pas de strategie Faiblement dominee pour le joueur " + str(player+1))

        return dom_stra

    def eliminateStrategy(self, tempComb, player, wstr):
        newComb = []
        print("eliminating "+str(wstr)+" of player "+str(player))
        print("length before "+str(len(tempComb)))
        for i, sub in enumerate(tempComb):
            if sub[0][player] != wstr:
                newComb.append(sub)  # remove the strategy from comb
        print("length before "+str(len(newComb)))
        return newComb

    def elim_succ_str_frt(self):
        print("elimination des strategies strictement dominnes")
        comb = self.comb
        nbr_stra = self.nbr_stra
        n_players = self.nplayers
        tempComb = comb  # tempo pour appliquer le traitement
        nbra_stra_temp = nbr_stra
        print("up up ")
        print(tempComb)
        text = ""
        reached_end = False
        eliminated = False
        while len(tempComb) > 2 and not reached_end:
            player = 0
            print("up")
            print(tempComb)
            wstr = []
            while player < n_players:
                wstr.append(self.getStrictWeakestStrategy(
                    tempComb, player, nbra_stra_temp))
                player += 1

            print("strategies are")
            print(wstr)
            print("eliminations")
            if(not self.check_if_found(wstr)):  # checking if all strategies can't be eliminated
                reached_end = True
                print("none of the players got weak strategy end of operation")
                text = "ya pas  de strategies dominantes" + "\n"
                break
            else:
                for i, sub in enumerate(wstr):
                    if sub != -1:
                        print("eliminating strategy " +
                              str(sub)+" of player "+str(i+1))
                        tempComb = list(self.eliminateStrategy(
                            tempComb, player, sub))
            # cone = input(" proceed ...")
        text += str(tempComb)
        self.output = text
        print(tempComb)
        self.show_results()

    def check_if_found(self, wstr):
        for i in wstr:
            if i != -1:
                return True
        return False

    def elim_succ_fbl_frt(self):
        print("elimination des strategies faiblement dominnes")
        comb = self.comb
        nbr_stra = self.nbr_stra
        n_players = self.nplayers
        tempComb = comb  # tempo pour appliquer le traitement
        nbra_stra_temp = nbr_stra
        print("up up ")
        print(tempComb)
        text = ""
        while len(tempComb) > n_players:
            player = 0
            dom_stra_exist = False
            print("up")
            print(tempComb)
            while player < n_players:
                wstr = self.getWeakWeakestStrategy(
                    tempComb, player, nbra_stra_temp)

                if wstr != -1:
                    print("eliminating strategy " + str(wstr+1) +
                          " of player " + str(player+1))
                    tempComb = self.eliminateStrategy(tempComb, player, wstr)
                    print("down")
                    print(tempComb)
                    dom_stra_exist = True
                    break

                player += 1

            if not dom_stra_exist:
                print("ya pas  de strategies dominante")
                text = "ya pas  de strategies dominante" + "\n"
                break
            # cone = input(" proceed ...")
        self.output = text + str(tempComb)
        print(tempComb)
        self.show_results()

    def get_val_all_str(self, player, comb):
        print("getting all values of all strategies of player " + str(player))
        player_comb = []
        for subc in comb:
            if subc[0][len(subc[0])-1] == player:
                player_comb.append(subc)
        return player_comb

    def get_max_str(self, player, strp, player_comb):
        max_vstr = player_comb[0]
        for subc in player_comb:
            if strp == subc[0][player]:
                if subc[1] > max_vstr[1]:
                    max_vstr = subc

        max_str = max_vstr[0].copy()
        max_str.pop()
        return max_str  # comb of max value of strategy strp

    # get the minumum of a given strategy of a certain player

    def get_min_str(self, player, strp, player_comb):
        min_vstr = player_comb[0]
        min_val = min_vstr[1]
        for subc in player_comb:
            if strp == subc[0][player]:
                if subc[1] < min_vstr[1]:
                    min_vstr = subc
                    min_val = min_vstr[1]

        return min_val  # comb of min value of strategy strp

    def get_max_all_str(self, player, player_comb, nbr_stra):
        all_str_max = []
        for strp in range(nbr_stra[player]):
            str_max = self.get_max_str(player, strp, player_comb)
            # print("max value of strategy "+str(strp)+ " of player "+ str(player) + " is " + str(str_max[1]))
            all_str_max.append(str_max)
        return all_str_max

    # get min of all strategies for security

    def get_min_all_str(self, player, player_comb, nbr_stra):
        all_str_min = []
        for strp in range(nbr_stra[player]):
            str_min = self.get_min_str(player, strp, player_comb)
            # print("min value of strategy "+str(strp)+ " of player "+ str(player) + " is " + str(str_min[1]))
            all_str_min.append(str_min)
        # calculate the max
        max_min = max(all_str_min)
        return max_min

    def exists(self, l, search_list):

        if search_list in l:
            return True
        return False

    def common(self, list1, list2):
        equils = []
        i1 = 0
        while i1 < len(list1):
            i2 = 0
            while i2 < len(list2):
                print(" list 1  = " + str(list1[i1]))
                print(" list 2  = " + str(list2[i2]))
                if list1[i1][0] == list2[i2][0] and list1[i1][1] == list2[i2][1]:
                    if list1[i1] not in equils:
                        equils.append(list1[i1])

                i2 += 1
            i1 += 1
        return equils

    def verify_equil(self, equil):
        print(equil)
        nash_equilibrium_list = []
        player1 = 0
        while player1 < len(equil):
            # check right side
            player2 = player1 + 1
            while player2 < len(equil):
                equils = self.common(equil[player1], equil[player2])
                if len(equils) > 0:
                    nash_equilibrium_list.append(equils)

                player2 += 1
            player1 += 1

        # print(nash_equilibrium_list)
        text = ""
        if len(nash_equilibrium_list) > 0:
            print("les profils d'equilibre de nash sont")
            text = "les profils d'equilibre de nash sont \n"
            print(nash_equilibrium_list)
            text += str(nash_equilibrium_list)
        else:
            print(" pas d'equilibre de nash")
            text = " pas d'equilibre de nash"
        self.output = text
        self.show_results()

    def nash_equi(self):
        print("nash equilibrium")
        # pour chaque joueur on va choisir la meilleure strategie qu'il trouve meilleur pour lui
        comb = self.comb
        nbr_stra = self.nbr_stra
        n_players = self.nplayers
        equil = []
        player = 0
        while player < n_players:
            player_comb = self.get_val_all_str(player, comb)
            print(player_comb)
            str_max = self.get_max_all_str(player, player_comb, nbr_stra)
            print(str_max)
            # equil.append(player)
            equil.append(str_max)
            # getBestStrategyAgainstRest(player,comb,nbr_stra,n_players)
            player += 1

        # print(equil)

        nash_list = self.verify_equil(equil)
        self.show_results()

    def compare_optimum_dom(self, l1, l2):
        for i in range(len(l1)):
            if l1[i] > l2[i]:
                return False
        return True

    def compare(self, l1, l2):
        for i in range(len(l1)):
            if l1[i] != l2[i]:
                return False
        return True

    def prof_pareto(self):
        print("optimum pareto (paretos dominants)")
        comb = self.comb
        nbr_stra = self.nbr_stra
        n_players = self.nplayers
        offs = []  # is a list containing strategie and it's values
        p = []
        #pay = []
        text = "profils pareto dominants : \n"
        for sub_comb in comb:
            print(sub_comb)
        #  print("ba3lolo")
            # print(sub_comb[1])
            # print(" "+str(sub_comb[0][len(sub_comb[0])-1])+" == "+str(n_players-1) )

            p.append(sub_comb[1])
            if sub_comb[0][len(sub_comb[0])-1] == n_players-1:
                l = sub_comb[0].copy()
                l.pop()
                print(" l = " + str(l))
        #       text += "strategie = "+str(l) + "\n"
                pay = []
                pay.append(l)
                pay.append(p)
                print(" gain = " + str(p))
        #        text += "gain = "+str(p) + "\n"
                offs.append(pay)
                print(" combined = " + str(pay))
                print(" list des strategies avec leurs gains = " + str(offs))
                #text += "combined = "+str(offs) + "\n"
                p = []

        copy_offs = offs.copy()
        print(offs)
        print("begin parkour")

        while len(copy_offs) > 0:
            val1 = copy_offs.pop()
            # current strategy comparing to other strategies
            strategy = val1[0]
            profil = []
            for sub in offs:
                if not self.compare(sub[0], strategy):
                    if self.compare_optimum_dom(val1[1], sub[1]):
                        profil.append(sub[0])
            print("profil dominant de la strategie " + str(strategy))
            print(profil)
            if len(profil) > 0:
                text += "\nrofil dominant de la strategie " + str(strategy)
                text += "\n "+str(profil)
            else:
                text += "\npas de pareto domin pour " + str(strategy)

        self.output = text
        self.show_results()

    def niv_sec(self):
        print("calcul de niv de securite")
        comb = self.comb
        nbr_stra = self.nbr_stra
        n_players = self.nplayers
        # pour chaque joueur on va calculer la son niveau de securite qu'il trouve meilleur pour lui
        niv_sec = []
        player = 0
        while player < n_players:
            player_comb = self.get_val_all_str(player, comb)
            print(player_comb)
            str_min = self.get_min_all_str(player, player_comb, nbr_stra)
            print(str_min)
            # equil.append(player)
            niv_sec.append(str_min)
            # getBestStrategyAgainstRest(player,comb,nbr_stra,n_players)
            player += 1
        print("les niveaux des securite de chaque joueur respectivement sont ")
        self.output = "les niveaux des securite de chaque joueur respectivement sont \n"
        print(niv_sec)
        self.output += str(niv_sec)
        self.show_results()

    def equi_mixte(self):
        print("equilibre de nash en strategies mixtes")
        comb = self.comb
        nbr_stra = self.nbr_stra
        n_players = self.nplayers
        # print(comb)
        # print(nbr_stra)
        # print(n_players)
        # expected utility of both or 3 strategies must be the same
        # create function sigmaU(player,strategy) which represents probability if player is going to play strategy
        # num of equations = num of unknowns , which can be solved
        unquit = True
        if n_players < 3:
            for i in nbr_stra:
                if i > 3:
                    print("le nombre de strategies doit etre au max 3")
                    unquit = False
                    break
            str_player1 = []
            str_player2 = []
            if unquit:
                str_player1 = self.get_val_all_str(0, comb)
                str_player2 = self.get_val_all_str(1, comb)
                print(str_player1)
                print(str_player2)
                # calculating first player probs
                sigma_p1 = self.calculateSigma(
                    str_player1, str_player2, nbr_stra)

    def calculateSigma(self, str_p1, str_p2, nbr_stra):
        print("calculating sigma ")
        sigmas = []
        # symbols_tab = []
        equations = []
        eq1 = sp.Function('eq1')
        eq2 = sp.Function('eq2')
        p = symbols('p')
        q = symbols('q')

        print("player 1 ")
        for sub in str_p1:
            print(sub)
        print("player 2 ")
        for sub in str_p2:
            print(sub)
        if nbr_stra[0] > 2:
            equations_1 = [
                Eq(str_p2[0][1] * p + str_p2[1][1] * q + (1-p-q) * str_p2[2][1], str_p2[3][1] * p + str_p2[4]
                   [1] * q + (1-p-q) * str_p2[5][1]),
                Eq(str_p2[3][1] * p + str_p2[4]
                   [1] * q + (1-p-q) * str_p2[5][1], str_p2[6][1] * p + str_p2[7][1] * q + (1-p-q) * str_p2[8][1])
            ]
        else:
            equations_1 = [
                Eq(str_p2[0][1] * p + (1-p) * str_p2[1][1], str_p2[2][1] * p + str_p2[3]
                   [1]*(1-p))
            ]

        if nbr_stra[1] > 2:
            equations_2 = [
                Eq(str_p1[0][1] * p + str_p1[1][1] * q + (1-p-q) * str_p1[2][1], str_p1[3][1] * p + str_p1[4]
                   [1] * q + (1-p-q) * str_p1[5][1]),
                Eq(str_p1[3][1] * p + str_p1[4]
                   [1] * q + (1-p-q) * str_p1[5][1], str_p1[6][1] * p + str_p1[7][1] * q + (1-p-q) * str_p1[8][1])
            ]
        else:
            equations_2 = [
                Eq(str_p1[0][1] * p + (1-p) * str_p1[1][1], str_p1[2][1] * p + str_p1[3]
                   [1]*(1-p))
            ]
        text = ""
        eqs1 = []
        eqs2 = []
        for sub in equations_1:
            eqs1.append(simplify(sub))
        for sub in equations_2:
            eqs2.append(simplify(sub))
        print(eqs1)
        print()
        print(eqs2)
        text += " premiere equation " + str(eqs1) + "\n"
        sol1 = solve(eqs1)
        sol2 = solve(eqs2)
        print("les probabilites de joueur1 sont ")
        text += "les probabilites de joueur1 sont \n"
        print(sol1)
        text += str(sol1) + "\n"
        z = 1
        if len(sol1) > 0:
            print(sol1.get(p))
            if sol1.get(q) != None:
                print(sol1.get(q))
                z -= sol1.get(p) - sol1.get(q)
                print('1-x-y = '+str(z))
            else:
                z -= sol1.get(p)
                print('1-p = '+str(z))

            text += str(z)+"\n"
        else:
            text = "pas de sol pour premier joueur \n"

        # print(q_sol)
        #z = 1-sol1[p]-sol1[q]
        # print(z)
        text += " 2eme equation " + str(eqs2) + "\n"
        print()
        print("les probabilites de joueur2 sont ")
        text += "les probabilites de joueur2 sont \n"
        print(sol2)
        text += str(sol2) + "\n"
        z = 1
        if len(sol2) > 0:
            print(sol2.get(p))
            if sol1.get(q) != None:
                print(sol2.get(q))
                z -= sol2.get(p) - sol2.get(q)
                print('1-x-y = '+str(z))
            else:
                z -= sol2.get(p)
                print('1-x = '+str(z))
            text += str(z)+"\n"
        else:
            text += "pas de sol pour deuxieme joueur \n"
        #z = 1-sol1[x]-sol1[y]
        # print(z)
        print()
        print()
        self.output = text
        self.show_results()

    def count_max_min(self, all_str, nbr_stra, player):
        mins = []
        if nbr_stra[player] > 2:
            i = 0
            l_vals = []
            for stra in all_str:
                print(stra)
                l_vals.append(stra[1])
                i += 1
                if i % 3 == 0:
                    mins.append(min(l_vals))
                    print("min of "+str(l_vals))
                    print("is ", min(l_vals))
                    l_vals = []

        else:
            i = 0
            l_vals = []
            for stra in all_str:
                print(stra)
                l_vals.append(stra[1])
                i += 1
                if i % 2 == 0:
                    mins.append(min(l_vals))
                    print("min of "+str(l_vals))
                    print("is ", min(l_vals))
                    l_vals = []

        print("found mins ")
        print(mins)
        max_min = max(mins)
        print("max _ min is : "+str(max_min))

        return max_min

    def count_min_max(self, all_str, nbr_stra, player):
        maxes = []
        if nbr_stra[player] > 2:
            i = 0
            l_vals = []
            for stra in all_str:
                print(stra)
                l_vals.append(stra[1])
                i += 1
                if i % 3 == 0:
                    maxes.append(max(l_vals))
                    print("max of "+str(l_vals))
                    print("is ", max(l_vals))
                    l_vals = []

        else:
            i = 0
            l_vals = []
            for stra in all_str:
                print(stra)
                l_vals.append(stra[1])
                i += 1
                if i % 2 == 0:
                    maxes.append(max(l_vals))
                    print("max of "+str(l_vals))
                    print("is ", max(l_vals))
                    l_vals = []

        print("found maxes ")
        print(maxes)
        min_max = min(maxes)
        print("min _ max is : "+str(min_max))

        return min_max

    def transpose_list_comb(self, all_str_j, nbr_stra, player):
        copy = all_str_j
        new_list = []
        x = 0
        for i in range(nbr_stra[player]):
            for j in range(nbr_stra[self.nplayers - player-1]):
                if x < nbr_stra[player]:
                    new_list.append(
                        all_str_j[j*nbr_stra[self.nplayers - player-1]+i])
                x += 1
        return new_list

    def count_min_max_mix(self, all_str_j, nbr_stra, player):
        print('calcul de min_max en mixte du joueur '+str(player+1))
        # SIMPLEX ALGORITHM MUST BE APLPLIED
        # simplex Algorithm
        text = 'calcul de max_min en mixte du joueur '+str(player+1)+"\n"
        if nbr_stra[player] > 2:  # if current player has 3 strategies
            # if other player has 3 strategies 3x3
            if nbr_stra[self.nplayers-player-1] > 2:
                text += "3x3 \n"
                A = np.array([
                    [all_str_j[0][1],
                        all_str_j[1][1],
                        all_str_j[2][1],
                        -1],
                    [all_str_j[3][1],
                        all_str_j[4][1],
                        all_str_j[5][1],
                        -1],
                    [all_str_j[6][1],
                        all_str_j[7][1],
                        all_str_j[8][1],
                        -1],
                    [1, 1, 1, 0],
                    [-1, -1, -1, 0]
                ])
                b = np.array([0, 0, 0, 1, -1])
                c = np.array([1, 0, 0, 0])

                res = linprog(c, A_ub=A, b_ub=b, bounds=(0, None))

                print('Optimal value:', res.fun, '\nX:', res.x)
                text += "Valeur optimal :\n"
                text += str(res.fun) + "\n"
                text += "probabilites :"
                text += str(res.x)
            else:  # if current player has 3 strategies and the other 2
                text += "3x2 \n"
                A = np.array([
                    [all_str_j[0][1],
                        all_str_j[1][1],
                        all_str_j[2][1],
                        -1],
                    [all_str_j[3][1],
                        all_str_j[4][1],
                        all_str_j[5][1],
                        -1],
                    [1, 1, 1, 0],
                    [-1, -1, -1, 0]
                ])
                b = np.array([0, 0, 1, -1])
                c = np.array([1, 0, 0, 0])

                res = linprog(c, A_ub=A, b_ub=b, bounds=(0, None))

                print('Optimal value:', res.fun, '\nX:', res.x)
                text += "Valeur optimal :\n"
                text += str(res.fun) + "\n"
                text += "probabilites :"
                text += str(res.x)
        else:  # 2x3 and 2x2
            # if other player has 3 strategies 2x3
            if nbr_stra[self.nplayers-player-1] > 2:
                text += "2x3 \n"
                A = np.array([
                    [all_str_j[0][1],
                        all_str_j[1][1],
                        -1],
                    [all_str_j[1][1],
                        all_str_j[3][1],
                        -1],
                    [all_str_j[4][1],
                        all_str_j[5][1],
                        -1],
                    [1, 1, 1, 0],
                    [-1, -1, -1, 0]
                ])
                b = np.array([0, 0, 0, 1, -1])
                c = np.array([1, 0, 0])

                res = linprog(c, A_ub=A, b_ub=b, bounds=(0, None))

                print('Optimal value:', res.fun, '\nX:', res.x)
                text += "Valeur optimal :\n"
                text += str(res.fun) + "\n"
                text += "probabilites :"
                text += str(res.x)
            else:  # if current player has 2 strategies
                # if other player has 2 strategies
                text += "2x2 \n"
                A = np.array([
                    [all_str_j[0][1],
                        all_str_j[1][1],
                        -1],
                    [all_str_j[2][1],
                        all_str_j[3][1],
                        -1],
                    [1, 1, 0],
                    [-1, -1, 0]
                ])
                b = np.array([0, 0, 0, 1, -1])
                c = np.array([1, 0, 0])

                res = linprog(c, A_ub=A, b_ub=b, bounds=(0, None))

                print('Optimal value:', res.fun, '\nX:', res.x)
                text += "Valeur optimal :\n"
                text += str(res.fun) + "\n"
                text += "probabilites :"
                text += str(res.x)
        self.output = text
        self.show_results()

    def count_max_min_mix(self, all_str_j, nbr_stra, player):

        print('calcul de max_min en mixte du joueur '+str(player+1))
        # SIMPLEX ALGORITHM MUST BE APLPLIED
        # simplex Algorithm
        text = 'calcul de max_min en mixte du joueur '+str(player+1)+"\n"

        if nbr_stra[player] > 2:  # if current player has 3 strategies
            # if other player has 3 strategies 3x3
            if nbr_stra[self.nplayers-player-1] > 2:
                text += "3x3 \n"
                A = np.array([
                    [-all_str_j[0][1],
                        -all_str_j[3][1],
                        -all_str_j[6][1],
                        1],
                    [-all_str_j[1][1],
                        -all_str_j[4][1],
                        -all_str_j[7][1],
                        1],
                    [-all_str_j[2][1],
                        -all_str_j[5][1],
                        -all_str_j[8][1],
                        1],
                    [1, 1, 1, 0],
                    [-1, -1, -1, 0]
                ])
                b = np.array([0, 0, 0, 1, -1])
                c = np.array([1, 0, 0, 0])

                res = linprog(c, A_ub=A, b_ub=b, bounds=(0, None))

                print('Optimal value:', res.fun, '\nX:', res.x)
                text += "Valeur optimal :\n"
                text += str(res.fun) + "\n"
                text += "probabilites :"
                text += str(res.x)
            else:  # 3x2
                text += "3x2 \n"
                A = np.array([
                    [-all_str_j[0][1],
                        -all_str_j[2][1],
                        -all_str_j[4][1],
                        1],
                    [-all_str_j[1][1],
                        -all_str_j[3][1],
                        -all_str_j[5][1],
                        1],
                    [1, 1, 1, 0],
                    [-1, -1, -1, 0]
                ])
                b = np.array([0, 0, 1, -1])
                c = np.array([1, 0, 0, 0])

                res = linprog(c, A_ub=A, b_ub=b, bounds=(0, None))

                print('Optimal value:', res.fun, '\nX:', res.x)
                text += "Valeur optimal :\n"
                text += str(res.fun) + "\n"
                text += "probabilites :"
                text += str(res.x)
        else:  # 2x3 and 2x2
            # if other player has 3 strategies 2x3
            if nbr_stra[self.nplayers-player-1] > 2:
                text += "2x3 \n"
                A = np.array([
                    [-all_str_j[0][1],
                        -all_str_j[3][1],
                        1],
                    [-all_str_j[1][1],
                        -all_str_j[4][1],
                        1],
                    [-all_str_j[2][1],
                        -all_str_j[5][1],
                        1],
                    [1, 1, 1, 0],
                    [-1, -1, -1, 0]
                ])
                b = np.array([0, 0, 0, 1, -1])
                c = np.array([1, 0, 0])

                res = linprog(c, A_ub=A, b_ub=b, bounds=(0, None))

                print('Optimal value:', res.fun, '\nX:', res.x)
                text += "Valeur optimal :\n"
                text += str(res.fun) + "\n"
                text += "probabilites :"
                text += str(res.x)
            else:  # if current player has 2 strategies
                # if other player has 2 strategies
                text += "2x2 \n"
                A = np.array([
                    [-all_str_j[0][1],
                        -all_str_j[2][1],
                        1],
                    [-all_str_j[1][1],
                        -all_str_j[3][1],
                        1],
                    [1, 1, 0],
                    [-1, -1, 0]
                ])
                b = np.array([0, 0, 1, -1])
                c = np.array([1, 0, 0])

                res = linprog(c, A_ub=A, b_ub=b, bounds=(0, None))

                print('Optimal value:', res.fun, '\nX:', res.x)
                text += "Valeur optimal :\n"
                text += str(res.fun) + "\n"
                text += "probabilites :"
                text += str(res.x)
        self.output = text
        self.show_results()

    def val_null_sum(self):
        print(" verification de la valeur du jeu a somme null")
        comb = self.comb
        nbr_stra = self.nbr_stra
        n_players = self.nplayers
        # the game must be a zero sum.
        # each player expected utility in EN = 0
        # the value in pure strategy is when minmax(p1) = maxmin(p2)
        # else it has to be mixed
        all_str_j = self.get_val_all_str(0, comb)
        print("les vals du tableau joueur 1")
        print(all_str_j)

        minmax = self.count_max_min(all_str_j, nbr_stra, 0)
        # transposing
        all_str_j2 = self.transpose_list_comb(all_str_j, nbr_stra, 1)
        print("les vals du tableau joueur 2")
        print(all_str_j2)
        maxmin = self.count_min_max(all_str_j2, nbr_stra, 0)
        diff = maxmin-minmax
        text = "minmax = "+str(minmax) + "maxmin = "+str(maxmin)
        self.output = text
        self.show_results()
        if diff == 0:
            print("point selle exist est "+str(maxmin))
            text = "point selle exist est "+str(maxmin) + "\n"
        else:
            print("strategie mixte")
            # pour J 1 arg max min f(o1,y)
            # pour J 2 arg min max f(x,o2)
            max_min = self.count_max_min_mix(all_str_j, nbr_stra, 0)
            min_max = self.count_max_min_mix(all_str_j, nbr_stra, 1)
            #text = "point selle exist est "+str(maxmin) + "\n"


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
