import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QComboBox, QPushButton, QVBoxLayout, QMessageBox
from ventana_evaluacion import VentanaEvaluacion

class VentanaLogin(QWidget):
    def __init__(self):
        super().__init__()
        self.inicializar_ui()

    def inicializar_ui(self):
        self.setWindowTitle("Capacitación Corporativa - Ingreso")
        self.setGeometry(100, 100, 450, 350) # Letra más grande

        # --- ESTILO CSS (QSS) PARA EL FONDO DEGRADADO ---
        self.setStyleSheet("""
            QWidget {
                background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #1b365d, stop:1 #4b779a);
                color: white;
                font-size: 16px;
            }
            QLabel {
                font-weight: bold;
                background: transparent;
            }
            QLineEdit, QComboBox {
                background-color: white;
                color: black;
                border: 1px solid #cccccc;
                border-radius: 4px;
                padding: 5px;
            }
            QPushButton {
                background-color: #2a9d8f;
                color: white;
                font-weight: bold;
                border-radius: 5px;
                padding: 10px;
            }
            QPushButton:hover {
                background-color: #264653;
            }
        """)

        # Componentes de la interfaz
        self.etiqueta_nombre = QLabel("Ingresa tu Nombre Completo:")
        self.entrada_nombre = QLineEdit()

        self.etiqueta_modulo = QLabel("Selecciona el Módulo de Capacitación:")
        self.combo_modulo = QComboBox()
        # Añadidos los nuevos módulos solicitados
        self.combo_modulo.addItems([
            "Seguridad e Higiene",
            "Atención al Cliente",
            "Ciberseguridad",
            "Liderazgo",
            "Protección de Datos"
        ])

        self.boton_ingresar = QPushButton("Comenzar Evaluación")
        self.boton_ingresar.clicked.connect(self.ingresar_a_evaluacion)

        # Diseño
        diseno = QVBoxLayout()
        diseno.setSpacing(15) # Espacio entre elementos
        diseno.addWidget(self.etiqueta_nombre)
        diseno.addWidget(self.entrada_nombre)
        diseno.addWidget(self.etiqueta_modulo)
        diseno.addWidget(self.combo_modulo)
        diseno.addWidget(self.boton_ingresar)

        self.setLayout(diseno)

    def ingresar_a_evaluacion(self):
        nombre = self.entrada_nombre.text().strip()
        modulo = self.combo_modulo.currentText()

        if nombre == "":
            QMessageBox.warning(self, "Error", "Por favor, ingresa tu nombre.")
        else:
            self.ventana_eval = VentanaEvaluacion(nombre, modulo)
            self.ventana_eval.show()
            self.close()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = VentanaLogin()
    ventana.show()
    sys.exit(app.exec_())