import sys
from PySide6 import QtWidgets

from productiveware.widgets import LoginWidget, MainWidget


if __name__ == '__main__':
    app = QtWidgets.QApplication()

    # login_form = LoginWidget()
    # login_form.setFixedSize(300, 150)
    # login_form.show()

    main_window = MainWidget()
    main_window.resize(800, 600)
    main_window.show()

    sys.exit(app.exec())
