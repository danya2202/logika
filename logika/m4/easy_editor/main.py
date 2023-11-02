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





def filter(filenames):
    result = []
    ext = ['png', 'jpg', 'bmp', 'jpeg', 'gif']

    for file in filenames:
        if file.split('.')[-1] in ext:
            result.append(file)
            
    return result

def showFiles():
    global workdir
    workdir = QFileDialog.getExistingDirectory()
    files = os.listdir(workdir)
    
    graphic_files = filter(files)

    lst_file.clear()
    lst_file.addItems(graphic_files)

class ImageProcessor():
    def __init__(self):
        self.original = None
        self.filename = None
        self.save_dir = 'Modifided/'

    def load_image(self, filename):
        self.filename = filename
        
        full_path = os.path.join(workdir, filename)
        
        self.original = Image.open(full_path)

    def show_image(self, path):
        lb_pic.hide()
            
        pixmapimage = QPixmap(path)
        w, h = lb_pic.width(), lb_pic.height()
            
        pixmapimage = pixmapimage.scaled(w, h, Qt.KeepAspectRatio)
            
        lb_pic.setPixmap(pixmapimage)
            
        lb_pic.show()
    
    def saveAndShowImage(self):
        path = os.path.join(workdir, self.save_dir)

        if not (os.path.exists(path) or os.path.isdir(path)):
            os.mkdir(path)

        
        image_path = os.path.join(path, self.filename)
        self.original.save(image_path)
        self.show_image(image_path)
        
    def do_bw(self):
        self.original = self.original.convert("L")
        self.saveAndShowImage()  
        
    def do_left(self):
        self.original = self.original.transpose(Image.ROTATE_90)
        self.saveAndShowImage()
    
    def do_right(self):
        self.original = self.original.transpose(Image.ROTATE_270)
        self.saveAndShowImage()
    
    def do_flip(self):
        self.original = self.original.transpose(Image.FLIP_LEFT_RIGHT)
        self.saveAndShowImage()
    
    def do_sharp(self):
        self.original = self.original.filter(ImageFilter.SHARPEN)
        self.saveAndShowImage()
    
        
        
        
        
             
def showChosenItem():
    filename = lst_file.currentItem().text()
    workimage.load_image(filename)
    full_path = os.path.join(workdir, filename)
    workimage.show_image(full_path)
    
workimage = ImageProcessor()

lst_file.itemClicked.connect(showChosenItem)





btn_folder.setStyleSheet('''
                         background-color: silver;
                         ''')
btn_leftrot.setStyleSheet('''
                         background-color: silver;
                         ''')
btn_rightrot.setStyleSheet('''
                         background-color: silver;
                         ''')
btn_riz.setStyleSheet('''
                         background-color: silver;
                         ''')
btn_BlWh.setStyleSheet('''
                         background-color: silver;
                         ''')
btn_flip.setStyleSheet('''
                         background-color: silver;
                         ''')
lst_file.setStyleSheet('''
                         background-color: silver;
                         ''')
window.setStyleSheet('''
                         background-color: gray;
                         ''')


    














































btn_riz.clicked.connect(workimage.do_sharp)
btn_flip.clicked.connect(workimage.do_flip)
btn_leftrot.clicked.connect(workimage.do_left)
btn_rightrot.clicked.connect(workimage.do_right)
btn_BlWh.clicked.connect(workimage.do_bw)
btn_folder.clicked.connect(showFiles)

window.resize(900,600)

window.setLayout(layout_editor)
window.show()
app.exec_()