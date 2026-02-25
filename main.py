# Standard Library
import sys

# Third Library
from PySide6.QtCore import Qt
from PySide6.QtGui import QFont, QFontDatabase, QIcon
from PySide6.QtWidgets import QApplication, QDialog

from config.graphic_config import graphic_settings
import config.resources_rc  # noqa: F401
from src.login_dialog import LoginDialog
from src.main_page import Dashboard


def main():
    app = QApplication([])
    # -------- Import Font --------
    font_id = QFontDatabase.addApplicationFont(graphic_settings.FONT_PATH)
    if font_id!=-1:
        font_family=QFontDatabase.applicationFontFamilies(font_id)[0]
        font=QFont(font_family)
        font.setPointSize(10)
        app.setFont(font)
    else:
        print("font NOT loading")

        
    app.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
    app.setWindowIcon(QIcon(graphic_settings.LOGO_PATH))
    login_modal = LoginDialog()
    if login_modal.exec() == QDialog.DialogCode.Accepted:
        main_page = Dashboard(user=login_modal.user_name)
        main_page.show()
        sys.exit(app.exec())


if __name__ == "__main__":
    main()
