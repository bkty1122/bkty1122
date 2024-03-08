'''
Use library PYQT5 from module qtpy to make a user interface for the web scrapping program
Logic of the program:
1. User input the keywords of document
2. User select the path for intrepreting horse_no csv file
3. User select the path for exporting the result file
3. User click the start button to start the web scrapping
4. The program will run the web scrapping program
5. The program will save the file to the selected path
'''
import sys
import PyQt5.QtWidgets as pyqt5
from backend import web_scrapping_d2

# sys.path.insert(0, "./D2-web-scrapping/lib/python3.10/site-packages")

class GUI(pyqt5.QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        # Set the layout
        layout = pyqt5.QFormLayout()
        self.setLayout(layout)
        # Set the label
        self.label_horse_no = pyqt5.QLabel("Horse No:")
        self.label_keywords = pyqt5.QLabel("Keywords:")
        self.label_path = pyqt5.QLabel("Path:")
        # Set the input
        self.input_horse_no = pyqt5.QLineEdit()
        self.input_keywords = pyqt5.QLineEdit()
        self.input_path = pyqt5.QLineEdit()
        # Set the button
        self.button_browse_horse_no = pyqt5.QPushButton("Horse_No Path")
        self.button_browse = pyqt5.QPushButton("Export Path")
        self.button_start = pyqt5.QPushButton("Start")
        # Add the label and input to the layout
        layout.addRow(self.label_horse_no, self.input_horse_no)
        # add button next to input_horse_no, adjust the layout
        layout.addRow(self.button_browse_horse_no)
        layout.addRow(self.label_keywords, self.input_keywords)
        layout.addRow(self.label_path, self.input_path)
        # add button next to input_path
        layout.addRow(self.button_browse)
        layout.addRow(self.button_start)
        # Set the button action
        self.button_browse.clicked.connect(self.browse)
        self.button_browse_horse_no.clicked.connect(self.browse_horse_no)
        self.button_start.clicked.connect(self.start)
        # Set the window
        self.setWindowTitle("Web Scrapping D2")
        self.setGeometry(300, 300, 300, 150)
        self.show()
    def browse_horse_no(self):
        # Open the file dialog
        file_path = pyqt5.QFileDialog.getOpenFileName(self, "Open File", "", "CSV Files (*.csv)")
        self.input_horse_no.setText(file_path[0])
    def browse(self):
        # Open the file dialog
        file_path = pyqt5.QFileDialog.getExistingDirectory(self, "Select Directory")
        self.input_path.setText(file_path)
    def start(self):
        # Get the input from the user
        horse_no = self.input_horse_no.text()
        keywords = self.input_keywords.text()
        path = self.input_path.text()
        # Run the web scrapping program
        web_scrapping_d2(horse_no, keywords, path).export_csv()
        # Show the message box
        pyqt5.QMessageBox.about(self, "Message", "The file has been saved to the selected path.")
        
if __name__ == '__main__':
    app = pyqt5.QApplication(sys.argv)
    ex = GUI()
    sys.exit(app.exec_())