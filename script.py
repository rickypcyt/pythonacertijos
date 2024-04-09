import sys
import random
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QLabel,
    QLineEdit,
    QPushButton,
    QMessageBox,
    QVBoxLayout,
)

# Función para leer los acertijos desde un archivo
def leer_acertijos(nombre_archivo):
    """
    Lee los acertijos desde un archivo y los devuelve como una lista de tuplas.
    Cada tupla contiene el acertijo y su solución.
    """
    acertijos = []
    with open(nombre_archivo, "r", encoding="utf-8") as archivo:
        for linea in archivo:
            acertijo, solucion = linea.strip().split(";")
            acertijos.append((acertijo, solucion))
    return acertijos


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Resuelve el acertijo")
        self.setGeometry(100, 100, 400, 300)
        self.initUI()

    def initUI(self):
        # Configurar el diseño de la ventana principal
        layout = QVBoxLayout()

        # Widgets para nombre y edad
        self.nombre_label = QLabel("¡Hola! ¿Cómo te llamas?")
        self.nombre_label.setAlignment(Qt.AlignCenter)
        self.nombre_label.setFont(QFont("Arial", 16))
        layout.addWidget(self.nombre_label)

        self.entry_nombre = QLineEdit()
        self.entry_nombre.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.entry_nombre)

        self.edad_label = QLabel("¿Cuál es tu edad?")
        self.edad_label.setAlignment(Qt.AlignCenter)
        self.edad_label.setFont(QFont("Arial", 16))
        layout.addWidget(self.edad_label)

        self.entry_edad = QLineEdit()
        self.entry_edad.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.entry_edad)

        self.boton_continuar = QPushButton("Continuar")
        self.boton_continuar.clicked.connect(self.preguntar_nombre_y_edad)
        self.boton_continuar.setFont(QFont("Arial", 14))
        layout.addWidget(self.boton_continuar)

        # Widgets para los acertijos
        self.label_acertijo = QLabel()
        self.label_acertijo.setAlignment(Qt.AlignCenter)
        self.label_acertijo.setFont(QFont("Arial", 18))
        layout.addWidget(self.label_acertijo)

        self.respuesta_usuario = QLineEdit()
        self.respuesta_usuario.setAlignment(Qt.AlignCenter)
        self.respuesta_usuario.setFont(QFont("Arial", 14))
        layout.addWidget(self.respuesta_usuario)

        self.boton_comprobar = QPushButton("Comprobar respuesta")
        self.boton_comprobar.clicked.connect(self.comprobar_respuesta)
        self.boton_comprobar.setFont(QFont("Arial", 14))
        layout.addWidget(self.boton_comprobar)

        self.boton_nuevo_acertijo = QPushButton("Nuevo acertijo")
        self.boton_nuevo_acertijo.clicked.connect(self.mostrar_nuevo_acertijo)
        self.boton_nuevo_acertijo.setFont(QFont("Arial", 14))
        layout.addWidget(self.boton_nuevo_acertijo)

        self.setLayout(layout)

        # Ocultar elementos de los acertijos al inicio
        self.label_acertijo.hide()
        self.respuesta_usuario.hide()
        self.boton_comprobar.hide()
        self.boton_nuevo_acertijo.hide()

        # Leer los acertijos desde el archivo
        self.acertijos = leer_acertijos("pythonacertijos/acertijos.txt")
        self.acertijo_actual = ""
        self.solucion_actual = ""

    def mostrar_nuevo_acertijo(self):
        """
        Mostrar un nuevo acertijo al azar de la lista de acertijos.
        """
        self.acertijo_actual, self.solucion_actual = random.choice(self.acertijos)
        self.respuesta_usuario.setText("")
        self.label_acertijo.setText(self.acertijo_actual)

    def comprobar_respuesta(self):
        """
        Comprobar si la respuesta del usuario es correcta y mostrar un mensaje.
        """
        solucion_ingresada = self.respuesta_usuario.text().strip().lower()
        if solucion_ingresada == self.solucion_actual.lower():
            QMessageBox.information(
                self, "¡Correcto!", "¡Bien hecho! La respuesta es correcta."
            )
        else:
            QMessageBox.critical(
                self,
                "Incorrecto",
                f"Lo siento, la respuesta correcta es: {self.solucion_actual}",
            )

    def preguntar_nombre_y_edad(self):
        """
        Obtener el nombre y la edad del usuario y mostrar un mensaje de bienvenida.
        """
        nombre = self.entry_nombre.text()
        edad = self.entry_edad.text()
        QMessageBox.information(
            self,
            "Bienvenido",
            f"¡Hola, {nombre}! Ya que tienes {edad} años de edad, ¿estás listo para resolver algunos acertijos?",
        )
        # Ocultar elementos de nombre y edad
        self.nombre_label.hide()
        self.entry_nombre.hide()
        self.edad_label.hide()
        self.entry_edad.hide()
        self.boton_continuar.hide()
        # Mostrar elementos de los acertijos
        self.label_acertijo.show()
        self.respuesta_usuario.show()
        self.boton_comprobar.show()
        self.boton_nuevo_acertijo.show()
        self.mostrar_nuevo_acertijo()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
