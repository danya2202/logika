from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication,QWidget, QLabel,QPushButton, QVBoxLayout,QRadioButton,QMessageBox,QHBoxLayout

application = QApplication([])
widget = QWidget()

pushbutton = QPushButton("натисни мене")

boxlayout = QVBoxLayout()

label = QLabel("текст")

radiobutt = QRadioButton("кнопка")

boxlayout.addWidget(label)
boxlayout.addWidget(pushbutton)
boxlayout.addWidget(radiobutt)
widget.setLayout(boxlayout)

widget.show()

application.exec_()



