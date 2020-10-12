import sys,re
from PyQt5 import uic, QtWidgets, QtGui

from PyQt5.QtWidgets import QMessageBox
from PIL import Image
qtCreatorFile = "./Interfaz_Principal/Main.ui" # Nombre del archivo aquí.
plotImg = './Interfaz_Principal/Captura.jpg'
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)
from Juego1 import Ruleta
from Juego2 import Altos_o_Bajos_Codificacionado
from Juego3 import LootBoxGame
from Juego4 import SuperTragaPerras
from Juego5 import CapsUI
from Juego6 import casino
from Juego7 import keno
from Juego8 import Jackpot
from Recarga import menu

import bd
from PyQt5.QtChart import QChart, QChartView, QLineSeries
from PyQt5.QtCore import QPointF
from PyQt5.QtGui import QPainter
from PyQt5.QtCore import Qt,QThread, pyqtSignal
from PyQt5 import QtCore, QtGui, QtWidgets
class MainW(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.showMaximized()
        
        self.imagen.setText("aaaaaaa")
        myimg = QtGui.QPixmap(plotImg)
        self.imagen.setPixmap(myimg)
        self.Juego1.clicked.connect(self.runjuego1)
        self.Juego2.clicked.connect(self.runjuego2)
        self.Juego3.clicked.connect(self.runjuego3)
        self.Juego4.clicked.connect(self.runjuego4)
        self.Juego5.clicked.connect(self.runjuego5)
        self.Juego6.clicked.connect(self.runjuego6)
        self.Juego7.clicked.connect(self.runjuego7)
        self.Juego8.clicked.connect(self.runjuego8)
        self.setupgraph()
        self.updatechart()
        self._actualizar.clicked.connect(self.updatechart)

        self._recargar.clicked.connect(self.recargar)
    def runjuego1(self):
        self.window = Ruleta.UIWindow()
        self.window.show()
    def runjuego2(self):
        self.window = Altos_o_Bajos_Codificacionado.MainWindow()
        self.window.show()
    def runjuego3(self):
        self.window = LootBoxGame.MyApp()
        self.window.show()
    def runjuego4(self):
        self.window = SuperTragaPerras.UIWindow()
        self.window.show()
    def runjuego5(self):
        self.window = CapsUI.UIWindow()
        self.window.show()
    def runjuego6(self):
        self.window = casino.MyApp()
        self.window.show()
    def runjuego7(self):
        self.window = keno.UIWindow()
        self.window.show()
    def runjuego8(self):
        self.window = Jackpot.UIWindow()
        self.window.show()
    def recargar(self):
        self.window = menu.MyApp()
        self.window.show()


    def setupgraph(self):
        self.chart =  QChart()
        self.chart.createDefaultAxes()
        self.chart.setAnimationOptions(QChart.SeriesAnimations)
        self.chart.setTitle("Saldo vs Tiempo")
        self.chart.legend().setVisible(True)
        self.chart.legend().setAlignment(Qt.AlignBottom)
        self.chartview = QChartView(self.chart)
        self.chartview.setRenderHint(QPainter.Antialiasing)
        self._graphlayout.addWidget(self.chartview)
    def updatechart(self):
        self.series = QLineSeries(self)
        self.datos = bd.getData()
        self.c = 0
        for x in self.datos:
            self.series.append(self.c,x)
            self.c+=1
        self.chart.removeAllSeries()
        self.chart.addSeries(self.series)
        self.chart.createDefaultAxes()

    def create_linechart(self):

        self.series = QLineSeries(self)
        self.datos = bd.getData()
        self.c = 0
        for x in self.datos:
            self.series.append(self.c,x)
            self.c+=1
        self.chart =  QChart()
        self.chart.addSeries(self.series)
        self.chart.createDefaultAxes()
        self.chart.setAnimationOptions(QChart.SeriesAnimations)
        self.chart.setTitle("Saldo vs Tiempo")
        self.chart.legend().setVisible(True)
        self.chart.legend().setAlignment(Qt.AlignBottom)
        self.chartview = QChartView(self.chart)
        self.chartview.setRenderHint(QPainter.Antialiasing)
        self._graphlayout.addWidget(self.chartview)
if __name__ == "__main__":
    app =  QtWidgets.QApplication(sys.argv)
    window = MainW()
    window.show()
    sys.exit(app.exec_())