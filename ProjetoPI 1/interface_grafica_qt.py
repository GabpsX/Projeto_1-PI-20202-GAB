from PyQt5 import QtWidgets, uic

import graph_linha

import graph_barras


class tela_inicio:
    def plot_gr(self):
        self.primeira_tela.ui.show()

    def plot_1(self):
        graph_linha.apresentarGraficoDeLinha()

    def plot_2(self):
        graph_barras.apresentarGragicodeBarras()

class execut(tela_inicio):

    def __init__(self):
        self.app = QtWidgets.QApplication([])

        self.primeira_tela = uic.loadUi("primeira_tela.ui")

        self.primeira_tela.pushButton.clicked.connect(self.plot_1)

        self.primeira_tela.pushButton_2.clicked.connect(self.plot_2)

        self.primeira_tela.show()

        self.app.exec()
execut()
