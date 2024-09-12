
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from abc import ABC, abstractmethod
import math
import ui.mainWindow2 as mainWindow
import sys


###############################
# Абстрактный класс "Фигура"
class Figure(ABC):
    @abstractmethod
    def area(self):
        pass

class Triangle(Figure):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def area(self):
         # Проверка на существование треугольника
        if self.a + self.b <= self.c or self.a + self.c <= self.b or self.b + self.c <= self.a:
            raise ValueError("Треугольник с такими сторонами не существует")

        # Формула Герона для вычисления площади треугольника
        s = (self.a + self.b + self.c) / 2
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))
    
class Trapezoid(Figure):
    def __init__(self, a, b, h):
        self.a = a
        self.b = b
        self.h = h

    def area(self):
        return (self.a + self.b) * self.h / 2

class Circle(Figure):
    def __init__(self, r):
        self.r = r

    def area(self):
        return math.pi * self.r ** 2

class Sector(Figure):
    def __init__(self, r, alpha):
        self.r = r
        self.alpha = alpha

    def area(self):
        if self.alpha > 360 or self.alpha <-360 :
            raise ValueError("Сектор с такими параметрами не существует")
        if self.alpha == 360 or self.alpha == -360 :
            self.alpha = 0
        return (math.pi * self.r ** 2)/360 * self.alpha

class Square(Figure):
    def __init__(self, a):
        self.a = a

    def area(self):
        return self.a ** 2

class Parallelogram(Figure):
    def __init__(self, a, h):
        self.a = a
        self.h = h

    def area(self):
        return self.a * self.h

class Rectangle(Figure):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def area(self):
        return self.a * self.b

class Rhombus(Figure):
    def __init__(self, d1, d2):
        self.d1 = d1
        self.d2 = d2

    def area(self):
        return (self.d1 * self.d2) / 2
    
###########################

class MainWindow(QMainWindow, mainWindow.Ui_MainWindow):

    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)


  # Привязываем кнопки к методам
        self.pushButton_9.clicked.connect(lambda: self.calculate_area(self.pushButton_9))
        self.pushButton_10.clicked.connect(lambda: self.calculate_area(self.pushButton_10))
        self.pushButton_11.clicked.connect(lambda: self.calculate_area(self.pushButton_11))
        self.pushButton_12.clicked.connect(lambda: self.calculate_area(self.pushButton_12))
        self.pushButton_13.clicked.connect(lambda: self.calculate_area(self.pushButton_13))
        self.pushButton_14.clicked.connect(lambda: self.calculate_area(self.pushButton_14))
        self.pushButton_15.clicked.connect(lambda: self.calculate_area(self.pushButton_15))
        self.pushButton_16.clicked.connect(lambda: self.calculate_area(self.pushButton_16))
    
    def calculate_area(self, button):
        try:
            if button == self.pushButton_9:
                # Рассчет площади для треугольника
                triangle = Triangle(float(self.lineEdit_2.text()), float(self.lineEdit_3.text()), float(self.lineEdit.text()))
                area = triangle.area()
                result_text = f"S треугольника = {area:.2f}"

            if button == self.pushButton_10:
                # Рассчет площади для трапеции
                trapezoid = Trapezoid(float(self.lineEdit_4.text()), float(self.lineEdit_5.text()), float(self.lineEdit_6.text()))
                area = trapezoid.area()
                result_text = f"S трапеции = {area:.2f}"

            if button == self.pushButton_11:
                # Рассчет площади для круга
                circle = Circle(float(self.lineEdit_7.text()))
                area = circle.area()
                result_text = f"S круга = {area:.2f}"

            if button == self.pushButton_12:
                # Рассчет площади для сектора
                sector = Sector(float(self.lineEdit_8.text()), float(self.lineEdit_9.text()))
                area = sector.area()
                result_text = f"S сектора = {area:.2f}"

            if button == self.pushButton_13:
                # Рассчет площади для квадрата
                square = Square(float(self.lineEdit_10.text()))
                area = square.area()
                result_text = f"S квадрата = {area:.2f}"

            if button == self.pushButton_14:
                # Рассчет площади для параллелограмма
                parallelogram = Parallelogram(float(self.lineEdit_11.text()), float(self.lineEdit_12.text()))
                area = parallelogram.area()
                result_text = f"S параллелограмма = {area:.2f}"

            if button == self.pushButton_15:
                # Рассчет площади для прямоугольника
                rectangle = Rectangle(float(self.lineEdit_13.text()), float(self.lineEdit_14.text()))
                area = rectangle.area()
                result_text = f"S прямоугольника = {area:.2f}"
            
            if button == self.pushButton_16:
                # Рассчет площади для ромба
                rhombus = Rhombus(float(self.lineEdit_15.text()), float(self.lineEdit_16.text()))
                area = rhombus.area()
                result_text = f"S ромба = {area:.2f}"

 
            existing_text = self.plainTextEdit.toPlainText()
            self.plainTextEdit.setPlainText(existing_text + result_text + "\n")
        except ValueError:
            QMessageBox.warning(self, "Ошибка", "Пожалуйста, введите корректные числовые значения.")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = MainWindow()
    form.show()
    app.exec_()
