"""
PyPDF - PDF Viewer & Editor
A modern, feature-rich PDF application built with PyQt6 and PyMuPDF
"""

import sys
import os
from pathlib import Path
from typing import Optional, List, Dict
import fitz  # PyMuPDF

from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QSplitter, QListWidget, QListWidgetItem, QTabWidget, QScrollArea,
    QLabel, QToolBar, QStatusBar, QFileDialog, QSlider, QSpinBox,
    QComboBox, QPushButton, QFrame, QMessageBox, QInputDialog,
    QGraphicsView, QGraphicsScene, QGraphicsPixmapItem, QSizePolicy,
    QMenu, QToolButton, QDockWidget, QLineEdit, QGridLayout,
    QStackedWidget, QCheckBox, QDialog, QDialogButtonBox, QProgressDialog,
    QGraphicsDropShadowEffect
)
from PyQt6.QtCore import Qt, QSize, QPointF, QRectF, pyqtSignal, QTimer, QMarginsF, QSettings
from PyQt6.QtGui import (
    QPixmap, QImage, QAction, QIcon, QFont, QPainter, QPen, QColor,
    QKeySequence, QWheelEvent, QMouseEvent, QCursor, QTransform,
    QPalette, QBrush, QLinearGradient, QPageLayout, QPageSize
)
from PyQt6.QtPrintSupport import QPrinter, QPrintDialog, QPrintPreviewDialog


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
    border-bottom: 2px solid #388bfd;
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
    background-color: #388bfd;
    width: 16px;
    height: 16px;
    border-radius: 8px;
    margin: -5px 0;
}

QSlider::handle:horizontal:hover {
    background-color: #58a6ff;
}

QSpinBox, QComboBox {
    background-color: #21262d;
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


# ============================================================================
# PDF PAGE WIDGET
# ============================================================================

class PDFPageView(QGraphicsView):
    """Custom graphics view for displaying PDF pages with zoom and pan - continuous scroll mode."""
    
    page_changed = pyqtSignal(int)
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.scene = QGraphicsScene(self)
        self.setScene(self.scene)
        
        self.pdf_doc: Optional[fitz.Document] = None
        self.current_page = 0
        self.zoom_level = 1.0
        self.min_zoom = 0.25
        self.max_zoom = 4.0
        
        self.pixmap_items: List[QGraphicsPixmapItem] = []  # All page items
        self.page_positions: List[float] = []  # Y position of each page
        self.page_gap = 20  # Gap between pages in pixels
        
        # Configure view
        self.setRenderHint(QPainter.RenderHint.Antialiasing)
        self.setRenderHint(QPainter.RenderHint.SmoothPixmapTransform)
        self.setViewportUpdateMode(QGraphicsView.ViewportUpdateMode.FullViewportUpdate)
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        self.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        self.setTransformationAnchor(QGraphicsView.ViewportAnchor.AnchorUnderMouse)
        self.setResizeAnchor(QGraphicsView.ViewportAnchor.AnchorUnderMouse)
        self.setDragMode(QGraphicsView.DragMode.ScrollHandDrag)
        
        # Background
        self.setBackgroundBrush(QBrush(QColor("#161b22")))
        
        # Connect scrollbar to track current page
        self.verticalScrollBar().valueChanged.connect(self._on_scroll)
        
        # Annotations
        self.annotations: List[Dict] = []
        self.current_tool = "select"  # select, highlight, text, draw
        self.drawing = False
        self.draw_start = None
        
    def load_pdf(self, file_path: str) -> bool:
        """Load a PDF file."""
        try:
            self.pdf_doc = fitz.open(file_path)
            self.current_page = 0
            self.zoom_level = 1.0
            self.render_all_pages()
            return True
        except Exception as e:
            print(f"Error loading PDF: {e}")
            return False
    
    def render_all_pages(self):
        """Render all pages stacked vertically for continuous scrolling."""
        if not self.pdf_doc:
            return
        
        self.scene.clear()
        self.pixmap_items.clear()
        self.page_positions.clear()
        
        current_y = self.page_gap
        max_width = 0
        
        # Calculate maximum page width to center all pages
        for i in range(len(self.pdf_doc)):
            page = self.pdf_doc[i]
            page_width = page.rect.width * self.zoom_level * 2
            max_width = max(max_width, page_width)
        
        # Render each page
        for i in range(len(self.pdf_doc)):
            page = self.pdf_doc[i]
            
            # Create a matrix for zoom
            mat = fitz.Matrix(self.zoom_level * 2, self.zoom_level * 2)  # 2x for better quality
            pix = page.get_pixmap(matrix=mat, alpha=False)
            
            # Convert to QImage
            img = QImage(pix.samples, pix.width, pix.height, pix.stride, QImage.Format.Format_RGB888)
            pixmap = QPixmap.fromImage(img)
            
            # Add to scene - centered horizontally
            pixmap_item = self.scene.addPixmap(pixmap)
            x_offset = (max_width - pixmap.width()) / 2
            pixmap_item.setPos(x_offset, current_y)
            
            self.pixmap_items.append(pixmap_item)
            self.page_positions.append(current_y)
            
            current_y += pixmap.height() + self.page_gap
        
        # Set scene rect
        total_height = current_y
        self.scene.setSceneRect(0, 0, max_width, total_height)
        
        # Scroll to current page
        if self.page_positions:
            self._scroll_to_page(self.current_page)
    
    def render_page(self):
        """Re-render all pages (for compatibility)."""
        self.render_all_pages()
    
    def set_zoom(self, zoom: float):
        """Set zoom level and re-render."""
        old_zoom = self.zoom_level
        self.zoom_level = max(self.min_zoom, min(zoom, self.max_zoom))
        if old_zoom != self.zoom_level:
            # Remember current page before re-render
            current = self.current_page
            self.render_all_pages()
            # Scroll back to the same page
            self._scroll_to_page(current)
    
    def zoom_in(self):
        """Zoom in by 25%."""
        self.set_zoom(self.zoom_level * 1.25)
    
    def zoom_out(self):
        """Zoom out by 25%."""
        self.set_zoom(self.zoom_level / 1.25)
    
    def fit_width(self):
        """Fit page to viewport width."""
        if not self.pdf_doc:
            return
        page = self.pdf_doc[self.current_page]
        page_width = page.rect.width
        viewport_width = self.viewport().width() - 40
        self.set_zoom(viewport_width / page_width / 2)
    
    def fit_page(self):
        """Fit entire page in viewport."""
        if not self.pdf_doc:
            return
        page = self.pdf_doc[self.current_page]
        page_rect = page.rect
        viewport = self.viewport().rect()
        
        width_ratio = (viewport.width() - 40) / page_rect.width / 2
        height_ratio = (viewport.height() - 40) / page_rect.height / 2
        
        self.set_zoom(min(width_ratio, height_ratio))
    
    def _scroll_to_page(self, page_num: int):
        """Scroll to show a specific page at the top of the view."""
        if not self.page_positions or page_num >= len(self.page_positions):
            return
        
        # Get the Y position of the page
        y_pos = self.page_positions[page_num]
        
        # Scroll to that position
        self.centerOn(self.scene.sceneRect().width() / 2, y_pos + 100)
    
    def _on_scroll(self):
        """Track scroll position to update current page indicator."""
        if not self.page_positions:
            return
        
        # Get the center Y position of the viewport in scene coordinates
        viewport_center = self.mapToScene(self.viewport().rect().center())
        center_y = viewport_center.y()
        
        # Find which page is at the center
        new_page = 0  # Default to first page if scrolled above all pages
        for i in range(len(self.page_positions) - 1, -1, -1):
            if center_y >= self.page_positions[i]:
                new_page = i
                break
        
        if self.current_page != new_page:
            self.current_page = new_page
            self.page_changed.emit(self.current_page)
    
    def go_to_page(self, page_num: int):
        """Navigate to a specific page by scrolling."""
        if not self.pdf_doc:
            return
        
        if 0 <= page_num < len(self.pdf_doc):
            self.current_page = page_num
            self._scroll_to_page(page_num)
            self.page_changed.emit(self.current_page)
    
    def next_page(self):
        """Go to next page."""
        self.go_to_page(self.current_page + 1)
    
    def prev_page(self):
        """Go to previous page."""
        self.go_to_page(self.current_page - 1)
    
    def get_page_count(self) -> int:
        """Get total number of pages."""
        return len(self.pdf_doc) if self.pdf_doc else 0
    
    def wheelEvent(self, event: QWheelEvent):
        """Handle mouse wheel for zoom with Ctrl."""
        if event.modifiers() == Qt.KeyboardModifier.ControlModifier:
            delta = event.angleDelta().y()
            if delta > 0:
                self.zoom_in()
            else:
                self.zoom_out()
            event.accept()
        else:
            super().wheelEvent(event)
    
    def close_pdf(self):
        """Close the current PDF."""
        if self.pdf_doc:
            self.pdf_doc.close()
            self.pdf_doc = None
        self.scene.clear()
        self.pixmap_items.clear()
        self.page_positions.clear()


# ============================================================================
# PAGE THUMBNAIL WIDGET
# ============================================================================

class PageThumbnail(QFrame):
    """A clickable thumbnail for a PDF page with drag-drop support."""
    
    clicked = pyqtSignal(int)
    selection_changed = pyqtSignal(int, bool)
    double_clicked = pyqtSignal(int)
    drag_started = pyqtSignal(int)
    
    def __init__(self, page_num: int, pixmap: QPixmap, theme: str = "dark", parent=None):
        super().__init__(parent)
        self.page_num = page_num
        self.selected = False
        self.current_theme = theme
        self.pixmap = pixmap
        self.drag_start_pos = None
        
        self.setAcceptDrops(True)
        self.setup_ui(pixmap)
        self.update_style()
    
    def setup_ui(self, pixmap: QPixmap):
        """Set up the thumbnail UI."""
        layout = QVBoxLayout(self)
        layout.setContentsMargins(8, 8, 8, 8)
        layout.setSpacing(6)
        
        # Thumbnail image
        self.image_label = QLabel()
        self.image_label.setPixmap(pixmap)
        self.image_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.image_label)
        
        # Page number label
        self.page_label = QLabel(f"Page {self.page_num + 1}")
        self.page_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.page_label.setStyleSheet("font-size: 12px; color: #8b949e;")
        layout.addWidget(self.page_label)
        
        # Selection checkbox
        self.checkbox = QCheckBox()
        self.checkbox.setStyleSheet("""
            QCheckBox {
                spacing: 0px;
            }
            QCheckBox::indicator {
                width: 18px;
                height: 18px;
                border-radius: 4px;
                border: 2px solid #30363d;
                background-color: #21262d;
            }
            QCheckBox::indicator:checked {
                background-color: #238636;
                border-color: #238636;
            }
            QCheckBox::indicator:hover {
                border-color: #8b949e;
            }
        """)
        self.checkbox.stateChanged.connect(self.on_checkbox_changed)
        
        checkbox_layout = QHBoxLayout()
        checkbox_layout.addStretch()
        checkbox_layout.addWidget(self.checkbox)
        checkbox_layout.addStretch()
        layout.addLayout(checkbox_layout)
        
        self.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.setFixedSize(180, 260)
        
        # Add drop shadow effect
        shadow = QGraphicsDropShadowEffect(self)
        shadow.setBlurRadius(15)
        shadow.setXOffset(0)
        shadow.setYOffset(4)
        shadow.setColor(QColor(0, 0, 0, 60))  # Light black shadow with transparency
        self.setGraphicsEffect(shadow)
        
        # Store original pixmap for rescaling
        self.original_pixmap = pixmap
    
    def update_size(self, width: int, height: int):
        """Update thumbnail size dynamically."""
        self.setFixedSize(width, height)
        
        # Rescale the image to fit
        img_width = width - 20  # Account for padding
        img_height = height - 60  # Account for label and checkbox
        
        scaled = self.original_pixmap.scaled(
            img_width, img_height,
            Qt.AspectRatioMode.KeepAspectRatio,
            Qt.TransformationMode.SmoothTransformation
        )
        self.image_label.setPixmap(scaled)
    
    def update_style(self):
        """Update the visual style based on selection state and theme."""
        if self.current_theme == "dark":
            if self.selected:
                self.setStyleSheet("""
                    PageThumbnail {
                        background-color: #1f6feb;
                        border: 2px solid #388bfd;
                        border-radius: 12px;
                    }
                """)
                self.page_label.setStyleSheet("font-size: 12px; color: #ffffff; font-weight: 600;")
            else:
                self.setStyleSheet("""
                    PageThumbnail {
                        background-color: #21262d;
                        border: 2px solid #30363d;
                        border-radius: 12px;
                    }
                    PageThumbnail:hover {
                        background-color: #30363d;
                        border-color: #8b949e;
                    }
                """)
                self.page_label.setStyleSheet("font-size: 12px; color: #8b949e;")
        else:  # light theme
            if self.selected:
                self.setStyleSheet("""
                    PageThumbnail {
                        background-color: #0969da;
                        border: 2px solid #0550ae;
                        border-radius: 12px;
                    }
                """)
                self.page_label.setStyleSheet("font-size: 12px; color: #ffffff; font-weight: 600;")
            else:
                self.setStyleSheet("""
                    PageThumbnail {
                        background-color: #ffffff;
                        border: 2px solid #d0d7de;
                        border-radius: 12px;
                    }
                    PageThumbnail:hover {
                        background-color: #f6f8fa;
                        border-color: #8b949e;
                    }
                """)
                self.page_label.setStyleSheet("font-size: 12px; color: #57606a;")
    
    def set_theme(self, theme: str):
        """Update the thumbnail theme."""
        self.current_theme = theme
        self.update_style()
    
    def on_checkbox_changed(self, state):
        """Handle checkbox state change."""
        self.selected = state == Qt.CheckState.Checked.value
        self.update_style()
        self.selection_changed.emit(self.page_num, self.selected)
    
    def set_selected(self, selected: bool):
        """Set the selection state."""
        self.selected = selected
        self.checkbox.blockSignals(True)
        self.checkbox.setChecked(selected)
        self.checkbox.blockSignals(False)
        self.update_style()
    
    def mousePressEvent(self, event: QMouseEvent):
        """Handle mouse click and start drag tracking."""
        if event.button() == Qt.MouseButton.LeftButton:
            self.drag_start_pos = event.pos()
            self.clicked.emit(self.page_num)
        super().mousePressEvent(event)
    
    def mouseDoubleClickEvent(self, event: QMouseEvent):
        """Handle double click to go to page."""
        if event.button() == Qt.MouseButton.LeftButton:
            self.double_clicked.emit(self.page_num)
        super().mouseDoubleClickEvent(event)
    
    def mouseMoveEvent(self, event: QMouseEvent):
        """Handle mouse move for drag initiation."""
        if self.drag_start_pos is None:
            return
        
        # Check if we've moved enough to start a drag
        if (event.pos() - self.drag_start_pos).manhattanLength() < 10:
            return
        
        # Start drag
        from PyQt6.QtCore import QMimeData
        from PyQt6.QtGui import QDrag
        
        drag = QDrag(self)
        mime_data = QMimeData()
        mime_data.setText(str(self.page_num))
        drag.setMimeData(mime_data)
        
        # Create drag pixmap
        drag_pixmap = self.pixmap.scaled(80, 100, Qt.AspectRatioMode.KeepAspectRatio)
        drag.setPixmap(drag_pixmap)
        drag.setHotSpot(drag_pixmap.rect().center())
        
        self.drag_started.emit(self.page_num)
        drag.exec(Qt.DropAction.MoveAction)
        self.drag_start_pos = None
    
    def mouseReleaseEvent(self, event: QMouseEvent):
        """Handle mouse release."""
        self.drag_start_pos = None
        super().mouseReleaseEvent(event)


