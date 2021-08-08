import webbrowser
from os.path import dirname, join, realpath
from PySide6.QtCore import Slot
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import *

from productiveware.client import *
from productiveware.config import *

_web_url = 'http://productiveware.objectobject.ca:3000/register'


# * Postponed login functionality
class LoginWidget(QWidget):
    def __init__(self, parent):
        super().__init__()

        self.setWindowTitle('productiveware: Log In')
        self.setWindowIcon(
            QIcon(join(dirname(realpath(__file__)), 'res/productiveware.png')))
        self.window_main = parent

        self.username = QLineEdit()
        self.password = QLineEdit()
        self.password.setEchoMode(QLineEdit.Password)
        self.login = QPushButton('Log In')
        self.register = QPushButton('Register')

        # Add functionality to buttons
        self.login.clicked.connect(self.on_pw_login_clicked)
        self.register.clicked.connect(self.on_pw_register_clicked)

        # Layout of login form
        layout = QVBoxLayout()
        hz_buttons = QHBoxLayout()

        # Main layout
        layout.addWidget(QLabel('Username'))
        layout.addWidget(self.username)
        layout.addWidget(QLabel('Password'))
        layout.addWidget(self.password)

        # Login/register buttons
        hz_buttons.addWidget(self.login)
        hz_buttons.addWidget(self.register)

        layout.addLayout(hz_buttons)
        layout.addStretch()

        self.setLayout(layout)

    @Slot()
    def on_pw_login_clicked(self):
        if not login(self.username.text(), self.password.text()):
            login_error = QMessageBox(QMessageBox.Critical, 'Invalid Credentials',
                                      f'The provided username and password are not valid. Please try again.',
                                      QMessageBox.Ok)
            login_error.show()
            return login_error.exec()

        self.hide()
        self.username.clear()
        self.password.clear()
        self.window_main.resize(800, 500)
        self.window_main.set_connected(True)
        self.window_main.show()

    @Slot()
    def on_pw_register_clicked(self):
        webbrowser.open(_web_url)
