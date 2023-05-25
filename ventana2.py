import sys

from PyQt5.QtGui import QPixmap, QFont
from PyQt5.QtWidgets import QMainWindow, QDesktopWidget, QLabel, QVBoxLayout, QScrollArea, QWidget, QGridLayout, \
    QButtonGroup, QPushButton, QApplication
from PyQt5 import QtGui
from ventana3 import Ventana3
from cliente import Cliente
import math
from ventana4 import Ventana4


class Ventana2(QMainWindow):

    def __init__(self, anterior):
        super(Ventana2, self).__init__(anterior)

        self.ventanaAnterior = anterior

        self.setWindowTitle("Usuarios Registrados")

        self.setWindowIcon(QtGui.QIcon("imagenes/descarga.png"))
        self.ancho = 1200
        self.alto = 800

        self.resize(self.ancho, self.alto)

        self.pantalla = self.frameGeometry()
        self.centro = QDesktopWidget().availableGeometry().center()
        self.pantalla.moveCenter(self.centro)
        self.move(self.pantalla.topLeft())

        self.setFixedWidth(self.ancho)
        self.setFixedHeight(self.alto)

        self.fondo = QLabel(self)
        self.imagenFondo = QPixmap("imagenes/img.png")
        self.fondo.setPixmap(self.imagenFondo)
        self.fondo.setScaledContents(True)
        self.resize(self.imagenFondo.width(), self.imagenFondo.height())

        self.setCentralWidget(self.fondo)

        self.vertical = QVBoxLayout()

        self.letrero1 = QLabel()

        self.letrero1.setText("                      Usuarios Registrados")

        self.letrero1.setFont(QFont("Comic Sans MS", 20))

        self.letrero1.setStyleSheet(" color: #000000;")

        self.vertical.addWidget(self.letrero1)

        self.vertical.addStretch()

        self.scrollArea = QScrollArea()

        self.scrollArea.setStyleSheet("background-color : transparent;")

        self.scrollArea.setWidgetResizable(True)

        self.contenedora = QWidget()

        self.cuadricula = QGridLayout(self.contenedora)

        self.scrollArea.setWidget(self.contenedora)

        self.vertical.addWidget(self.scrollArea)

        self.file = open('datos/clientes.txt', 'rb')

        self.usuarios = []

        while self.file:
            linea = self.file.readline().decode('UTF-8')

            # obtenemos del string una lista con 11 datos separados por ;
            lista = linea.split(";")
            # se para si ya no hay mas registros en el archivo
            if linea == '':
                break

            # creamos un objeto tipo cliente llamado u
            u = Cliente(
                lista[0],
                lista[1],
                lista[2],
                lista[3],
                lista[4],
                lista[5],
                lista[6],
                lista[7],
                lista[8],
                lista[9],
                lista[10],
            )

            # METEMOS EL OBJETO EN LA LISTA DE USUARIOS
            self.usuarios.append(u)

        # cerramos el archivo
        self.file.close()

        # En este punto tenemos la lista usuarios con todos los usuarios

        self.numeroUsuarios = len(self.usuarios)

        self.contador = 0

        self.elementosPorColumna = 2

        self.numeroFilas = math.ceil(self.numeroUsuarios / self.elementosPorColumna) + 1

        self.botones = QButtonGroup()

        self.botones.setExclusive(False)

        for fila in range(1, self.numeroFilas):
            for columna in range(1, self.elementosPorColumna + 1):

                if self.contador < self.numeroUsuarios:

                    self.ventanaAuxiliar = QWidget()

                    self.ventanaAuxiliar.setFixedWidth(200)
                    self.ventanaAuxiliar.setFixedHeight(100)

                    self.verticalCuadricula = QVBoxLayout()

                    self.botonAccion = QPushButton(self.usuarios[self.contador].documento)

                    self.botonAccion.setFixedWidth(150)

                    self.botonAccion.setStyleSheet("background-color : #000000;"
                                                   "color : #FFFFFF;"
                                                   "padding: 10 px;"
                                                   )

                    self.verticalCuadricula.addWidget(self.botonAccion)

                    self.botones.addButton(self.botonAccion, int(self.usuarios[self.contador].documento))

                    self.verticalCuadricula.addStretch()

                    self.ventanaAuxiliar.setLayout(self.verticalCuadricula)

                    self.cuadricula.addWidget(self.ventanaAuxiliar, fila, columna)

                    self.contador += 1

        self.botones.idClicked.connect(self.metodo_accionBotones)

        self.botonFormaTabular = QPushButton("Forma Tabular")

        self.botonFormaTabular.setFixedWidth(125)

        self.botonFormaTabular.setStyleSheet("background-color : #000000;"
                                       "color : #FFFFFF;"
                                       "padding: 10 px;"
                                       )

        self.botonFormaTabular.clicked.connect(self.metodo_botonFormaTabular)

        self.vertical.addWidget(self.botonFormaTabular)

        self.botonVolver = QPushButton("Volver")

        self.botonVolver.setFixedWidth(100)

        self.botonVolver.setStyleSheet("background-color : #000000;"
                                                   "color : #FFFFFF;"
                                                   "padding: 10 px;"
                                                   )

        self.botonVolver.clicked.connect(self.metodo_botonVolver)

        self.vertical.addWidget(self.botonVolver)



        #-----------OJO PONER AL FINAL QUE BENDICION------------

        self.fondo.setLayout(self.vertical)

    def metodo_accionBotones(self, documento):
        #print(documento)
        self.hide()
        self.ventana4 = Ventana4(self, documento)
        self.ventana4.show()

    def metodo_botonVolver(self):
        self.hide()
        self.ventanaAnterior.show()

    def metodo_botonFormaTabular(self):
        self.hide()
        self.ventana3 = Ventana3(self)
        self.ventana3.show()

if __name__ == '__main__':

    # hacer que la aplicacion se genere
    app = QApplication(sys.argv)

    # crear un objeto de tipo Ventana1 con el nombre ventana1
    ventana2 = Ventana2()

    # hacer que el objeto ventana1 se vea
    ventana2.show()

    # codigo para terminar la aplicacion
    sys.exit(app.exec_())
