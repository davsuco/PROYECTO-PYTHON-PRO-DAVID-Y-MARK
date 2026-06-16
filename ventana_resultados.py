from PyQt5.QtWidgets import QWidget, QLabel, QPushButton, QVBoxLayout

class VentanaResultados(QWidget):
    def __init__(self, nombre_usuario, modulo_seleccionado, puntaje):
        super().__init__()
        self.usuario = nombre_usuario
        self.modulo = modulo_seleccionado
        self.puntaje = puntaje

        self.inicializar_ui()

    def inicializar_ui(self):
        self.setWindowTitle("Resultado de la Evaluación")
        self.setGeometry(100, 100, 350, 250)

        # Etiquetas de información general
        self.etiqueta_titulo = QLabel("--- RESULTADO DE EVALUACIÓN ---")
        self.etiqueta_info = QLabel(f"Empleado: {self.usuario}\nMódulo: {self.modulo}\nPuntaje: {self.puntaje}%")

        self.etiqueta_estado = QLabel("")
        self.etiqueta_comprobante = QLabel("")

        # Lógica para determinar si aprobó (nota mayor o igual a 70%)
        if self.puntaje >= 70:
            self.etiqueta_estado.setText("ESTADO: ¡APROBADO!")
            self.etiqueta_comprobante.setText("COMPROBANTE GENERADO:\nCertificado de capacitación emitido con éxito.")
        else:
            self.etiqueta_estado.setText("ESTADO: REPROBADO")
            self.etiqueta_comprobante.setText(f"Debes repasar el contenido del módulo:\n-> {self.modulo}")

        # Botón para cerrar sesión y volver a la ventana 1
        self.boton_cerrar_sesion = QPushButton("Cerrar Sesión")
        self.boton_cerrar_sesion.clicked.connect(self.volver_al_login)

        # Diseño y empaquetado
        diseno = QVBoxLayout()
        diseno.addWidget(self.etiqueta_titulo)
        diseno.addWidget(self.etiqueta_info)
        diseno.addWidget(self.etiqueta_estado)
        diseno.addWidget(self.etiqueta_comprobante)
        diseno.addWidget(self.boton_cerrar_sesion)
        self.setLayout(diseno)

    def volver_al_login(self):
        # Importación local para evitar un "error de importación circular"
        # (ya que login importa a evaluacion, evaluacion a resultados, y resultados a login)
        from ventana_login import VentanaLogin

        self.nueva_sesion = VentanaLogin()
        self.nueva_sesion.show()
        self.close()