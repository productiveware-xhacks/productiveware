import sys
from PySide6 import QtWidgets

from productiveware.widgets.main_window import MainWidget


if __name__ == '__main__':
    app = QtWidgets.QApplication()

    main_window = MainWidget()
    main_window.resize(800, 600)
    main_window.show()

    sys.exit(app.exec())
