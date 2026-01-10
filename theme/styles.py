
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

MIDNIGHT_BLUE_THEME = """
QMainWindow {
    background-color: #0b1021;
}

QWidget {
    background-color: #0b1021;
    color: #a4b1cd;
    font-family: 'Segoe UI', 'SF Pro Display', -apple-system, sans-serif;
    font-size: 13px;
}

QMenuBar {
    background-color: #0f152a;
    border-bottom: 1px solid #1e2540;
    padding: 4px;
}

QMenuBar::item {
    background-color: transparent;
    padding: 6px 12px;
    border-radius: 4px;
}

QMenuBar::item:selected {
    background-color: #1a223e;
}

QMenu {
    background-color: #0f152a;
    border: 1px solid #1e2540;
    border-radius: 8px;
    padding: 4px;
}

QMenu::item {
    padding: 8px 32px 8px 16px;
    border-radius: 4px;
}

QMenu::item:selected {
    background-color: #3e6cd5;
}

QToolBar {
    background-color: #0f152a;
    border: none;
    border-bottom: 1px solid #1e2540;
    padding: 8px;
    spacing: 8px;
}

QToolButton {
    background-color: #1a223e;
    border: 1px solid #1e2540;
    border-radius: 6px;
    padding: 8px 12px;
    color: #a4b1cd;
    font-weight: 500;
}

QToolButton:hover {
    background-color: #242c4c;
    border-color: #4c5d8a;
}

QToolButton:pressed {
    background-color: #3e6cd5;
    border-color: #3e6cd5;
    color: white;
}

QPushButton {
    background-color: #2b55b7;
    border: none;
    border-radius: 6px;
    padding: 8px 16px;
    color: white;
    font-weight: 600;
}

QPushButton:hover {
    background-color: #3562ca;
}

QPushButton:pressed {
    background-color: #2b55b7;
}

QPushButton#secondaryBtn {
    background-color: #1a223e;
    border: 1px solid #1e2540;
    color: #a4b1cd;
}

QPushButton#secondaryBtn:hover {
    background-color: #242c4c;
    border-color: #4c5d8a;
}

QListWidget {
    background-color: #0b1021;
    border: none;
    outline: none;
    padding: 8px;
}

QListWidget::item {
    background-color: #0f152a;
    border: 1px solid transparent;
    border-radius: 8px;
    padding: 12px;
    margin: 4px 0;
    color: #a4b1cd;
}

QListWidget::item:hover {
    background-color: #1a223e;
    border-color: #1e2540;
}

QListWidget::item:selected {
    background-color: #1f4287;
    border-color: #3e6cd5;
}

QTabWidget::pane {
    background-color: #0b1021;
    border: none;
}

QTabBar::tab {
    background-color: #0f152a;
    border: 1px solid #1e2540;
    border-bottom: none;
    border-top-left-radius: 8px;
    border-top-right-radius: 8px;
    padding: 10px 20px;
    margin-right: 4px;
    color: #6b7a99;
}

QTabBar::tab:selected {
    background-color: #0b1021;
    color: #a4b1cd;
    border-bottom: 2px solid #3e6cd5;
}

QTabBar::tab:hover:!selected {
    background-color: #1a223e;
}

QScrollArea {
    background-color: #0b1021;
    border: none;
}

QScrollBar:vertical {
    background-color: #0b1021;
    width: 12px;
    border-radius: 6px;
}

QScrollBar::handle:vertical {
    background-color: #1e2540;
    border-radius: 6px;
    min-height: 40px;
}

QScrollBar::handle:vertical:hover {
    background-color: #2b3558;
}

QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {
    height: 0;
}

QScrollBar:horizontal {
    background-color: #0b1021;
    height: 12px;
    border-radius: 6px;
}

QScrollBar::handle:horizontal {
    background-color: #1e2540;
    border-radius: 6px;
    min-width: 40px;
}

QScrollBar::handle:horizontal:hover {
    background-color: #2b3558;
}

QScrollBar::add-line:horizontal, QScrollBar::sub-line:horizontal {
    width: 0;
}

QSlider::groove:horizontal {
    background-color: #1a223e;
    height: 6px;
    border-radius: 3px;
}

QSlider::handle:horizontal {
    background-color: #3e6cd5;
    width: 16px;
    height: 16px;
    border-radius: 8px;
    margin: -5px 0;
}

QSlider::handle:horizontal:hover {
    background-color: #4c7ce9;
}

QSpinBox, QComboBox {
    background-color: #0b1021;
    border: 1px solid #1e2540;
    border-radius: 6px;
    padding: 6px 12px;
    color: #a4b1cd;
}

QSpinBox:hover, QComboBox:hover {
    border-color: #4c5d8a;
}

QSpinBox:focus, QComboBox:focus {
    border-color: #3e6cd5;
}

QComboBox::drop-down {
    border: none;
    padding-right: 8px;
}

QStatusBar {
    background-color: #0f152a;
    border-top: 1px solid #1e2540;
    color: #6b7a99;
}

QLabel#titleLabel {
    font-size: 24px;
    font-weight: 700;
    color: #a4b1cd;
}

QLabel#subtitleLabel {
    font-size: 14px;
    color: #6b7a99;
}

QFrame#separator {
    background-color: #1e2540;
    max-height: 1px;
}

QGraphicsView {
    background-color: #0f152a;
    border: none;
}

QDockWidget {
    titlebar-close-icon: none;
    titlebar-normal-icon: none;
}

QDockWidget::title {
    background-color: #0f152a;
    padding: 12px;
    font-weight: 600;
    border-bottom: 1px solid #1e2540;
}

QLineEdit {
    background-color: #1a223e;
    border: 1px solid #1e2540;
    border-radius: 6px;
    padding: 8px 12px;
    color: #a4b1cd;
}

QLineEdit:focus {
    border-color: #3e6cd5;
}
"""

