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
from bs4 import BeautifulSoup
import pandas as pd
import urllib.request
import datetime
import csv

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

class web_scrapping_d2():
    def __init__(self, horse_no, keywords ,path):
        self.horse_no = self.convert_csv_to_list(horse_no) # user select list of horse_no from csv
        self.keywords = str.lower(keywords)
        self.path = path
    def web_scrap(self):
        url_link = "https://edpapp.corp.hkjc.com:8243/drs_cr/src/vdislist.jsp?keyword="
        url_link_end = "&year=&category="
        data_unclean = []
        # Loop through the list of horse_no, and return the data_unclean with beautifulsoup
        for i in self.horse_no:
            url_link_full = urllib.request.urlopen(url_link + i + url_link_end)
            tree = BeautifulSoup(url_link_full, "lxml")
            tab_tag = tree.select("table")[1]
            tab_data = [[str.lower(item.text) for item in row_data.select("td")] for row_data in tab_tag.select("tr")]
            for j in range(1, len(tab_data)):
                href = tab_tag.select("tr")[j].select("td")[-1].select("a")[0].get("href")
                tab_data[j].append(href)
                tab_data[j].insert(0, i)
            data_unclean.extend(tab_data)
            # data_unclean.pop(0)
            print(f'Horse No {i} has successfully added to the list.')
        return data_unclean
    def export_csv(self):
        data_unclean = self.web_scrap()
        data_unclean
        date_time = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
        df_data_unclean = pd.DataFrame(data_unclean, columns = ['horse_no','index', 'category', 'date','document_name','view','Link'])
        df_data_unclean = df_data_unclean.fillna(value= "N/A")
        df_data_clean = df_data_unclean.loc[df_data_unclean['document_name'].str.contains(self.keywords)]
        df_data_clean.to_csv(self.path + date_time + '_completed_D2_search.csv', header = ['horse_no','index', 'category', 'date','document_name','view','Link'], index=False)
        return print(f"File has successfully exported to {self.path}")
    @staticmethod
    def convert_csv_to_list(csv_file):
        with open(csv_file, 'r') as file:
            csv_reader = csv.reader(file)
            data_list = []
            for row in csv_reader:
                data_list.extend(row)
            return data_list


if __name__ == '__main__':
    app = pyqt5.QApplication(sys.argv)
    ex = GUI()
    sys.exit(app.exec_())