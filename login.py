from PySide2.QtWidgets import QWidget, QMessageBox
from ui_form import Ui_Login

class Login(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Login()
        self.ui.setupUi(self)

        self.ui.signinBtn.clicked.connect(self.signBtnClicked)

    def signBtnClicked(self):
        userInput = self.ui.usernameField.text()
        passInput = self.ui.passwordField.text()

        if (userInput == "admin" and passInput == "admin"):
            QMessageBox.information(self, "Login Success", "Welcome to Panel")
        else:
            QMessageBox.warning(self,"Login Failed", "Username or password is incorrect!")