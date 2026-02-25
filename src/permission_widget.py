# Standard Library
import json
import sys
from typing import Dict

# Third Library
from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QApplication,
    QDialog,
    QLabel,
    QListWidget,
    QPushButton,
    QTreeWidget,
    QTreeWidgetItem,
    QVBoxLayout,
    QWidget,
)

from config.page_config import page_settings

ORIGIN = ["تولید", "100", "101", "کارگاه ساخت"]
GOODS = ["خرسك و ذوبي", "فروسيليكومنگنز", "ضايعات ورودي", "سرباره كوره و پاتيل", "جرم نسوز", "اهن اسفنجي ورودي"]
DESTINATIONS = ["کارگاه ساخت", "تولید", "بیرون"]


class ScopeDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("تنظیم محدودیت دسترسی")
        self.resize(300, 400)

        layout = QVBoxLayout(self)

        layout.addWidget(QLabel("کالاهای مجاز:"))
        self.goods_list = QListWidget()
        self.goods_list.addItems(GOODS)
        self.goods_list.setSelectionMode(QListWidget.SelectionMode.MultiSelection)
        layout.addWidget(self.goods_list)

        layout.addWidget(QLabel("مبداهای مجاز:"))
        self.org_list = QListWidget()
        self.org_list.addItems(ORIGIN)
        self.org_list.setSelectionMode(QListWidget.SelectionMode.MultiSelection)
        layout.addWidget(self.org_list)
        layout.addWidget(QLabel("مقصدهای مجاز:"))

        self.dest_list = QListWidget()
        self.dest_list.addItems(DESTINATIONS)
        self.dest_list.setSelectionMode(QListWidget.SelectionMode.MultiSelection)
        layout.addWidget(self.dest_list)

        save_btn = QPushButton("تایید")
        save_btn.clicked.connect(self.accept)
        layout.addWidget(save_btn)

    def get_scope(self):
        return {
            "goods": [i.text() for i in self.goods_list.selectedItems()],
            "destinations": [i.text() for i in self.dest_list.selectedItems()],
        }


class PermissionPage(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("مدیریت دسترسی نقش")
        self.resize(600, 500)

        self.permission_scopes = {}

        layout = QVBoxLayout(self)
        layout.setContentsMargins(15, 15, 15, 15)

        self.tree = QTreeWidget()
        self.tree.setHeaderLabel("دسترسی ها")
        self.tree.setContextMenuPolicy(Qt.ContextMenuPolicy.CustomContextMenu)
        self.tree.customContextMenuRequested.connect(self.open_scope_dialog)

        layout.addWidget(self.tree)

        self.build_tree()

        save_btn = QPushButton("ذخیره")
        save_btn.clicked.connect(self.export_permissions)
        save_btn.setStyleSheet("""
                                    QPushButton {
                                                background-color: #c62828;
                                                color: white;
                                                border-radius: 8px;
                                                font-size:11pt;
                                    }
                                    QPushButton {
                                                background-color: #8e0000;
                                    }
                                """)
        layout.addWidget(save_btn)

    def build_tree(self):
        for parent, child in page_settings.PAGE_DICT.items():
            parent_tree_item = QTreeWidgetItem(self.tree, [parent])
            parent_tree_item.setFlags(
                parent_tree_item.flags() | Qt.ItemFlag.ItemIsUserCheckable | Qt.ItemFlag.ItemIsAutoTristate
            )
            parent_tree_item.setCheckState(0, Qt.CheckState.Unchecked)
            if isinstance(child, Dict):
                for item, _ in child.items():
                    child_tree_item = QTreeWidgetItem(parent_tree_item, [item])
                    child_tree_item.setFlags(child_tree_item.flags() | Qt.ItemFlag.ItemIsUserCheckable)
                    child_tree_item.setCheckState(0, Qt.CheckState.Unchecked)
        self.tree.collapseAll()

    def open_scope_dialog(self, position):
        item = self.tree.itemAt(position)
        if not item or item.childCount() > 0:
            return

        dialog = ScopeDialog(self)
        if dialog.exec():
            scope = dialog.get_scope()
            key = self.get_item_path(item)
            self.permission_scopes[key] = scope
            item.setBackground(0, Qt.GlobalColor.yellow)

    def get_item_path(self, item):
        parts = []
        while item:
            parts.insert(0, item.text(0))
            item = item.parent()
        return "/".join(parts)

    def export_permissions(self):
        result = {}

        root = self.tree.invisibleRootItem()
        for i in range(root.childCount()):
            parent = root.child(i)
            for j in range(parent.childCount()):
                child = parent.child(j)
                if child.checkState(0) == Qt.CheckState.Checked:
                    key = self.get_item_path(child)
                    result[key] = self.permission_scopes.get(key, {})

        print(json.dumps(result, ensure_ascii=False, indent=4))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = PermissionPage()
    window.show()
    sys.exit(app.exec())
