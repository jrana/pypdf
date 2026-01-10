"""
Loading overlay widget for PyPDF application.
"""

from PyQt6.QtWidgets import QWidget, QLabel, QVBoxLayout
from PyQt6.QtCore import Qt, QTimer, QPropertyAnimation, QRect
from PyQt6.QtGui import QPainter, QColor, QPen


class LoadingOverlay(QWidget):
    """Semi-transparent overlay with loading spinner."""
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setAttribute(Qt.WidgetAttribute.WA_TransparentForMouseEvents, False)
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint)
        
        # Setup UI
        layout = QVBoxLayout(self)
        layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        self.label = QLabel("Loading PDF...")
        self.label.setStyleSheet("""
            QLabel {
                color: white;
                font-size: 18px;
                font-weight: 600;
                background-color: rgba(0, 0, 0, 180);
                padding: 20px 40px;
                border-radius: 10px;
            }
        """)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.label)
        
        # Animation properties
        self.angle = 0
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.rotate)
        
    def showEvent(self, event):
        """Start animation when shown."""
        super().showEvent(event)
        self.timer.start(50)  # Update every 50ms
        
    def hideEvent(self, event):
        """Stop animation when hidden."""
        super().hideEvent(event)
        self.timer.stop()
        
    def rotate(self):
        """Rotate the spinner."""
        self.angle = (self.angle + 10) % 360
        self.update()
        
    def paintEvent(self, event):
        """Draw the spinner."""
        super().paintEvent(event)
        
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)
        
        # Draw semi-transparent background
        painter.fillRect(self.rect(), QColor(0, 0, 0, 100))
        
        # Draw spinner
        center_x = self.width() // 2
        center_y = self.height() // 2 - 60
        radius = 30
        
        painter.setPen(QPen(QColor(255, 255, 255, 200), 4))
        
        for i in range(12):
            angle = self.angle + i * 30
            opacity = int(255 * (i / 12))
            painter.setPen(QPen(QColor(255, 255, 255, opacity), 4))
            
            import math
            x1 = center_x + radius * 0.6 * math.cos(math.radians(angle))
            y1 = center_y + radius * 0.6 * math.sin(math.radians(angle))
            x2 = center_x + radius * math.cos(math.radians(angle))
            y2 = center_y + radius * math.sin(math.radians(angle))
            
            painter.drawLine(int(x1), int(y1), int(x2), int(y2))
