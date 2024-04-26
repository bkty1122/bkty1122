import tkinter as tk
from tkinter import filedialog, messagebox
from backend import WebScrapingD2
import threading

'''
https://stackoverflow.com/questions/9539566/how-can-i-make-portable-python-desktop-application 
For packing app into exe file
'''


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
        
        # add logo to the app
        self.logo = tk.PhotoImage(file="icon.png")
        self.iconphoto(False, self.logo)

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
        self.status.grid(row=5, column=0, columnspan=3, sticky=tk.W+tk.E)

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