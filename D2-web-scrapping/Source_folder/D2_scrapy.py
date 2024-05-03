import tkinter as tk
from tkinter import filedialog, messagebox
import threading
from bs4 import BeautifulSoup
import urllib.request
import datetime
import csv

'''
https://stackoverflow.com/questions/9539566/how-can-i-make-portable-python-desktop-application 
For packing app into exe file
'''

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

    def export_csv(self):
        data = self.web_scrap()
        now = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
        filepath = f"{self.path}/{now}_completed_D2_search.csv"
        
        with open(filepath, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(['horse_no', 'index', 'category', 'date', 'document_name', 'view', 'Link'])
            for row in data:
                # assume that the 'document_name' is the fifth column
                # prevent error if the 'document_name' is empty
                if len(row) >= 5:
                    if self.keywords in row[4]:
                        writer.writerow(row)
                else:
                    pass
        print(f"File has been exported to {filepath}")
        
    @staticmethod
    def convert_csv_to_list(csv_file):
        with open(csv_file, mode='r', newline='', encoding='utf-8') as file:
            reader = csv.reader(file)
            # clear empty rows and return only the first column, clear symbol
            col = [row[0].replace(' ', '') for row in reader if row]
            return col  # Read only the first column which is assumed to contain horse numbers

class ScraperThread(threading.Thread):
    def __init__(self, horse_no_file, keywords, path, callback_success, callback_error, update_status):
        super().__init__()
        self.scraper = WebScrapingD2(horse_no_file, keywords, path, update_status)
        self.callback_success = callback_success
        self.callback_error = callback_error
        self.update_status = update_status

    def run(self):
        try:
            self.update_status('Scraping started...')
            self.scraper.export_csv()
            self.callback_success("The file has been saved successfully.")
            self.update_status('Scraping completed successfully.')
        except Exception as e:
            self.callback_error(e)
            self.update_status('Scraping failed.')

class GUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Web Scraping App")
        self.geometry("350x250")

        tk.Label(self, text="Horse No:").grid(row=0, column=0)
        self.input_horse_no = tk.Entry(self)
        self.input_horse_no.grid(row=0, column=1)
        tk.Button(self, text="Horse_No Path", command=self.browse_horse_no).grid(row=0, column=2)

        tk.Label(self, text="Keywords:").grid(row=1, column=0)
        self.input_keywords = tk.Entry(self)
        self.input_keywords.grid(row=1, column=1)

        tk.Label(self, text="Path:").grid(row=2, column=0)
        self.input_path = tk.Entry(self)
        self.input_path.grid(row=2, column=1)
        tk.Button(self, text="Export Path", command=self.browse).grid(row=2, column=2)

        tk.Button(self, text="Start", command=self.start).grid(row=3, column=1)

        # Status bar
        self.status = tk.Label(self, text="", bd=1, relief=tk.SUNKEN, anchor=tk.W)
        self.status.grid(row=8, column=1, columnspan=3, sticky=tk.W+tk.E, rowspan=3)

    def browse_horse_no(self):
        file_path = filedialog.askopenfilename(title="Open File", filetypes=(("CSV Files", "*.csv"),))
        if file_path:
            self.input_horse_no.delete(0, tk.END)
            self.input_horse_no.insert(0, file_path)

    def browse(self):
        file_path = filedialog.askdirectory(title="Select Directory")
        if file_path:
            self.input_path.delete(0, tk.END)
            self.input_path.insert(0, file_path)

    def start(self):
        horse_no_file = self.input_horse_no.get()
        keywords = self.input_keywords.get().lower()
        path = self.input_path.get()
        
        if not all([horse_no_file, keywords, path]):
            messagebox.showwarning("Missing Information", "All fields are required.")
            return
        
        self.thread = ScraperThread(horse_no_file, keywords, path, self.on_finished, self.on_error, self.update_status_bar)
        self.thread.start()

    def update_status_bar(self, message):
        self.status.config(text=message)

    def on_finished(self, message):
        messagebox.showinfo("Success", message)

    def on_error(self, exception):
        messagebox.showerror("Error", f"Failed to scrape and export data: {str(exception)}")

if __name__ == '__main__':
    app = GUI()
    app.mainloop()
