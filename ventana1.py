import sys

from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QMainWindow, QLabel, QDesktopWidget, QHBoxLayout, QApplication
from PyQt5 import QtGui


class Ventana1(QMainWindow):

    def __init__(self, parent = None):
        super(Ventana1, self).__init__(parent)

        self.setWindowTitle("Formulario de registro")

        self.setWindowIcon(QtGui.QIcon("imagenes/descarga.png"))
        self.ancho = 1000
        self.alto = 600

        self.resize(self.ancho, self.alto)

        self.pantalla = self.frameGeometry()
        self.centro = QDesktopWidget().availableGeometry().center()
        self.pantalla.moveCenter(self.centro)
        self.move(self.pantalla.topLeft())

        self.setFixedWidth(self.ancho)
        self.setFixedHeight(self.alto)

        self.fondo = QLabel(self)
        self.imagenFondo = QPixmap("imagenes/fondoventana1.jpg")
        self.fondo.setPixmap(self.imagenFondo)
        self.fondo.setScaledContents(True)
        self.resize(self.imagenFondo.width(), self.imagenFondo.height())

        self.setCentralWidget(self.fondo)

        self.horizontal = QHBoxLayout()
        self.horizontal.setContentsMargins(30, 30, 30, 30)

        # Poner al final el establecimiento del layout

        self.fondo.setLayout(self.horizontal)

if __name__ == '__main__':

    # hacer que la aplicacion se genere
    app = QApplication(sys.argv)

    # crear un objeto de tipo Ventana1 con el nombre ventana1
    ventana1 = Ventana1()

    # hacer que el objeto ventana1 se vea
    ventana1.show()

    # codigo para terminar la aplicacion
    sys.exit(app.exec_())






