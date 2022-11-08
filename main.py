from PySide2.QtWidgets import QApplication
from mainWindow import MainWindow
import sys

app = QApplication()
#Ventana de app
window = MainWindow()
window.show()
sys.exit(app.exec_())