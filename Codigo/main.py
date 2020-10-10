import sys,re
from PyQt5 import uic, QtWidgets, QtGui

from PyQt5.QtWidgets import QMessageBox
from PIL import Image
qtCreatorFile = "./Interfaz_Principal/Main.ui" # Nombre del archivo aquí.
plotImg = './Interfaz_Principal/Captura.jpg'
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)
from Juego1 import Ruleta
from Juego2 import Altos_o_Bajos_Codificacionado
from Juego4 import SuperTragaPerras
from Juego5 import CapsUI
from Juego6 import casino
from Juego7 import keno
from Juego8 import Jackpot
from Recarga import menu


from PyQt5.QtChart import QChart, QChartView, QLineSeries
from PyQt5.QtCore import QPointF
from PyQt5.QtGui import QPainter
from PyQt5.QtCore import Qt




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
        self.Juego4.clicked.connect(self.runjuego4)
        self.Juego5.clicked.connect(self.runjuego5)
        self.Juego6.clicked.connect(self.runjuego6)
        self.Juego7.clicked.connect(self.runjuego7)
        self.Juego8.clicked.connect(self.runjuego8)
        # self.create_linechart()

        self._recargar.clicked.connect(self.recargar)
    def runjuego1(self):
        self.window = Ruleta.UIWindow()
        self.window.show()
    def runjuego2(self):
        self.window = Altos_o_Bajos_Codificacionado.MainWindow()
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

    # def create_linechart(self):

    #     series = QLineSeries(self)
    #     series.append(0,6)
    #     series.append(2, 4)
    #     series.append(3, 8)
    #     series.append(7, 4)
    #     series.append(10, 5)

    #     series << QPointF(11, 1) << QPointF(13, 3) << QPointF(17, 6) << QPointF(18, 3) << QPointF(20, 2)


    #     chart =  QChart()

    #     chart.addSeries(series)
    #     chart.createDefaultAxes()
    #     chart.setAnimationOptions(QChart.SeriesAnimations)
    #     chart.setTitle("Line Chart Example")

    #     chart.legend().setVisible(True)
    #     chart.legend().setAlignment(Qt.AlignBottom)


    #     chartview = QChartView(chart)
    #     chartview.setRenderHint(QPainter.Antialiasing)
    #     self._graphlayout.addWidget(self._tstpush,0,0)
    #     # self.setCentralWidget(chartview)

if __name__ == "__main__": 
    app =  QtWidgets.QApplication(sys.argv)
    window = MainW()
    window.show()
    sys.exit(app.exec_())