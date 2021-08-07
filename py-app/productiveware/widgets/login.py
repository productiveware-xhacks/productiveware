# import webbrowser
# from PySide6.QtCore import Slot
# from PySide6.QtWidgets import (
#     QHBoxLayout, QVBoxLayout, QLabel, QLineEdit, QPushButton, QWidget)


# * Postponed login functionality
# class LoginWidget(QWidget):
#     def __init__(self, parent: QWidget):
#         super().__init__()

#         self.setWindowTitle('productiveware: Log In')

#         self.username = QLineEdit()
#         self.password = QLineEdit()
#         self.login = QPushButton('Log In')
#         self.register = QPushButton('Register')

#         # Add functionality to buttons
#         self.login.clicked.connect(self.on_pw_login_clicked)
#         self.register.clicked.connect(self.on_pw_register_clicked)

#         # Layout of login form
#         layout = QVBoxLayout()
#         hz_buttons = QHBoxLayout()

#         # Main layout
#         layout.addWidget(QLabel('Username'))
#         layout.addWidget(self.username)
#         layout.addWidget(QLabel('Password'))
#         layout.addWidget(self.password)

#         # Login/register buttons
#         hz_buttons.addWidget(self.login)
#         hz_buttons.addWidget(self.register)

#         layout.addLayout(hz_buttons)
#         layout.addStretch()

#         self.setLayout(layout)

#     @Slot()
#     def on_pw_login_clicked(self):
#         # TODO: add login functionality when back-end adds API
#         self.close()

#     @Slot()
#     def on_pw_register_clicked(self):
#         # TODO: change URL to productiveware register page
#         webbrowser.open('https://www.google.ca')
