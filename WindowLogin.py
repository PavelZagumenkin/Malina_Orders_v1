from PyQt6 import QtWidgets
from main import Main
from ui.login import Ui_WindowLogin

class WindowLogin(QtWidgets.QMainWindow, Main):
    def __init__(self):
        super().__init__()
        self.ui = Ui_WindowLogin()
        self.ui.setupUi(self)
        self.ui.label_login_password.setFocus()  # Фокус по умолчанию на тексте
        self.ui.btn_login.clicked.connect(self.login)
        self.base_line_edit = [self.ui.line_login, self.ui.line_password]