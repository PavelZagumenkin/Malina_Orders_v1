import sys
from PyQt6 import QtWidgets
from Windows.WindowsLogin import WindowLogin

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    WindowLogin = WindowLogin()
    WindowLogin.show()
    sys.exit(app.exec())
