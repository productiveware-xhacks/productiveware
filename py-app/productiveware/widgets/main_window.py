import requests
import webbrowser
from os.path import dirname, exists, join, realpath
from typing import List
from PySide6.QtCore import Qt, Slot
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import *

from productiveware import encryption
from productiveware.client import base_url
from productiveware.config import *
from productiveware.widgets.log import LogWidget
from productiveware.widgets.login import LoginWidget


todo_url = f'{base_url}/todo'
test_url = f'{base_url}/api/user'


class MainWidget(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('productiveware')
        self.setWindowIcon(
            QIcon(join(dirname(realpath(__file__)), 'res/productiveware.png')))
        widget = QWidget()
        layout = QGridLayout()

        # Backend stuff
        self.status = QStatusBar()
        self.status_refresh = QPushButton('Refresh Connection')
        self.token = get_token()

        self.is_connected(self._check_connection())

        # Profile specific elements
        self.pw_profile = QPushButton('View Todo List')
        self.pw_logout = QPushButton('Log out')

        # Directory list elements
        self.dir_list = QListWidget()
        self.dir_add = QPushButton('Add Directory')
        self.dir_browse = QPushButton('Browse Directory...')
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
        self.pw_profile.clicked.connect(self.on_pw_profile_clicked)
        self.pw_logout.clicked.connect(self.on_pw_logout_clicked)
        self.dir_add.clicked.connect(self.on_dir_add_clicked)
        self.dir_browse.clicked.connect(self.on_dir_browse_clicked)
        self.dir_remove.clicked.connect(self.on_dir_remove_clicked)
        self.decrypt_select.clicked.connect(self.on_decrypt_select_clicked)
        self.status_refresh.clicked.connect(self.on_status_refresh_clicked)
        self.save_list.clicked.connect(self.on_save_list_clicked)
        self.decrypt_log.clicked.connect(self.on_decrypt_log_clicked)

        layout.addWidget(self.pw_profile, 0, 0, Qt.AlignLeft)
        layout.addWidget(QLabel('Targeted files: '), 0, 1)
        layout.addWidget(QLabel('Encrypted files: '), 0, 2)
        layout.addWidget(self.pw_logout, 0, 3, Qt.AlignRight)
        layout.addWidget(self.dir_list, 1, 0, 5, 3)
        layout.addWidget(self.dir_add, 1, 3)
        layout.addWidget(self.dir_browse, 2, 3)
        layout.addWidget(self.dir_remove, 3, 3)
        layout.addWidget(QLabel('Decryptions earned: '),
                         4, 3, Qt.AlignBottom)
        layout.addWidget(self.decrypt_select, 5, 3)
        layout.addWidget(self.status_refresh, 6, 0, Qt.AlignLeft)
        layout.addWidget(self.save_list, 6, 2, Qt.AlignRight)
        layout.addWidget(self.decrypt_log, 6, 3)

        widget.setLayout(layout)
        self.setCentralWidget(widget)
        self.setStatusBar(self.status)

        # Children widgets
        self.window_log = LogWidget()
        self.window_login = LoginWidget(self)

        if self.token is None:
            self.window_login.setFixedSize(300, 150)
            self.window_login.show()

        else:
            self.resize(800, 500)
            self.show()

    @Slot()
    def on_pw_profile_clicked(self):
        webbrowser.open(todo_url)

    @Slot()
    def on_pw_logout_clicked(self):
        set_token(None)
        self.hide()
        self.window_login.show()

    @Slot()
    def on_dir_list_double_clicked(self, item: QListWidgetItem):
        item.setFlags(item.flags() | Qt.ItemIsEditable)

    @Slot()
    def on_dir_list_item_changed(self, current: QListWidgetItem, prev: QListWidgetItem):
        new_list = self._get_list_items()

        if new_list != self.old_list:
            self.save_list.setEnabled(True)

        if prev is not None and prev.flags() & Qt.ItemIsEditable != 0:
            prev.setFlags(prev.flags() ^ Qt.ItemIsEditable)

    @Slot()
    def on_dir_add_clicked(self):
        self.dir_list.addItem(QListWidgetItem('Double click to edit...'))

    @Slot()
    def on_dir_browse_clicked(self):
        browser = QFileDialog(self)
        browser.setFileMode(QFileDialog.Directory)

        if browser.exec():
            self.dir_list.addItems(browser.selectedFiles())
            self.save_list.setEnabled(True)

    @Slot()
    def on_dir_remove_clicked(self):
        current = self.dir_list.currentItem()

        if current is not None:
            remove_target_folder(current.text())
            self.dir_list.takeItem(self.dir_list.row(current))

    @Slot()
    def on_decrypt_select_clicked(self):
        browser = QFileDialog(self, filter='.pw_encrypt')
        browser.setFileMode(QFileDialog.ExistingFiles)
        
        if browser.exec():
            for target in browser.selectedFiles():
                encryption.decrypt_file(target)

    @Slot()
    def on_status_refresh_clicked(self):
        if self._check_connection():
            self.status_refresh.setEnabled(False)

    @Slot()
    def on_save_list_clicked(self):
        items = self._get_list_items()
        clear_target_folders()

        for item in items:
            if not exists(item):
                warn = QMessageBox(QMessageBox.Warning, 'Invalid Path', f'The entry "{item}" is invalid.',
                                   QMessageBox.Ok)
                warn.show()
                return warn.exec()

        for item in items:
            add_target_folder(item)

        self.save_list.setEnabled(False)

    @Slot()
    def on_decrypt_log_clicked(self):
        self.window_log.show()

    def is_connected(self, connected: bool):
        if connected:
            self.status.setStyleSheet('QStatusBar { color: green; }')
            self.status.showMessage('Connected')

        else:
            self.status.setStyleSheet('QStatusBar { color: red; }')
            self.status.showMessage('Disconnected')

    def _get_list_items(self) -> List[str]:
        items = []
        for i in range(self.dir_list.count()):
            items.append(self.dir_list.item(i).text())

        return items

    def _check_connection(self) -> bool:
        try:
            # Not the greatest solution but it works
            requests.get(test_url)
            self.is_connected(True)
            self.status_refresh.setEnabled(False)
            return True

        except requests.exceptions.ConnectionError:
            self.is_connected(False)
            not_connected = QMessageBox(QMessageBox.Critical, 'Unable to Connect',
                                        'The productiveware client was unable to connect to the server. ' +
                                        'Please check your internet connection and click on "Refresh Connection".',
                                        QMessageBox.Ok)
            not_connected.show()
            not_connected.exec()
            return False
