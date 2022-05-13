from PyQt5.QtCore import QRect, QSize, Qt
from PyQt5.QtGui import QFont, QIcon
from PyQt5.QtWidgets import QComboBox, QTextEdit, QLineEdit, QSpinBox, QHBoxLayout, QPushButton, QVBoxLayout, QWidget

class Caesar_ui:
    def setup_UI(self):
        
        ### Main ###
        self.setWindowTitle("Шифр Цезаря")
        self.setWindowIcon(QIcon('assets/icon.png'))
        self.setGeometry(600,100,1080,720)

        ### Widgets ###
        self.central = QWidget(self)
        self.setCentralWidget(self.central)

        self.textEdit_Input = QTextEdit()
        self.textEdit_Input.setFont(QFont("Arial", 22))

        self.textEdit_Output = QTextEdit()
        self.textEdit_Output.setFont(QFont("Arial", 22))
        self.textEdit_Output.setReadOnly(True)
        
        self.btn_translate = QPushButton('Перевести')
        self.btn_translate.clicked.connect(self.onTranslateClicked)

        self.box_mode = QComboBox()
        self.box_mode.addItems(['Зашифровать', 'Расшифровать'])

        self.spin_offset = QSpinBox()
        self.spin_offset.setMinimum(-26)
        self.spin_offset.setMaximum(26)
        self.spin_offset.setValue(1)

        ### Layouts ###

        self.lo1 = QVBoxLayout()
        self.lo1.addWidget(self.textEdit_Input)

        self.lo2 = QHBoxLayout()
        self.lo2.addWidget(self.btn_translate)
        self.lo2.addWidget(self.box_mode)
        self.lo2.addWidget(self.spin_offset)

        self.lo3 = QHBoxLayout()
        self.lo3.addWidget(self.textEdit_Output)

        self.gen_lo1 = QVBoxLayout()
        self.gen_lo1.addLayout(self.lo1)
        self.gen_lo1.addLayout(self.lo2)
        self.gen_lo1.addLayout(self.lo3)
        self.central.setLayout(self.gen_lo1)