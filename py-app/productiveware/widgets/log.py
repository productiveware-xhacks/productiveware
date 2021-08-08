from os.path import dirname, join, realpath
from PySide6.QtCore import Qt, Slot
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import *
from productiveware import config


class LogWidget(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Event Logs')
        self.setWindowIcon(
            QIcon(join(dirname(realpath(__file__)), 'res/productiveware.png')))

        self.log = QTextEdit()
        self.log.append(config.get_log())
        # self.log.setEnabled(False)
        self.log.setReadOnly(True)
        self.exit = QPushButton('Exit')
        self.exit.clicked.connect(self.on_exit_clicked)

        layout = QVBoxLayout()
        layout.addWidget(self.log)
        layout.addWidget(self.exit, alignment=Qt.AlignRight)
        self.setLayout(layout)

    @Slot()
    def on_exit_clicked(self):
        self.close()

