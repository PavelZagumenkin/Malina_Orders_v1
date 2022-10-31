import sys
from PyQt6 import QtWidgets
from Windows.WindowsLogin import WindowLogin

class Main():
    def __init__(self):
        super().__init__()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    WindowLogin = WindowLogin()
    WindowLogin.show()
    sys.exit(app.exec())