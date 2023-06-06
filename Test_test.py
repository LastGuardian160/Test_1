from Test import Ui_MainWindow


ui = Ui_MainWindow() # создание объекта класса Ui_MainWindow
value = ui.sliderValueChanged() # вызов метода sliderValueChanged(), чтобы получить значение value
print(value)

