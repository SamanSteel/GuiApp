# Third Library
from pydantic_settings import BaseSettings, SettingsConfigDict


class Graphic(BaseSettings):
    model_config = SettingsConfigDict()
    FONT_PATH: str = ":/assets/Vazirmatn.ttf"
    HEADER_STYLE: str = "font-size:18px; font-weight:bold;"
    HEADER_TITLE: str = "مجتمع فولاد سامان"
    HEIGHT: int = 800
    LOGO_PATH: str = ":/assets/saman.png"
    SIDEBAR_WIDTH: int = 220
    WIDTH: int = 1200
    WINDOW_TITLE: str = "مجتمع فولاد سامان"


""" 
            QListWidget {
                background-color: #f4f4f4;
                font-family: "Vazirmtn";
                font-size: 12pt;
            }
            QListWidget::item:selected {
                background-color: #2563eb;
            }
            QTreeWidget {
                background-color: white;
                border: 1px solid #dddddd;
                padding: 5px;
            }
            QTreeWidget::item:selected {
                background-color: #ffcdd2;
                color: black;
            }
            QPushButton {
                backgroud-color: #c62828;
                color:white;
                border-redius: 6px;
                padding: 6px 12 px;
            }
            QPushButton:hover{
                background-color: #8e0000;
            }
            QHeaderView::section{
                background-color: #eeeeee
                padding: 4px;
                border: none;
            }
            """

graphic_settings = Graphic()
