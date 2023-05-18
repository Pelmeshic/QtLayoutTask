# Имопртирую библиотеки

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLabel, QRadioButton

# Создание окна

app = QApplication([])
win = QWidget()
win.show()

# Создание лаяутов

main_layout = QHBoxLayout() #V - вертикальная направляющая

layout_v_1 = QVBoxLayout()
layout_v_2 = QVBoxLayout()
layout_v_3 = QVBoxLayout()

main_layout.addLayout(layout_v_1)
main_layout.addLayout(layout_v_2)
main_layout.addLayout(layout_v_3)

# Создаем кнопки

button_1 = QPushButton()
button_2 = QPushButton()
button_3 = QPushButton()
button_4 = QPushButton()
button_5 = QPushButton()
button_6 = QPushButton()
button_7 = QPushButton()

# Присоединяем кнопочки

layout_v_1.addWidget(button_1)
layout_v_1.addWidget(button_2)
layout_v_1.addWidget(button_3)

layout_v_2.addWidget(button_4)

layout_v_3.addWidget(button_5)
layout_v_3.addWidget(button_6)
layout_v_3.addWidget(button_7)

win.setLayout(main_layout) #устанаваливаем окну win layout - main_layout
app.exec_()
