# Standard Library
import sys

# Third Library
from PySide6.QtCore import QRect, Qt
from PySide6.QtWidgets import (
    QApplication,
    QDialog,
    QGridLayout,
    QGroupBox,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QPushButton,
)

from utils.login_ldap import authenticate


class LoginDialog(QDialog):
    def __init__(self):
        super().__init__()
        # config
        self.setWindowTitle("مجتمع فولاد سامان")
        self.setGeometry(QRect(100, 100, 400, 350))
        self.user_name = ""
        layout = QGridLayout(self)
        layout.setContentsMargins(20, 20, 20, 20)

        main_group_box = QGroupBox(title="ورود")
        main_group_box.setAlignment(Qt.AlignmentFlag.AlignCenter)
        main_group_box.setFixedSize(300, 200)
        layout.addWidget(main_group_box)

        # Login Layout
        login_group_layout = QGridLayout()
        login_group_layout.setSpacing(15)
        main_group_box.setLayout(login_group_layout)

        # User Name Group
        username_label = QLabel(text="نام کاربری")
        username_entry = QLineEdit()
        username_entry.setFixedWidth(200)
        username_entry.setPlaceholderText("نام کاربری خود را وارد کنید")
        username_entry.textChanged.connect(
            lambda: self._status_label_handler("با نام کاربری و رمز عبور خود وارد شوید", "blue")
        )

        # Password Group
        password_label = QLabel(text="رمز عبور")
        password_entry = QLineEdit()
        password_entry.setEchoMode(QLineEdit.EchoMode.Password)
        password_entry.setFixedWidth(200)
        password_entry.setPlaceholderText("رمز عبور خود را وارد کنید")
        password_entry.textChanged.connect(lambda: self._status_label_handler("رمز عبور خود را وارد کنید", "blue"))
        password_entry.returnPressed.connect(lambda: self._login_handler(username_entry.text(), password_entry.text()))

        # Login Group
        guest_button = QPushButton("کاربر مهمان")
        login_button = QPushButton("ورود")
        button_group = QHBoxLayout()
        button_group.addWidget(login_button)
        button_group.addWidget(guest_button)

        # Status
        self.status_lable = QLabel(text="با نام کاربری و رمز عبور خود وارد شوید")
        self.status_lable.setStyleSheet("color: blue;")

        login_button.clicked.connect(lambda: self._login_handler(username_entry.text(), password_entry.text()))
        guest_button.clicked.connect(lambda: self._login_handler("guest", "guest"))

        # Config Login Layout
        login_group_layout.addWidget(username_label, 0, 0, alignment=Qt.AlignmentFlag.AlignLeft)
        login_group_layout.addWidget(username_entry, 0, 1, alignment=Qt.AlignmentFlag.AlignRight)
        login_group_layout.addWidget(password_label, 1, 0, alignment=Qt.AlignmentFlag.AlignLeft)
        login_group_layout.addWidget(password_entry, 1, 1, alignment=Qt.AlignmentFlag.AlignRight)
        login_group_layout.addLayout(button_group, 2, 0, 1, 2, alignment=Qt.AlignmentFlag.AlignHCenter)
        login_group_layout.addWidget(self.status_lable, 3, 0, 1, 2, alignment=Qt.AlignmentFlag.AlignCenter)

    def _login_handler(self, username, password):
        if username == "" or password == "":
            self._status_label_handler("نام کاربری یا رمز عبور وارد نشده است.", "red")
        elif username == password and username == "guest":
            self._status_label_handler("کاربر مهمان", "green")
            self.accept()
            self.user_name = "مهمان"
        else:
            authenticate_result = authenticate(username, password)
            if authenticate_result:
                self._status_label_handler("ورود موفقیت آمیز بود.", "green")
                self.accept()
                self.user_name = authenticate_result
            else:
                self._status_label_handler("نام کاربری یا رمز عبور اشتباه است.", "red")

    def _status_label_handler(self, text, color):
        self.status_lable.setText(text)
        self.status_lable.setStyleSheet(f"color: {color};")


if __name__ == "__main__":
    app = QApplication([])
    window = LoginDialog()
    window.show()
    sys.exit(app.exec())
