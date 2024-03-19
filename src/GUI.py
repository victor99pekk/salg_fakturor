from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from test import iter_folder
from PyQt5.QtCore import Qt, QEvent
import Place as Place

class DragDropWidget(QWidget):
    def __init__(self):
        super().__init__()

        self.targetFolder = ""
        self.inputPath = ""

        # Set up the layout
        layout = QVBoxLayout()
        font1 = QFont("Arial", 20)  # Set font family and size
        font2 = QFont("Arial", 15,)
        self.fontError = QFont("Arial", 11)

        self.instruct = QTextEdit(self)
        self.instruct.setFont(font2)
        self.instruct.setPlaceholderText("1. välj input folder (folder med fakturor som ska sammanställas)\n2. Namnge output folder(namn för foldern där excelfilerna kommer ligga)\n3. Klicka på 'Sammanställ'")
        self.instruct.setMinimumHeight(200)
        self.instruct.setReadOnly(True)
        layout.addWidget(self.instruct)

        # Create a QLabel to act as the drag-and-drop area
        self.folder_label = QTextEdit(self)
        self.folder_label.setFont(font2)
        self.folder_label.setPlaceholderText("Välj input folder ->")
        self.folder_label.setMaximumHeight(35)
        self.folder_label.setMaximumWidth(200)
        self.folder_label.setReadOnly(True)

        self.textBox = QTextEdit(self)
        self.textBox.setAcceptDrops(True)
        self.textBox.setPlaceholderText("Namnge folder:     (ex: Januari21)")
        self.textBox.setMaximumHeight(35)
        self.textBox.setFont(font1)
        self.textBox.installEventFilter(self)

        self.button = QPushButton("Sammanställ")
        self.button.setFont(font2)
        self.button.setMaximumHeight(35)
        self.button.setMaximumWidth(110)
        self.button.setStyleSheet("background-color: green;")
        self.button.clicked.connect(self.click)

        self.text_field = QLineEdit()
        self.text_field.setReadOnly(True)
        self.text_field.setFont(font1)
        self.text_field.setPlaceholderText("")
        self.text_field.setMaximumHeight(40)
        self.text_field.setMaximumWidth(220)

        # error message if wrong format
        self.error = QLineEdit()
        self.error.setReadOnly(True)
        self.error.setFont(font1)
        self.error.setPlaceholderText("")
        self.error.setMaximumHeight(300)
        self.error.setMaximumWidth(360)
        self.error.setStyleSheet("background-color: white; color: black;")

        self.open_button = QPushButton("Folder")
        self.open_button.clicked.connect(self.open_folder)

        inputFileButton = QHBoxLayout()
        inputFileButton.addWidget(self.folder_label)
        inputFileButton.addWidget(self.open_button)
        layout.addLayout(inputFileButton)

        targetFileButton = QHBoxLayout()
        targetFileButton.addWidget(self.button)
        targetFileButton.addWidget(self.text_field)
        layout.addWidget(self.open_button)
        layout.addWidget(self.error)
        layout.addLayout(targetFileButton)

        layout.addWidget(self.textBox)

        self.setLayout(layout)
    
    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Return or event.key() == Qt.Key_Enter:
            print("Enter key pressed")
            self.click()
    def eventFilter(self, obj, event):
        if obj is self.textBox and event.type() == QEvent.KeyPress and (event.key() == Qt.Key_Return or event.key() == Qt.Key_Enter):
            self.button.click()
            return True
        return super().eventFilter(obj, event)

    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls():
            event.accept()
        else:
            event.ignore()

    def dropEvent(self, event):     #currently not being used
        for url in event.mimeData().urls():
            file_path = url.toLocalFile()
            self.inputPath = file_path
    
    def click(self):
        self.targetFolder = self.textBox.toPlainText()
        if self.targetFolder == "" or self.inputPath == "":
            self.text_field.setText("Namnge folder")
            self.text_field.setStyleSheet("background-color: red;")
            #print(self.targetFolder, self.inputPath)
        else:
            list = iter_folder(self.inputPath, self.targetFolder)
            if list:
                message = "Felaktigt format på följande: \n"
                for i in list:
                    message += i + "\n"
                #self.error.setText(message)
                self.instruct.setFont(self.fontError)
                self.instruct.setPlaceholderText(message)
                self.text_field.setStyleSheet("background-color: red;")
                self.text_field.setText("programmet kördes inte")
            else:
                self.text_field.setText("Sammanställning klar")
                self.text_field.setStyleSheet("background-color: green;")
            self.textBox.clear()

    def open_file(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Open File", "", "All Files (*)")
        if file_path:
            with open(file_path, 'r') as file:
                text = file.read()
                self.text_edit.setPlainText(text)
    
    def open_folder(self):
        folder_path = QFileDialog.getExistingDirectory(self, "Open Folder")
        if folder_path:
            self.folder_label.setText("Vald folder: " + folder_path.split("/")[-1])
            self.folder_label.setStyleSheet("background-color: green;")
            self.inputPath = folder_path
