import tkinter as tk
import reader
from tkinter import filedialog
from tkinter import messagebox
from docx import Document


class app:
    def __init__(self):

        self.WIDTH = 800
        self.HEIGHT = 300
        self.mainapp = tk.Tk()
        self.new_label = tk.Label(text="Name The New File:", font=("Arial", 12))
        self.new_input = tk.Entry(
            self.mainapp, width=55, font=("Arial", 12), relief="sunken"
        )
        self.words_label = tk.Label(text="Insert Keywords:", font=("Arial", 12))
        self.words_input = tk.Entry(
            self.mainapp, width=55, font=("Arial", 12), relief="sunken"
        )
        self.pages_label = tk.Label(text="Page Number", font=("Arial", 12))
        self.pages_input = tk.Entry(
            self.mainapp, width=55, font=("Arial", 12), relief="sunken"
        )
        self.convert_button = tk.Button(
            text="CONVERT",
            width=55,
            height=3,
            font=("Arial", 17),
            relief="raised",
            command=self.convert,
        )

        self.mainapp.title("PDF Reader")
        self.mainapp.geometry(str(self.WIDTH) + "x" + str(self.HEIGHT))
        self.mainapp.resizable(width="false", height="false")

        self.new_label.pack()
        self.new_label.place(relx=0.02, rely=0.1)

        self.new_input.pack()
        self.new_input.place(relx=0.3, rely=0.1)

        # Insert Key Words

        self.words_label.pack()
        self.words_label.place(relx=0.02, rely=0.2)

        self.words_input.pack()
        self.words_input.place(relx=0.3, rely=0.2)

        # Pages
        self.pages_label.pack()
        self.pages_label.place(relx=0.02, rely=0.3)

        self.pages_input.pack()
        self.pages_input.place(relx=0.3, rely=0.3)

        # Convert Button
        self.convert_button.pack()
        self.convert_button.place(relx=0.05, rely=0.5)

    def get_words(self):
        words = self.words_input.get()
        if words != "":
            return words

    def get_pages(self):
        pages = self.pages_input.get()
        if pages != "":
            try:
                int(self.pages_input.get())
            except:
                tk.messagebox.showwarning("Error", "Not a Number")
            return pages

    def open_file_explorer(self):
        return filedialog.askopenfilename()

    def convert(self):
        with open("words.txt", "r") as f:
            words = f.read()
            words = words.strip(" ")
            words = words + " "
            words = words.split("\n")
        doc = Document()
        text = reader.removing_cite(
            reader.open_PDF(self.open_file_explorer(), self.get_pages())
        )
        reader.important_sentences(text, doc, words)
        name = self.new_input.get() + ".docx"
        print('finished')
        return doc.save(name)

