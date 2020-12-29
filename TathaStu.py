import sys
from PySide2.QtWidgets import QApplication, QMainWindow
# from UI_Central import Ui_MainWindow
# from UI_PL import Ui_MainWindow
# from UI_Fashion import Ui_MainWindow
from UI_Grocery import Ui_MainWindow
# from UI_HNF import Ui_MainWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec_())

