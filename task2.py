# Имопртирую библиотеки

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLabel, QRadioButton

# Создание окна

app = QApplication([])
win = QWidget()
win.show()

# Создание лаяутов

main_layout = QHBoxLayout() #V - вертикальная направляющая

layout_h_1 = QVBoxLayout()

# Создаем кнопки

button_1 = QPushButton()
button_2 = QPushButton()
button_3 = QPushButton()
button_4 = QPushButton()
button_5 = QPushButton()

# Присоединяем кнопочки

layout_h_1.addWidget(button_1)
layout_h_1.addWidget(button_2)
layout_h_1.addWidget(button_3)


main_layout.addWidget(button_4)
main_layout.addLayout(layout_h_1)
main_layout.addWidget(button_5)

win.setLayout(main_layout) #устанаваливаем окну win layout - main_layout
app.exec_()
