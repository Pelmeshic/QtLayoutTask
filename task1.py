# Имопртирую библиотеки

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLabel, QRadioButton

# Создание окна

app = QApplication([])
win = QWidget()
win.show()

# Создание лаяута

main_layout = QHBoxLayout() 

# Создание кнопки

button_1 = QPushButton()
button_2 = QPushButton()
button_3 = QPushButton()

# Соединение

main_layout.addWidget(button_1)
main_layout.addWidget(button_2)
main_layout.addWidget(button_3)


win.setLayout(main_layout) #устанаваливаем окну win layout - main_layout
app.exec_()
