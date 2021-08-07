import os
from PySide6 import QtCore, QtWidgets, QtGui

class MainWidget(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('productiveware')
        self.setWindowIcon(QtGui.QIcon(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'res/productiveware.png')))
        widget = QtWidgets.QWidget()
        layout = QtWidgets.QGridLayout()
        self.status = QtWidgets.QStatusBar()
        self.status.showMessage('Connecting...')


        # Profile specific elements
        self.pw_profile = QtWidgets.QPushButton('Profile')
        self.pw_logout = QtWidgets.QPushButton('Log out')

        # Directory list elements
        self.dir_list = QtWidgets.QListWidget()
        self.dir_add = QtWidgets.QPushButton('Add Directory')
        self.dir_remove = QtWidgets.QPushButton('Remove Directory')
        
        # Encryption/decryption elements
        self.decrypt_select = QtWidgets.QPushButton('Decrypt file...')
        self.decrypt_log = QtWidgets.QPushButton('View encryption log...')


        layout.addWidget(self.pw_profile, 0, 0, alignment=QtCore.Qt.AlignLeft)
        layout.addWidget(QtWidgets.QLabel('Targeted files: '), 0, 1)
        layout.addWidget(QtWidgets.QLabel('Encrypted files: '), 0, 2)
        layout.addWidget(self.pw_logout, 0, 3, alignment=QtCore.Qt.AlignRight)
        layout.addWidget(self.dir_list, 1, 0, 5, 3)
        layout.addWidget(self.dir_add, 1, 3)
        layout.addWidget(self.dir_remove, 2, 3)
        layout.addWidget(QtWidgets.QLabel('Decryptions earned: '), 3, 3, alignment=QtCore.Qt.AlignBottom)
        layout.addWidget(self.decrypt_select, 4, 3)
        layout.addWidget(self.decrypt_log, 5, 3)

        widget.setLayout(layout)
        self.setCentralWidget(widget)
        
        self.setStatusBar(self.status)


class LoginWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('productiveware: Log In')
        self.username = QtWidgets.QLineEdit()
        self.password = QtWidgets.QLineEdit()
        self.login = QtWidgets.QPushButton('Log In')
        self.register = QtWidgets.QPushButton('Register')

        # Add functionality to buttons
        self.login.clicked.connect(self.action_login)

        # Layout of login form
        layout = QtWidgets.QVBoxLayout()
        hz_buttons = QtWidgets.QHBoxLayout()

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

    @QtCore.Slot()
    def action_login(self):
        # TODO: add login functionality when back-end adds API
        self.close()