# ============================================================================
# PDF GRID VIEW
# ============================================================================

class PDFGridView(QScrollArea):
    """Grid view showing all PDF pages as thumbnails with drag-drop reordering."""
    
    # Constants for responsive grid
    MAX_COLUMNS = 6
    MIN_THUMB_WIDTH = 150
    THUMB_ASPECT_RATIO = 1.4  # height = width * aspect_ratio
    GRID_MARGIN = 24
    GRID_SPACING = 16
    
    page_selected = pyqtSignal(int)
    selection_changed = pyqtSignal(list)
    go_to_page = pyqtSignal(int)
    pages_reordered = pyqtSignal(int, int)  # source_page, target_page
    pdf_modified = pyqtSignal()  # Emitted when PDF is modified
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.pdf_doc: Optional[fitz.Document] = None
        self.thumbnails: List[PageThumbnail] = []
        self.selected_pages: set = set()
        self.current_theme = "dark"
        self.drag_source_page = -1
        self.current_thumb_size = (180, 260)  # Default size
        
        self.setAcceptDrops(True)
        self.setup_ui()
    
    def setup_ui(self):
        """Set up the grid view UI."""
        self.setWidgetResizable(True)
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        
        # Container widget
        self.container = QWidget()
        self.grid_layout = QGridLayout(self.container)
        self.grid_layout.setSpacing(self.GRID_SPACING)
        self.grid_layout.setContentsMargins(self.GRID_MARGIN, self.GRID_MARGIN, 
                                            self.GRID_MARGIN, self.GRID_MARGIN)
        
        self.setWidget(self.container)
        
        self.apply_theme_style()
    
    def calculate_layout(self) -> tuple:
        """Calculate optimal columns and thumbnail size based on available width."""
        # Get available width (account for scrollbar)
        available_width = self.width() - self.GRID_MARGIN * 2 - 20  # 20 for scrollbar
        
        if available_width <= 0:
            return 4, 180, 260
        
        # Try each column count from MAX to 1 and find the best fit
        for cols in range(self.MAX_COLUMNS, 0, -1):
            # Calculate thumbnail width for this column count
            total_spacing = (cols - 1) * self.GRID_SPACING
            thumb_width = (available_width - total_spacing) // cols
            
            # If thumbnail would be too small, try fewer columns
            if thumb_width >= self.MIN_THUMB_WIDTH or cols == 1:
                thumb_height = int(thumb_width * self.THUMB_ASPECT_RATIO)
                return cols, thumb_width, thumb_height
        
        # Fallback
        return 1, available_width, int(available_width * self.THUMB_ASPECT_RATIO)
    
    def apply_theme_style(self):
        """Apply the current theme style."""
        if self.current_theme == "dark":
            self.setStyleSheet("""
                QScrollArea {
                    background-color: #0d1117;
                    border: none;
                }
                QWidget {
                    background-color: #0d1117;
                }
            """)
        else:
            self.setStyleSheet("""
                QScrollArea {
                    background-color: #f6f8fa;
                    border: none;
                }
                QWidget {
                    background-color: #f6f8fa;
                }
            """)
    
    def set_theme(self, theme: str):
        """Set the theme for the grid view and all thumbnails."""
        self.current_theme = theme
        self.apply_theme_style()
        
        # Update all thumbnails
        for thumbnail in self.thumbnails:
            thumbnail.set_theme(theme)
    
    def load_pdf(self, pdf_doc: fitz.Document):
        """Load thumbnails from a PDF document."""
        self.pdf_doc = pdf_doc
        self.clear_thumbnails()
        self.selected_pages.clear()
        
        if not pdf_doc:
            return
        
        # Calculate responsive layout
        cols, thumb_width, thumb_height = self.calculate_layout()
        self.current_thumb_size = (thumb_width, thumb_height)
        
        for i in range(len(pdf_doc)):
            page = pdf_doc[i]
            
            # Create thumbnail at higher resolution for quality when scaling
            mat = fitz.Matrix(0.5, 0.5)
            pix = page.get_pixmap(matrix=mat, alpha=False)
            
            img = QImage(pix.samples, pix.width, pix.height, pix.stride, QImage.Format.Format_RGB888)
            pixmap = QPixmap.fromImage(img)
            
            # Scale to fit thumbnail size
            img_width = thumb_width - 20
            img_height = thumb_height - 60
            scaled_pixmap = pixmap.scaled(
                img_width, img_height,
                Qt.AspectRatioMode.KeepAspectRatio,
                Qt.TransformationMode.SmoothTransformation
            )
            
            thumbnail = PageThumbnail(i, scaled_pixmap, self.current_theme)
            thumbnail.update_size(thumb_width, thumb_height)
            thumbnail.original_pixmap = pixmap  # Store full-res for rescaling
            thumbnail.clicked.connect(self.on_thumbnail_clicked)
            thumbnail.selection_changed.connect(self.on_selection_changed)
            thumbnail.double_clicked.connect(self.on_thumbnail_double_clicked)
            thumbnail.drag_started.connect(self.on_drag_started)
            
            row = i // cols
            col = i % cols
            self.grid_layout.addWidget(thumbnail, row, col)
            self.thumbnails.append(thumbnail)
    
    def clear_thumbnails(self):
        """Remove all thumbnails."""
        for thumb in self.thumbnails:
            thumb.deleteLater()
        self.thumbnails.clear()
        
        # Clear layout
        while self.grid_layout.count():
            item = self.grid_layout.takeAt(0)
            if item.widget():
                item.widget().deleteLater()
    
    def on_thumbnail_clicked(self, page_num: int):
        """Handle thumbnail click."""
        self.page_selected.emit(page_num)
    
    def on_selection_changed(self, page_num: int, selected: bool):
        """Handle selection change."""
        if selected:
            self.selected_pages.add(page_num)
        else:
            self.selected_pages.discard(page_num)
        
        self.selection_changed.emit(sorted(self.selected_pages))
    
    def on_thumbnail_double_clicked(self, page_num: int):
        """Handle double click to navigate to page."""
        self.go_to_page.emit(page_num)
    
    def get_selected_pages(self) -> List[int]:
        """Get list of selected page numbers."""
        return sorted(self.selected_pages)
    
    def select_all(self):
        """Select all pages."""
        for thumb in self.thumbnails:
            thumb.set_selected(True)
            self.selected_pages.add(thumb.page_num)
        self.selection_changed.emit(sorted(self.selected_pages))
    
    def deselect_all(self):
        """Deselect all pages."""
        for thumb in self.thumbnails:
            thumb.set_selected(False)
        self.selected_pages.clear()
        self.selection_changed.emit([])
    
    def select_range(self, start: int, end: int):
        """Select a range of pages."""
        for thumb in self.thumbnails:
            if start <= thumb.page_num <= end:
                thumb.set_selected(True)
                self.selected_pages.add(thumb.page_num)
        self.selection_changed.emit(sorted(self.selected_pages))
    
    def resizeEvent(self, event):
        """Handle resize to adjust grid columns and thumbnail sizes."""
        super().resizeEvent(event)
        if self.pdf_doc and self.thumbnails:
            # Recalculate responsive layout
            cols, thumb_width, thumb_height = self.calculate_layout()
            
            # Only resize if size changed significantly (avoid excessive redraws)
            if abs(thumb_width - self.current_thumb_size[0]) > 10:
                self.current_thumb_size = (thumb_width, thumb_height)
                
                # Update all thumbnail sizes
                for thumb in self.thumbnails:
                    thumb.update_size(thumb_width, thumb_height)
            
            # Rearrange thumbnails in grid
            for i, thumb in enumerate(self.thumbnails):
                row = i // cols
                col = i % cols
                self.grid_layout.addWidget(thumb, row, col)
    
    def on_drag_started(self, page_num: int):
        """Track which page started the drag."""
        self.drag_source_page = page_num
    
    def dragEnterEvent(self, event):
        """Accept drag events from page thumbnails."""
        if event.mimeData().hasText():
            event.acceptProposedAction()
    
    def dragMoveEvent(self, event):
        """Handle drag move to show drop indicator."""
        if event.mimeData().hasText():
            event.acceptProposedAction()
    
    def dropEvent(self, event):
        """Handle drop to reorder pages."""
        if not event.mimeData().hasText():
            return
        
        source_page = int(event.mimeData().text())
        
        # Find target position based on drop location
        drop_pos = event.position().toPoint()
        widget_pos = self.widget().mapFrom(self, drop_pos)
        
        target_page = self.get_page_at_position(widget_pos)
        
        if target_page >= 0 and target_page != source_page:
            self.pages_reordered.emit(source_page, target_page)
        
        event.acceptProposedAction()
        self.drag_source_page = -1
    
    def get_page_at_position(self, pos) -> int:
        """Get page number at given position."""
        for thumb in self.thumbnails:
            if thumb.geometry().contains(pos):
                return thumb.page_num
        
        # If not over a thumbnail, find nearest
        if self.thumbnails:
            # Check if beyond last thumbnail
            last_thumb = self.thumbnails[-1]
            if pos.y() > last_thumb.geometry().bottom():
                return len(self.thumbnails) - 1
        
        return -1
    
    def refresh_thumbnails(self):
        """Refresh all thumbnails after page order change."""
        if not self.pdf_doc:
            return
        
        # Store current selection
        old_selection = self.selected_pages.copy()
        
        # Clear and reload
        self.clear_thumbnails()
        self.selected_pages.clear()
        
        # Calculate responsive layout
        cols, thumb_width, thumb_height = self.calculate_layout()
        self.current_thumb_size = (thumb_width, thumb_height)
        
        for i in range(len(self.pdf_doc)):
            page = self.pdf_doc[i]
            
            # Higher resolution for quality when scaling
            mat = fitz.Matrix(0.5, 0.5)
            pix = page.get_pixmap(matrix=mat, alpha=False)
            
            img = QImage(pix.samples, pix.width, pix.height, pix.stride, QImage.Format.Format_RGB888)
            pixmap = QPixmap.fromImage(img)
            
            img_width = thumb_width - 20
            img_height = thumb_height - 60
            scaled_pixmap = pixmap.scaled(
                img_width, img_height,
                Qt.AspectRatioMode.KeepAspectRatio,
                Qt.TransformationMode.SmoothTransformation
            )
            
            thumbnail = PageThumbnail(i, scaled_pixmap, self.current_theme)
            thumbnail.update_size(thumb_width, thumb_height)
            thumbnail.original_pixmap = pixmap  # Store full-res for rescaling
            thumbnail.clicked.connect(self.on_thumbnail_clicked)
            thumbnail.selection_changed.connect(self.on_selection_changed)
            thumbnail.double_clicked.connect(self.on_thumbnail_double_clicked)
            thumbnail.drag_started.connect(self.on_drag_started)
            
            row = i // cols
            col = i % cols
            self.grid_layout.addWidget(thumbnail, row, col)
            self.thumbnails.append(thumbnail)
        
        self.selection_changed.emit([])


# ============================================================================
# SPLIT PDF DIALOG
# ============================================================================

