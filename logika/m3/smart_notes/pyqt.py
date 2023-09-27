from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QApplication, QWidget, QTextEdit, QLabel, 
    QListWidget, QPushButton, QLineEdit, QHBoxLayout, QVBoxLayout, QInputDialog,
    QTableWidget,  QListWidgetItem, QFormLayout, 
    QGroupBox, QButtonGroup, QRadioButton, QSpinBox)

import json

app = QApplication([])

window = QWidget()
window.show()

field_text = QTextEdit()

lb_notes = QLabel('')

btn_note_create = QPushButton()
btn_note_delete = QPushButton()
btn_note_save = QPushButton()

lb_teg = QLabel('')

lst_tags = QListWidget()

col2 = QVBoxLayout()

layout_notes = QHBoxLayout()

lst_notes = QLabel()


















col2

row1 = QHBoxLayout()
row1.addWidget(btn_note_create)
row1.addWidget(btn_note_delete)

col2.addLayout(row1)
col2.addWidget(btn_note_save)

def show_notes():
    key = lst_notes.selectedItems()[0].text()
    


# lst_notes.itemClick.connect(show_notes)

with open('smart_notes/notes.json', 'r', encoding='utf8') as file:
    notes = json.load(file)

window.setLayout(layout_notes)
window.show()
app.exec_()

