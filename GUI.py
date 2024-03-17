import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *


class DragDropWidget(QWidget):
    def __init__(self):
        super().__init__()

        # Set up the layout
        layout = QVBoxLayout()

        # Create a QLabel to act as the drag-and-drop area
        self.drag_drop_label = QLabel("Drag and drop files here")
        self.drag_drop_label.setStyleSheet("border: 2px dashed #aaa; padding: 20px;")
        layout.addWidget(self.drag_drop_label)

        self.textBox = QTextEdit(self)
        self.textBox.setAcceptDrops(True)
        self.textBox.setPlaceholderText("Namn för folder: (ex: Jan21)")
        layout.addWidget(self.textBox)

        self.setLayout(layout)

    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls():
            event.accept()
        else:
            event.ignore()

    def dropEvent(self, event):
        for url in event.mimeData().urls():
            file_path = url.toLocalFile()
            print("Dropped file:", file_path)
            # Process the dropped file here


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = DragDropWidget()
    window.setWindowTitle("Drag and Drop Example")
    window.setGeometry(100, 100, 400, 300)
    window.show()
    sys.exit(app.exec_())
