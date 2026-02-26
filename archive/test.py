# Standard Library
import sys

# Third Library
# Third Party
from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QApplication,
    QGroupBox,
    QHBoxLayout,
    QLabel,
    QPushButton,
    QSizePolicy,
    QVBoxLayout,
    QWidget,
)


class MainPage(QWidget):
    def __init__(self):
        super().__init__()

        # Window Config
        self.setWindowTitle("مجتمع فولاد سامان")
        self.resize(750, 750)

        # ====== Main Layout ======
        main_layout = QVBoxLayout(self)
        main_layout.setContentsMargins(20, 20, 20, 20)
        main_layout.setSpacing(15)

        # ====== Access Section ======
        self.access_group = QGroupBox("دسترسی‌ها")
        self.access_group.setAlignment(Qt.AlignmentFlag.AlignCenter)

        access_layout = QVBoxLayout()
        access_layout.setSpacing(10)

        # نمونه دکمه‌ها
        access_layout.addWidget(QPushButton("مدیریت کاربران"))
        access_layout.addWidget(QPushButton("گزارشات"))
        access_layout.addWidget(QPushButton("تنظیمات سیستم"))

        access_layout.addStretch()

        self.access_group.setLayout(access_layout)

        self.access_group.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)

        # ====== Bottom User Bar ======
        self.user_group = QGroupBox()
        self.user_group.setFixedHeight(50)

        user_layout = QHBoxLayout()
        user_layout.setContentsMargins(10, 5, 10, 5)

        self.user_label = QLabel("کاربر: admin")
        logout_btn = QPushButton("خروج")

        user_layout.addWidget(self.user_label)
        user_layout.addStretch()
        user_layout.addWidget(logout_btn)

        self.user_group.setLayout(user_layout)

        # ====== Add To Main Layout ======
        main_layout.addWidget(self.access_group, 1)
        main_layout.addWidget(self.user_group, 0)


if __name__ == "__main__":
    app = QApplication([])
    window = MainPage()
    window.show()
    sys.exit(app.exec())
