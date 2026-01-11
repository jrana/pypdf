"""
Link handling methods for PDFPageView
"""

def _extract_links_from_page(self, page_num: int, x_offset: float, y_offset: float):
    """Extract links from a PDF page and store them with scene coordinates."""
    if not self.pdf_doc:
        return
    
    page = self.pdf_doc[page_num]
    links = page.get_links()
    
    for link in links:
        if 'from' in link:
            rect = link['from']
            # Convert PDF coordinates to scene coordinates
            # PDF coordinates are in points, we need to scale by zoom
            scale = self.zoom_level * 2  # Match rendering scale
            scene_rect = QRectF(
                x_offset + rect.x0 * scale,
                y_offset + rect.y0 * scale,
                (rect.x1 - rect.x0) * scale,
                (rect.y1 - rect.y0) * scale
            )
            
            link_info = {
                'page': page_num,
                'rect': scene_rect,
                'uri': link.get('uri', ''),
                'page_dest': link.get('page', -1)
            }
            self.links.append(link_info)


def mousePressEvent(self, event: QMouseEvent):
    """Handle mouse press to detect link clicks."""
    if event.button() == Qt.MouseButton.LeftButton:
        # Convert to scene coordinates
        scene_pos = self.mapToScene(event.pos())
        
        # Check if click is on a link
        for link in self.links:
            if link['rect'].contains(scene_pos):
                self._handle_link_click(link)
                event.accept()
                return
    
    super().mousePressEvent(event)


def mouseMoveEvent(self, event: QMouseEvent):
    """Handle mouse move to change cursor over links."""
    scene_pos = self.mapToScene(event.pos())
    
    # Check if hovering over a link
    over_link = False
    for link in self.links:
        if link['rect'].contains(scene_pos):
            over_link = True
            break
    
    # Change cursor
    if over_link:
        self.viewport().setCursor(Qt.CursorShape.PointingHandCursor)
    else:
        self.viewport().setCursor(Qt.CursorShape.ArrowCursor)
    
    super().mouseMoveEvent(event)


def _handle_link_click(self, link: dict):
    """Handle clicking on a link."""
    import webbrowser
    
    if link['uri']:
        # External URL
        webbrowser.open(link['uri'])
    elif link['page_dest'] >= 0:
        # Internal page link
        self.go_to_page(link['page_dest'])