class SplitPDFDialog(QDialog):
    """Dialog for splitting selected pages into a new PDF."""
    
    def __init__(self, selected_pages: List[int], total_pages: int, parent=None):
        super().__init__(parent)
        self.selected_pages = selected_pages
        self.total_pages = total_pages
        
        self.setWindowTitle("Split PDF")
        self.setMinimumWidth(400)
        self.setup_ui()
    
    def setup_ui(self):
        """Set up the dialog UI."""
        layout = QVBoxLayout(self)
        layout.setSpacing(16)
        layout.setContentsMargins(24, 24, 24, 24)
        
        # Title
        title = QLabel("Extract Pages to New PDF")
        title.setStyleSheet("font-size: 18px; font-weight: 600; color: #c9d1d9;")
        layout.addWidget(title)
        
        # Selection info
        if self.selected_pages:
            pages_str = self.format_page_ranges(self.selected_pages)
            info_text = f"Selected pages: {pages_str}"
            count_text = f"({len(self.selected_pages)} of {self.total_pages} pages)"
        else:
            info_text = "No pages selected"
            count_text = "Use the grid view to select pages"
        
        info_label = QLabel(info_text)
        info_label.setStyleSheet("color: #c9d1d9; font-size: 14px;")
        info_label.setWordWrap(True)
        layout.addWidget(info_label)
        
        count_label = QLabel(count_text)
        count_label.setStyleSheet("color: #8b949e; font-size: 13px;")
        layout.addWidget(count_label)
        
        # Manual page range input
        layout.addSpacing(8)
        range_label = QLabel("Or enter page range manually:")
        range_label.setStyleSheet("color: #8b949e; font-size: 13px;")
        layout.addWidget(range_label)
        
        self.range_input = QLineEdit()
        self.range_input.setPlaceholderText("e.g., 1-5, 8, 10-12")
        self.range_input.setStyleSheet("""
            QLineEdit {
                background-color: #21262d;
                border: 1px solid #30363d;
                border-radius: 6px;
                padding: 10px;
                color: #c9d1d9;
                font-size: 14px;
            }
            QLineEdit:focus {
                border-color: #388bfd;
            }
        """)
        if self.selected_pages:
            self.range_input.setText(self.format_page_ranges(self.selected_pages))
        layout.addWidget(self.range_input)
        
        # Buttons
        layout.addSpacing(16)
        button_layout = QHBoxLayout()
        
        cancel_btn = QPushButton("Cancel")
        cancel_btn.setObjectName("secondaryBtn")
        cancel_btn.clicked.connect(self.reject)
        button_layout.addWidget(cancel_btn)
        
        button_layout.addStretch()
        
        self.save_btn = QPushButton("Save as New PDF")
        self.save_btn.setEnabled(bool(self.selected_pages) or bool(self.range_input.text()))
        self.save_btn.clicked.connect(self.accept)
        button_layout.addWidget(self.save_btn)
        
        layout.addLayout(button_layout)
        
        # Connect input to enable/disable save button
        self.range_input.textChanged.connect(self.on_range_changed)
    
    def format_page_ranges(self, pages: List[int]) -> str:
        """Format page numbers as ranges (e.g., 1-3, 5, 7-9)."""
        if not pages:
            return ""
        
        # Convert to 1-based page numbers
        pages = [p + 1 for p in sorted(pages)]
        ranges = []
        start = pages[0]
        end = pages[0]
        
        for p in pages[1:]:
            if p == end + 1:
                end = p
            else:
                if start == end:
                    ranges.append(str(start))
                else:
                    ranges.append(f"{start}-{end}")
                start = end = p
        
        if start == end:
            ranges.append(str(start))
        else:
            ranges.append(f"{start}-{end}")
        
        return ", ".join(ranges)
    
    def parse_page_ranges(self, text: str) -> List[int]:
        """Parse page range string into list of page numbers (0-based)."""
        pages = set()
        
        for part in text.split(","):
            part = part.strip()
            if not part:
                continue
            
            if "-" in part:
                try:
                    start, end = part.split("-", 1)
                    start = int(start.strip()) - 1  # Convert to 0-based
                    end = int(end.strip()) - 1
                    if 0 <= start <= end < self.total_pages:
                        pages.update(range(start, end + 1))
                except ValueError:
                    continue
            else:
                try:
                    page = int(part) - 1  # Convert to 0-based
                    if 0 <= page < self.total_pages:
                        pages.add(page)
                except ValueError:
                    continue
        
        return sorted(pages)
    
    def on_range_changed(self, text: str):
        """Handle range input change."""
        pages = self.parse_page_ranges(text)
        self.save_btn.setEnabled(bool(pages))
    
    def get_pages_to_extract(self) -> List[int]:
        """Get the final list of pages to extract."""
        text = self.range_input.text().strip()
        if text:
            return self.parse_page_ranges(text)
        return sorted(self.selected_pages)


# ============================================================================
# INSERT PAGES DIALOG
# ============================================================================

class InsertPageThumbnail(QFrame):
    """Small thumbnail for insert dialog with selection support."""
    
    clicked = pyqtSignal(int)
    
    def __init__(self, page_num: int, pixmap: QPixmap, parent=None):
        super().__init__(parent)
        self.page_num = page_num
        self.selected = False
        self.setup_ui(pixmap)
        self.update_style()
    
    def setup_ui(self, pixmap: QPixmap):
        """Set up the thumbnail UI."""
        layout = QVBoxLayout(self)
        layout.setContentsMargins(4, 4, 4, 4)
        layout.setSpacing(2)
        
        # Thumbnail image
        self.image_label = QLabel()
        scaled = pixmap.scaled(80, 110, Qt.AspectRatioMode.KeepAspectRatio, 
                               Qt.TransformationMode.SmoothTransformation)
        self.image_label.setPixmap(scaled)
        self.image_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.image_label)
        
        # Page number
        self.page_label = QLabel(f"{self.page_num + 1}")
        self.page_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.page_label.setStyleSheet("font-size: 11px; color: #8b949e;")
        layout.addWidget(self.page_label)
        
        self.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.setFixedSize(90, 140)
    
    def update_style(self):
        """Update visual style based on selection."""
        if self.selected:
            self.setStyleSheet("""
                InsertPageThumbnail {
                    background-color: #238636;
                    border: 2px solid #2ea043;
                    border-radius: 8px;
                }
            """)
            self.page_label.setStyleSheet("font-size: 11px; color: #ffffff; font-weight: 600;")
        else:
            self.setStyleSheet("""
                InsertPageThumbnail {
                    background-color: #21262d;
                    border: 2px solid #30363d;
                    border-radius: 8px;
                }
                InsertPageThumbnail:hover {
                    background-color: #30363d;
                    border-color: #8b949e;
                }
            """)
            self.page_label.setStyleSheet("font-size: 11px; color: #8b949e;")
    
    def set_selected(self, selected: bool):
        """Set selection state."""
        self.selected = selected
        self.update_style()
    
    def mousePressEvent(self, event):
        """Handle click."""
        if event.button() == Qt.MouseButton.LeftButton:
            self.clicked.emit(self.page_num)
        super().mousePressEvent(event)


class InsertPagesDialog(QDialog):
    """Dialog for inserting pages from another PDF with thumbnail preview."""
    
    def __init__(self, src_doc: fitz.Document, target_page_count: int, parent=None):
        super().__init__(parent)
        self.src_doc = src_doc
        self.source_page_count = len(src_doc)
        self.target_page_count = target_page_count
        self.selected_pages: set = set()
        self.thumbnails: List[InsertPageThumbnail] = []
        
        self.setWindowTitle("Insert PDF Pages")
        self.setMinimumSize(600, 500)
        self.setup_ui()
    
    def setup_ui(self):
        """Set up the dialog UI."""
        layout = QVBoxLayout(self)
        layout.setSpacing(12)
        layout.setContentsMargins(20, 20, 20, 20)
        
        # Title
        title = QLabel("Insert Pages from PDF")
        title.setStyleSheet("font-size: 18px; font-weight: 600; color: #c9d1d9;")
        layout.addWidget(title)
        
        # Source info
        info_label = QLabel(f"Source PDF has {self.source_page_count} page{'s' if self.source_page_count != 1 else ''} • Click thumbnails to select pages")
        info_label.setStyleSheet("color: #8b949e; font-size: 13px;")
        layout.addWidget(info_label)
        
        # Selection mode buttons
        mode_layout = QHBoxLayout()
        
        self.all_pages_btn = QPushButton("📄 All Pages")
        self.all_pages_btn.setCheckable(True)
        self.all_pages_btn.setChecked(True)
        self.all_pages_btn.setStyleSheet("""
            QPushButton {
                background-color: #238636;
                border-radius: 6px;
                padding: 8px 16px;
                font-weight: 500;
            }
            QPushButton:!checked {
                background-color: #21262d;
            }
            QPushButton:!checked:hover {
                background-color: #30363d;
            }
        """)
        self.all_pages_btn.clicked.connect(self.on_all_pages_clicked)
        mode_layout.addWidget(self.all_pages_btn)
        
        self.select_pages_btn = QPushButton("🖱️ Select Pages")
        self.select_pages_btn.setCheckable(True)
        self.select_pages_btn.setStyleSheet("""
            QPushButton {
                background-color: #238636;
                border-radius: 6px;
                padding: 8px 16px;
                font-weight: 500;
            }
            QPushButton:!checked {
                background-color: #21262d;
            }
            QPushButton:!checked:hover {
                background-color: #30363d;
            }
        """)
        self.select_pages_btn.clicked.connect(self.on_select_pages_clicked)
        mode_layout.addWidget(self.select_pages_btn)
        
        mode_layout.addStretch()
        
        # Selection info label
        self.selection_info = QLabel("")
        self.selection_info.setStyleSheet("color: #58a6ff; font-size: 12px;")
        mode_layout.addWidget(self.selection_info)
        
        layout.addLayout(mode_layout)
        
        # Thumbnail grid in scroll area
        self.scroll_area = QScrollArea()
        self.scroll_area.setWidgetResizable(True)
        self.scroll_area.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.scroll_area.setStyleSheet("""
            QScrollArea {
                background-color: #0d1117;
                border: 1px solid #30363d;
                border-radius: 8px;
            }
        """)
        
        self.thumb_container = QWidget()
        self.thumb_layout = QGridLayout(self.thumb_container)
        self.thumb_layout.setSpacing(8)
        self.thumb_layout.setContentsMargins(12, 12, 12, 12)
        
        self.scroll_area.setWidget(self.thumb_container)
        layout.addWidget(self.scroll_area, 1)  # Give it stretch factor
        
        # Load thumbnails
        self.load_thumbnails()
        
        # Insert position
        pos_frame = QFrame()
        pos_frame.setStyleSheet("background-color: #161b22; border-radius: 8px; padding: 8px;")
        pos_layout = QHBoxLayout(pos_frame)
        pos_layout.setContentsMargins(12, 8, 12, 8)
        
        pos_label = QLabel("Insert after page:")
        pos_label.setStyleSheet("color: #c9d1d9; font-size: 14px;")
        pos_layout.addWidget(pos_label)
        
        self.insert_pos_spin = QSpinBox()
        self.insert_pos_spin.setRange(0, self.target_page_count)
        self.insert_pos_spin.setValue(self.target_page_count)  # Default to end
        self.insert_pos_spin.setSpecialValueText("Beginning")
        self.insert_pos_spin.setFixedWidth(80)
        pos_layout.addWidget(self.insert_pos_spin)
        
        pos_info = QLabel(f"(0 = beginning, {self.target_page_count} = end)")
        pos_info.setStyleSheet("color: #8b949e; font-size: 12px;")
        pos_layout.addWidget(pos_info)
        
        pos_layout.addStretch()
        layout.addWidget(pos_frame)
        
        # Buttons
        button_layout = QHBoxLayout()
        
        cancel_btn = QPushButton("Cancel")
        cancel_btn.setObjectName("secondaryBtn")
        cancel_btn.clicked.connect(self.reject)
        button_layout.addWidget(cancel_btn)
        
        button_layout.addStretch()
        
        self.insert_btn = QPushButton("Insert All Pages")
        self.insert_btn.clicked.connect(self.accept)
        button_layout.addWidget(self.insert_btn)
        
        layout.addLayout(button_layout)
    
    def load_thumbnails(self):
        """Load thumbnails from source PDF."""
        cols = 6  # Number of columns in grid
        
        for i in range(self.source_page_count):
            page = self.src_doc[i]
            
            # Create thumbnail
            mat = fitz.Matrix(0.3, 0.3)  # Small scale for thumbnails
            pix = page.get_pixmap(matrix=mat, alpha=False)
            
            img = QImage(pix.samples, pix.width, pix.height, pix.stride, QImage.Format.Format_RGB888)
            pixmap = QPixmap.fromImage(img)
            
            thumbnail = InsertPageThumbnail(i, pixmap, self)
            thumbnail.clicked.connect(self.on_thumbnail_clicked)
            
            row = i // cols
            col = i % cols
            self.thumb_layout.addWidget(thumbnail, row, col)
            self.thumbnails.append(thumbnail)
    
    def on_thumbnail_clicked(self, page_num: int):
        """Handle thumbnail click."""
        # Switch to select mode if not already
        if self.all_pages_btn.isChecked():
            self.on_select_pages_clicked()
        
        # Toggle selection
        thumb = self.thumbnails[page_num]
        if page_num in self.selected_pages:
            self.selected_pages.remove(page_num)
            thumb.set_selected(False)
        else:
            self.selected_pages.add(page_num)
            thumb.set_selected(True)
        
        self.update_selection_info()
    
    def on_all_pages_clicked(self):
        """Handle all pages mode."""
        self.all_pages_btn.setChecked(True)
        self.select_pages_btn.setChecked(False)
        
        # Clear visual selection
        for thumb in self.thumbnails:
            thumb.set_selected(False)
        self.selected_pages.clear()
        
        self.selection_info.setText("")
        self.insert_btn.setText("Insert All Pages")
    
    def on_select_pages_clicked(self):
        """Handle select pages mode."""
        self.all_pages_btn.setChecked(False)
        self.select_pages_btn.setChecked(True)
        self.update_selection_info()
    
    def update_selection_info(self):
        """Update the selection info label."""
        count = len(self.selected_pages)
        if count == 0:
            self.selection_info.setText("No pages selected")
            self.insert_btn.setText("Insert Pages")
            self.insert_btn.setEnabled(False)
        else:
            self.selection_info.setText(f"{count} page{'s' if count != 1 else ''} selected")
            self.insert_btn.setText(f"Insert {count} Page{'s' if count != 1 else ''}")
            self.insert_btn.setEnabled(True)
    
    def get_insert_position(self) -> int:
        """Get the insert position (0-based page index)."""
        return self.insert_pos_spin.value()
    
    def get_selected_pages(self) -> List[int]:
        """Get list of selected page indices (0-based), sorted."""
        if self.all_pages_btn.isChecked():
            return list(range(self.source_page_count))
        return sorted(self.selected_pages)


# ============================================================================
# PDF TAB WIDGET
# ============================================================================

