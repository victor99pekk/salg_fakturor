import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *


class DragDropWidget(QWidget):
    def __init__(self):
        super().__init__()

        # Set up the layout
        layout = QVBoxLayout()
        font1 = QFont("Arial", 20)  # Set font family and size
        font2 = QFont("Arial", 15)

        # Create a QLabel to act as the drag-and-drop area
        self.drag_drop_label = QLabel("Dra hit foldern med filerna som ska samanställas")
        self.drag_drop_label.setFont(font2)
        self.drag_drop_label.setStyleSheet("border: 2px dashed #aaa; padding: 20px;")
        layout.addWidget(self.drag_drop_label)

        self.textBox = QTextEdit(self)
        self.textBox.setAcceptDrops(True)
        self.textBox.setPlaceholderText("Namn för folder: (ex: Jan21)")
        self.textBox.setMaximumHeight(35)
        self.textBox.setFont(font1)

        self.button = QPushButton("Sammanställ")
        self.button.setFont(font2)
        self.button.setMaximumHeight(35)
        self.button.setMaximumWidth(110)
        self.button.setStyleSheet("background-color: green;")
        layout.addWidget(self.button)
        #self.setStyle(QStyleFactory.create('Fusion'))

        self.text_field = QLineEdit()
        layout.addWidget(self.text_field)

        # Create a central widget and set the layout
        

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
