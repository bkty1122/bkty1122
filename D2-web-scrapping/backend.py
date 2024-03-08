from bs4 import BeautifulSoup
import pandas as pd
import urllib.request
import datetime
import csv

csv_file_path = 'Horse_No.csv'

path = 'C:/Users/beckytykwok/Documents/Python/D2-web-scrapping-mini-program/'

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
        return print(f"File has successfully exported to {path}")
    @staticmethod
    def convert_csv_to_list(csv_file):
        with open(csv_file, 'r') as file:
            csv_reader = csv.reader(file)
            data_list = []
            for row in csv_reader:
                data_list.extend(row)
            return data_list


# Test
web_scrapping_d2(csv_file_path, 'CT Examination', path).export_csv()