class PDFTab(QWidget):
    """Widget for a single PDF tab with viewer and controls."""
    
    def __init__(self, file_path: str, parent=None):
        super().__init__(parent)
        self.file_path = file_path
        self.file_name = Path(file_path).name
        self.modified = False
        self.current_view = "single"  # "single" or "grid"
        self.selected_pages: List[int] = []
        self.current_theme = "dark"  # Track current theme for delayed loading
        
        self.setup_ui()
        self.load_pdf()
    
    def setup_ui(self):
        """Set up the tab UI."""
        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)
        
        # Page navigation bar
        self.nav_bar = QFrame()
        self.nav_bar.setStyleSheet("""
            QFrame {
                background-color: #21262d;
                border-bottom: 1px solid #30363d;
                padding: 8px;
            }
        """)
        nav_layout = QHBoxLayout(self.nav_bar)
        nav_layout.setContentsMargins(12, 8, 12, 8)
        
        # View mode toggle buttons
        self.single_view_btn = QPushButton("📄 Single")
        self.single_view_btn.setFixedHeight(36)
        self.single_view_btn.setCheckable(True)
        self.single_view_btn.setChecked(True)
        self.single_view_btn.setStyleSheet("""
            QPushButton {
                background-color: #388bfd;
                border-radius: 6px;
                padding: 0 16px;
                font-weight: 600;
            }
            QPushButton:checked {
                background-color: #388bfd;
            }
            QPushButton:!checked {
                background-color: #30363d;
            }
            QPushButton:!checked:hover {
                background-color: #484f58;
            }
        """)
        self.single_view_btn.clicked.connect(lambda: self.set_view_mode("single"))
        nav_layout.addWidget(self.single_view_btn)
        
        self.grid_view_btn = QPushButton("⊞ Grid")
        self.grid_view_btn.setFixedHeight(36)
        self.grid_view_btn.setCheckable(True)
        self.grid_view_btn.setStyleSheet("""
            QPushButton {
                background-color: #30363d;
                border-radius: 6px;
                padding: 0 16px;
                font-weight: 600;
            }
            QPushButton:checked {
                background-color: #388bfd;
            }
            QPushButton:!checked {
                background-color: #30363d;
            }
            QPushButton:!checked:hover {
                background-color: #484f58;
            }
        """)
        self.grid_view_btn.clicked.connect(lambda: self.set_view_mode("grid"))
        nav_layout.addWidget(self.grid_view_btn)
        
        # Separator
        self.sep1 = QFrame()
        self.sep1.setFrameShape(QFrame.Shape.VLine)
        self.sep1.setStyleSheet("background-color: #30363d; max-width: 1px; margin: 0 8px;")
        nav_layout.addWidget(self.sep1)
        
        # Previous page button
        self.prev_btn = QPushButton("◀")
        self.prev_btn.setFixedSize(36, 36)
        self.prev_btn.setStyleSheet("""
            QPushButton {
                background-color: #30363d;
                border-radius: 6px;
                font-size: 14px;
            }
            QPushButton:hover { background-color: #484f58; }
        """)
        self.prev_btn.clicked.connect(self.prev_page)
        nav_layout.addWidget(self.prev_btn)
        
        # Page indicator
        self.page_spin = QSpinBox()
        self.page_spin.setMinimum(1)
        self.page_spin.setFixedWidth(70)
        self.page_spin.valueChanged.connect(self.on_page_spin_changed)
        nav_layout.addWidget(self.page_spin)
        
        self.page_label = QLabel("/ 0")
        self.page_label.setStyleSheet("color: #8b949e; padding: 0 8px;")
        nav_layout.addWidget(self.page_label)
        
        # Next page button
        self.next_btn = QPushButton("▶")
        self.next_btn.setFixedSize(36, 36)
        self.next_btn.setStyleSheet("""
            QPushButton {
                background-color: #30363d;
                border-radius: 6px;
                font-size: 14px;
            }
            QPushButton:hover { background-color: #484f58; }
        """)
        self.next_btn.clicked.connect(self.next_page)
        nav_layout.addWidget(self.next_btn)
        
        nav_layout.addStretch()
        
        # Selection info label (for grid view)
        self.selection_label = QLabel("")
        self.selection_label.setStyleSheet("color: #58a6ff; font-weight: 500; padding: 0 12px;")
        self.selection_label.hide()
        nav_layout.addWidget(self.selection_label)
        
        # Split PDF button
        self.split_btn = QPushButton("✂ Split PDF")
        self.split_btn.setFixedHeight(36)
        self.split_btn.setStyleSheet("""
            QPushButton {
                background-color: #8957e5;
                border-radius: 6px;
                padding: 0 16px;
                font-weight: 600;
            }
            QPushButton:hover {
                background-color: #a371f7;
            }
            QPushButton:disabled {
                background-color: #30363d;
                color: #484f58;
            }
        """)
        self.split_btn.clicked.connect(self.show_split_dialog)
        nav_layout.addWidget(self.split_btn)
        
        # Separator
        self.sep2 = QFrame()
        self.sep2.setFrameShape(QFrame.Shape.VLine)
        self.sep2.setStyleSheet("background-color: #30363d; max-width: 1px; margin: 0 8px;")
        nav_layout.addWidget(self.sep2)
        
        # Zoom controls
        self.zoom_out_btn = QPushButton("−")
        self.zoom_out_btn.setFixedSize(36, 36)
        self.zoom_out_btn.setStyleSheet("""
            QPushButton {
                background-color: #30363d;
                border-radius: 6px;
                font-size: 18px;
                font-weight: bold;
            }
            QPushButton:hover { background-color: #484f58; }
        """)
        self.zoom_out_btn.clicked.connect(self.zoom_out)
        nav_layout.addWidget(self.zoom_out_btn)
        
        self.zoom_slider = QSlider(Qt.Orientation.Horizontal)
        self.zoom_slider.setRange(25, 400)
        self.zoom_slider.setValue(100)
        self.zoom_slider.setFixedWidth(150)
        self.zoom_slider.valueChanged.connect(self.on_zoom_slider_changed)
        nav_layout.addWidget(self.zoom_slider)
        
        self.zoom_in_btn = QPushButton("+")
        self.zoom_in_btn.setFixedSize(36, 36)
        self.zoom_in_btn.setStyleSheet("""
            QPushButton {
                background-color: #30363d;
                border-radius: 6px;
                font-size: 18px;
                font-weight: bold;
            }
            QPushButton:hover { background-color: #484f58; }
        """)
        self.zoom_in_btn.clicked.connect(self.zoom_in)
        nav_layout.addWidget(self.zoom_in_btn)
        
        self.zoom_label = QLabel("100%")
        self.zoom_label.setFixedWidth(50)
        self.zoom_label.setStyleSheet("color: #8b949e; padding-left: 8px;")
        nav_layout.addWidget(self.zoom_label)
        
        # Fit buttons
        self.fit_width_btn = QPushButton("Fit Width")
        self.fit_width_btn.setProperty("class", "secondaryBtn")
        self.fit_width_btn.setObjectName("secondaryBtn")
        self.fit_width_btn.clicked.connect(self.fit_width)
        nav_layout.addWidget(self.fit_width_btn)
        
        self.fit_page_btn = QPushButton("Fit Page")
        self.fit_page_btn.setProperty("class", "secondaryBtn")
        self.fit_page_btn.setObjectName("secondaryBtn")
        self.fit_page_btn.clicked.connect(self.fit_page)
        nav_layout.addWidget(self.fit_page_btn)
        
        layout.addWidget(self.nav_bar)
        
        # Grid view controls bar (shown only in grid view)
        self.grid_controls = QFrame()
        self.grid_controls.setStyleSheet("""
            QFrame {
                background-color: #161b22;
                border-bottom: 1px solid #30363d;
                padding: 6px;
            }
        """)
        grid_controls_layout = QHBoxLayout(self.grid_controls)
        grid_controls_layout.setContentsMargins(12, 6, 12, 6)
        
        select_all_btn = QPushButton("Select All")
        select_all_btn.setObjectName("secondaryBtn")
        select_all_btn.clicked.connect(self.select_all_pages)
        grid_controls_layout.addWidget(select_all_btn)
        
        deselect_all_btn = QPushButton("Deselect All")
        deselect_all_btn.setObjectName("secondaryBtn")
        deselect_all_btn.clicked.connect(self.deselect_all_pages)
        grid_controls_layout.addWidget(deselect_all_btn)
        
        # Separator
        sep = QFrame()
        sep.setFrameShape(QFrame.Shape.VLine)
        sep.setStyleSheet("background-color: #30363d; max-width: 1px; margin: 0 8px;")
        grid_controls_layout.addWidget(sep)
        
        # Delete button
        self.delete_pages_btn = QPushButton("🗑️ Delete")
        self.delete_pages_btn.setObjectName("dangerBtn")
        self.delete_pages_btn.setStyleSheet("""
            QPushButton {
                background-color: #da3633;
                color: white;
                border-radius: 6px;
                padding: 6px 12px;
                font-weight: 600;
            }
            QPushButton:hover { background-color: #f85149; }
            QPushButton:disabled { background-color: #484f58; color: #8b949e; }
        """)
        self.delete_pages_btn.clicked.connect(self.delete_selected_pages)
        self.delete_pages_btn.setEnabled(False)
        grid_controls_layout.addWidget(self.delete_pages_btn)
        
        # Insert PDF button
        insert_pdf_btn = QPushButton("📄 Insert PDF")
        insert_pdf_btn.setObjectName("secondaryBtn")
        insert_pdf_btn.clicked.connect(self.insert_pdf_pages)
        grid_controls_layout.addWidget(insert_pdf_btn)
        
        # Insert image button
        insert_image_btn = QPushButton("🖼️ Insert Image")
        insert_image_btn.setObjectName("secondaryBtn")
        insert_image_btn.clicked.connect(self.insert_image_as_page)
        grid_controls_layout.addWidget(insert_image_btn)
        
        grid_controls_layout.addStretch()
        
        self.grid_selection_info = QLabel("Drag pages to reorder • Select pages for editing")
        self.grid_selection_info.setStyleSheet("color: #8b949e; font-size: 13px;")
        grid_controls_layout.addWidget(self.grid_selection_info)
        
        self.grid_controls.hide()
        layout.addWidget(self.grid_controls)
        
        # Stacked widget for single/grid views
        self.view_stack = QStackedWidget()
        
        # Single page view
        self.pdf_view = PDFPageView()
        self.pdf_view.page_changed.connect(self.on_page_changed)
        self.view_stack.addWidget(self.pdf_view)
        
        # Grid view
        self.grid_view = PDFGridView()
        self.grid_view.selection_changed.connect(self.on_grid_selection_changed)
        self.grid_view.go_to_page.connect(self.go_to_page_from_grid)
        self.grid_view.pages_reordered.connect(self.on_pages_reordered)
        self.view_stack.addWidget(self.grid_view)
        
        layout.addWidget(self.view_stack)
    
    def load_pdf(self):
        """Load the PDF file."""
        if self.pdf_view.load_pdf(self.file_path):
            page_count = self.pdf_view.get_page_count()
            self.page_spin.setMaximum(page_count)
            self.page_label.setText(f"/ {page_count}")
            self.page_spin.setValue(1)
            
            # Fit to width initially
            QTimer.singleShot(100, self.fit_width)
            
            # Load grid view (delayed for performance)
            QTimer.singleShot(200, self.load_grid_view)
    
    def load_grid_view(self):
        """Load the grid view with thumbnails."""
        if self.pdf_view.pdf_doc:
            # Set theme before loading so thumbnails get correct theme
            self.grid_view.current_theme = self.current_theme
            self.grid_view.apply_theme_style()
            self.grid_view.load_pdf(self.pdf_view.pdf_doc)
    
    def set_view_mode(self, mode: str):
        """Switch between single and grid view."""
        self.current_view = mode
        
        if mode == "single":
            self.view_stack.setCurrentIndex(0)
            self.single_view_btn.setChecked(True)
            self.grid_view_btn.setChecked(False)
            self.grid_controls.hide()
            self.selection_label.hide()
            # Show single-page navigation and zoom controls
            self.prev_btn.show()
            self.next_btn.show()
            self.page_spin.show()
            self.page_label.show()
            self.zoom_out_btn.show()
            self.zoom_slider.show()
            self.zoom_in_btn.show()
            self.zoom_label.show()
            self.fit_width_btn.show()
            self.fit_page_btn.show()
        else:
            self.view_stack.setCurrentIndex(1)
            self.single_view_btn.setChecked(False)
            self.grid_view_btn.setChecked(True)
            self.grid_controls.show()
            self.update_selection_label()
            # Hide single-page navigation and zoom controls in grid view
            self.prev_btn.hide()
            self.next_btn.hide()
            self.page_spin.hide()
            self.page_label.hide()
            self.zoom_out_btn.hide()
            self.zoom_slider.hide()
            self.zoom_in_btn.hide()
            self.zoom_label.hide()
            self.fit_width_btn.hide()
            self.fit_page_btn.hide()
    
    def on_grid_selection_changed(self, pages: List[int]):
        """Handle grid selection change."""
        self.selected_pages = pages
        self.update_selection_label()
        # Enable/disable delete button based on selection
        self.delete_pages_btn.setEnabled(len(pages) > 0)
    
    def update_selection_label(self):
        """Update the selection info label."""
        count = len(self.selected_pages)
        if count > 0:
            self.selection_label.setText(f"{count} page{'s' if count != 1 else ''} selected")
            self.selection_label.show()
        else:
            self.selection_label.hide()
        
        # Update grid info
        total = self.pdf_view.get_page_count()
        if count > 0:
            self.grid_selection_info.setText(f"{count} of {total} pages selected")
        else:
            self.grid_selection_info.setText("Click pages to select them for splitting")
    
    def select_all_pages(self):
        """Select all pages in grid view."""
        self.grid_view.select_all()
    
    def deselect_all_pages(self):
        """Deselect all pages in grid view."""
        self.grid_view.deselect_all()
    
    def go_to_page_from_grid(self, page_num: int):
        """Navigate to page from grid double-click."""
        self.pdf_view.go_to_page(page_num)
        self.set_view_mode("single")
    
    def show_split_dialog(self):
        """Show the split PDF dialog."""
        total_pages = self.pdf_view.get_page_count()
        dialog = SplitPDFDialog(self.selected_pages, total_pages, self)
        
        if dialog.exec() == QDialog.DialogCode.Accepted:
            pages_to_extract = dialog.get_pages_to_extract()
            if pages_to_extract:
                self.split_pdf(pages_to_extract)
    
    def split_pdf(self, pages: List[int]):
        """Extract selected pages to a new PDF file."""
        if not pages:
            return
        
        # Get save location
        default_name = Path(self.file_path).stem + "_split.pdf"
        save_path, _ = QFileDialog.getSaveFileName(
            self,
            "Save Split PDF",
            str(Path(self.file_path).parent / default_name),
            "PDF Files (*.pdf)"
        )
        
        if not save_path:
            return
        
        try:
            # Create new PDF with selected pages
            src_doc = self.pdf_view.pdf_doc
            new_doc = fitz.open()
            
            for page_num in sorted(pages):
                new_doc.insert_pdf(src_doc, from_page=page_num, to_page=page_num)
            
            new_doc.save(save_path)
            new_doc.close()
            
            QMessageBox.information(
                self,
                "Success",
                f"Successfully created new PDF with {len(pages)} page{'s' if len(pages) != 1 else ''}:\n{save_path}"
            )
            
        except Exception as e:
            QMessageBox.critical(
                self,
                "Error",
                f"Failed to create PDF:\n{str(e)}"
            )
    
    def on_pages_reordered(self, source_page: int, target_page: int):
        """Handle page reordering via drag-drop."""
        if not self.pdf_view.pdf_doc:
            return
        
        doc = self.pdf_view.pdf_doc
        
        # Move page in the document
        try:
            doc.move_page(source_page, target_page)
            self.modified = True
            self.refresh_after_edit()
            
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Failed to reorder pages:\n{str(e)}")
    
    def delete_selected_pages(self):
        """Delete the selected pages from the PDF."""
        if not self.selected_pages:
            QMessageBox.warning(self, "No Selection", "Please select pages to delete.")
            return
        
        if not self.pdf_view.pdf_doc:
            return
        
        doc = self.pdf_view.pdf_doc
        page_count = len(doc)
        
        # Confirm deletion
        if len(self.selected_pages) >= page_count:
            QMessageBox.warning(
                self, "Cannot Delete",
                "Cannot delete all pages. At least one page must remain."
            )
            return
        
        pages_str = ", ".join(str(p + 1) for p in sorted(self.selected_pages)[:10])
        if len(self.selected_pages) > 10:
            pages_str += f"... ({len(self.selected_pages)} total)"
        
        reply = QMessageBox.question(
            self,
            "Confirm Delete",
            f"Delete {len(self.selected_pages)} page{'s' if len(self.selected_pages) != 1 else ''}?\n\nPages: {pages_str}\n\nThis action cannot be undone.",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
            QMessageBox.StandardButton.No
        )
        
        if reply != QMessageBox.StandardButton.Yes:
            return
        
        try:
            # Delete pages in reverse order to maintain indices
            for page_num in sorted(self.selected_pages, reverse=True):
                doc.delete_page(page_num)
            
            self.modified = True
            self.selected_pages.clear()
            self.refresh_after_edit()
            
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Failed to delete pages:\n{str(e)}")
    
    def insert_pdf_pages(self):
        """Insert pages from another PDF file."""
        if not self.pdf_view.pdf_doc:
            return
        
        # Get PDF file to insert
        file_path, _ = QFileDialog.getOpenFileName(
            self,
            "Select PDF to Insert",
            "",
            "PDF Files (*.pdf)"
        )
        
        if not file_path:
            return
        
        src_doc = None
        try:
            src_doc = fitz.open(file_path)
            
            # Ask where to insert
            current_page_count = len(self.pdf_view.pdf_doc)
            
            # Create dialog for insertion options with thumbnail preview
            dialog = InsertPagesDialog(src_doc, current_page_count, self)
            
            if dialog.exec() == QDialog.DialogCode.Accepted:
                insert_pos = dialog.get_insert_position()
                selected_pages = dialog.get_selected_pages()
                
                # Insert the pages
                doc = self.pdf_view.pdf_doc
                
                # Insert pages one by one to support non-contiguous selection
                for i, page_num in enumerate(selected_pages):
                    doc.insert_pdf(src_doc, from_page=page_num, to_page=page_num, 
                                   start_at=insert_pos + i)
                
                self.modified = True
                self.refresh_after_edit()
                
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Failed to insert PDF:\n{str(e)}")
        finally:
            if src_doc:
                src_doc.close()
    
    def insert_image_as_page(self):
        """Insert images as new PDF pages."""
        if not self.pdf_view.pdf_doc:
            return
        
        # Get image files
        file_paths, _ = QFileDialog.getOpenFileNames(
            self,
            "Select Images to Insert",
            "",
            "Image Files (*.png *.jpg *.jpeg *.gif *.bmp *.tiff *.webp)"
        )
        
        if not file_paths:
            return
        
        try:
            doc = self.pdf_view.pdf_doc
            current_page_count = len(doc)
            
            # Ask where to insert
            position, ok = QInputDialog.getInt(
                self,
                "Insert Position",
                f"Insert after page (0 = at beginning, {current_page_count} = at end):",
                current_page_count,  # Default to end
                0,
                current_page_count
            )
            
            if not ok:
                return
            
            # Insert each image as a page
            for i, img_path in enumerate(file_paths):
                # Get image dimensions
                img = fitz.open(img_path)
                
                if img.is_pdf:
                    # It's actually a PDF, insert it directly
                    doc.insert_pdf(img, start_at=position + i)
                else:
                    # It's an image
                    img_rect = img[0].rect
                    
                    # Create a new page with appropriate size
                    # Use A4 as base and scale to fit
                    page_width = 612  # Letter width in points
                    page_height = 792  # Letter height in points
                    
                    # Calculate scale to fit image on page with margins
                    margin = 36  # 0.5 inch margins
                    available_width = page_width - 2 * margin
                    available_height = page_height - 2 * margin
                    
                    scale_x = available_width / img_rect.width
                    scale_y = available_height / img_rect.height
                    scale = min(scale_x, scale_y)
                    
                    # Create page
                    new_page = doc.new_page(pno=position + i, width=page_width, height=page_height)
                    
                    # Calculate centered position
                    img_width = img_rect.width * scale
                    img_height = img_rect.height * scale
                    x = (page_width - img_width) / 2
                    y = (page_height - img_height) / 2
                    
                    # Insert image
                    rect = fitz.Rect(x, y, x + img_width, y + img_height)
                    new_page.insert_image(rect, filename=img_path)
                
                img.close()
            
            self.modified = True
            self.refresh_after_edit()
            
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Failed to insert images:\n{str(e)}")
    
    def refresh_after_edit(self):
        """Refresh the view after editing the PDF."""
        if not self.pdf_view.pdf_doc:
            return
        
        # Update page count
        page_count = len(self.pdf_view.pdf_doc)
        self.page_spin.setMaximum(page_count)
        self.page_label.setText(f"/ {page_count}")
        
        # Ensure current page is valid
        current_page = self.pdf_view.current_page
        if current_page >= page_count:
            current_page = max(0, page_count - 1)
            self.pdf_view.current_page = current_page
        
        # Refresh the single page view
        self.pdf_view.render_page()
        
        # Refresh the grid view
        self.grid_view.refresh_thumbnails()
        
        # Clear selection
        self.selected_pages.clear()
        self.update_selection_label()
        self.delete_pages_btn.setEnabled(False)
        
        # Update page spin
        self.page_spin.setValue(current_page + 1)
    
    def save_pdf(self):
        """Save the current PDF."""
        if not self.pdf_view.pdf_doc:
            return
        
        try:
            self.pdf_view.pdf_doc.save(self.file_path, incremental=True, encryption=fitz.PDF_ENCRYPT_KEEP)
            self.modified = False
            QMessageBox.information(self, "Success", f"PDF saved successfully:\n{self.file_path}")
        except Exception as e:
            # If incremental save fails, try regular save
            try:
                self.pdf_view.pdf_doc.save(self.file_path)
                self.modified = False
                QMessageBox.information(self, "Success", f"PDF saved successfully:\n{self.file_path}")
            except Exception as e2:
                QMessageBox.critical(self, "Error", f"Failed to save PDF:\n{str(e2)}")
    
    def save_pdf_as(self):
        """Save the current PDF to a new file."""
        if not self.pdf_view.pdf_doc:
            return
        
        save_path, _ = QFileDialog.getSaveFileName(
            self,
            "Save PDF As",
            str(Path(self.file_path).parent / (Path(self.file_path).stem + "_edited.pdf")),
            "PDF Files (*.pdf)"
        )
        
        if not save_path:
            return
        
        try:
            self.pdf_view.pdf_doc.save(save_path)
            QMessageBox.information(self, "Success", f"PDF saved successfully:\n{save_path}")
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Failed to save PDF:\n{str(e)}")
    
    def prev_page(self):
        self.pdf_view.prev_page()
    
    def next_page(self):
        self.pdf_view.next_page()
    
    def zoom_in(self):
        self.pdf_view.zoom_in()
        self.update_zoom_display()
    
    def zoom_out(self):
        self.pdf_view.zoom_out()
        self.update_zoom_display()
    
    def fit_width(self):
        self.pdf_view.fit_width()
        self.update_zoom_display()
    
    def fit_page(self):
        self.pdf_view.fit_page()
        self.update_zoom_display()
    
    def on_page_spin_changed(self, value):
        self.pdf_view.go_to_page(value - 1)
    
    def on_page_changed(self, page_num):
        self.page_spin.blockSignals(True)
        self.page_spin.setValue(page_num + 1)
        self.page_spin.blockSignals(False)
    
    def on_zoom_slider_changed(self, value):
        zoom = value / 100.0
        self.pdf_view.set_zoom(zoom)
        self.zoom_label.setText(f"{value}%")
    
    def update_zoom_display(self):
        zoom_percent = int(self.pdf_view.zoom_level * 100)
        self.zoom_slider.blockSignals(True)
        self.zoom_slider.setValue(zoom_percent)
        self.zoom_slider.blockSignals(False)
        self.zoom_label.setText(f"{zoom_percent}%")
    
    def update_styles_for_theme(self, theme: str):
        """Update tab-specific styles for the given theme."""
        self.current_theme = theme  # Store for delayed grid loading
        if theme == "dark":
            # Navigation bar
            nav_bar_style = """
                QFrame {
                    background-color: #21262d;
                    border-bottom: 1px solid #30363d;
                    padding: 8px;
                }
            """
            btn_style = """
                QPushButton {
                    background-color: #30363d;
                    border-radius: 6px;
                    font-size: 14px;
                    color: #c9d1d9;
                }
                QPushButton:hover { background-color: #484f58; }
            """
            zoom_btn_style = """
                QPushButton {
                    background-color: #30363d;
                    border-radius: 6px;
                    font-size: 18px;
                    font-weight: bold;
                    color: #c9d1d9;
                }
                QPushButton:hover { background-color: #484f58; }
            """
            toggle_btn_style = """
                QPushButton {
                    background-color: #30363d;
                    border-radius: 6px;
                    padding: 0 16px;
                    font-weight: 600;
                    color: #c9d1d9;
                }
                QPushButton:checked {
                    background-color: #388bfd;
                    color: white;
                }
                QPushButton:!checked {
                    background-color: #30363d;
                }
                QPushButton:!checked:hover {
                    background-color: #484f58;
                }
            """
            grid_controls_style = """
                QFrame {
                    background-color: #161b22;
                    border-bottom: 1px solid #30363d;
                    padding: 6px;
                }
            """
            separator_color = "#30363d"
            label_color = "#8b949e"
            selection_color = "#58a6ff"
        else:
            # Light theme
            nav_bar_style = """
                QFrame {
                    background-color: #f6f8fa;
                    border-bottom: 1px solid #d0d7de;
                    padding: 8px;
                }
            """
            btn_style = """
                QPushButton {
                    background-color: #eaeef2;
                    border-radius: 6px;
                    font-size: 14px;
                    color: #1f2328;
                }
                QPushButton:hover { background-color: #d0d7de; }
            """
            zoom_btn_style = """
                QPushButton {
                    background-color: #eaeef2;
                    border-radius: 6px;
                    font-size: 18px;
                    font-weight: bold;
                    color: #1f2328;
                }
                QPushButton:hover { background-color: #d0d7de; }
            """
            toggle_btn_style = """
                QPushButton {
                    background-color: #eaeef2;
                    border-radius: 6px;
                    padding: 0 16px;
                    font-weight: 600;
                    color: #1f2328;
                }
                QPushButton:checked {
                    background-color: #0969da;
                    color: white;
                }
                QPushButton:!checked {
                    background-color: #eaeef2;
                }
                QPushButton:!checked:hover {
                    background-color: #d0d7de;
                }
            """
            grid_controls_style = """
                QFrame {
                    background-color: #f6f8fa;
                    border-bottom: 1px solid #d0d7de;
                    padding: 6px;
                }
            """
            separator_color = "#d0d7de"
            label_color = "#57606a"
            selection_color = "#0969da"
        
        # Update navigation bar
        self.nav_bar.setStyleSheet(nav_bar_style)
        
        # Update view toggle buttons
        self.single_view_btn.setStyleSheet(toggle_btn_style)
        self.grid_view_btn.setStyleSheet(toggle_btn_style)
        
        # Update separators
        self.sep1.setStyleSheet(f"background-color: {separator_color}; max-width: 1px; margin: 0 8px;")
        self.sep2.setStyleSheet(f"background-color: {separator_color}; max-width: 1px; margin: 0 8px;")
        
        # Update navigation buttons
        self.prev_btn.setStyleSheet(btn_style)
        self.next_btn.setStyleSheet(btn_style)
        
        # Update zoom buttons
        self.zoom_out_btn.setStyleSheet(zoom_btn_style)
        self.zoom_in_btn.setStyleSheet(zoom_btn_style)
        
        # Update labels
        self.page_label.setStyleSheet(f"color: {label_color}; padding: 0 8px;")
        self.zoom_label.setStyleSheet(f"color: {label_color}; padding-left: 8px;")
        self.selection_label.setStyleSheet(f"color: {selection_color}; font-weight: 500; padding: 0 12px;")
        
        # Update grid controls
        self.grid_controls.setStyleSheet(grid_controls_style)
        self.grid_selection_info.setStyleSheet(f"color: {label_color}; font-size: 13px;")
        
        # Update grid view theme
        self.grid_view.set_theme(theme)
    
    def print_pdf(self):
        """Print the current PDF document."""
        if not self.pdf_view.pdf_doc:
            QMessageBox.warning(self, "No Document", "No PDF document is open.")
            return
        
        printer = QPrinter(QPrinter.PrinterMode.HighResolution)
        printer.setDocName(self.file_name)
        
        # Show print dialog
        dialog = QPrintDialog(printer, self)
        dialog.setWindowTitle("Print PDF")
        
        if dialog.exec() == QPrintDialog.DialogCode.Accepted:
            self.do_print(printer)
    
    def print_preview(self):
        """Show print preview dialog."""
        if not self.pdf_view.pdf_doc:
            QMessageBox.warning(self, "No Document", "No PDF document is open.")
            return
        
        printer = QPrinter(QPrinter.PrinterMode.HighResolution)
        printer.setDocName(self.file_name)
        
        preview = QPrintPreviewDialog(printer, self)
        preview.setWindowTitle(f"Print Preview - {self.file_name}")
        preview.paintRequested.connect(self.do_print)
        preview.exec()
    
    def do_print(self, printer: QPrinter):
        """Perform the actual printing."""
        if not self.pdf_view.pdf_doc:
            return
        
        painter = QPainter()
        if not painter.begin(printer):
            QMessageBox.critical(self, "Print Error", "Failed to start printing.")
            return
        
        try:
            doc = self.pdf_view.pdf_doc
            page_count = len(doc)
            
            # Get printer page rect
            page_rect = printer.pageRect(QPrinter.Unit.DevicePixel)
            
            for i in range(page_count):
                if i > 0:
                    printer.newPage()
                
                # Get the PDF page
                page = doc[i]
                
                # Calculate scale to fit the page
                pdf_rect = page.rect
                
                # Calculate scaling factor to fit page while maintaining aspect ratio
                scale_x = page_rect.width() / pdf_rect.width
                scale_y = page_rect.height() / pdf_rect.height
                scale = min(scale_x, scale_y) * 0.95  # 95% to leave margin
                
                # Render at high resolution
                mat = fitz.Matrix(scale, scale)
                pix = page.get_pixmap(matrix=mat, alpha=False)
                
                # Convert to QImage
                img = QImage(pix.samples, pix.width, pix.height, pix.stride, 
                            QImage.Format.Format_RGB888)
                
                # Center on page
                x_offset = (page_rect.width() - pix.width) / 2
                y_offset = (page_rect.height() - pix.height) / 2
                
                # Draw the image
                painter.drawImage(int(x_offset), int(y_offset), img)
                
        except Exception as e:
            QMessageBox.critical(self, "Print Error", f"Error during printing:\n{str(e)}")
        finally:
            painter.end()
    
    def close_tab(self):
        """Clean up when tab is closed."""
        self.pdf_view.close_pdf()


