import sys
import PyQt5.QtWidgets as QtWidgets
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QThread, pyqtSignal
from backend import WebScrapingD2

class ScraperThread(QThread):
    finished = pyqtSignal(str)
    error = pyqtSignal(Exception)

    def __init__(self, horse_no_file, keywords, path):
        super().__init__()
        self.scraper = WebScrapingD2(horse_no_file, keywords, path)

    def run(self):
        try:
            self.scraper.export_csv()
            self.finished.emit("The file has been saved successfully.")
        except Exception as e:
            self.error.emit(e)

class GUI(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        layout = QtWidgets.QFormLayout()
        self.setLayout(layout)

        self.label_horse_no = QtWidgets.QLabel("Horse No:")
        self.label_keywords = QtWidgets.QLabel("Keywords:")
        self.label_path = QtWidgets.QLabel("Path:")
        
        self.input_horse_no = QtWidgets.QLineEdit()
        self.input_keywords = QtWidgets.QLineEdit()
        self.input_path = QtWidgets.QLineEdit()

        self.button_browse_horse_no = QtWidgets.QPushButton("Horse_No Path")
        self.button_browse = QtWidgets.QPushButton("Export Path")
        self.button_start = QtWidgets.QPushButton("Start")

        layout.addRow(self.label_horse_no, self.input_horse_no)
        layout.addRow(self.button_browse_horse_no)
        layout.addRow(self.label_keywords, self.input_keywords)
        layout.addRow(self.label_path, self.input_path)
        layout.addRow(self.button_browse)
        layout.addRow(self.button_start)

        self.button_browse.clicked.connect(self.browse)
        self.button_browse_horse_no.clicked.connect(self.browse_horse_no)
        self.button_start.clicked.connect(self.start)
        
        self.setWindowTitle("Web Scraping App")
        self.setWindowIcon(QIcon('icon.ico'))
        self.setGeometry(300, 300, 350, 200)
        self.show()

    def browse_horse_no(self):
        file_path, _ = QtWidgets.QFileDialog.getOpenFileName(self, "Open File", "", "CSV Files (*.csv)")
        if file_path:
            self.input_horse_no.setText(file_path)

    def browse(self):
        file_path = QtWidgets.QFileDialog.getExistingDirectory(self, "Select Directory")
        if file_path:
            self.input_path.setText(file_path)

    def start(self):
        horse_no_file = self.input_horse_no.text()
        keywords = self.input_keywords.text().lower()
        path = self.input_path.text()
        
        if not all([horse_no_file, keywords, path]):
            QtWidgets.QMessageBox.warning(self, "Missing Information", "All fields are required.")
            return
        
        self.thread = ScraperThread(horse_no_file, keywords, path)
        self.thread.finished.connect(self.on_finished)
        self.thread.error.connect(self.on_error)
        self.thread.start()

    def on_finished(self, message):
        QtWidgets.QMessageBox.information(self, "Success", message)

    def on_error(self, exception):
        QtWidgets.QMessageBox.critical(self, "Error", f"Failed to scrape and export data: {str(exception)}")


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    ex = GUI()
    sys.exit(app.exec_())