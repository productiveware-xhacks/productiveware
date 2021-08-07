from PySide6 import QtCore, QtWidgets, QtGui


# class MainWidget(QtWidgets.QWidget):
#     def __init__(self, username, password):
#         super().__init__()

#         self.setWindowTitle("productiveware")

#         self.pw_profile = QtWidgets.QPushButton()


class LoginWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('productiveware: Log In')
        self.username = QtWidgets.QLineEdit(self)
        self.password = QtWidgets.QLineEdit(self)
        self.login = QtWidgets.QPushButton('Log In', self)
        self.register = QtWidgets.QPushButton('Register', self)

        # Layout of login form
        layout = QtWidgets.QVBoxLayout(self)
        hz_buttons = QtWidgets.QHBoxLayout(self)

        # Main layout
        layout.addWidget(QtWidgets.QLabel('Username'))
        layout.addWidget(self.username)
        layout.addWidget(QtWidgets.QLabel('Password'))
        layout.addWidget(self.password)

        # Login/register buttons
        hz_buttons.addWidget(self.login)
        hz_buttons.addWidget(self.register)

        layout.addLayout(hz_buttons)
        layout.addStretch()

        self.setLayout(layout)
