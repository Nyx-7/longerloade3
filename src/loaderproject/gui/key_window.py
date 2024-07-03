import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QVBoxLayout, QHBoxLayout, QPushButton, QLabel, QFrame, QSizePolicy
from PyQt5.QtCore import Qt, QPoint
from PyQt5.QtGui import QIcon, QPixmap
import pywinstyles

class KeyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.key_input = None
        self.mpos = None
        self.info_box = None  # Добавляем атрибут info_box
        self.initUI()

    def initUI(self):
        self.setFixedSize(650, 406)
        self.setWindowTitle('Key Input')
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setStyleSheet("QWidget {border-radius: 10px;}")
        self.setWindowIcon(QIcon('img/my_icon.ico'))

        # Создаем вертикальный layout
        layout = QVBoxLayout()

        # Создаем информационный бокс
        self.info_box = QFrame(self)
        self.info_box.setFrameShape(QFrame.StyledPanel)
        self.info_box.setStyleSheet("background-color: gray; border-radius: 10px;")
        self.info_box.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.info_box.setFixedSize(500, 300)  # Измените эти значения в соответствии с вашими потребностями


        # Создаем layout для info_box
        info_box_layout = QVBoxLayout()
        self.info_box.setLayout(info_box_layout)

        # Добавляем картинку
        label = QLabel(self)
        pixmap = QPixmap('img/my_image.png')
        label.setPixmap(pixmap)
        label.setScaledContents(True)  # Масштабируем изображение, чтобы оно занимало всю доступную ширину и высоту
        self.info_box.layout().addWidget(label)

        # Создаем горизонтальный layout для кнопки Key
        bottom_layout = QHBoxLayout()

        self.key_button = QPushButton('Key', self)
        self.key_button.clicked.connect(self.show_key_input)
        self.key_button.setStyleSheet("background-color: rgba(0, 0, 139, 0.1); border-radius: 5px;")  # Устанавливаем цвет кнопки темно-синим и прозрачность 90%

        # Добавляем кнопку в layout info_box, а не в основной layout
        bottom_layout.addWidget(self.key_button)
        self.info_box.layout().addLayout(bottom_layout)

        # Добавляем горизонтальный layout в вертикальный layout
        layout.addStretch()  # Добавляем растяжение перед info_box
        layout.addWidget(self.info_box)
        layout.addStretch()  # Добавляем растяжение после info_box

        self.setLayout(layout)

        # Применяем стиль из py-window-styles
        pywinstyles.apply_style(self, 'acrylic')

        self.show()

    def show_key_input(self):
        if self.key_input is None:
            self.key_input = QLineEdit(self)
            # Перемещаем поле ввода внутрь info_box
            self.key_input.move((self.info_box.width() - self.key_input.width()) // 2, self.info_box.height() - self.key_input.height())
            self.key_input.show()
        else:
            self.key_input.show()

    def mousePressEvent(self, event):
        self.mpos = event.pos()

    def mouseMoveEvent(self, event):
        if self.mpos:
            diff = event.pos() - self.mpos
            new_pos = self.pos() + diff
            self.move(new_pos)

    def mouseReleaseEvent(self, event):
        self.mpos = None

app = QApplication([])
ex = KeyWindow()
app.exec_()