# ============================================================================
# MAIN WINDOW
# ============================================================================

class PDFViewerApp(QMainWindow):
    """Main application window."""
    
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PyPDF")
        self.setMinimumSize(1200, 800)
        self.resize(1400, 900)
        
        self.current_folder = None
        self.open_files: Dict[str, PDFTab] = {}
        self.current_theme = "dark"  # Track current theme
        
        self.setup_ui()
        self.setup_menu()
        self.setup_toolbar()
        self.setup_statusbar()
        self.show_welcome()
    
    def setup_ui(self):
        """Set up the main UI layout."""
        # Central widget with splitter
        central = QWidget()
        self.setCentralWidget(central)
        layout = QHBoxLayout(central)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)
        
        # Splitter for sidebar and content
        self.splitter = QSplitter(Qt.Orientation.Horizontal)
        layout.addWidget(self.splitter)
        
        # Left sidebar (file list)
        self.sidebar = QFrame()
        self.sidebar.setMinimumWidth(250)
        self.sidebar.setMaximumWidth(400)
        sidebar_layout = QVBoxLayout(self.sidebar)
        sidebar_layout.setContentsMargins(0, 0, 0, 0)
        sidebar_layout.setSpacing(0)
        
        # Sidebar header
        sidebar_header = QFrame()
        sidebar_header.setStyleSheet("""
            QFrame {
                background-color: #161b22;
                border-bottom: 1px solid #30363d;
            }
        """)
        header_layout = QVBoxLayout(sidebar_header)
        header_layout.setContentsMargins(16, 16, 16, 16)
        
        folder_title = QLabel("📁 PDF Files")
        folder_title.setStyleSheet("font-size: 16px; font-weight: 600; color: #c9d1d9;")
        header_layout.addWidget(folder_title)
        
        self.folder_path_label = QLabel("No folder selected")
        self.folder_path_label.setStyleSheet("font-size: 12px; color: #8b949e; margin-top: 4px;")
        self.folder_path_label.setWordWrap(True)
        header_layout.addWidget(self.folder_path_label)
        
        sidebar_layout.addWidget(sidebar_header)
        
        # File list
        self.file_list = QListWidget()
        self.file_list.itemDoubleClicked.connect(self.on_file_double_clicked)
        sidebar_layout.addWidget(self.file_list)
        
        # Initially hide sidebar
        self.sidebar.hide()
        
        self.splitter.addWidget(self.sidebar)
        
        # Right content area (tabs)
        self.content_area = QFrame()
        content_layout = QVBoxLayout(self.content_area)
        content_layout.setContentsMargins(0, 0, 0, 0)
        content_layout.setSpacing(0)
        
        # Tab widget
        self.tab_widget = QTabWidget()
        self.tab_widget.setTabsClosable(True)
        self.tab_widget.setMovable(True)
        self.tab_widget.setDocumentMode(True)
        self.tab_widget.tabCloseRequested.connect(self.close_tab)
        content_layout.addWidget(self.tab_widget)
        
        self.splitter.addWidget(self.content_area)
        self.splitter.setSizes([280, 1120])
    
    def setup_menu(self):
        """Set up the menu bar."""
        menubar = self.menuBar()
        
        # File menu
        file_menu = menubar.addMenu("&File")
        
        new_action = QAction("New PDF...", self)
        new_action.setShortcut(QKeySequence.StandardKey.New)
        new_action.triggered.connect(self.new_document)
        file_menu.addAction(new_action)
        
        open_action = QAction("Open File...", self)
        open_action.setShortcut(QKeySequence.StandardKey.Open)
        open_action.triggered.connect(self.open_file)
        file_menu.addAction(open_action)
        
        open_folder_action = QAction("Open Folder...", self)
        open_folder_action.setShortcut("Ctrl+Shift+O")
        open_folder_action.triggered.connect(self.open_folder)
        file_menu.addAction(open_folder_action)
        
        file_menu.addSeparator()
        
        save_action = QAction("Save", self)
        save_action.setShortcut(QKeySequence.StandardKey.Save)
        save_action.triggered.connect(self.save_pdf_current)
        file_menu.addAction(save_action)
        
        save_as_action = QAction("Save As...", self)
        save_as_action.setShortcut("Ctrl+Shift+S")
        save_as_action.triggered.connect(self.save_pdf_as_current)
        file_menu.addAction(save_as_action)
        
        file_menu.addSeparator()
        
        print_action = QAction("Print...", self)
        print_action.setShortcut(QKeySequence.StandardKey.Print)
        print_action.triggered.connect(self.print_current)
        file_menu.addAction(print_action)
        
        print_preview_action = QAction("Print Preview...", self)
        print_preview_action.setShortcut("Ctrl+Shift+P")
        print_preview_action.triggered.connect(self.print_preview_current)
        file_menu.addAction(print_preview_action)
        
        file_menu.addSeparator()
        
        close_action = QAction("Close Tab", self)
        close_action.setShortcut("Ctrl+W")
        close_action.triggered.connect(self.close_current_tab)
        file_menu.addAction(close_action)
        
        file_menu.addSeparator()
        
        exit_action = QAction("Exit", self)
        exit_action.setShortcut(QKeySequence.StandardKey.Quit)
        exit_action.triggered.connect(self.close)
        file_menu.addAction(exit_action)
        
        # View menu
        view_menu = menubar.addMenu("&View")
        
        zoom_in_action = QAction("Zoom In", self)
        zoom_in_action.setShortcut("Ctrl++")
        zoom_in_action.triggered.connect(self.zoom_in_current)
        view_menu.addAction(zoom_in_action)
        
        zoom_out_action = QAction("Zoom Out", self)
        zoom_out_action.setShortcut("Ctrl+-")
        zoom_out_action.triggered.connect(self.zoom_out_current)
        view_menu.addAction(zoom_out_action)
        
        view_menu.addSeparator()
        
        fit_width_action = QAction("Fit Width", self)
        fit_width_action.setShortcut("Ctrl+1")
        fit_width_action.triggered.connect(self.fit_width_current)
        view_menu.addAction(fit_width_action)
        
        fit_page_action = QAction("Fit Page", self)
        fit_page_action.setShortcut("Ctrl+2")
        fit_page_action.triggered.connect(self.fit_page_current)
        view_menu.addAction(fit_page_action)
        
        view_menu.addSeparator()
        
        single_view_action = QAction("Single Page View", self)
        single_view_action.setShortcut("Ctrl+3")
        single_view_action.triggered.connect(self.set_single_view)
        view_menu.addAction(single_view_action)
        
        grid_view_action = QAction("Grid View", self)
        grid_view_action.setShortcut("Ctrl+4")
        grid_view_action.triggered.connect(self.set_grid_view)
        view_menu.addAction(grid_view_action)
        
        view_menu.addSeparator()
        
        toggle_sidebar_action = QAction("Toggle Sidebar", self)
        toggle_sidebar_action.setShortcut("Ctrl+B")
        toggle_sidebar_action.triggered.connect(self.toggle_sidebar)
        view_menu.addAction(toggle_sidebar_action)
        
        view_menu.addSeparator()
        
        # Theme submenu
        theme_menu = view_menu.addMenu("Theme")
        
        self.dark_theme_action = QAction("🌙 Dark Theme", self)
        self.dark_theme_action.setCheckable(True)
        self.dark_theme_action.setChecked(True)
        self.dark_theme_action.triggered.connect(lambda: self.set_theme("dark"))
        theme_menu.addAction(self.dark_theme_action)
        
        self.light_theme_action = QAction("☀️ Light Theme", self)
        self.light_theme_action.setCheckable(True)
        self.light_theme_action.triggered.connect(lambda: self.set_theme("light"))
        theme_menu.addAction(self.light_theme_action)
        
        # Edit menu
        edit_menu = menubar.addMenu("&Edit")
        
        delete_pages_action = QAction("Delete Selected Pages", self)
        delete_pages_action.setShortcut("Delete")
        delete_pages_action.triggered.connect(self.delete_pages_current)
        edit_menu.addAction(delete_pages_action)
        
        edit_menu.addSeparator()
        
        insert_pdf_action = QAction("Insert Pages from PDF...", self)
        insert_pdf_action.setShortcut("Ctrl+I")
        insert_pdf_action.triggered.connect(self.insert_pdf_current)
        edit_menu.addAction(insert_pdf_action)
        
        insert_image_action = QAction("Insert Images as Pages...", self)
        insert_image_action.setShortcut("Ctrl+Shift+I")
        insert_image_action.triggered.connect(self.insert_image_current)
        edit_menu.addAction(insert_image_action)
        
        edit_menu.addSeparator()
        
        split_pdf_action = QAction("Extract Pages to New PDF...", self)
        split_pdf_action.setShortcut("Ctrl+E")
        split_pdf_action.triggered.connect(self.split_pdf_current)
        edit_menu.addAction(split_pdf_action)
        
        edit_menu.addSeparator()
        
        select_all_action = QAction("Select All Pages", self)
        select_all_action.setShortcut("Ctrl+A")
        select_all_action.triggered.connect(self.select_all_pages_current)
        edit_menu.addAction(select_all_action)
        
        deselect_all_action = QAction("Deselect All Pages", self)
        deselect_all_action.setShortcut("Ctrl+Shift+A")
        deselect_all_action.triggered.connect(self.deselect_all_pages_current)
        edit_menu.addAction(deselect_all_action)
        
        # Navigate menu
        nav_menu = menubar.addMenu("&Navigate")
        
        next_page_action = QAction("Next Page", self)
        next_page_action.setShortcut("Right")
        next_page_action.triggered.connect(self.next_page_current)
        nav_menu.addAction(next_page_action)
        
        prev_page_action = QAction("Previous Page", self)
        prev_page_action.setShortcut("Left")
        prev_page_action.triggered.connect(self.prev_page_current)
        nav_menu.addAction(prev_page_action)
        
        nav_menu.addSeparator()
        
        go_to_page_action = QAction("Go to Page...", self)
        go_to_page_action.setShortcut("Ctrl+G")
        go_to_page_action.triggered.connect(self.go_to_page_dialog)
        nav_menu.addAction(go_to_page_action)
        
        # Help menu
        help_menu = menubar.addMenu("&Help")
        
        about_action = QAction("About", self)
        about_action.triggered.connect(self.show_about)
        help_menu.addAction(about_action)
    
    def setup_toolbar(self):
        """Set up the main toolbar."""
        toolbar = QToolBar("Main Toolbar")
        toolbar.setMovable(False)
        toolbar.setIconSize(QSize(24, 24))
        self.addToolBar(toolbar)
        
        # New document button
        new_btn = QToolButton()
        new_btn.setText("📝 New")
        new_btn.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextOnly)
        new_btn.setStyleSheet("""
            QToolButton {
                background-color: #238636;
                border: 1px solid #238636;
            }
            QToolButton:hover {
                background-color: #2ea043;
                border-color: #2ea043;
            }
        """)
        new_btn.clicked.connect(self.new_document)
        toolbar.addWidget(new_btn)
        
        # Open file button
        open_btn = QToolButton()
        open_btn.setText("📄 Open")
        open_btn.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextOnly)
        open_btn.clicked.connect(self.open_file)
        toolbar.addWidget(open_btn)
        
        # Open folder button
        folder_btn = QToolButton()
        folder_btn.setText("📁 Folder")
        folder_btn.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextOnly)
        folder_btn.clicked.connect(self.open_folder)
        toolbar.addWidget(folder_btn)
        
        toolbar.addSeparator()
        
        # Navigation buttons
        prev_btn = QToolButton()
        prev_btn.setText("◀ Prev")
        prev_btn.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextOnly)
        prev_btn.clicked.connect(self.prev_page_current)
        toolbar.addWidget(prev_btn)
        
        next_btn = QToolButton()
        next_btn.setText("Next ▶")
        next_btn.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextOnly)
        next_btn.clicked.connect(self.next_page_current)
        toolbar.addWidget(next_btn)
        
        toolbar.addSeparator()
        
        # Zoom buttons
        zoom_out_btn = QToolButton()
        zoom_out_btn.setText("🔍−")
        zoom_out_btn.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextOnly)
        zoom_out_btn.clicked.connect(self.zoom_out_current)
        toolbar.addWidget(zoom_out_btn)
        
        zoom_in_btn = QToolButton()
        zoom_in_btn.setText("🔍+")
        zoom_in_btn.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextOnly)
        zoom_in_btn.clicked.connect(self.zoom_in_current)
        toolbar.addWidget(zoom_in_btn)
        
        toolbar.addSeparator()
        
        # Save button
        save_btn = QToolButton()
        save_btn.setText("💾 Save")
        save_btn.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextOnly)
        save_btn.setStyleSheet("""
            QToolButton {
                background-color: #238636;
                border: 1px solid #238636;
            }
            QToolButton:hover {
                background-color: #2ea043;
                border-color: #2ea043;
            }
        """)
        save_btn.clicked.connect(self.save_pdf_current)
        toolbar.addWidget(save_btn)
        
        toolbar.addSeparator()
        
        # Print button
        print_btn = QToolButton()
        print_btn.setText("🖨️ Print")
        print_btn.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextOnly)
        print_btn.clicked.connect(self.print_current)
        toolbar.addWidget(print_btn)
        
        toolbar.addSeparator()
        
        # Theme toggle button
        self.theme_btn = QToolButton()
        self.theme_btn.setText("☀️ Light")
        self.theme_btn.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextOnly)
        self.theme_btn.clicked.connect(self.toggle_theme)
        toolbar.addWidget(self.theme_btn)
    
    def toggle_theme(self):
        """Toggle between dark and light theme."""
        if self.current_theme == "dark":
            self.set_theme("light")
            self.theme_btn.setText("🌙 Dark")
        else:
            self.set_theme("dark")
            self.theme_btn.setText("☀️ Light")
    
    def setup_statusbar(self):
        """Set up the status bar."""
        self.statusbar = QStatusBar()
        self.setStatusBar(self.statusbar)
        self.statusbar.showMessage("Ready")
    
    def show_welcome(self):
        """Show welcome screen."""
        welcome = QWidget()
        layout = QVBoxLayout(welcome)
        layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        # Welcome content
        title = QLabel("📚 PyPDF")
        title.setObjectName("titleLabel")
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(title)
        
        subtitle = QLabel("Create, view, and edit PDF documents")
        subtitle.setObjectName("subtitleLabel")
        subtitle.setAlignment(Qt.AlignmentFlag.AlignCenter)
        subtitle.setStyleSheet("margin-bottom: 32px;")
        layout.addWidget(subtitle)
        
        # Action buttons
        btn_layout = QHBoxLayout()
        btn_layout.setSpacing(16)
        
        new_pdf_btn = QPushButton("📝 Create New PDF")
        new_pdf_btn.setFixedSize(180, 48)
        new_pdf_btn.setStyleSheet("""
            QPushButton {
                background-color: #238636;
                font-weight: 600;
            }
            QPushButton:hover {
                background-color: #2ea043;
            }
        """)
        new_pdf_btn.clicked.connect(self.new_document)
        btn_layout.addWidget(new_pdf_btn)
        
        open_file_btn = QPushButton("📄 Open File")
        open_file_btn.setFixedSize(140, 48)
        open_file_btn.clicked.connect(self.open_file)
        btn_layout.addWidget(open_file_btn)
        
        open_folder_btn = QPushButton("📁 Open Folder")
        open_folder_btn.setFixedSize(140, 48)
        open_folder_btn.clicked.connect(self.open_folder)
        btn_layout.addWidget(open_folder_btn)
        
        layout.addLayout(btn_layout)
        
        # Features list
        features = QLabel("""
            <div style="margin-top: 48px; color: #8b949e; text-align: center;">
                <p><b>Features:</b></p>
                <p>✓ <span style="color: #3fb950;">Create new PDFs</span> from scratch</p>
                <p>✓ <span style="color: #58a6ff;">Edit PDFs</span> - reorder, delete, insert pages</p>
                <p>✓ Insert pages from other PDFs or images</p>
                <p>✓ <span style="color: #a371f7;">Extract pages</span> to new PDF file</p>
                <p>✓ View with smooth zoom and scrolling</p>
                <p>✓ Grid view to see all pages at once</p>
                <p>✓ 🖨️ Print with preview support</p>
                <p>✓ 🌙 Dark / ☀️ Light theme</p>
            </div>
        """)
        features.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(features)
        
        self.tab_widget.addTab(welcome, "Welcome")
    
    def open_file(self):
        """Open a single PDF file."""
        file_path, _ = QFileDialog.getOpenFileName(
            self,
            "Open PDF File",
            "",
            "PDF Files (*.pdf);;All Files (*)"
        )
        
        if file_path:
            self.open_pdf(file_path)
    
    def new_document(self):
        """Create a new blank PDF document."""
        # Ask for save location first
        file_path, _ = QFileDialog.getSaveFileName(
            self,
            "Create New PDF",
            "Untitled.pdf",
            "PDF Files (*.pdf)"
        )
        
        if not file_path:
            return
        
        # Ensure .pdf extension
        if not file_path.lower().endswith('.pdf'):
            file_path += '.pdf'
        
        try:
            # Create a new PDF with one blank page
            doc = fitz.open()
            
            # Add a blank A4 page (595 x 842 points)
            page = doc.new_page(width=595, height=842)
            
            # Save the document
            doc.save(file_path)
            doc.close()
            
            # Open the newly created document
            self.open_pdf(file_path)
            
            # Switch to grid view to make it easy to add pages
            tab = self.get_current_tab()
            if tab:
                tab.set_view_mode("grid")
            
            self.statusbar.showMessage(f"Created new PDF: {Path(file_path).name}")
            
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Failed to create PDF:\n{str(e)}")
    
    def open_folder(self):
        """Open a folder containing PDF files."""
        folder_path = QFileDialog.getExistingDirectory(
            self,
            "Open Folder",
            ""
        )
        
        if folder_path:
            self.load_folder(folder_path)
    
    def load_folder(self, folder_path: str):
        """Load all PDF files from a folder."""
        self.current_folder = folder_path
        self.folder_path_label.setText(folder_path)
        
        # Find all PDF files
        pdf_files = []
        for file in Path(folder_path).iterdir():
            if file.suffix.lower() == ".pdf":
                pdf_files.append(file)
        
        pdf_files.sort(key=lambda x: x.name.lower())
        
        # Populate file list
        self.file_list.clear()
        for pdf_file in pdf_files:
            item = QListWidgetItem(f"📄 {pdf_file.name}")
            item.setData(Qt.ItemDataRole.UserRole, str(pdf_file))
            self.file_list.addItem(item)
        
        # Show sidebar
        self.sidebar.show()
        
        # Update status
        self.statusbar.showMessage(f"Found {len(pdf_files)} PDF files in folder")
        
        # Open first file if available
        if pdf_files:
            self.open_pdf(str(pdf_files[0]))
    
    def on_file_double_clicked(self, item: QListWidgetItem):
        """Handle double-click on file list item."""
        file_path = item.data(Qt.ItemDataRole.UserRole)
        if file_path:
            self.open_pdf(file_path)
    
    def open_pdf(self, file_path: str):
        """Open a PDF file in a new tab."""
        # Check if already open
        if file_path in self.open_files:
            # Switch to existing tab
            tab = self.open_files[file_path]
            index = self.tab_widget.indexOf(tab)
            if index >= 0:
                self.tab_widget.setCurrentIndex(index)
            return
        
        # Remove welcome tab if present
        for i in range(self.tab_widget.count()):
            if self.tab_widget.tabText(i) == "Welcome":
                self.tab_widget.removeTab(i)
                break
        
        # Create new tab
        try:
            tab = PDFTab(file_path)
            file_name = Path(file_path).name
            
            # Apply current theme to new tab
            tab.update_styles_for_theme(self.current_theme)
            if self.current_theme == "dark":
                tab.pdf_view.setBackgroundBrush(QBrush(QColor("#161b22")))
            else:
                tab.pdf_view.setBackgroundBrush(QBrush(QColor("#eaeef2")))
            
            # Truncate long names
            display_name = file_name if len(file_name) <= 30 else file_name[:27] + "..."
            
            index = self.tab_widget.addTab(tab, f"📄 {display_name}")
            self.tab_widget.setTabToolTip(index, file_path)
            self.tab_widget.setCurrentIndex(index)
            
            self.open_files[file_path] = tab
            self.statusbar.showMessage(f"Opened: {file_name}")
            
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Failed to open PDF:\n{e}")
    
    def close_tab(self, index: int):
        """Close a tab."""
        widget = self.tab_widget.widget(index)
        
        # Find and remove from open_files
        for path, tab in list(self.open_files.items()):
            if tab == widget:
                tab.close_tab()
                del self.open_files[path]
                break
        
        self.tab_widget.removeTab(index)
        
        # Show welcome if no tabs remain
        if self.tab_widget.count() == 0:
            self.show_welcome()
    
    def close_current_tab(self):
        """Close the current tab."""
        index = self.tab_widget.currentIndex()
        if index >= 0 and self.tab_widget.tabText(index) != "Welcome":
            self.close_tab(index)
    
    def get_current_tab(self) -> Optional[PDFTab]:
        """Get the current PDF tab."""
        widget = self.tab_widget.currentWidget()
        if isinstance(widget, PDFTab):
            return widget
        return None
    
    def zoom_in_current(self):
        """Zoom in on current tab."""
        tab = self.get_current_tab()
        if tab:
            tab.zoom_in()
    
    def zoom_out_current(self):
        """Zoom out on current tab."""
        tab = self.get_current_tab()
        if tab:
            tab.zoom_out()
    
    def fit_width_current(self):
        """Fit width on current tab."""
        tab = self.get_current_tab()
        if tab:
            tab.fit_width()
    
    def fit_page_current(self):
        """Fit page on current tab."""
        tab = self.get_current_tab()
        if tab:
            tab.fit_page()
    
    def next_page_current(self):
        """Next page on current tab."""
        tab = self.get_current_tab()
        if tab:
            tab.next_page()
    
    def prev_page_current(self):
        """Previous page on current tab."""
        tab = self.get_current_tab()
        if tab:
            tab.prev_page()
    
    def go_to_page_dialog(self):
        """Show dialog to go to specific page."""
        tab = self.get_current_tab()
        if not tab:
            return
        
        page_count = tab.pdf_view.get_page_count()
        page, ok = QInputDialog.getInt(
            self,
            "Go to Page",
            f"Enter page number (1-{page_count}):",
            tab.pdf_view.current_page + 1,
            1,
            page_count
        )
        
        if ok:
            tab.pdf_view.go_to_page(page - 1)
    
    def toggle_sidebar(self):
        """Toggle sidebar visibility."""
        self.sidebar.setVisible(not self.sidebar.isVisible())
    
    def set_theme(self, theme: str):
        """Set the application theme."""
        self.current_theme = theme
        
        # Save preference
        settings = QSettings("PyPDF", "PyPDF")
        settings.setValue("theme", theme)
        
        # Update menu checkmarks
        self.dark_theme_action.setChecked(theme == "dark")
        self.light_theme_action.setChecked(theme == "light")
        
        # Apply stylesheet
        if theme == "dark":
            QApplication.instance().setStyleSheet(DARK_THEME)
            self.update_inline_styles_dark()
        else:
            QApplication.instance().setStyleSheet(LIGHT_THEME)
            self.update_inline_styles_light()
        
        # Update PDF view backgrounds
        for tab in self.open_files.values():
            if theme == "dark":
                tab.pdf_view.setBackgroundBrush(QBrush(QColor("#161b22")))
            else:
                tab.pdf_view.setBackgroundBrush(QBrush(QColor("#eaeef2")))
            tab.update_styles_for_theme(theme)
        
        self.statusbar.showMessage(f"Switched to {theme.capitalize()} theme")
    
    def update_inline_styles_dark(self):
        """Update inline styles for dark theme."""
        # Update sidebar header
        if hasattr(self, 'sidebar'):
            for child in self.sidebar.findChildren(QFrame):
                if child.styleSheet() and "background-color" in child.styleSheet():
                    child.setStyleSheet("""
                        QFrame {
                            background-color: #161b22;
                            border-bottom: 1px solid #30363d;
                        }
                    """)
    
    def update_inline_styles_light(self):
        """Update inline styles for light theme."""
        # Update sidebar header
        if hasattr(self, 'sidebar'):
            for child in self.sidebar.findChildren(QFrame):
                if child.styleSheet() and "background-color" in child.styleSheet():
                    child.setStyleSheet("""
                        QFrame {
                            background-color: #f6f8fa;
                            border-bottom: 1px solid #d0d7de;
                        }
                    """)
    
    def set_single_view(self):
        """Set single page view on current tab."""
        tab = self.get_current_tab()
        if tab:
            tab.set_view_mode("single")
    
    def set_grid_view(self):
        """Set grid view on current tab."""
        tab = self.get_current_tab()
        if tab:
            tab.set_view_mode("grid")
    
    def split_pdf_current(self):
        """Show split dialog for current tab."""
        tab = self.get_current_tab()
        if tab:
            tab.show_split_dialog()
    
    def save_pdf_current(self):
        """Save the current tab's PDF."""
        tab = self.get_current_tab()
        if tab:
            tab.save_pdf()
        else:
            QMessageBox.information(self, "No Document", "Please open a PDF file first.")
    
    def save_pdf_as_current(self):
        """Save the current tab's PDF as a new file."""
        tab = self.get_current_tab()
        if tab:
            tab.save_pdf_as()
        else:
            QMessageBox.information(self, "No Document", "Please open a PDF file first.")
    
    def delete_pages_current(self):
        """Delete selected pages in current tab."""
        tab = self.get_current_tab()
        if tab:
            tab.delete_selected_pages()
        else:
            QMessageBox.information(self, "No Document", "Please open a PDF file first.")
    
    def insert_pdf_current(self):
        """Insert pages from another PDF into current tab."""
        tab = self.get_current_tab()
        if tab:
            tab.insert_pdf_pages()
        else:
            QMessageBox.information(self, "No Document", "Please open a PDF file first.")
    
    def insert_image_current(self):
        """Insert images as pages into current tab."""
        tab = self.get_current_tab()
        if tab:
            tab.insert_image_as_page()
        else:
            QMessageBox.information(self, "No Document", "Please open a PDF file first.")
    
    def select_all_pages_current(self):
        """Select all pages in current tab's grid view."""
        tab = self.get_current_tab()
        if tab:
            tab.set_view_mode("grid")
            tab.select_all_pages()
    
    def deselect_all_pages_current(self):
        """Deselect all pages in current tab's grid view."""
        tab = self.get_current_tab()
        if tab:
            tab.deselect_all_pages()
    
    def print_current(self):
        """Print the current tab's PDF."""
        tab = self.get_current_tab()
        if tab:
            tab.print_pdf()
        else:
            QMessageBox.information(self, "No Document", "Please open a PDF file first.")
    
    def print_preview_current(self):
        """Show print preview for current tab."""
        tab = self.get_current_tab()
        if tab:
            tab.print_preview()
        else:
            QMessageBox.information(self, "No Document", "Please open a PDF file first.")
    
    def show_about(self):
        """Show about dialog with logo."""
        import os
        
        dialog = QDialog(self)
        dialog.setWindowTitle("About PyPDF")
        dialog.setFixedWidth(520)
        
        layout = QVBoxLayout(dialog)
        layout.setSpacing(15)
        layout.setContentsMargins(30, 25, 30, 25)
        
        # Logo
        logo_label = QLabel()
        logo_path = os.path.join(os.path.dirname(__file__), "img", "pypdflogo.png")
        if os.path.exists(logo_path):
            logo_pixmap = QPixmap(logo_path)
            scaled_logo = logo_pixmap.scaled(100, 100, Qt.AspectRatioMode.KeepAspectRatio, 
                                              Qt.TransformationMode.SmoothTransformation)
            logo_label.setPixmap(scaled_logo)
        else:
            logo_label.setText("🔖")
            logo_label.setStyleSheet("font-size: 64px;")
        logo_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(logo_label)
        
        # Title and version
        #title_label = QLabel("<h1 style='margin: 0;'>PyPDF</h1>")
        #title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        #layout.addWidget(title_label)
        
        subtitle_label = QLabel("PDF Viewer, Creator & Editor")
        subtitle_label.setStyleSheet("color: #8b949e; font-size: 14px;")
        subtitle_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(subtitle_label)
        
        version_label = QLabel("Version 2.2")
        version_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(version_label)
        
        # Description
        desc_label = QLabel("A modern PDF viewer, creator and editor built with PyQt6 and PyMuPDF")
        desc_label.setWordWrap(True)
        desc_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(desc_label)
        
        # Tab widget for Features, Shortcuts, License
        tab_widget = QTabWidget()
        tab_widget.setFixedHeight(220)
        
        # Features tab
        features_widget = QWidget()
        features_layout = QVBoxLayout(features_widget)
        features_layout.setContentsMargins(10, 10, 10, 10)
        
        features_scroll = QScrollArea()
        features_scroll.setWidgetResizable(True)
        features_scroll.setFrameShape(QFrame.Shape.NoFrame)
        
        features_content = QWidget()
        features_content_layout = QVBoxLayout(features_content)
        features_content_layout.setContentsMargins(0, 0, 10, 0)
        
        features_text = """
        <ul style="margin: 0; padding-left: 20px;">
            <li><b>Create PDF</b> - Start new documents from scratch</li>
            <li>View PDF files with smooth rendering</li>
            <li>Open multiple PDFs in tabs</li>
            <li><b>Grid View</b> - See all pages as thumbnails</li>
            <li><b>Edit PDF</b> - Reorder, delete, insert pages</li>
            <li><b>Insert Pages</b> - From other PDFs or images</li>
            <li><b>Extract Pages</b> - Split to new PDF file</li>
            <li><b>Print</b> - Print with preview support</li>
            <li><b>Dark/Light Theme</b> - Switch via View menu</li>
        </ul>
        """
        features_label = QLabel(features_text)
        features_label.setWordWrap(True)
        features_label.setAlignment(Qt.AlignmentFlag.AlignTop)
        features_content_layout.addWidget(features_label)
        
        features_scroll.setWidget(features_content)
        features_layout.addWidget(features_scroll)
        tab_widget.addTab(features_widget, "Features")
        
        # Shortcuts tab
        shortcuts_widget = QWidget()
        shortcuts_layout = QVBoxLayout(shortcuts_widget)
        shortcuts_layout.setContentsMargins(10, 10, 10, 10)
        
        shortcuts_scroll = QScrollArea()
        shortcuts_scroll.setWidgetResizable(True)
        shortcuts_scroll.setFrameShape(QFrame.Shape.NoFrame)
        
        shortcuts_content = QWidget()
        shortcuts_content_layout = QVBoxLayout(shortcuts_content)
        shortcuts_content_layout.setContentsMargins(0, 0, 10, 0)
        
        shortcuts_text = """
        <table style="width: 100%;" cellpadding="5">
            <tr><td><b>Ctrl+N</b></td><td>New PDF document</td></tr>
            <tr><td><b>Ctrl+O</b></td><td>Open file</td></tr>
            <tr><td><b>Ctrl+S</b></td><td>Save document</td></tr>
            <tr><td><b>Ctrl+Shift+S</b></td><td>Save as...</td></tr>
            <tr><td><b>Ctrl+I</b></td><td>Insert PDF pages</td></tr>
            <tr><td><b>Ctrl+Shift+I</b></td><td>Insert images as pages</td></tr>
            <tr><td><b>Ctrl+P</b></td><td>Print document</td></tr>
            <tr><td><b>Delete</b></td><td>Delete selected pages</td></tr>
            <tr><td><b>Ctrl++</b></td><td>Zoom in</td></tr>
            <tr><td><b>Ctrl+-</b></td><td>Zoom out</td></tr>
        </table>
        """
        shortcuts_label = QLabel(shortcuts_text)
        shortcuts_label.setWordWrap(True)
        shortcuts_label.setAlignment(Qt.AlignmentFlag.AlignTop)
        shortcuts_content_layout.addWidget(shortcuts_label)
        
        shortcuts_scroll.setWidget(shortcuts_content)
        shortcuts_layout.addWidget(shortcuts_scroll)
        tab_widget.addTab(shortcuts_widget, "Shortcuts")
        
        # Author tab
        author_widget = QWidget()
        author_layout = QVBoxLayout(author_widget)
        author_layout.setContentsMargins(15, 15, 15, 15)
        author_layout.setSpacing(12)
        
        author_text = """
        <p style="font-size: 14px; margin-bottom: 15px;">
            <b>👤 Author</b><br>
            <span style="font-size: 16px;">Jitendra Rana</span>
        </p>
        <p style="font-size: 14px; margin-bottom: 15px;">
            <b>📧 Email</b><br>
            <a href="mailto:jsrana+pypdf@gmail.com" style="color: #58a6ff;">jsrana+pypdf@gmail.com</a>
        </p>
        <p style="font-size: 14px; margin-bottom: 15px;">
            <b>🔗 GitHub Repository</b><br>
            <a href="https://github.com/jrana/pypdf" style="color: #58a6ff;">https://github.com/jrana/pypdf</a>
        </p>
        <p style="font-size: 12px; color: #8b949e; margin-top: 20px;">
            Built with ❤️ using PyQt6 and PyMuPDF
        </p>
        """
        author_label = QLabel(author_text)
        author_label.setWordWrap(True)
        author_label.setOpenExternalLinks(True)
        author_label.setAlignment(Qt.AlignmentFlag.AlignTop)
        author_layout.addWidget(author_label)
        author_layout.addStretch()
        tab_widget.addTab(author_widget, "Author")
        
        # License tab
        license_widget = QWidget()
        license_layout = QVBoxLayout(license_widget)
        license_layout.setContentsMargins(10, 10, 10, 10)
        
        license_scroll = QScrollArea()
        license_scroll.setWidgetResizable(True)
        license_scroll.setFrameShape(QFrame.Shape.NoFrame)
        
        license_content = QWidget()
        license_content_layout = QVBoxLayout(license_content)
        license_content_layout.setContentsMargins(0, 0, 10, 0)
        
        license_text = """
        <p><b>MIT License</b></p>
        <p style="color: #8b949e;">
        Copyright © 2025 Jitendra Rana<br><br>
        Permission is hereby granted, free of charge, to any person obtaining a copy
        of this software and associated documentation files (the "Software"), to deal
        in the Software without restriction, including without limitation the rights
        to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
        copies of the Software, and to permit persons to whom the Software is
        furnished to do so, subject to the following conditions:<br><br>
        The above copyright notice and this permission notice shall be included in all
        copies or substantial portions of the Software.<br><br>
        THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
        IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
        FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
        AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
        LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
        OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
        SOFTWARE.
        </p>
        """
        license_label = QLabel(license_text)
        license_label.setWordWrap(True)
        license_label.setAlignment(Qt.AlignmentFlag.AlignTop)
        license_content_layout.addWidget(license_label)
        
        license_scroll.setWidget(license_content)
        license_layout.addWidget(license_scroll)
        tab_widget.addTab(license_widget, "License")
        
        layout.addWidget(tab_widget)
        
        # Close button
        close_btn = QPushButton("Close")
        close_btn.clicked.connect(dialog.accept)
        close_btn.setFixedWidth(100)
        
        btn_layout = QHBoxLayout()
        btn_layout.addStretch()
        btn_layout.addWidget(close_btn)
        btn_layout.addStretch()
        layout.addLayout(btn_layout)
        
        dialog.exec()
    
    def closeEvent(self, event):
        """Handle application close."""
        # Check for unsaved changes
        unsaved_files = []
        for file_path, tab in self.open_files.items():
            if tab.modified:
                unsaved_files.append(tab.file_name)
        
        if unsaved_files:
            # Show warning dialog
            msg = QMessageBox(self)
            msg.setIcon(QMessageBox.Icon.Warning)
            msg.setWindowTitle("Unsaved Changes")
            
            if len(unsaved_files) == 1:
                msg.setText(f"'{unsaved_files[0]}' has unsaved changes.")
            else:
                files_list = "\n".join(f"• {f}" for f in unsaved_files)
                msg.setText(f"The following files have unsaved changes:\n\n{files_list}")
            
            msg.setInformativeText("Do you want to quit without saving?")
            msg.setStandardButtons(
                QMessageBox.StandardButton.Discard | 
                QMessageBox.StandardButton.Cancel
            )
            msg.setDefaultButton(QMessageBox.StandardButton.Cancel)
            msg.button(QMessageBox.StandardButton.Discard).setText("Quit Without Saving")
            
            result = msg.exec()
            
            if result == QMessageBox.StandardButton.Cancel:
                event.ignore()
                return
        
        # Close all open PDFs
        for tab in self.open_files.values():
            tab.close_tab()
        event.accept()


# ============================================================================
# MAIN ENTRY POINT
# ============================================================================

def main():
    app = QApplication(sys.argv)
    app.setStyle("Fusion")
    
    # Set application icon
    icon_path = os.path.join(os.path.dirname(__file__), "img", "pypdf.ico")
    if os.path.exists(icon_path):
        app.setWindowIcon(QIcon(icon_path))
    
    # Load saved theme preference (default to dark)
    settings = QSettings("PyPDF", "PyPDF")
    saved_theme = settings.value("theme", "dark")
    
    # Apply initial theme
    if saved_theme == "light":
        app.setStyleSheet(LIGHT_THEME)
    else:
        app.setStyleSheet(DARK_THEME)
    
    window = PDFViewerApp()
    
    # Set theme in window (updates menu checkmarks and internal state)
    window.current_theme = saved_theme
    window.dark_theme_action.setChecked(saved_theme == "dark")
    window.light_theme_action.setChecked(saved_theme == "light")
    if saved_theme == "light":
        window.update_inline_styles_light()
        window.theme_btn.setText("🌙 Dark")
    else:
        window.update_inline_styles_dark()
        window.theme_btn.setText("☀️ Light")
    
    window.show()
    
    sys.exit(app.exec())


if __name__ == "__main__":
    main()


