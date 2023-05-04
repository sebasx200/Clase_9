import sys

from PyQt5.QtGui import QPixmap, QFont
from PyQt5.QtWidgets import QMainWindow, QLabel, QDesktopWidget, QHBoxLayout, QApplication, QFormLayout, QLineEdit, \
    QPushButton
from PyQt5 import QtGui


class Ventana1(QMainWindow):

    def __init__(self, parent = None):
        super(Ventana1, self).__init__(parent)

        self.setWindowTitle("Formulario de registro")

        self.setWindowIcon(QtGui.QIcon("imagenes/descarga.png"))
        self.ancho = 1200
        self.alto = 600

        self.resize(self.ancho, self.alto)

        self.pantalla = self.frameGeometry()
        self.centro = QDesktopWidget().availableGeometry().center()
        self.pantalla.moveCenter(self.centro)
        self.move(self.pantalla.topLeft())

        self.setFixedWidth(self.ancho)
        self.setFixedHeight(self.alto)

        self.fondo = QLabel(self)
        self.imagenFondo = QPixmap("imagenes/fondoventana.jpg")
        self.fondo.setPixmap(self.imagenFondo)
        self.fondo.setScaledContents(True)
        self.resize(self.imagenFondo.width(), self.imagenFondo.height())

        self.setCentralWidget(self.fondo)

        self.horizontal = QHBoxLayout()
        self.horizontal.setContentsMargins(20, 20, 20, 20)

        # lado izquierdo
        self.ladoIzquierdo = QFormLayout()

        self.letrero1 = QLabel("Información del cliente")
        self.letrero1.setFont(QFont("Comic Sans MS", 20))
        self.letrero1.setStyleSheet("color: #000080;")
        self.ladoIzquierdo.addRow(self.letrero1)

        self.letrero2 = QLabel()
        self.letrero2.setText("Ingrese la información del cliente"
                              "\nen el formulario de abajo. Los campos marcados"
                              "\ncon asterisco * son obligatorios")
        self.letrero2.setFont(QFont("Comic Sans MS", 12))
        self.letrero1.setStyleSheet("color: #000080;")
        self.ladoIzquierdo.addRow(self.letrero2)

        self.nombreCompleto = QLineEdit()
        self.nombreCompleto.setFixedWidth(250)

        self.ladoIzquierdo.addRow("Nombre completo *", self.nombreCompleto)

        self.usuario = QLineEdit()
        self.usuario.setFixedWidth(250)

        self.ladoIzquierdo.addRow("Usuario *", self.usuario)

        self.contrasena = QLineEdit()
        self.contrasena.setFixedWidth(250)
        self.contrasena.setEchoMode(QLineEdit.Password)

        self.ladoIzquierdo.addRow("Contraseña *", self.contrasena)

        self.contrasena2 = QLineEdit()
        self.contrasena2.setFixedWidth(250)
        self.contrasena2.setEchoMode(QLineEdit.Password)

        self.ladoIzquierdo.addRow("Confirme contraseña *", self.contrasena2)

        self.documento = QLineEdit()
        self.documento.setFixedWidth(250)

        self.ladoIzquierdo.addRow("Documento *", self.documento)

        self.correo = QLineEdit()
        self.correo.setFixedWidth(250)

        self.ladoIzquierdo.addRow("Correo electrónico *", self.correo)

        self.botonRegistrar = QPushButton("Registrar")
        self.botonRegistrar.setFixedWidth(90)
        self.botonRegistrar.setFont(QFont("Comic Sans MS", 12))
        self.botonRegistrar.setStyleSheet("background-color: #6495ED; color: #E6E6FA; padding: 5px;")

        self.botonRegistrar.clicked.connect(self.accion_botonRegistrar)

        self.botonLimpiar = QPushButton("Limpiar")
        self.botonLimpiar.setFixedWidth(90)
        self.botonLimpiar.setFont(QFont("Comic Sans MS", 12))
        self.botonLimpiar.setStyleSheet("background-color: #6495ED; color: #E6E6FA; padding: 5px;")

        self.botonLimpiar.clicked.connect(self.accion_botonLimpiar)

        self.ladoIzquierdo.addRow(self.botonRegistrar, self.botonLimpiar)

        self.horizontal.addLayout(self.ladoIzquierdo)


        # Poner al final el establecimiento del layout

        self.fondo.setLayout(self.horizontal)

    def accion_botonRegistrar(self):
        print("Boton 1")

    def accion_botonLimpiar(self):
        print("Botón 2")

if __name__ == '__main__':

    # hacer que la aplicacion se genere
    app = QApplication(sys.argv)

    # crear un objeto de tipo Ventana1 con el nombre ventana1
    ventana1 = Ventana1()

    # hacer que el objeto ventana1 se vea
    ventana1.show()

    # codigo para terminar la aplicacion
    sys.exit(app.exec_())






