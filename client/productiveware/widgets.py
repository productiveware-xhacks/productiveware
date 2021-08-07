from os.path import dirname, exists, join, realpath
from typing import List
from PySide6.QtCore import Qt, Slot
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import (QHBoxLayout, QVBoxLayout, QGridLayout, QLabel,
                               QLineEdit, QListWidget, QListWidgetItem, QMainWindow, QPushButton,
                               QStatusBar, QWidget)

from .config import *


class MainWidget(QMainWindow):
    def __init__(self):
        super().__init__()

        # Children widgets
        self.widget_login = LoginWidget(self)

        self.setWindowTitle('productiveware')
        self.setWindowIcon(
            QIcon(join(dirname(realpath(__file__)), 'res/productiveware.png')))
        widget = QWidget()
        layout = QGridLayout()
        self.status = QStatusBar()
        self.status.showMessage('Connecting...')

        # Profile specific elements
        self.pw_profile = QPushButton('Profile')
        self.pw_logout = QPushButton('Log out')

        # Directory list elements
        self.dir_list = QListWidget()
        self.dir_add = QPushButton('Add Directory')
        self.dir_remove = QPushButton('Remove Directory')

        for path in get_target_folders():
            self.dir_list.addItem(QListWidgetItem(path))

        self.old_list = self._get_list_items()

        # Encryption/decryption elements
        self.decrypt_select = QPushButton('Decrypt file...')
        self.decrypt_log = QPushButton('View encryption log...')

        # Save state elements
        self.save_list = QPushButton('Save')
        self.save_list.setEnabled(False)

        # Directory list events
        self.dir_list.itemDoubleClicked.connect(
            self.on_dir_list_double_clicked)
        self.dir_list.currentItemChanged.connect(self.on_dir_list_item_changed)

        # Button events
        self.dir_add.clicked.connect(self.on_dir_add_clicked)
        self.dir_remove.clicked.connect(self.on_dir_remove_clicked)
        self.save_list.clicked.connect(self.on_save_list_clicked)

        layout.addWidget(self.pw_profile, 0, 0, Qt.AlignLeft)
        layout.addWidget(QLabel('Targeted files: '), 0, 1)
        layout.addWidget(QLabel('Encrypted files: '), 0, 2)
        layout.addWidget(self.pw_logout, 0, 3, Qt.AlignRight)
        layout.addWidget(self.dir_list, 1, 0, 5, 3)
        layout.addWidget(self.dir_add, 1, 3)
        layout.addWidget(self.dir_remove, 2, 3)
        layout.addWidget(QLabel('Decryptions earned: '),
                         4, 3, Qt.AlignBottom)
        layout.addWidget(self.decrypt_select, 5, 3)
        layout.addWidget(self.decrypt_log, 6, 3)
        layout.addWidget(self.save_list, 6, 2, Qt.AlignRight)

        widget.setLayout(layout)
        self.setCentralWidget(widget)
        self.setStatusBar(self.status)

    @Slot()
    def on_dir_list_double_clicked(self, item: QListWidgetItem):
        item.setFlags(item.flags() | Qt.ItemIsEditable)

    @Slot()
    def on_dir_list_item_changed(self, current: QListWidgetItem, prev: QListWidgetItem):
        new_list = self._get_list_items()
        print(new_list)
        print(self.old_list)

        if new_list != self.old_list:
            self.save_list.setEnabled(True)

        if prev is not None and prev.flags() & Qt.ItemIsEditable != 0:
            prev.setFlags(prev.flags() ^ Qt.ItemIsEditable)

    @Slot()
    def on_dir_add_clicked(self):
        self.dir_list.addItem(QListWidgetItem('Enter path here...'))

    @Slot()
    def on_dir_remove_clicked(self):
        current = self.dir_list.currentItem()

        if current is not None:
            remove_target_folder(current.text())
            self.dir_list.takeItem(self.dir_list.row(current))

        self.save_list.setEnabled(True)

    @Slot()
    def on_save_list_clicked(self):
        items = self._get_list_items()
        clear_target_folders()

        for item in items:
            add_target_folder(item)

        self.save_list.setEnabled(False)

    def _get_list_items(self) -> List[str]:
        items = []
        for i in range(self.dir_list.count()):
            items.append(self.dir_list.item(i).text())

        return items


class LoginWidget(QWidget):
    def __init__(self, parent: QWidget):
        super().__init__()

        self.setWindowTitle('productiveware: Log In')
        self.username = QLineEdit()
        self.password = QLineEdit()
        self.login = QPushButton('Log In')
        self.register = QPushButton('Register')

        # Add functionality to buttons
        self.login.clicked.connect(self.action_login)

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
    def action_login(self):
        # TODO: add login functionality when back-end adds API
        self.close()
