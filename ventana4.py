from PyQt5.QtGui import QPixmap, QFont
from PyQt5.QtWidgets import QMainWindow, QDesktopWidget, QLabel, QHBoxLayout, QFormLayout, QLineEdit, QPushButton, \
    QDialog, QDialogButtonBox, QVBoxLayout
from PyQt5 import QtGui, QtCore
from PyQt5.QtCore import Qt
from cliente import Cliente

class Ventana4(QMainWindow):
    def __init__(self, anterior, documento):
        super(Ventana4, self).__init__(None)

        self.ventanaAnterior = anterior

        self.Documento = documento

        self.setWindowTitle("Editar usuario")

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

        self.fondo.setStyleSheet("background-color: #00868B")

        self.setCentralWidget(self.fondo)

        self.horizontal = QHBoxLayout()

        self.horizontal.setContentsMargins(30,30,30,30)

        # layout izquierdo

        self.ladoIzquierdo = QFormLayout()

        self.letrero1 = QLabel("Editar cliente")
        self.letrero1.setFont(QFont("Comic Sans MS", 18))
        self.letrero1.setStyleSheet("color: #000000;"
                                    "background-color: #FFFFFF;")
        self.ladoIzquierdo.addRow(self.letrero1)



        # letrero 2 QUE MARAVILLA
        self.letrero2 = QLabel()
        self.letrero2.setText("Por favor ingrese la información del cliente"
                              "\nen el formulario de abajo. Los campos marcados"
                              "\ncon asterisco * son obligatorios")
        self.letrero2.setFont(QFont("Comic Sans MS", 11))
        self.letrero2.setStyleSheet("color: #000000;"
                                    "background-color: #FFFFFF;")
        self.ladoIzquierdo.addRow(self.letrero2)

        self.nombreCompleto = QLineEdit()
        self.nombreCompleto.setFixedWidth(250)

        self.ladoIzquierdo.addRow("Nombre completo *", self.nombreCompleto)

        self.usuario = QLineEdit()
        self.usuario.setFixedWidth(250)

        self.ladoIzquierdo.addRow("Usuario *", self.usuario)

        self.contraseña = QLineEdit()
        self.contraseña.setFixedWidth(250)
        self.contraseña.setEchoMode(QLineEdit.Password)

        self.ladoIzquierdo.addRow("Contraseña *", self.contraseña)

        self.contraseña2 = QLineEdit()
        self.contraseña2.setFixedWidth(250)
        self.contraseña2.setEchoMode(QLineEdit.Password)

        self.ladoIzquierdo.addRow("Confirme contraseña *", self.contraseña2)

        self.documento = QLineEdit()
        self.documento.setFixedWidth(250)

        self.ladoIzquierdo.addRow("Documento *", self.documento)

        self.correo = QLineEdit()
        self.correo.setFixedWidth(250)
        self.correo.setStyleSheet("margin-bottom: 25px")

        self.ladoIzquierdo.addRow("Correo electrónico *", self.correo)

        # BOTON EDITAR
        self.botonEditar = QPushButton("Editar")
        self.botonEditar.setFixedWidth(120)
        self.botonEditar.setFont(QFont("Comic Sans MS", 12))
        self.botonEditar.setStyleSheet("background-color: #000000; color: #E6E6FA; padding: 5px;")

        self.botonEditar.clicked.connect(self.accion_botonEditar)

        # BOTON LIMPIAR
        self.botonLimpiar = QPushButton("Limpiar")
        self.botonLimpiar.setFixedWidth(120)
        self.botonLimpiar.setFont(QFont("Comic Sans MS", 12))
        self.botonLimpiar.setStyleSheet("background-color: #000000; color: #E6E6FA; padding: 5px;"
                                        )

        self.botonLimpiar.clicked.connect(self.accion_botonLimpiar)

        self.ladoIzquierdo.addRow(self.botonEditar, self.botonLimpiar)

        # BOTON ELIMINAR
        self.botonEliminar = QPushButton("Eliminar")
        self.botonEliminar.setFixedWidth(120)
        self.botonEliminar.setFont(QFont("Comic Sans MS", 12))
        self.botonEliminar.setStyleSheet("background-color: #000000; color: #E6E6FA; padding: 5px;")

        self.botonEliminar.clicked.connect(self.accion_botonEliminar)

        self.ladoIzquierdo.addRow(self.botonEliminar)

        # BOTON VOLVER
        self.botonVolver = QPushButton("Volver")
        self.botonVolver.setFixedWidth(120)
        self.botonVolver.setFont(QFont("Comic Sans MS", 12))
        self.botonVolver.setStyleSheet("background-color : #000000;"
                                       "color : #FFFFFF;"
                                       )

        self.botonVolver.clicked.connect(self.accion_botonVolver)

        self.ladoIzquierdo.addRow(self.botonVolver)

        self.horizontal.addLayout(self.ladoIzquierdo)

        # Lado Derecho

        self.ladoDerecho = QFormLayout()
        self.ladoDerecho.setContentsMargins(100, 0, 0, 0)

        self.letrero3 = QLabel("Editar Recuperar contraseña")
        self.letrero3.setFont(QFont("Comic Sans MS", 18))
        self.letrero3.setStyleSheet("color: #000000;"
                                    "background-color: #FFFFFF;")
        self.ladoDerecho.addRow(self.letrero3)

        self.letrero4 = QLabel()
        self.letrero4.setText("Por favor ingrese la información para recuperar"
                              "\nla contraseña. Los campos marcados"
                              "\ncon asterisco * son obligatorios.")
        self.letrero4.setFont(QFont("Comic Sans MS", 11))
        self.letrero4.setStyleSheet("color: #000000;"
                                    "background-color:#FFFFFF;")

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

        self.horizontal.addLayout(self.ladoDerecho)

        # OJO PONER AL FINAL JJ NIÑO LADRON
        self.fondo.setLayout(self.horizontal)

    # ------------------CONSTRUCCION DE LA VENTANA EMERGENTE--------------------

        self.ventanaDialogo = QDialog(None, QtCore.Qt.WindowSystemMenuHint | QtCore.Qt.WindowTitleHint)
        self.ventanaDialogo.resize(300, 150)

        # Botón aceptar------------------------------

        self.botonAceptar = QDialogButtonBox.Ok
        self.opcionesBotones = QDialogButtonBox(self.botonAceptar)
        self.opcionesBotones.accepted.connect(self.ventanaDialogo.accept)

    # ----------------------------------------------------------------------------

        self.ventanaDialogo.setWindowModality(Qt.ApplicationModal)

        self.vertical = QVBoxLayout()

        self.mensaje = QLabel("")
        self.mensaje.setStyleSheet("background-color: #6959CD; color: #E6E6FA; padding: 5px;"
                                   "border-radius:10px")
        self.mensaje.setFont(QFont("Comic Sans MS", 10))

        self.vertical.addWidget(self.mensaje)
        self.vertical.addWidget(self.opcionesBotones)
        self.ventanaDialogo.setLayout(self.vertical)

        self.cargar_datos()

    def accion_botonEditar(self):
        self.datosCorrectos = True

        self.ventanaDialogo.setWindowTitle("Formulario de edicion")

        if(
            self.contraseña.text() != self.contraseña2.text()
        ):
            self.datosCorrectos = False

            self.mensaje.setText("Las contraseñas no coinciden")

            self.ventanaDialogo.exec_()

        if(
                self.nombreCompleto.text() == ''
                or self.usuario.text() == ''
                or self.contraseña.text() == ''
                or self.contraseña2.text() == ''
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

            self.mensaje.setText("Debe seleccionar un usuario con un documento valido!")

            self.ventanaDialogo.exec_()

            self.accion_botonVolver()

        if self.datosCorrectos:

            self.file = open('datos/clientes.txt', 'rb')

            usuarios = []

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
                usuarios.append(u)

            # cerramos el archivo
            self.file.close()

            existeDocumento = False

            for u in usuarios:
                if int(u.documento) == self.Documento:
                    u.usuario = self.usuario.text()
                    u.contraseña = self.contraseña.text()
                    u.correo = self.correo.text()
                    u.pregunta1 = self.pregunta1.text()
                    u.respuesta1 = self.Respuestapregunta1.text()
                    u.pregunta2 = self.pregunta2.text()
                    u.respuesta2 = self.Respuestapregunta2.text()
                    u.pregunta3 = self.pregunta3.text()
                    u.respuesta3 = self.Respuestapregunta3.text()

                    existeDocumento = True
                    break

            if (
                    not existeDocumento
            ):
                # escribimos texto explicativo
                self.mensaje.setText("No existe un usuario con este documento:\n"
                                     + str(self.Documento))

                # hacemos que la ventana de dialogo se vea
                self.ventanaDialogo.exec_()

            self.file = open('datos/clientes.txt', 'wb')

            for u in usuarios:
                self.file.write(bytes(u.nombreCompleto + ";"
                                      + u.usuario + ";"
                                      + u.contraseña + ";"
                                      + u.documento + ";"
                                      + u.correo + ";"
                                      + u.pregunta1 + ";"
                                      + u.respuesta1 + ";"
                                      + u.pregunta2 + ";"
                                      + u.respuesta2 + ";"
                                      + u.pregunta3 + ";"
                                      + u.respuesta3, encoding='UTF-8'))
            self.file.close()

            if(
                existeDocumento
            ):
                self.mensaje.setText("Usuario actualizado correctamente!")

                self.ventanaDialogo.exec_()

                self.accion_botonLimpiar()

                self.accion_botonVolver()

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
        self.contraseña.setText('')
        self.contraseña2.setText('')
        self.documento.setText('')
        self.correo.setText('')
        self.pregunta1.setText('')
        self.pregunta2.setText('')
        self.pregunta3.setText('')
        self.Respuestapregunta1.setText('')
        self.Respuestapregunta2.setText('')
        self.Respuestapregunta3.setText('')

    def accion_botonEliminar(self):
        self.datosCorrectos = True

        self.eliminar = False

        if (
                self.nombreCompleto.text() == ''
                or self.usuario.text() == ''
                or self.contraseña.text() == ''
                or self.contraseña2.text() == ''
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

            self.mensaje.setText("Debe seleccionar un usuario con un documento valido!")

            self.ventanaDialogo.exec_()

            self.accion_botonVolver()

        if self.datosCorrectos:



            # ------------------CONSTRUCCION DE LA VENTANA EMERGENTE--------------------

            self.ventanaDialogoEliminar = QDialog(None, QtCore.Qt.WindowSystemMenuHint | QtCore.Qt.WindowTitleHint)
            self.ventanaDialogoEliminar.resize(300, 150)

            self.ventanaDialogoEliminar.setWindowModality(Qt.ApplicationModal)

            self.verticalEliminar = QVBoxLayout()


            self.mensajeEliminar = QLabel("¿Está seguro que desea eliminar este registro de usuario?")
            self.mensajeEliminar.setStyleSheet("background-color: #6959CD; color: #E6E6FA; padding: 5px;"
                                       "border-radius:10px")
            self.mensajeEliminar.setFont(QFont("Comic Sans MS", 10))

            self.verticalEliminar.addWidget(self.mensajeEliminar)

            self.opcionesEliminar = QDialogButtonBox.Ok | QDialogButtonBox.Cancel
            self.opcionesBox = QDialogButtonBox(self.opcionesEliminar)


            self.opcionesBox.accepted.connect(self.ok_opcion)
            self.opcionesBox.rejected.connect(self.cancel_opcion)



            self.verticalEliminar.addWidget(self.opcionesBox)

            self.ventanaDialogoEliminar.setLayout(self.verticalEliminar)

            self.ventanaDialogoEliminar.exec_()

        if self.eliminar:
            self.file = open('datos/clientes.txt', 'rb')

            usuarios = []

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
                usuarios.append(u)

            # cerramos el archivo
            self.file.close()

            existeDocumento = False

            for u in usuarios:
                if int(u.documento) == self.Documento:
                    usuarios.remove(u)
                    existeDocumento = True
                    break

            self.file = open('datos/clientes.txt', 'wb')

            for u in usuarios:
                self.file.write(bytes(u.nombreCompleto + ";"
                                      + u.usuario + ";"
                                      + u.contraseña + ";"
                                      + u.documento + ";"
                                      + u.correo + ";"
                                      + u.pregunta1 + ";"
                                      + u.respuesta1 + ";"
                                      + u.pregunta2 + ";"
                                      + u.respuesta2 + ";"
                                      + u.pregunta3 + ";"
                                      + u.respuesta3, encoding='UTF-8'))
            self.file.close()

            if(
                existeDocumento
            ):
                self.mensaje.setText("Usuario eliminado exitosamente!")

                self.ventanaDialogo.exec_()

                self.accion_botonLimpiar()

                self.accion_botonVolver()


    def ok_opcion(self):
        self.ventanaDialogoEliminar.close()
        self.eliminar = True

    def cancel_opcion(self):
        self.ventanaDialogoEliminar.close()


    def accion_botonVolver(self):
        self.hide()
        self.ventanaAnterior.show()

    def cargar_datos(self):
        self.file = open('datos/clientes.txt', 'rb')

        usuarios = []

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
            usuarios.append(u)

        # cerramos el archivo
        self.file.close()

        existeDocumento = False

        for u in usuarios:
            if int(u.documento) == self.Documento:
                self.nombreCompleto.setText(u.nombreCompleto)
                self.nombreCompleto.setReadOnly(True)
                self.usuario.setText(u.usuario)
                self.contraseña.setText(u.contraseña)
                self.contraseña2.setText(u.contraseña)
                self.documento.setText(u.documento)
                self.documento.setReadOnly(True)
                self.correo.setText(u.correo)
                self.pregunta1.setText(u.pregunta1)
                self.Respuestapregunta1.setText(u.respuesta1)
                self.pregunta2.setText(u.pregunta2)
                self.Respuestapregunta2.setText(u.respuesta2)
                self.pregunta3.setText(u.pregunta3)
                self.Respuestapregunta3.setText(u.respuesta3)
                existeDocumento = True
                break

        if (
                not existeDocumento
        ):
            # escribimos texto explicativo
            self.mensaje.setText("No existe un usuario con este documento:\n"
                                 + str(self.Documento))

            # hacemos que la ventana de dialogo se vea
            self.ventanaDialogo.exec_()

            self.accion_botonVolver()




