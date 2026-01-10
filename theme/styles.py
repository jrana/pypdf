
# ============================================================================
# STYLES
# ============================================================================

DARK_THEME = """
QMainWindow {
    background-color: #0d1117;
}

QWidget {
    background-color: #0d1117;
    color: #c9d1d9;
    font-family: 'Segoe UI', 'SF Pro Display', -apple-system, sans-serif;
    font-size: 13px;
}

QMenuBar {
    background-color: #161b22;
    border-bottom: 1px solid #30363d;
    padding: 4px;
}

QMenuBar::item {
    background-color: transparent;
    padding: 6px 12px;
    border-radius: 4px;
}

QMenuBar::item:selected {
    background-color: #21262d;
}

QMenu {
    background-color: #161b22;
    border: 1px solid #30363d;
    border-radius: 8px;
    padding: 4px;
}

QMenu::item {
    padding: 8px 32px 8px 16px;
    border-radius: 4px;
}

QMenu::item:selected {
    background-color: #388bfd;
}

QToolBar {
    background-color: #161b22;
    border: none;
    border-bottom: 1px solid #30363d;
    padding: 8px;
    spacing: 8px;
}

QToolButton {
    background-color: #21262d;
    border: 1px solid #30363d;
    border-radius: 6px;
    padding: 8px 12px;
    color: #c9d1d9;
    font-weight: 500;
}

QToolButton:hover {
    background-color: #30363d;
    border-color: #8b949e;
}

QToolButton:pressed {
    background-color: #388bfd;
    border-color: #388bfd;
    color: white;
}

QPushButton {
    background-color: #238636;
    border: none;
    border-radius: 6px;
    padding: 8px 16px;
    color: white;
    font-weight: 600;
}

QPushButton:hover {
    background-color: #2ea043;
}

QPushButton:pressed {
    background-color: #238636;
}

QPushButton#secondaryBtn {
    background-color: #21262d;
    border: 1px solid #30363d;
    color: #c9d1d9;
}

QPushButton#secondaryBtn:hover {
    background-color: #30363d;
    border-color: #8b949e;
}

QListWidget {
    background-color: #0d1117;
    border: none;
    outline: none;
    padding: 8px;
}

QListWidget::item {
    background-color: #161b22;
    border: 1px solid transparent;
    border-radius: 8px;
    padding: 12px;
    margin: 4px 0;
    color: #c9d1d9;
}

QListWidget::item:hover {
    background-color: #21262d;
    border-color: #30363d;
}

QListWidget::item:selected {
    background-color: #1f6feb;
    border-color: #388bfd;
}

QTabWidget::pane {
    background-color: #0d1117;
    border: none;
}

QTabBar::tab {
    background-color: #161b22;
    border: 1px solid #30363d;
    border-bottom: none;
    border-top-left-radius: 8px;
    border-top-right-radius: 8px;
    padding: 10px 20px;
    margin-right: 4px;
    color: #8b949e;
}

QTabBar::tab:selected {
    background-color: #0d1117;
    color: #c9d1d9;
    border-bottom: 2px solid #fd8c73;
}

QTabBar::tab:hover:!selected {
    background-color: #21262d;
}

QScrollArea {
    background-color: #0d1117;
    border: none;
}

QScrollBar:vertical {
    background-color: #0d1117;
    width: 12px;
    border-radius: 6px;
}

QScrollBar::handle:vertical {
    background-color: #30363d;
    border-radius: 6px;
    min-height: 40px;
}

QScrollBar::handle:vertical:hover {
    background-color: #484f58;
}

QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {
    height: 0;
}

QScrollBar:horizontal {
    background-color: #0d1117;
    height: 12px;
    border-radius: 6px;
}

QScrollBar::handle:horizontal {
    background-color: #30363d;
    border-radius: 6px;
    min-width: 40px;
}

QScrollBar::handle:horizontal:hover {
    background-color: #484f58;
}

QScrollBar::add-line:horizontal, QScrollBar::sub-line:horizontal {
    width: 0;
}

QSlider::groove:horizontal {
    background-color: #21262d;
    height: 6px;
    border-radius: 3px;
}

QSlider::handle:horizontal {
    background-color: #1f6feb;
    width: 16px;
    height: 16px;
    border-radius: 8px;
    margin: -5px 0;
}

QSlider::handle:horizontal:hover {
    background-color: #388bfd;
}

QSpinBox, QComboBox {
    background-color: #0d1117;
    border: 1px solid #30363d;
    border-radius: 6px;
    padding: 6px 12px;
    color: #c9d1d9;
}

QSpinBox:hover, QComboBox:hover {
    border-color: #8b949e;
}

QSpinBox:focus, QComboBox:focus {
    border-color: #388bfd;
}

QComboBox::drop-down {
    border: none;
    padding-right: 8px;
}

QStatusBar {
    background-color: #161b22;
    border-top: 1px solid #30363d;
    color: #8b949e;
}

QLabel#titleLabel {
    font-size: 24px;
    font-weight: 700;
    color: #c9d1d9;
}

QLabel#subtitleLabel {
    font-size: 14px;
    color: #8b949e;
}

QFrame#separator {
    background-color: #30363d;
    max-height: 1px;
}

QGraphicsView {
    background-color: #161b22;
    border: none;
}

QDockWidget {
    titlebar-close-icon: none;
    titlebar-normal-icon: none;
}

QDockWidget::title {
    background-color: #161b22;
    padding: 12px;
    font-weight: 600;
    border-bottom: 1px solid #30363d;
}

QLineEdit {
    background-color: #21262d;
    border: 1px solid #30363d;
    border-radius: 6px;
    padding: 8px 12px;
    color: #c9d1d9;
}

QLineEdit:focus {
    border-color: #388bfd;
}
"""

