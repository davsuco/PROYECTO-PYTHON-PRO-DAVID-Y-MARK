from PyQt5.QtWidgets import QWidget, QLabel, QRadioButton, QPushButton, QVBoxLayout, QMessageBox, QButtonGroup
# Importamos la ventana de resultados para mostrar el final
from ventana_resultados import VentanaResultados

class VentanaEvaluacion(QWidget):
    def __init__(self, nombre_usuario, modulo_seleccionado):
        super().__init__()
        # Guardamos los datos recibidos en variables de la clase
        self.usuario = nombre_usuario
        self.modulo = modulo_seleccionado

        # Variables para controlar el progreso del cuestionario
        self.indice_pregunta = 0
        self.respuestas_correctas = 0

        # Diccionario con las preguntas según el módulo seleccionado
        self.banco_preguntas = {
            "Seguridad e Higiene": [
                {"pregunta": "¿Qué color indica obligación en los carteles de seguridad?", "opciones": ["Azul", "Rojo", "Amarillo"], "correcta": "Azul"},
                {"pregunta": "¿Qué se debe hacer en caso de evacuación?", "opciones": ["Usar el ascensor", "Salir en orden por la salida de emergencia", "Correr gritando"], "correcta": "Salir en orden por la salida de emergencia"}
            ],
            "Atención al Cliente": [
                {"pregunta": "¿Cuál es el primer paso al recibir una queja?", "opciones": ["Discutir con el cliente", "Escuchar activamente con empatía", "Ignorar el problema"], "correcta": "Escuchar activamente con empatía"},
                {"pregunta": "¿Qué significa una comunicación asertiva?", "opciones": ["Hablar fuerte", "Expresarse de forma clara y respetuosa", "Darle siempre la razón al cliente"], "correcta": "Expresarse de forma clara y respetuosa"}
            ]
        }

        # Obtenemos la lista de preguntas específica para este módulo
        self.preguntas_actuales = self.banco_preguntas[self.modulo]

        self.inicializar_ui()

    def inicializar_ui(self):
        self.setWindowTitle(f"Evaluación: {self.modulo}")
        self.setGeometry(100, 100, 400, 300)

        # Componentes de la interfaz
        self.etiqueta_saludo = QLabel(f"Empleado: {self.usuario}")
        self.etiqueta_pregunta = QLabel("")

        # Opciones de respuesta (Radio Buttons)
        self.opcion1 = QRadioButton("")
        self.opcion2 = QRadioButton("")
        self.opcion3 = QRadioButton("")

        # Grupo para que solo se pueda marcar una opción a la vez
        self.grupo_opciones = QButtonGroup()
        self.grupo_opciones.addButton(self.opcion1)
        self.grupo_opciones.addButton(self.opcion2)
        self.grupo_opciones.addButton(self.opcion3)

        self.boton_siguiente = QPushButton("Siguiente Pregunta")
        self.boton_siguiente.clicked.connect(self.procesar_respuesta)

        # Diseño
        diseno = QVBoxLayout()
        diseno.addWidget(self.etiqueta_saludo)
        diseno.addWidget(self.etiqueta_pregunta)
        diseno.addWidget(self.opcion1)
        diseno.addWidget(self.opcion2)
        diseno.addWidget(self.opcion3)
        diseno.addWidget(self.boton_siguiente)
        self.setLayout(diseno)

        # Mostrar la primera pregunta al cargar la ventana
        self.cargar_pregunta()

    def cargar_pregunta(self):
        # Limpiar la selección anterior
        self.grupo_opciones.setExclusive(False)
        self.opcion1.setChecked(False)
        self.opcion2.setChecked(False)
        self.opcion3.setChecked(False)
        self.grupo_opciones.setExclusive(True)

        # Obtener los datos de la pregunta actual
        datos_pregunta = self.preguntas_actuales[self.indice_pregunta]
        self.etiqueta_pregunta.setText(datos_pregunta["pregunta"])
        self.opcion1.setText(datos_pregunta["opciones"][0])
        self.opcion2.setText(datos_pregunta["opciones"][1])
        self.opcion3.setText(datos_pregunta["opciones"][2])

    def procesar_respuesta(self):
        # Verificar cuál opción fue seleccionada
        opcion_seleccionada = ""
        if self.opcion1.isChecked():
            opcion_seleccionada = self.opcion1.text()
        elif self.opcion2.isChecked():
            opcion_seleccionada = self.opcion2.text()
        elif self.opcion3.isChecked():
            opcion_seleccionada = self.opcion3.text()

        # Si no seleccionó nada, lanzar advertencia
        if opcion_seleccionada == "":
            QMessageBox.warning(self, "Advertencia", "Por favor, selecciona una respuesta.")
            return

        # Verificar si es correcta
        respuesta_correcta = self.preguntas_actuales[self.indice_pregunta]["correcta"]
        if opcion_seleccionada == respuesta_correcta:
            self.respuestas_correctas += 1

        # Avanzar a la siguiente pregunta o terminar
        self.indice_pregunta += 1
        if self.indice_pregunta < len(self.preguntas_actuales):
            self.cargar_pregunta()
        else:
            # Calcular puntaje final (sobre 100 puntos)
            puntaje_final = (self.respuestas_correctas / len(self.preguntas_actuales)) * 100

            # Abrir la Ventana 3 enviando los resultados obtenidos
            self.ventana_res = VentanaResultados(self.usuario, self.modulo, puntaje_final)
            self.ventana_res.show()
            self.close()