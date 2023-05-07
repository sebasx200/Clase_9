import sys

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap, QFont
from PyQt5.QtWidgets import QMainWindow, QLabel, QDesktopWidget, QHBoxLayout, QApplication, QFormLayout, QLineEdit, \
    QPushButton, QDialog, QDialogButtonBox, QVBoxLayout
from PyQt5 import QtGui, QtCore


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

        # Lado Derecho

        self.ladoDerecho = QFormLayout()
        self.ladoDerecho.setContentsMargins(100, 0, 0, 0)

        self.letrero3 = QLabel("Recuperar contraseña")
        self.letrero3.setFont(QFont("Comic Sans MS", 20))
        self.letrero3.setStyleSheet("color: #000080;")
        self.ladoDerecho.addRow(self.letrero3)

        self.letrero4 = QLabel()
        self.letrero4.setText("Por favor ingrese la información para recuperar"
                              "\nla contraseña. Los campos marcados"
                              "\ncon asterisco * son obligatorios.")
        self.letrero4.setFont(QFont("Comic Sans MS", 12))
        self.letrero4.setStyleSheet("color: #000080;")
        self.ladoDerecho.addRow(self.letrero4)

# ---------PREGUNTA 1-------------------------------------------

        self.letreroPregunta1 = QLabel("Pregunta de verificación 1*")
        self.ladoDerecho.addRow(self.letreroPregunta1)
        self.pregunta1 = QLineEdit()
        self.pregunta1.setFixedWidth(320)
        self.ladoDerecho.addRow(self.pregunta1)

        self.letreroPregunta1R = QLabel("Respuesta de verificación 1*")
        self.ladoDerecho.addRow(self.letreroPregunta1R)
        self.Respuestapregunta1 = QLineEdit()
        self.Respuestapregunta1.setFixedWidth(320)
        self.ladoDerecho.addRow(self.Respuestapregunta1)

# ---------PREGUNTA 2-------------------------------------------

        self.letreroPregunta2 = QLabel("Pregunta de verificación 2*")
        self.ladoDerecho.addRow(self.letreroPregunta2)
        self.pregunta2 = QLineEdit()
        self.pregunta2.setFixedWidth(320)
        self.ladoDerecho.addRow(self.pregunta2)

        self.letreroPregunta2R = QLabel("Respuesta de verificación 2*")
        self.ladoDerecho.addRow(self.letreroPregunta2R)
        self.Respuestapregunta2 = QLineEdit()
        self.Respuestapregunta2.setFixedWidth(320)
        self.ladoDerecho.addRow(self.Respuestapregunta2)

# ---------PREGUNTA 3-------------------------------------------

        self.letreroPregunta3 = QLabel("Pregunta de verificación 3*")
        self.ladoDerecho.addRow(self.letreroPregunta3)
        self.pregunta3 = QLineEdit()
        self.pregunta3.setFixedWidth(320)
        self.ladoDerecho.addRow(self.pregunta3)

        self.letreroPregunta3R = QLabel("Respuesta de verificación 3*")
        self.ladoDerecho.addRow(self.letreroPregunta3R)
        self.Respuestapregunta3 = QLineEdit()
        self.Respuestapregunta3.setFixedWidth(320)
        self.ladoDerecho.addRow(self.Respuestapregunta3)

