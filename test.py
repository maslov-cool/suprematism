import io
import sys
import math

from PyQt6 import uic  # Импортируем uic
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.QtGui import QColor, QPainter, QCursor, QPolygonF
from PyQt6.QtCore import Qt, QPointF, QRectF
import random

design = '''<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>MainWindow</class>
 <widget class="QMainWindow" name="MainWindow">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>1000</width>
    <height>1000</height>
   </rect>
  </property>
  <property name="minimumSize">
   <size>
    <width>1000</width>
    <height>1000</height>
   </size>
  </property>
  <property name="maximumSize">
   <size>
    <width>1000</width>
    <height>1000</height>
   </size>
  </property>
  <property name="windowTitle">
   <string>Супрематизм</string>
  </property>
  <widget class="QWidget" name="centralwidget"/>
 </widget>
 <resources/>
 <connections/>
</ui>
'''


class Suprematism(QMainWindow):
    def __init__(self):
        super().__init__()
        f = io.StringIO(design)
        uic.loadUi(f, self)  # Загружаем дизайн
        self.setMouseTracking(True)
        self.object = ''
        self.coords_ = []

    def mousePressEvent(self, event):
        # Получаем координаты курсора
        x = event.position().x()
        y = event.position().y()
        self.coords_ = [x, y]

        if event.button() == Qt.MouseButton.LeftButton:
            self.object = 'ellipse'
        elif event.button() == Qt.MouseButton.RightButton:
            self.object = 'rect'
        self.update()

    def keyPressEvent(self, event):
        # Проверяем, была ли нажата клавиша пробела
        if event.key() == Qt.Key.Key_Space:
            x = self.mapFromGlobal(QCursor.pos()).x()
            y = self.mapFromGlobal(QCursor.pos()).y()
            self.coords_ = [x, y]
            self.object = 'triangle'
            self.update()

    def mouseMoveEvent(self, event):
        self.coords_ = [event.pos().x(), event.pos().y()]

    def paintEvent(self, a0):
        if self.object:
            qp = QPainter()
            qp.begin(self)

            if self.object == 'ellipse':
                A = random.randint(20, 100)
                qp.setBrush(QColor(random.randrange(256), random.randrange(256), random.randrange(256)))
                qp.drawEllipse(QPointF(self.coords_[0], self.coords_[1]), A, A)
            elif self.object == 'triangle':
                A = random.randint(20, 100)
                qp.setBrush(QColor(random.randrange(256), random.randrange(256), random.randrange(256)))
                points = [
                    QPointF(self.coords_[0], self.coords_[1] - A),  # Вершина 1
                    QPointF(self.coords_[0] + math.cos(7 * math.pi / 6) * A,
                            self.coords_[1] - math.sin(7 * math.pi / 6) * A),  # Вершина 2
                    QPointF(self.coords_[0] + math.cos(11 * math.pi / 6) * A,
                            self.coords_[1] - math.sin(7 * math.pi / 6) * A)  # Вершина 3
                ]
                polygon = QPolygonF(points)  # Создаем многоугольник из точек
                qp.drawPolygon(polygon)  # Рисуем треугольник
            elif self.object == 'rect':
                A = random.randint(20, 100)
                qp.setBrush(QColor(random.randrange(256), random.randrange(256), random.randrange(256)))
                qp.drawRect(QRectF(self.coords_[0] - A / 2, self.coords_[1] - A / 2, A, A))  # Рисуем треугольник
            qp.end()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    program = Suprematism()
    program.show()
    sys.exit(app.exec())