LIGHT_THEME = """
QMainWindow {
    background-color: #ffffff;
}

QWidget {
    background-color: #ffffff;
    color: #1f2328;
    font-family: 'Segoe UI', 'SF Pro Display', -apple-system, sans-serif;
    font-size: 13px;
}

QMenuBar {
    background-color: #f6f8fa;
    border-bottom: 1px solid #d0d7de;
    padding: 4px;
}

QMenuBar::item {
    background-color: transparent;
    padding: 6px 12px;
    border-radius: 4px;
}

QMenuBar::item:selected {
    background-color: #eaeef2;
}

QMenu {
    background-color: #ffffff;
    border: 1px solid #d0d7de;
    border-radius: 8px;
    padding: 4px;
}

QMenu::item {
    padding: 8px 32px 8px 16px;
    border-radius: 4px;
    color: #1f2328;
}

QMenu::item:selected {
    background-color: #0969da;
    color: white;
}

QToolBar {
    background-color: #f6f8fa;
    border: none;
    border-bottom: 1px solid #d0d7de;
    padding: 8px;
    spacing: 8px;
}

QToolButton {
    background-color: #ffffff;
    border: 1px solid #d0d7de;
    border-radius: 6px;
    padding: 8px 12px;
    color: #1f2328;
    font-weight: 500;
}

QToolButton:hover {
    background-color: #f3f4f6;
    border-color: #8b949e;
}

QToolButton:pressed {
    background-color: #0969da;
    border-color: #0969da;
    color: white;
}

QPushButton {
    background-color: #1f883d;
    border: none;
    border-radius: 6px;
    padding: 8px 16px;
    color: white;
    font-weight: 600;
}

QPushButton:hover {
    background-color: #2da44e;
}

QPushButton:pressed {
    background-color: #1f883d;
}

QPushButton#secondaryBtn {
    background-color: #f6f8fa;
    border: 1px solid #d0d7de;
    color: #1f2328;
}

QPushButton#secondaryBtn:hover {
    background-color: #eaeef2;
    border-color: #8b949e;
}

QListWidget {
    background-color: #ffffff;
    border: none;
    outline: none;
    padding: 8px;
}

QListWidget::item {
    background-color: #f6f8fa;
    border: 1px solid transparent;
    border-radius: 8px;
    padding: 12px;
    margin: 4px 0;
    color: #1f2328;
}

QListWidget::item:hover {
    background-color: #eaeef2;
    border-color: #d0d7de;
}

QListWidget::item:selected {
    background-color: #0969da;
    border-color: #0550ae;
    color: white;
}

QTabWidget::pane {
    background-color: #ffffff;
    border: none;
}

QTabBar::tab {
    background-color: #f6f8fa;
    border: 1px solid #d0d7de;
    border-bottom: none;
    border-top-left-radius: 8px;
    border-top-right-radius: 8px;
    padding: 10px 20px;
    margin-right: 4px;
    color: #57606a;
}

QTabBar::tab:selected {
    background-color: #ffffff;
    color: #1f2328;
    border-bottom: 2px solid #0969da;
}

QTabBar::tab:hover:!selected {
    background-color: #eaeef2;
}

QScrollArea {
    background-color: #ffffff;
    border: none;
}

QScrollBar:vertical {
    background-color: #ffffff;
    width: 12px;
    border-radius: 6px;
}

QScrollBar::handle:vertical {
    background-color: #d0d7de;
    border-radius: 6px;
    min-height: 40px;
}

QScrollBar::handle:vertical:hover {
    background-color: #8b949e;
}

QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {
    height: 0;
}

QScrollBar:horizontal {
    background-color: #ffffff;
    height: 12px;
    border-radius: 6px;
}

QScrollBar::handle:horizontal {
    background-color: #d0d7de;
    border-radius: 6px;
    min-width: 40px;
}

QScrollBar::handle:horizontal:hover {
    background-color: #8b949e;
}

QScrollBar::add-line:horizontal, QScrollBar::sub-line:horizontal {
    width: 0;
}

QSlider::groove:horizontal {
    background-color: #eaeef2;
    height: 6px;
    border-radius: 3px;
}

QSlider::handle:horizontal {
    background-color: #0969da;
    width: 16px;
    height: 16px;
    border-radius: 8px;
    margin: -5px 0;
}

QSlider::handle:horizontal:hover {
    background-color: #0550ae;
}

QSpinBox, QComboBox {
    background-color: #ffffff;
    border: 1px solid #d0d7de;
    border-radius: 6px;
    padding: 6px 12px;
    color: #1f2328;
}

QSpinBox:hover, QComboBox:hover {
    border-color: #8b949e;
}

QSpinBox:focus, QComboBox:focus {
    border-color: #0969da;
}

QComboBox::drop-down {
    border: none;
    padding-right: 8px;
}

QStatusBar {
    background-color: #f6f8fa;
    border-top: 1px solid #d0d7de;
    color: #57606a;
}

QLabel#titleLabel {
    font-size: 24px;
    font-weight: 700;
    color: #1f2328;
}

QLabel#subtitleLabel {
    font-size: 14px;
    color: #57606a;
}

QFrame#separator {
    background-color: #d0d7de;
    max-height: 1px;
}

QGraphicsView {
    background-color: #eaeef2;
    border: none;
}

QDockWidget {
    titlebar-close-icon: none;
    titlebar-normal-icon: none;
}

QDockWidget::title {
    background-color: #f6f8fa;
    padding: 12px;
    font-weight: 600;
    border-bottom: 1px solid #d0d7de;
}

QLineEdit {
    background-color: #ffffff;
    border: 1px solid #d0d7de;
    border-radius: 6px;
    padding: 8px 12px;
    color: #1f2328;
}

QLineEdit:focus {
    border-color: #0969da;
}
"""
