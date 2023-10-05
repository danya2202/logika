from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QApplication, QWidget, QTextEdit, QLabel, 
    QListWidget, QPushButton, QLineEdit, QHBoxLayout, QVBoxLayout, QInputDialog,
    QTableWidget,  QListWidgetItem, QFormLayout, 
    QGroupBox, QButtonGroup, QRadioButton, QSpinBox)

import json

def writeToFile():
    with open('notes.json', 'w', encoding='utf8') as file:
        json.dump(notes, file, ensure_ascii=False, sort_keys=True, indent=4)
app = QApplication([])

window = QWidget()
window.show()

field_text = QTextEdit()

lb_notes = QLabel('')

lst_list = QListWidget()

btn_note_create = QPushButton('створити')
btn_note_delete = QPushButton('видалити')
btn_note_save = QPushButton('зберегти')

lb_teg = QLabel('')



lst_text = QListWidget()

layout_notes = QHBoxLayout()
col1 = QVBoxLayout()
col2 = QVBoxLayout()

layout_notes.addLayout(col1, stretch=2)
layout_notes.addLayout(col2, stretch=1)

col1.addWidget(field_text)

lst_notes = QListWidget()

btn_tag_seacrh = QPushButton('шукати')
btn_tag_add = QPushButton('додати')
btn_tag_unpin = QPushButton('відкріпити')

lb_tags = QLabel('')
lst_tags = QListWidget()
field_tag = QLineEdit()

row1 = QHBoxLayout()
row2 = QHBoxLayout()



col2.addWidget(lst_text)
row1.addWidget(btn_note_create)
row1.addWidget(btn_note_delete)
row1.addWidget(btn_note_save)

row2.addWidget(lst_tags)




col2.addLayout(row1)
col2.addLayout(row2)
col2.addWidget(field_tag)
col2.addWidget(btn_tag_seacrh)
col2.addWidget(btn_tag_unpin)
col2.addWidget(btn_tag_add)


def show_notes():
    key = lst_notes.selectedItems()[0].text()
    field_text.setText(notes[key]['текст'])


    lst_tags.clear()
    lst_tags.addItems(notes[key]['теги'])

with open('notes.json', 'r', encoding='utf8') as file:
    notes = json.load(file)

def show_note():
    key = lst_notes.currentItem().text()

    print(notes[key]['текст'])

def add_note():
    note_name, ok = QInputDialog.getText(window, 'додаток', 'Назва замітки')

    if note_name and ok:
        
        notes[note_name] = {"текст": '', "теги": []}
        lst_notes.addItem(note_name)

def save_note():
    if lst_notes.currentItem():
        key = lst_notes.currentItem().text()
        notes[key]['текст'] = field_text.toPlainText()

        
        writeToFile()
        
    else:
        print("no")
        
def del_note():
        if lst_notes.currentItem():
            key = lst_notes.currentItem().text()
            del notes[key]
            
            
            
            field_text.clear()
            lst_notes.clear()
            lst_tags.clear()
            
            writeToFile()

lst_notes.itemClicked.connect(show_notes)   

btn_note_create.clicked.connect(add_note)
btn_note_save.clicked.connect(save_note)
btn_note_delete.clicked.connect(del_note)
lst_notes.addItems(notes)


window.setLayout(layout_notes)
window.show()
app.exec_()

