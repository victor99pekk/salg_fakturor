from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from test import iter_folder
from PyQt5.QtCore import *
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
        self.fontError = QFont("Arial", 13)

        #self.button_group = QButtonGroup()
        self.box = QHBoxLayout()
        self.radio_button1 = QRadioButton("Dark-mode", self)
        self.box.addWidget(self.radio_button1)
        #self.button_group.addButton(self.radio_button1)
        # Create radio button 2
        self.radio_button2 = QRadioButton("Light-mode", self)
        self.box.addWidget(self.radio_button2)
        layout.addLayout(self.box)
        #self.button_group.addButton(self.radio_button2)
        self.radio_button1.clicked.connect(self.changeColor)
        self.radio_button2.clicked.connect(self.changeColor)

        self.instruct = QTextEdit(self)
        self.instruct.setFont(font2)
        self.instruct.setPlaceholderText("1. välj input folder som har fakturorna som ska sammanställas, och inget mer\n\n2. Namnge output foldern(namn för foldern där excelfilerna kommer ligga)\n\n3. Klicka på 'Sammanställ, så kommer din output foldern ligga på ditt desktop i 'salg_fakturor'-foldern")
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
        self.textBox.setPlaceholderText("Namnge folder här:     (ex: Januari21)")
        self.textBox.setMaximumHeight(35)
        self.textBox.setFont(font1)
        self.textBox.installEventFilter(self)
        self.textBox.setFocus()

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
        layout.addLayout(targetFileButton)

        layout.addWidget(self.textBox)

        self.setLayout(layout)

        self.settings = QSettings("myapp", "mainwindow")
        self.button_state = self.settings.value("button_state", False, type=bool)
        self.radio_button1.setChecked(self.button_state)
        self.radio_button2.setChecked(not self.button_state)

        self.radio_button1.clicked.connect(self.save_state)
        self.radio_button2.clicked.connect(self.save_state)

        if not self.button_state:
            self.light()

    def save_state(self):
        # Save the state of the button
        self.settings.setValue("button_state", self.button.isChecked())

    def changeColor(self):
        sender = self.sender()
        if sender.text() == "Dark-mode":
            # Dark mode settings
            self.dark()
        else:
            self.light()

    def dark(self):
        self.setStyleSheet("""
            background-color: rgb(30, 30, 30); 
            color: white;
            border: 2px solid gray;  /* Add border to input widgets and buttons */
            border-radius: 5px;  /* Add border radius for a softer look */
            """)
        self.instruct.setStyleSheet("background-color: rgb(170, 170, 170); color: black; border: 2px solid gray; border-radius: 5px;")  # Style for self.instructions
        self.open_button.setStyleSheet("background-color: rgb(190, 90, 190); color: black; border: 2px solid gray; border-radius: 5px;")  # Style for self.open_file_button
        self.textBox.setStyleSheet("background-color: rgb(170, 170, 170); color: black; border: 2px solid gray; border-radius: 5px;")  # Style for self.textBox

    def light(self):
        # Light mode settings
            self.setStyleSheet("""
                background-color: rgb(230, 230, 190); 
                color: black;
                border: 2px solid gray;  /* Add border to input widgets and buttons */
                border-radius: 5px;  /* Add border radius for a softer look */
                """)
            self.instruct.setStyleSheet("background-color: rgb(245, 245, 245); color: black; border: 2px solid gray; border-radius: 5px;")  # Style for self.instructions
            self.textBox.setStyleSheet("background-color: rgb(245, 245, 245); color: black; border: 2px solid gray; border-radius: 5px;")  # Style for self.text_field
            self.open_button.setStyleSheet("background-color: rgb(60, 110, 200); color: black; border: 2px solid gray; border-radius: 5px;")  # Style for self.open_file_button

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
        if self.targetFolder == "" and self.inputPath == "":
            self.instruct.setPlaceholderText("Namnge folder för de sammanställda filerna och välj input folder med fakturorna som ska sammanställas")
            self.text_field.setStyleSheet("background-color: red;")
        elif self.targetFolder == "":
            self.instruct.setPlaceholderText("Du glömde nange foldern för de sammanställda filerna")
            self.text_field.setStyleSheet("background-color: red;")
        elif self.inputPath == "":
            self.instruct.setPlaceholderText("Du glömde välja foldern med fakturor som ska sammanställas")
            self.text_field.setStyleSheet("background-color: red;")
        else:
            list = iter_folder(self.inputPath, self.targetFolder)
            if list:
                message = "Felaktigt format på följande: \n"
                for i in list:
                    message += i + "\n"
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