# ---------------------------------------------------------------------------

        self.botonBuscar = QPushButton("Buscar")
        self.botonBuscar.setFixedWidth(90)
        self.botonBuscar.setFont(QFont("Comic Sans MS", 12))
        self.botonBuscar.setStyleSheet("background-color: #6495ED; color: #E6E6FA; padding: 5px;")

        self.botonBuscar.clicked.connect(self.accion_botonBuscar)

        self.botonRecuperar = QPushButton("Recuperar")
        self.botonRecuperar.setFixedWidth(90)
        self.botonRecuperar.setFont(QFont("Comic Sans MS", 12))
        self.botonRecuperar.setStyleSheet("background-color: #6495ED; color: #E6E6FA; padding: 5px;")

        self.botonLimpiar.clicked.connect(self.accion_botonRecuperar)

        self.ladoDerecho.addRow(self.botonBuscar, self.botonRecuperar)

        self.horizontal.addLayout(self.ladoDerecho)


        # Poner al final el establecimiento del layout

        self.fondo.setLayout(self.horizontal)

    def accion_botonRegistrar(self):

        self.ventanaDialogo = QDialog(None, QtCore.Qt.WindowSystemMenuHint | QtCore.Qt.WindowTitleHint)
        self.ventanaDialogo.resize(300, 150)

        # Botón aceptar------------------------------

        self.botonAceptar = QDialogButtonBox.Ok
        self.opcionesBotones = QDialogButtonBox(self.botonAceptar)
        self.opcionesBotones.accepted.connect(self.ventanaDialogo.accept)

       # ----------------------------------------------------------------------------

        self.ventanaDialogo.setWindowTitle("Validar número de empleados")
        self.ventanaDialogo.setWindowModality(Qt.ApplicationModal)

        self.vertical = QVBoxLayout()

        self.mensaje = QLabel("")
        self.mensaje.setStyleSheet("background-color: #6959CD; color: #E6E6FA; padding: 5px;"
                                   "border-radius:10px")
        self.mensaje.setFont(QFont("Comic Sans MS", 10))

        self.vertical.addWidget(self.mensaje)
        self.vertical.addWidget(self.opcionesBotones)
        self.ventanaDialogo.setLayout(self.vertical)

        self.datosCorrectos = True

        if (self.contrasena.text() != self.contrasena2.text()):

            self.datosCorrectos = False

            self.mensaje.setText("La confirmación de la contraseña no coincide")

            self.ventanaDialogo.exec_()

        if (



        self.nombreCompleto.text() == ''
        or self.usuario.text() == ''
        or self.contrasena.text() == ''
        or self.contrasena2.text() == ''
        or self.documento.text() == ''
        or self.correo.text() == ''
        or self.pregunta1.text() == ''
        or self.pregunta2.text() == ''
        or self.pregunta3.text() == ''
        or self.Respuestapregunta1.text() == ''
        or self.Respuestapregunta1.text() == ''
        or self.Respuestapregunta3.text() == ''
        ):

            self.datosCorrectos = False
            self.mensaje.setText("Debe ingresar todos los campos con *")
            self.ventanaDialogo.exec_()

        if self.datosCorrectos:

            self.file = open('datos/clientes.txt', 'ab')
            self.file.write(bytes(self.nombreCompleto.text() + ";"
                                  + self.usuario.text() + ";"
                                  + self.contrasena.text() + ";"
                                  + self.contrasena2.text() + ";"
                                  + self.documento.text() + ";"
                                  + self.correo.text() + ";"
                                  + self.pregunta1.text() + ";"
                                  + self.pregunta2.text() + ";"
                                  + self.pregunta3.text() + ";"
                                  + self.Respuestapregunta1.text() + ";"
                                  + self.Respuestapregunta2.text() + ";"
                                  + self.Respuestapregunta3.text() + "\n"
                                  , encoding = 'UTF-8'))
            self.file.close()

            self.file = open('datos/clientes.txt', 'rb')
            while self.file:
                linea = self.file.readline().decode('UTF-8')
                print(linea)
                if linea == '':
                    break
            self.file.close()




    def accion_botonLimpiar(self):
        self.nombreCompleto.setText('')
        self.usuario.setText('')
        self.contrasena.setText('')
        self.contrasena2.setText('')
        self.documento.setText('')
        self.correo.setText('')
        self.pregunta1.setText('')
        self.pregunta2.setText('')
        self.pregunta3.setText('')
        self.Respuestapregunta1.setText('')
        self.Respuestapregunta2.setText('')
        self.Respuestapregunta3.setText('')
    def accion_botonBuscar(self):
        pass

    def accion_botonRecuperar(self):
        pass

if __name__ == '__main__':

    # hacer que la aplicacion se genere
    app = QApplication(sys.argv)

    # crear un objeto de tipo Ventana1 con el nombre ventana1
    ventana1 = Ventana1()

    # hacer que el objeto ventana1 se vea
    ventana1.show()

    # codigo para terminar la aplicacion
    sys.exit(app.exec_())






