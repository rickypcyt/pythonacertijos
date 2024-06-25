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
    QRadioButton,
    QButtonGroup,
)

# Función para leer los acertijos desde un archivo
def leer_acertijos(nombre_archivo):
    """
    Lee los acertijos desde un archivo y los devuelve como una lista de listas.
    Cada lista contiene el acertijo y sus tres respuestas posibles.
    """
    acertijos = []
    try:
        with open(nombre_archivo, "r", encoding="utf-8") as archivo:
            for linea in archivo:
                partes = linea.strip().split(";")
                if len(partes) == 4:  # Asumiendo que cada línea tiene un acertijo y tres respuestas
                    acertijo = partes[0]
                    respuestas = partes[1:]
                    acertijos.append([acertijo] + respuestas)
                else:
                    print(f"Línea ignorada: {linea.strip()}")  # Mensaje de depuración
    except FileNotFoundError:
        print(f"Archivo no encontrado: {nombre_archivo}")
    except Exception as e:
        print(f"Error al leer el archivo: {e}")
    
    print(f"Acertijos cargados: {len(acertijos)}")  # Mensaje de depuración
    return acertijos


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Resuelve el acertijo")
        self.setGeometry(100, 100, 400, 400)
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

        self.opcion1 = QRadioButton()
        self.opcion2 = QRadioButton()
        self.opcion3 = QRadioButton()
        self.opciones_layout = QVBoxLayout()
        self.opciones_layout.addWidget(self.opcion1)
        self.opciones_layout.addWidget(self.opcion2)
        self.opciones_layout.addWidget(self.opcion3)
        layout.addLayout(self.opciones_layout)

        self.button_group = QButtonGroup()
        self.button_group.addButton(self.opcion1)
        self.button_group.addButton(self.opcion2)
        self.button_group.addButton(self.opcion3)

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
        self.opcion1.hide()
        self.opcion2.hide()
        self.opcion3.hide()
        self.boton_comprobar.hide()
        self.boton_nuevo_acertijo.hide()

        # Leer los acertijos desde el archivo
        self.acertijos = leer_acertijos("pythonacertijos/acertijos.txt")
        self.acertijo_actual = []
        self.respuestas_posibles = []

    def mostrar_nuevo_acertijo(self):
        """
        Mostrar un nuevo acertijo al azar de la lista de acertijos.
        """
        if not self.acertijos:
            QMessageBox.critical(self, "Error", "No hay acertijos disponibles.")
            return

        self.acertijo_actual = random.choice(self.acertijos)
        self.label_acertijo.setText(self.acertijo_actual[0])

        # Mostrar las respuestas posibles en los radio buttons
        self.respuestas_posibles = self.acertijo_actual[1:]
        random.shuffle(self.respuestas_posibles)

        self.opcion1.setText(self.respuestas_posibles[0])
        self.opcion2.setText(self.respuestas_posibles[1])
        self.opcion3.setText(self.respuestas_posibles[2])

        # Mostrar los elementos de los acertijos
        self.label_acertijo.show()
        self.opcion1.show()
        self.opcion2.show()
        self.opcion3.show()
        self.boton_comprobar.show()
        self.boton_nuevo_acertijo.show()

    def comprobar_respuesta(self):
        """
        Comprobar si la respuesta del usuario es correcta y mostrar un mensaje.
        """
        respuesta_seleccionada = None
        if self.opcion1.isChecked():
            respuesta_seleccionada = self.opcion1.text()
        elif self.opcion2.isChecked():
            respuesta_seleccionada = self.opcion2.text()
        elif self.opcion3.isChecked():
            respuesta_seleccionada = self.opcion3.text()

        if respuesta_seleccionada == self.acertijo_actual[1]:
            QMessageBox.information(
                self, "¡Correcto!", "¡Bien hecho! La respuesta es correcta."
            )
        else:
            QMessageBox.critical(
                self,
                "Incorrecto",
                f"Lo siento, la respuesta correcta es: {self.acertijo_actual[1]}",
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
        self.opcion1.show()
        self.opcion2.show()
        self.opcion3.show()
        self.boton_comprobar.show()
        self.boton_nuevo_acertijo.show()
        self.mostrar_nuevo_acertijo()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
