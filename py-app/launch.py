import sys
from PySide6 import QtWidgets

from productiveware.widgets.main_window import MainWidget


if __name__ == '__main__':
    app = QtWidgets.QApplication()
    main_window = MainWidget()
    sys.exit(app.exec())
