import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *


class DragDropWidget(QWidget):
    def __init__(self):
        super().__init__()

        self.targetFolder = ""
        self.inputPath = ""

        # Set up the layout
        layout = QVBoxLayout()
        font1 = QFont("Arial", 20)  # Set font family and size
        font2 = QFont("Arial", 15)

        # Create a QLabel to act as the drag-and-drop area
        self.folder_label = QTextEdit(self)
        self.folder_label.setFont(font2)
        layout.addWidget(self.folder_label)
        self.folder_label.setReadOnly(True)

        self.textBox = QTextEdit(self)
        self.textBox.setAcceptDrops(True)
        self.textBox.setPlaceholderText("Namnge folder:     (ex: Jan21)")
        self.textBox.setMaximumHeight(35)
        self.textBox.setFont(font1)

        self.button = QPushButton("Sammanställ")
        self.button.setFont(font2)
        self.button.setMaximumHeight(35)
        self.button.setMaximumWidth(110)
        self.button.setStyleSheet("background-color: green;")
        self.button.clicked.connect(self.click)
        #layout.addWidget(self.button)
        #self.setStyle(QStyleFactory.create('Fusion'))

        self.text_field = QLineEdit()
        self.text_field.setReadOnly(True)
        self.text_field.setFont(font1)
        self.text_field.setPlaceholderText("")
        self.text_field.setMaximumHeight(40)
        self.text_field.setMaximumWidth(220)

        self.open_button = QPushButton("Folder")
        self.open_button.clicked.connect(self.open_folder)


        # Create a central widget and set the layout

        button_layout = QHBoxLayout()
        button_layout.addWidget(self.button)
        button_layout.addWidget(self.text_field)
        layout.addWidget(self.open_button)
        layout.addLayout(button_layout)
        

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
            self.inputPath = file_path
            # Process the dropped file here
    
    def click(self, event):
        self.targetFolder = self.textBox.toPlainText()
        if self.targetFolder == "" or self.inputPath == "":
            self.text_field.setText("Namnge folder")
            self.text_field.setStyleSheet("background-color: red;")
            print(self.targetFolder, self.inputPath)
            #self.text_edit.setStyleSheet("color: white;")
        else:
            self.text_field.setText("Sammanställning klar")
            self.text_field.setStyleSheet("background-color: green;")
            #self.text_edit.setStyleSheet("color: white;")
            # Call the function to merge the files
            # merge_files(self.inputPath, self.targetFolder)

    def open_file(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Open File", "", "All Files (*)")
        if file_path:
            with open(file_path, 'r') as file:
                text = file.read()
                self.text_edit.setPlainText(text)
    
    def open_folder(self):
        folder_path = QFileDialog.getExistingDirectory(self, "Open Folder")
        if folder_path:
            # Perform actions with the selected folder path
            self.text_field.setText(folder_path)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = DragDropWidget()
    window.setWindowTitle("Faktura Sammanställare")
    window.setGeometry(100, 100, 400, 300)
    window.show()
    sys.exit(app.exec_())
