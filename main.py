import sys
from PySide2.QtWidgets import QApplication, QWidget
from login import Login
# class Login(QWidget):
#     def __init__(self, parent=None):
#         super().__init__(parent)
#         self.ui = Ui_Login()
#         self.ui.setupUi(self)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = Login()
    widget.show()
    sys.exit(app.exec_())
