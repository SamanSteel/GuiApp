# Standard Library
from datetime import datetime
import sys
from typing import Dict, Optional
import webbrowser

# Third Library
from PySide6.QtCore import QFile, Qt, QTimer
from PySide6.QtGui import QPainter, QPixmap
from PySide6.QtWidgets import (
    QApplication,
    QFrame,
    QGridLayout,
    QHBoxLayout,
    QLabel,
    QListWidget,
    QMainWindow,
    QPushButton,
    QStackedWidget,
    QVBoxLayout,
    QWidget,
)

from config.graphic_config import graphic_settings
from config.page_config import page_settings
import config.resources_rc  # noqa: F401
from src.permission_widget import PermissionPage


class Dashboard(QMainWindow):
    def __init__(self, user: str):
        super().__init__()
        self.user = user
        self.setWindowTitle(graphic_settings.WINDOW_TITLE)
        self.resize(graphic_settings.WIDTH, graphic_settings.HEIGHT)
        self.setLayoutDirection(Qt.LayoutDirection.RightToLeft)

        # ===== Central Widget =====

        central = QWidget()
        self.setCentralWidget(central)

        main_layout = QVBoxLayout(central)
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.setSpacing(0)

        # ===== Header =====

        header = QFrame()
        header.setFixedHeight(60)
        header.setStyleSheet("""
            background-color: #eeeeee; 
            padding: 4px; 
            border: none;
            """)
        header_layout = QHBoxLayout(header)
        header_layout.setContentsMargins(20, 0, 20, 0)

        title = QLabel(graphic_settings.HEADER_TITLE)
        title.setStyleSheet(graphic_settings.HEADER_STYLE)
        logo = QLabel()
        logo.setPixmap(
            QPixmap(QFile(graphic_settings.LOGO_PATH).fileName()).scaled(
                40, 40, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation
            )
        )

        header_layout.addWidget(logo)
        header_layout.addWidget(title)
        header_layout.addStretch()

        main_layout.addWidget(header)

        # ===== Middle Section =====

        middle = QHBoxLayout()
        main_layout.addLayout(middle)

        # ===== Sidebar =====

        self.sidebar = QListWidget()
        self.sidebar.setFixedWidth(graphic_settings.SIDEBAR_WIDTH)
        self.sidebar.addItems(list(page_settings.PAGE_DICT.keys()))
        self.sidebar.setStyleSheet("""
                                QListWidget {
                                    background-color: #202020;
                                    border: none;
                                    outline: none;
                                    font-size: 12pt;
                                }
                                QListWidget::item {
                                    padding: 10px 14px;
                                    border-radius: 8px;
                                    color: #dddddd
                                }
                                QListWidget::item:selected {
                                    background-color: #c62828;
                                    color: white;
                                }
                                QListWidget::item:hover {
                                    background-color: #333333;
                                }""")

        middle.addWidget(self.sidebar)

        # ===== Content Area =====

        self.stack = QStackedWidget()

        for parent, child in page_settings.PAGE_DICT.items():
            if parent == "صفحه اصلی":
                self.stack.addWidget(self.create_dashboard_page())
            elif parent == "مدیریت نرم افزار":
                self.stack.addWidget(PermissionPage())
            else:
                self.stack.addWidget(self.create_link_page(child))
        middle.addWidget(self.stack)

        self.sidebar.currentRowChanged.connect(self.stack.setCurrentIndex)

        # ===== Status Bar (Bottom) =====

        status = QFrame()
        status.setFixedHeight(35)
        status.setStyleSheet("background-color: #eeeeee;")

        status_layout = QHBoxLayout(status)
        status_layout.setContentsMargins(20, 0, 20, 0)

        self.user_label = QLabel(f"کاربر: {self.user}")
        self.time_label = QLabel()
        self.connection_label = QLabel("● متصل")

        status_layout.addWidget(self.user_label)
        status_layout.addSpacing(20)
        status_layout.addWidget(self.connection_label)
        status_layout.addStretch()
        status_layout.addWidget(self.time_label)

        main_layout.addWidget(status)

        # ===== Timer for Clock =====
        timer = QTimer(self)
        timer.timeout.connect(self.update_time)
        timer.start(1000)
        self.update_time()

    # -------- WaterMark Logo  --------

    def paintEvent(self, event):
        super().paintEvent(event)
        painter = QPainter(self)
        pixmap = QPixmap(QFile(graphic_settings.LOGO_PATH).fileName())
        scaled = pixmap.scaled(
            self.width() * 0.6,
            self.height() * 0.6,
            Qt.AspectRatioMode.KeepAspectRatio,
            Qt.TransformationMode.SmoothTransformation,
        )
        painter.setOpacity(0.06)
        x = (self.width() - scaled.width() - graphic_settings.SIDEBAR_WIDTH) // 2
        y = (self.height() - scaled.height()) // 2
        painter.drawPixmap(x, y, scaled)

    # -------- Dashboard Pages --------

    def create_dashboard_page(self):
        page = QWidget()
        layout = QVBoxLayout(page)
        layout.setSpacing(10)
        layout.setContentsMargins(15, 15, 15, 15)
        layout.addWidget(QLabel("📊 آمار امروز", alignment=Qt.AlignmentFlag.AlignCenter))
        layout.addWidget(QLabel("تولید روزانه: 1250 تن"))
        layout.addWidget(QLabel("ضایعات: 2.3%"))
        layout.addWidget(QLabel("سفارشات فعال: 18"))

        layout.addStretch()
        return page

    # ------- Link Page  --------

    def create_link_page(self, link_dict: Optional[Dict | str]):
        page = QWidget()

        layout = QGridLayout(page)
        layout.setSpacing(5)
        layout.setContentsMargins(15, 15, 15, 15)

        if not isinstance(link_dict, Dict):
            return page
        counter = 0

        for title, link in link_dict.items():
            btn = QPushButton(title)
            btn.setCursor(Qt.CursorShape.PointingHandCursor)
            btn.setFixedHeight(40)
            btn.setStyleSheet("""
                                    QPushButton {
                                                background-color: #c62828;
                                                color: white;
                                                border-radius: 8px;
                                                font-size:13pt;
                                    }
                                    QPushButton:hover {
                                                background-color: #8e0000;
                                    }
                                """)
            btn.clicked.connect(lambda checked=False, url_link=link: webbrowser.open(url_link))

            layout.addWidget(btn, counter // 2, counter % 2)
            counter += 1
        return page

    def update_time(self):
        self.time_label.setText(datetime.now().strftime("%Y-%m-%d  %H:%M:%S"))


if __name__ == "__main__":
    app = QApplication([])
    window = Dashboard()
    window.show()
    sys.exit(app.exec())
