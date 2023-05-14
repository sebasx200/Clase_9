from PyQt5.QtGui import QPixmap, QFont
from PyQt5.QtWidgets import QMainWindow, QDesktopWidget, QLabel, QVBoxLayout, QScrollArea, QTableWidget, \
    QTableWidgetItem, QPushButton
from PyQt5 import QtGui
from cliente import Cliente

class Ventana3(QMainWindow):

    def __init__(self, anterior):
        super(Ventana3, self).__init__(anterior)

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
        self.imagenFondo = QPixmap("imagenes/img_1.png")
        self.fondo.setPixmap(self.imagenFondo)
        self.fondo.setScaledContents(True)
        self.resize(self.imagenFondo.width(), self.imagenFondo.height())

        self.setCentralWidget(self.fondo)

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

        self.vertical = QVBoxLayout()

        self.letrero1 = QLabel()

        self.letrero1.setText("                                Usuarios Registrados")

        self.letrero1.setFont(QFont("Comic Sans MS", 20))

        self.letrero1.setStyleSheet(" color: #FFFFFF;")

        self.vertical.addWidget(self.letrero1)

        self.vertical.addStretch()

        self.scrollArea = QScrollArea()

        self.scrollArea.setWidgetResizable(True)

        self.tabla = QTableWidget()

        self.tabla.setColumnCount(11)

        self.tabla.setColumnWidth(0, 150)
        self.tabla.setColumnWidth(1, 150)
        self.tabla.setColumnWidth(2, 150)
        self.tabla.setColumnWidth(3, 150)
        self.tabla.setColumnWidth(4, 150)
        self.tabla.setColumnWidth(5, 150)
        self.tabla.setColumnWidth(6, 150)
        self.tabla.setColumnWidth(7, 150)
        self.tabla.setColumnWidth(8, 150)
        self.tabla.setColumnWidth(9, 150)
        self.tabla.setColumnWidth(10, 150)

        self.tabla.setHorizontalHeaderLabels(['Nombre',
                                              'Usuario',
                                              'Contraseña',
                                              'Documento',
                                              'Correo',
                                              'Pregunta 1',
                                              'Respuesta 1',
                                              'Pregunta 2',
                                              'Respuesta 2',
                                              'Pregunta 3',
                                              'Respuesta 3'])

        self.tabla.setRowCount(self.numeroUsuarios)

        for u in self.usuarios:
            self.tabla.setItem(self.contador, 0 , QTableWidgetItem(u.nombreCompleto))
            self.tabla.setItem(self.contador, 1, QTableWidgetItem(u.usuario))
            self.tabla.setItem(self.contador, 2, QTableWidgetItem(u.contraseña))
            self.tabla.setItem(self.contador, 3, QTableWidgetItem(u.documento))
            self.tabla.setItem(self.contador, 4, QTableWidgetItem(u.correo))
            self.tabla.setItem(self.contador, 5, QTableWidgetItem(u.pregunta1))
            self.tabla.setItem(self.contador, 6, QTableWidgetItem(u.respuesta1))
            self.tabla.setItem(self.contador, 7, QTableWidgetItem(u.pregunta2))
            self.tabla.setItem(self.contador, 8, QTableWidgetItem(u.respuesta2))
            self.tabla.setItem(self.contador, 9, QTableWidgetItem(u.pregunta3))
            self.tabla.setItem(self.contador, 10, QTableWidgetItem(u.respuesta3))
            self.contador += 1

        self.scrollArea.setWidget(self.tabla)


        self.vertical.addWidget(self.scrollArea)

        self.vertical.addStretch()

        self.botonVolver = QPushButton("Volver")

        self.botonVolver.setFixedWidth(100)

        self.botonVolver.setStyleSheet("background-color : #FFFFFF;"
                                       "color : #000000;"
                                       "padding: 10 px;"
                                       )

        self.botonVolver.clicked.connect(self.metodo_botonVolver)

        self.vertical.addWidget(self.botonVolver)

        #-----------OJO PONER AL FINAL DIOS MIO-------------
        self.fondo.setLayout(self.vertical)


    def metodo_botonVolver(self):
        self.hide()
        self.ventanaAnterior.show()

