from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap 

from PIL import Image, ImageFilter

import os

app = QApplication([])

window = QWidget()



btn_leftrot = QPushButton('ліво')
btn_rightrot = QPushButton('право')
btn_folder = QPushButton('папка')
btn_BlWh = QPushButton('Ч/Б')
btn_flip = QPushButton('зеркало')
btn_riz = QPushButton('різкість')

lst_file = QListWidget()
lb_pic = QLabel('картинка')

layout_editor = QHBoxLayout()

col1 = QVBoxLayout()
col2 = QVBoxLayout()
rov = QHBoxLayout()

col1.addWidget(btn_folder)
col1.addWidget(lst_file)

rov.addWidget(btn_leftrot)
rov.addWidget(btn_rightrot)
rov.addWidget(btn_BlWh)
rov.addWidget(btn_flip)
rov.addWidget(btn_riz)

col2.addWidget(lb_pic)
col2.addLayout(rov)

layout_editor.addLayout(col1, 1)
layout_editor.addLayout(col2, 4)

workdir = QFileDialog.getExistingDirectory()

files = os.listdir(workdir)
print(workdir)
def filter(filenames):
    result = []
    ext = ['png', 'jpg', 'bmp', 'jpeg', 'gif']

    for file in filenames:
        if file.split('.')[-1] in ext:
            result.append(file)
            
    return result 
filter(files)    




























































window.setLayout(layout_editor)
window.show()
app.exec_()