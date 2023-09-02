from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
        QApplication, QWidget, 
        QTableWidget, QListWidget, QListWidgetItem,
        QLineEdit, QFormLayout,
        QHBoxLayout, QVBoxLayout, 
        QGroupBox, QButtonGroup, QRadioButton,  
        QPushButton, QLabel, QSpinBox)


txt_Quastion = QLineEdit('')
txt_Answer = QLineEdit('')
txt_Wrong1 = QLineEdit('')
txt_Wrong2 = QLineEdit('')
txt_Wrong3 = QLineEdit('')

layout_form = QFormLayout()

layout_form.addRow('Питання:', txt_Quastion)
layout_form.addRow('Правильна відповідь:', txt_Answer)
layout_form.addRow('НЕ правильний варіант №1:', txt_Wrong1)
layout_form.addRow('НЕ правильний варіант №2:', txt_Wrong2)
layout_form.addRow('НЕ правильний варіант №3:', txt_Wrong3)












