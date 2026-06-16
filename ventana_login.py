import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QComboBox, QPushButton, QVBoxLayout, QMessageBox
# Importamos la ventana de evaluación para poder abrirla después
from ventana_evaluacion import VentanaEvaluacion

class VentanaLogin(QWidget):
    def __init__(self):
        super().__init__()
        self.inicializar_ui()

    def inicializar_ui(self):
        self.setWindowTitle("Capacitación Corporativa - Ingreso")
        self.setGeometry(100, 100, 300, 250)

        # Crear los componentes de la interfaz
        self.etiqueta_nombre = QLabel("Ingresa tu Nombre Completo:")
        self.entrada_nombre = QLineEdit()

        self.etiqueta_modulo = QLabel("Selecciona el Módulo:")
        self.combo_modulo = QComboBox()
        self.combo_modulo.addItem("Seguridad e Higiene")
        self.combo_modulo.addItem("Atención al Cliente")

        self.boton_ingresar = QPushButton("Comenzar Evaluación")
        # Conectar el botón con el método para validar e ingresar
        self.boton_ingresar.clicked.connect(self.ingresar_a_evaluacion)

        # Organizar los componentes en un diseño vertical (Layout)
        diseno = QVBoxLayout()
        diseno.addWidget(self.etiqueta_nombre)
        diseno.addWidget(self.entrada_nombre)
        diseno.addWidget(self.etiqueta_modulo)
        diseno.addWidget(self.combo_modulo)
        diseno.addWidget(self.boton_ingresar)

        self.setLayout(diseno)

    def ingresar_a_evaluacion(self):
        # Capturamos el texto y lo convertimos a minúsculas para validar de forma segura
        nombre = self.entrada_nombre.text().strip()
        modulo = self.combo_modulo.currentText()

        # Validación simple: que el campo no esté vacío
        if nombre == "":
            QMessageBox.warning(self, "Error", "Por favor, ingresa tu nombre.")
        else:
            # Si el nombre es válido, abrimos la Ventana 2 pasándole los datos
            self.ventana_eval = VentanaEvaluacion(nombre, modulo)
            self.ventana_eval.show()
            self.close() # Cerramos la ventana de login actual

# Bloque principal para arrancar la aplicación desde este archivo
if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = VentanaLogin()
    ventana.show()
    sys.exit(app.exec_())