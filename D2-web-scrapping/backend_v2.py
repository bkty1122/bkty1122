from bs4 import BeautifulSoup
import urllib.request
from html.parser import HTMLParser
import datetime
import csv

class WebScrapingD2():
    def __init__(self, horse_no, keywords, path, update_status=None):
        self.horse_no = self.convert_csv_to_list(horse_no)
        self.keywords = str.lower(keywords)
        self.path = path
        self.update_status = update_status

    def web_scrap(self):
        url_link = "https://edpapp.corp.hkjc.com:8243/drs_cr/src/vdislist.jsp?keyword="
        url_link_end = "&year=&category="
        data_unclean = []
        for i in self.horse_no:
            if self.update_status:
                self.update_status(f'Scraping: Horse No {i}')
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
        # parser = HTMLParser()
        # for i in self.horse_no:
        #     if self.update_status:
        #         self.update_status(f'Scraping: Horse No {i}')
        #     url_link_full = urllib.request.urlopen(url_link + i + url_link_end)
        #     tree = BeautifulSoup(url_link_full, "html.parser")
        #     tab_tag = tree.select("table")[1]
        #     tab_data = [[str.lower(item.text) for item in row_data.select("td")] for row_data in tab_tag.select("tr")]
        #     for j in range(1, len(tab_data)):
        #         href = tab_tag.select("tr")[j].select("td")[-1].select("a")[0].get("href")
        #         tab_data[j].append(href)
        #         tab_data[j].insert(0, i)
        #     data_unclean.extend(tab_data)
        #     print(f'Horse No {i} has successfully added to the list.')    
        # return data_unclean

    def export_csv(self):
        data = self.web_scrap()
        now = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
        filepath = f"{self.path}/{now}_completed_D2_search.csv"
        
        with open(filepath, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(['horse_no', 'index', 'category', 'date', 'document_name', 'view', 'Link'])
            for row in data:
                if self.keywords in row[4]:  # Assuming 'document_name' is the fifth element
                    writer.writerow(row)
        
        print(f"File has been exported to {filepath}")
        
    @staticmethod
    def convert_csv_to_list(csv_file):
        with open(csv_file, mode='r', newline='', encoding='utf-8') as file:
            reader = csv.reader(file)
            return [row[0] for row in reader if row]  # Read only the first column which is assumed to contain horse numbers