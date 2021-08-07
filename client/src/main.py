import sys
from PySide6 import QtWidgets

from . import widgets


if __name__ == '__main__':
    app = QtWidgets.QApplication()

    login_form = widgets.LoginWidget()
    login_form.setFixedSize(300, 150)
    login_form.show()

    sys.exit(app.exec())