EGGPLANT_THEME = """
QMainWindow {
    background-color: #50384e;
}

QWidget {
    background-color: #50384e;
    color: #ece0ec;
    font-family: 'Segoe UI', 'SF Pro Display', -apple-system, sans-serif;
    font-size: 13px;
}

QMenuBar {
    background-color: #3a2839;
    border-bottom: 1px solid #6b5069;
    padding: 4px;
}

QMenuBar::item {
    background-color: transparent;
    padding: 6px 12px;
    border-radius: 4px;
}

QMenuBar::item:selected {
    background-color: #664963;
}

QMenu {
    background-color: #3a2839;
    border: 1px solid #6b5069;
    border-radius: 8px;
    padding: 4px;
}

QMenu::item {
    padding: 8px 32px 8px 16px;
    border-radius: 4px;
}

QMenu::item:selected {
    background-color: #8e44ad;
}

QToolBar {
    background-color: #3a2839;
    border: none;
    border-bottom: 1px solid #6b5069;
    padding: 8px;
    spacing: 8px;
}

QToolButton {
    background-color: #50384e;
    border: 1px solid #6b5069;
    border-radius: 6px;
    padding: 8px 12px;
    color: #ece0ec;
    font-weight: 500;
}

QToolButton:hover {
    background-color: #664963;
    border-color: #a0809d;
}

QToolButton:pressed {
    background-color: #8e44ad;
    border-color: #8e44ad;
    color: white;
}

QPushButton {
    background-color: #8e44ad;
    border: none;
    border-radius: 6px;
    padding: 8px 16px;
    color: white;
    font-weight: 600;
}

QPushButton:hover {
    background-color: #9b59b6;
}

QPushButton:pressed {
    background-color: #8e44ad;
}

QPushButton#secondaryBtn {
    background-color: #50384e;
    border: 1px solid #6b5069;
    color: #ece0ec;
}

QPushButton#secondaryBtn:hover {
    background-color: #664963;
    border-color: #a0809d;
}

QListWidget {
    background-color: #50384e;
    border: none;
    outline: none;
    padding: 8px;
}

QListWidget::item {
    background-color: #3a2839;
    border: 1px solid transparent;
    border-radius: 8px;
    padding: 12px;
    margin: 4px 0;
    color: #ece0ec;
}

QListWidget::item:hover {
    background-color: #664963;
    border-color: #6b5069;
}

QListWidget::item:selected {
    background-color: #71368a;
    border-color: #8e44ad;
}

QTabWidget::pane {
    background-color: #50384e;
    border: none;
}

QTabBar::tab {
    background-color: #3a2839;
    border: 1px solid #6b5069;
    border-bottom: none;
    border-top-left-radius: 8px;
    border-top-right-radius: 8px;
    padding: 10px 20px;
    margin-right: 4px;
    color: #b0a0b0;
}

QTabBar::tab:selected {
    background-color: #50384e;
    color: #ece0ec;
    border-bottom: 2px solid #8e44ad;
}

QTabBar::tab:hover:!selected {
    background-color: #664963;
}

QScrollArea {
    background-color: #50384e;
    border: none;
}

QScrollBar:vertical {
    background-color: #50384e;
    width: 12px;
    border-radius: 6px;
}

QScrollBar::handle:vertical {
    background-color: #6b5069;
    border-radius: 6px;
    min-height: 40px;
}

QScrollBar::handle:vertical:hover {
    background-color: #856583;
}

QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {
    height: 0;
}

QScrollBar:horizontal {
    background-color: #50384e;
    height: 12px;
    border-radius: 6px;
}

QScrollBar::handle:horizontal {
    background-color: #6b5069;
    border-radius: 6px;
    min-width: 40px;
}

QScrollBar::handle:horizontal:hover {
    background-color: #856583;
}

QScrollBar::add-line:horizontal, QScrollBar::sub-line:horizontal {
    width: 0;
}

QSlider::groove:horizontal {
    background-color: #3a2839;
    height: 6px;
    border-radius: 3px;
}

QSlider::handle:horizontal {
    background-color: #8e44ad;
    width: 16px;
    height: 16px;
    border-radius: 8px;
    margin: -5px 0;
}

QSlider::handle:horizontal:hover {
    background-color: #9b59b6;
}

QSpinBox, QComboBox {
    background-color: #3a2839;
    border: 1px solid #6b5069;
    border-radius: 6px;
    padding: 6px 12px;
    color: #ece0ec;
}

QSpinBox:hover, QComboBox:hover {
    border-color: #a0809d;
}

QSpinBox:focus, QComboBox:focus {
    border-color: #8e44ad;
}

QComboBox::drop-down {
    border: none;
    padding-right: 8px;
}

QStatusBar {
    background-color: #3a2839;
    border-top: 1px solid #6b5069;
    color: #b0a0b0;
}

QLabel#titleLabel {
    font-size: 24px;
    font-weight: 700;
    color: #ece0ec;
}

QLabel#subtitleLabel {
    font-size: 14px;
    color: #b0a0b0;
}

QFrame#separator {
    background-color: #6b5069;
    max-height: 1px;
}

QGraphicsView {
    background-color: #3a2839;
    border: none;
}

QDockWidget {
    titlebar-close-icon: none;
    titlebar-normal-icon: none;
}

QDockWidget::title {
    background-color: #3a2839;
    padding: 12px;
    font-weight: 600;
    border-bottom: 1px solid #6b5069;
}

QLineEdit {
    background-color: #3a2839;
    border: 1px solid #6b5069;
    border-radius: 6px;
    padding: 8px 12px;
    color: #ece0ec;
}

QLineEdit:focus {
    border-color: #8e44ad;
}
"""
