from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
        QApplication, QWidget, 
        QTableWidget, QListWidget, QListWidgetItem,
        QLineEdit, QFormLayout,
        QHBoxLayout, QVBoxLayout, 
        QGroupBox, QButtonGroup, QRadioButton,  
        QPushButton, QLabel, QSpinBox)
app = QApplication([])

btn_ok = QPushButton("відповісти")
btn_sleep = QPushButton("відпочити")
btn_meny = QPushButton("меню")

lb_question = QLabel('')

box_min = QSpinBox()
box_min.setValue(5)

RadioGroupBox = QGroupBox("варіанти відповідей")
RadioGroup = QButtonGroup()

r_btn1 = QRadioButton("z")
r_btn2 = QRadioButton("d")
r_btn3 = QRadioButton("f")
r_btn4 = QRadioButton("g")

RadioGroup.addButton(r_btn1)
RadioGroup.addButton(r_btn2)
RadioGroup.addButton(r_btn3)
RadioGroup.addButton(r_btn4)

layout_ans1 = QHBoxLayout()
layout_ans2 = QVBoxLayout()
layout_ans3 = QVBoxLayout()

layout_ans2.addWidget(r_btn1)
layout_ans2.addWidget(r_btn2)
layout_ans3.addWidget(r_btn3)
layout_ans3.addWidget(r_btn4)

layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3)

RadioGroupBox.setLayout(layout_ans1)

AnsGroupBox = QGroupBox('Результат тесту')
lb_result = QLabel('')
lb_correct = QLabel('')


layout_res = QVBoxLayout()
layout_res.addWidget(lb_result, alignment=(Qt.AlignLeft | Qt.AlignTop))
layout_res.addWidget(lb_correct, alignment=Qt.AlignHCenter, stretch=2)

AnsGroupBox.setLayout(layout_res)

AnsGroupBox.hide()

layout_card = QVBoxLayout()
layout_line1 = QHBoxLayout()
layout_line2 = QHBoxLayout()
layout_line3 = QHBoxLayout()
layout_line4 = QHBoxLayout()

layout_line1.addWidget(btn_meny)
layout_line1.addStretch(1)
layout_line1.addWidget(btn_sleep)
layout_line1.addWidget(box_min)
layout_line1.addWidget(QLabel('хвилин'))

layout_line2.addWidget(lb_question, alignment=(Qt.AlignHCenter | Qt.AlignVCenter))

layout_line3.addWidget(RadioGroupBox)
layout_line3.addWidget(AnsGroupBox)

layout_line4.addStretch(1)
layout_line4.addWidget(btn_ok)
layout_line4.addStretch(1)

layout_card.addLayout(layout_line1)
layout_card.addLayout(layout_line2)
layout_card.addLayout(layout_line3)
layout_card.addLayout(layout_line4)

# віджети, які треба буде розмістити:
# кнопка повернення в основне вікно 
# кнопка прибирає вікно і повертає його після закінчення таймера
# введення кількості хвилин
# кнопка відповіді "Ок" / "Наступний"
# текст питання

# Опиши групу перемикачів

# Опиши панень з результатами

# Розмісти весь вміст в лейаути. Найбільшим лейаутом буде layout_card

# Результат роботи цього модуля: віджети поміщені всередину layout_card, який можна призначити вікну.
def show_result():
    ''' показати панель відповідей '''
    RadioGroupBox.hide()
    AnsGroupBox.show()
    btn_ok.setText("Наступне питання")


def show_question():
    ''' показати панель запитань '''
    RadioGroupBox.show()
    AnsGroupBox.hide()
    btn_ok.setText("Відповісти")


    RadioGroup.setExclusive(False)
    r_btn1.setChecked(False)
    r_btn2.setChecked(False)
    r_btn3.setChecked(False)
    r_btn4.setChecked(False)

    RadioGroup.setExclusive(True)

