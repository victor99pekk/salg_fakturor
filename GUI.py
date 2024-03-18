import os
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import pandas as pd
from test import run
from DataKeeper import DataKeeper
import Place
from WriteToExcel import write

columns_to_keep = ['Datum', 'Tjänst', 'Distrikt', 'Resor (km)', 'Resor (km)', 'Resor (kostnad)', 'Kostnad']


class DragDropWidget(QWidget):
    def __init__(self):
        super().__init__()

        self.targetFolder = ""
        self.inputPath = ""

        # Set up the layout
        layout = QVBoxLayout()
        font1 = QFont("Arial", 20)  # Set font family and size
        font2 = QFont("Arial", 15)

        self.instruct = QTextEdit(self)
        self.instruct.setFont(font2)
        self.instruct.setPlaceholderText("1. välj input folder (folder med fakturor som ska sammanställas)\n2. Namnge output folder(namn för foldern där excelfilerna kommer ligga)\n3. Klicka på 'Sammanställ'")
        self.instruct.setMinimumHeight(100)
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
        self.textBox.setPlaceholderText("Namnge folder:     (ex: Jan21)")
        self.textBox.setMaximumHeight(35)
        self.textBox.setFont(font1)

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

    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls():
            event.accept()
        else:
            event.ignore()

    def dropEvent(self, event):     #currently not being used
        for url in event.mimeData().urls():
            file_path = url.toLocalFile()
            self.inputPath = file_path
    
    def click(self, event):
        self.targetFolder = self.textBox.toPlainText()
        if self.targetFolder == "" or self.inputPath == "":
            self.text_field.setText("Namnge folder")
            self.text_field.setStyleSheet("background-color: red;")
            print(self.targetFolder, self.inputPath)
            #self.text_edit.setStyleSheet("color: white;")
        else:
            #run(self.inputPath, self.targetFolder)
            self.iter_folder(self.inputPath, self.targetFolder)
            self.text_field.setText("Sammanställning klar")
            self.text_field.setStyleSheet("background-color: green;")
            self.textBox.clear()

    def iter_folder(self, folder_path, target_folder):
        #dataKeeper = DataKeeper()
        map = {}
        for place in Place.getPlaces():
            map[place] = pd.DataFrame(columns=columns_to_keep)

        for filename in os.listdir(folder_path):
            file_path = os.path.join(folder_path, filename)
            if os.path.isfile(file_path) and filename.endswith('.xls'):
                #dataKeeper = run(file_path, target_folder, dataKeeper)
                print(file_path)
                run(file_path, map)
        for place in map:
            outputPath = target_folder + "/" + str(place)
            #write(outputPath, dataKeeper.map[place])
            write(outputPath, map[place])


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

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = DragDropWidget()
    window.setWindowTitle("Faktura Sammanställare")
    window.setGeometry(100, 100, 400, 300)
    window.show()
    sys.exit(app.exec_())
