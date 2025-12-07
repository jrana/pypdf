# PyPDF - PDF Viewer & Editor

A modern, feature-rich PDF viewer and editor built with PyQt6 and PyMuPDF.

![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)
![PyQt6](https://img.shields.io/badge/PyQt6-6.6+-green.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

## Features

### Create & Edit
- **📝 Create New PDFs** - Start new documents from scratch
- **🔀 Reorder Pages** - Drag and drop pages in grid view to reorder
- **🗑️ Delete Pages** - Remove selected pages from the PDF
- **📄+ Insert PDF Pages** - Insert pages from another PDF at any position
- **🖼️ Insert Images** - Add images as new PDF pages
- **✂️ Extract Pages** - Split selected pages into a new PDF file
- **💾 Save Changes** - Save modified PDFs

### Viewing
- **📄 View PDF Files** - Smooth, high-quality PDF rendering
- **🔍 Zoom Controls** - Zoom in/out with slider, buttons, or Ctrl+scroll
- **📑 Tabbed Interface** - Open multiple PDFs in separate tabs
- **📁 Folder Browsing** - Open an entire folder and browse all PDFs from the sidebar
- **⊞ Grid View** - View all pages as responsive thumbnails (max 4 per row)

### Other
- **🖨️ Print Support** - Print PDFs with print preview
- **🌙/☀️ Dark & Light Themes** - Toggle between beautiful dark and light interfaces
- **⌨️ Keyboard Navigation** - Full keyboard support for efficient navigation

## Installation

### Prerequisites

- Python 3.9 or higher
- pip (Python package installer)

### Install Dependencies

```bash
pip install -r requirements.txt
```

Or install packages individually:

```bash
pip install PyQt6 PyMuPDF
```

## Usage

### Running the Application

```bash
python pdf_viewer.py
```

### Creating a New PDF

1. Click **"📝 Create New PDF"** on the welcome screen, or
2. Use the menu: File → New PDF... (`Ctrl+N`), or
3. Click the green **"📝 New"** button in the toolbar

After creating:
- A new PDF with one blank A4 page is created
- The document opens in Grid View for easy editing
- Add content by inserting images or pages from other PDFs
- Delete the blank page if not needed

### Opening Files

1. **Single File**: Click "Open File" or press `Ctrl+O`
2. **Entire Folder**: Click "Open Folder" or press `Ctrl+Shift+O`

When opening a folder:
- All PDF files are listed in the left sidebar
- Double-click any file to open it in a new tab
- Each PDF opens in its own tab for easy switching

### Keyboard Shortcuts

| Action | Shortcut |
|--------|----------|
| New PDF | `Ctrl+N` |
| Open File | `Ctrl+O` |
| Open Folder | `Ctrl+Shift+O` |
| Save | `Ctrl+S` |
| Save As | `Ctrl+Shift+S` |
| Print | `Ctrl+P` |
| Print Preview | `Ctrl+Shift+P` |
| Close Tab | `Ctrl+W` |
| Next Page | `→` (Right Arrow) |
| Previous Page | `←` (Left Arrow) |
| Go to Page | `Ctrl+G` |
| Zoom In | `Ctrl++` or `Ctrl+Scroll Up` |
| Zoom Out | `Ctrl+-` or `Ctrl+Scroll Down` |
| Fit Width | `Ctrl+1` |
| Fit Page | `Ctrl+2` |
| Single Page View | `Ctrl+3` |
| Grid View | `Ctrl+4` |
| Toggle Sidebar | `Ctrl+B` |
| Insert PDF Pages | `Ctrl+I` |
| Insert Images | `Ctrl+Shift+I` |
| Delete Pages | `Delete` |
| Extract Pages | `Ctrl+E` |
| Select All Pages | `Ctrl+A` |
| Deselect All Pages | `Ctrl+Shift+A` |
| Exit | `Ctrl+Q` |

### Mouse Controls

- **Scroll**: Navigate through pages
- **Ctrl + Scroll**: Zoom in/out
- **Click and Drag**: Pan around the document (when zoomed in)
- **Drag in Grid View**: Reorder pages

## Editing PDFs

### Creating a PDF from Images

1. Click **"📝 Create New PDF"** to start a new document
2. Click **"🖼️ Insert Image"** to add your images
3. Select multiple images at once if needed
4. Delete the initial blank page (select it and press `Delete`)
5. Drag pages to reorder as needed
6. Save with `Ctrl+S`

### Reordering Pages

1. Switch to **Grid View** (`Ctrl+4` or click "⊞ Grid")
2. **Drag and drop** any page thumbnail to a new position
3. The page order is updated immediately
4. Save your changes with `Ctrl+S`

### Deleting Pages

1. Switch to **Grid View** 
2. **Select pages** by clicking thumbnails or using checkboxes
3. Click the **"🗑️ Delete"** button or press `Delete`
4. Confirm the deletion
5. Save your changes

### Inserting Pages from Another PDF

1. Click **"📄+ Insert PDF"** or press `Ctrl+I`
2. Select the PDF file to insert from
3. Choose which pages to insert (all or a range)
4. Choose the insert position
5. Click "Insert Pages"

### Inserting Images as Pages

1. Click **"🖼️ Insert Image"** or press `Ctrl+Shift+I`
2. Select one or more image files (PNG, JPG, GIF, BMP, TIFF, WebP)
3. Choose the insert position
4. Images are automatically sized to fit the page

### Extracting Pages to New PDF

1. Switch to **Grid View**
2. Select the pages you want to extract
3. Click **"✂ Extract"** or press `Ctrl+E`
4. Optionally modify the page selection in the dialog
5. Click "Save as New PDF" and choose a location

### Saving Changes

- **Save**: `Ctrl+S` - Saves changes to the original file
- **Save As**: `Ctrl+Shift+S` - Save to a new file

## Theme Switching

Switch between Dark and Light themes:
- **Via Toolbar**: Click the "☀️ Light" / "🌙 Dark" button
- **Via Menu**: View → Theme → Dark Theme / Light Theme

## Project Structure

```
pypdf/
├── pdf_viewer.py      # Main application
├── requirements.txt   # Python dependencies
└── README.md         # This file
```

## Dependencies

| Package | Version | Purpose |
|---------|---------|---------|
| PyQt6 | >= 6.6.0 | GUI framework |
| PyMuPDF | >= 1.23.0 | PDF rendering and manipulation |

## Troubleshooting

### Common Issues

**"No module named 'fitz'"**
- Install PyMuPDF: `pip install PyMuPDF`
- Note: The import is `fitz`, but the package name is `PyMuPDF`

**"No module named 'PyQt6'"**
- Install PyQt6: `pip install PyQt6`

**PDF not rendering correctly**
- Ensure you have the latest version of PyMuPDF
- Try updating: `pip install --upgrade PyMuPDF`

**Changes not saving**
- Some PDFs have restrictions. Try "Save As" to create a new copy.

## License

This project is open source and available under the MIT License.

## Contributing

Contributions are welcome! Feel free to:
- Report bugs
- Suggest new features
- Submit pull requests

---

Made with ❤️ using Python, PyQt6, and PyMuPDF
