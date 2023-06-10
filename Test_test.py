from Test import Ui_MainWindow
from PyQt5 import QtCore, QtGui, QtWidgets

ui = Ui_MainWindow()


def value():
    value = ui.sliderValueChanged()  # вызов метода sliderValueChanged(), чтобы получить значение value
    print(value)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    value()
    sys.exit(app.exec())

