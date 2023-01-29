__author__ = "Süleyman Bozkurt"
__version__ = "v2.2"
__maintainer__ = "Süleyman Bozkurt"
__email__ = "sbozkurt.mbg@gmail.com"
__date__ = '28.01.2023'
__update__ = '29.01.2023'

from Bio import Medline
from Bio import Entrez
Entrez.email = "sbozkurt.mbg@gmail.com" # email me for any questions
# if there is problem here, assign multiple random emails
import glob
import PyPDF2
import os
import shutil
from tkinter.font import Font
from tkinter.scrolledtext import ScrolledText
from threading import Thread
from tkinter import messagebox
########################################################################
from tkinter import ttk
import webbrowser
import tkinter as tk
from tkinter import *
import tkinter.messagebox
import tkinter.filedialog
import traceback
from tkinter.ttk import Style

class HowTo(ttk.Frame):
    def __init__(self, parent):
        s = Style()
        s.configure('My.TFrame', background='#f6fffe')
        ttk.Frame.__init__(self, parent, style="My.TFrame")

        self.font = Font(family="Times New Roman", size=16)
        from PIL import ImageTk, Image
        img = Image.open("files/description.png")
        img.thumbnail((750, 750))
        img = ImageTk.PhotoImage(img)
        panel = Label(self, image=img)
        panel.image = img
        panel.place(x=100, y=20)

        label2 = Label(self, text="Video description: ", font=self.font).place(x=120, y=510)

        self.clickme = Button(self, text='https://www.youtube.com/watch?v=Zc78L8_r6Cg', fg='#d80000',
                                font=Font(family="Times New Roman", size=18, weight='bold'), command=self.callback)
        self.clickme.place(x=300, y=500)

    def callback(self):
        webbrowser.open_new('https://www.youtube.com/watch?v=Zc78L8_r6Cg')

class about(ttk.Frame):

    def __init__(self, parent):

        textAboutMe = """
        Hello! My name is Süleyman Bozkurt and I am a senior PhD student in the field of biochemistry. 
        My research focuses on mitochondrial protein import and proteomics, 
        and I am particularly interested in understanding how it's impact on cellular function.
        In addition to my research, I am also interested in building my own apps and sharing them with others. 
        I am a huge fan of Python and enjoy using R for visualizations. I believe that these tools 
        can help make complex scientific data more accessible and easier to understand.
        I am passionate about using my skills and knowledge to make a positive impact in the scientific community. 
        I am always looking for new ways to learn and grow, and I enjoy collaborating with others 
        to find innovative solutions to complex problems.
        I hope this gives you a sense of who I am and what I am interested in. 
        If you have any questions or would like to learn more about my work, please don't hesitate to contact me.
        """

        ttk.Frame.__init__(self, parent)
        self.font = Font(family="Times New Roman", size=20)
        label2 = Label(self, text="")
        label2.grid(padx=1000, pady=800)
        label2 = Label(self, text="ABOUT ME!",font=self.font)
        label2.place(x=420, y=35)

        label = tk.Label(self, font = Font(family="Times New Roman", size=14),
                         text = textAboutMe,
                         )

        label.place(x=40, y=75)
        from PIL import ImageTk, Image
        # Open the image using PIL
        self.github_logo = Image.open("./files/github.png")
        self.linkedin_logo = Image.open("./files/linkedin.png")
        self.twitter_logo = Image.open("./files/twitter.png")
        self.ibc2_logo = Image.open("./files/ibc2logo.png")

        # Resize the image
        self.github_logo = self.github_logo.resize((100, 100), resample=Image.Resampling.LANCZOS)
        self.linkedin_logo = self.linkedin_logo.resize((100, 100), resample=Image.Resampling.LANCZOS)
        self.twitter_logo = self.twitter_logo.resize((100, 100), resample=Image.Resampling.LANCZOS)
        self.ibc2_logo = self.ibc2_logo.resize((100, 100), resample=Image.Resampling.LANCZOS)

        # Create a PhotoImage object from the resized image
        self.github_logo = ImageTk.PhotoImage(self.github_logo)
        self.linkedin_logo = ImageTk.PhotoImage(self.linkedin_logo)
        self.twitter_logo = ImageTk.PhotoImage(self.twitter_logo)
        self.ibc2_logo = ImageTk.PhotoImage(self.ibc2_logo)

        # Create clickable link to your website
        website_link = tk.Label(self, image=self.ibc2_logo, text="Website", fg="blue", cursor="hand2")
        website_link.place(x=220, y=370)
        website_link.bind("<Button-1>", self.open_website)

        # Create clickable link to your GitHub page with logo
        github_link = tk.Button(self, image=self.github_logo, cursor="hand2", bd=0, highlightthickness=0,
                                activebackground="white")
        github_link.place(x=370, y=370)
        github_link.bind("<Button-1>", self.open_github)

        # Create clickable link to your LinkedIn profile with logo
        linkedin_link = tk.Button(self, image=self.linkedin_logo, cursor="hand2", bd=0, highlightthickness=0,
                                  activebackground="white")
        linkedin_link.place(x=520, y=370)
        linkedin_link.bind("<Button-1>", self.open_linkedin)

        # Create clickable link to your Twitter profile with logo
        twitter_link = tk.Button(self, image=self.twitter_logo, cursor="hand2", bd=0, highlightthickness=0,
                                 activebackground="white")
        twitter_link.place(x=670, y=370)
        twitter_link.bind("<Button-1>", self.open_twitter)

        label2 = Label(self, text="You can reach me one of these profiles!",font=self.font)
        label2.place(x=270, y=500)

    def open_github(self, event):
        # Open your GitHub page in the default web browser
        import webbrowser
        webbrowser.open("https://github.com/science64")

    def open_website(self, event):
        # Open your website in the default web browser
        import webbrowser
        webbrowser.open("https://biochem2.com/people/bozkurt-sueleyman")

    def open_linkedin(self, event):
        # Open your LinkedIn profile in the default web browser
        import webbrowser
        webbrowser.open("https://www.linkedin.com/in/s%C3%BCleyman-bozkurt-51080b60/")

    def open_twitter(self, event):
        # Open your LinkedIn profile in the default web browser
        import webbrowser
        webbrowser.open("https://twitter.com/science_mbg")

    def callback(self, url):
        webbrowser.open_new(url)

class support(ttk.Frame):
    def __init__(self, parent):
        ttk.Frame.__init__(self, parent)
        self.font = Font(family="Times New Roman", size=16)
        from PIL import ImageTk, Image
        img = Image.open("files/buymecofee.jpeg")
        img = img.resize((800, 400), Image.Resampling.LANCZOS)
        img = ImageTk.PhotoImage(img)
        panel = Label(self, image=img)
        panel.image = img
        panel.place(x=80, y=20, width=800, height=400)

        label2 = Label(self, text="You can support by buying a coffee ☕️ here ", font=self.font)
        label2.grid(padx=1000, pady=800)
        label2.place(x=300, y=450)

        self.clickme = Button(self, text='https://www.buymeacoffee.com/science64', fg='black', bg='#FFC19E',
                                font=Font(family="Times New Roman", size=18, weight='bold'), command=self.callback)
        self.clickme.place(x=270, y=500)

    def callback(self):
        webbrowser.open_new('https://www.buymeacoffee.com/science64')

class fomatter(ttk.Frame):
    def __init__(self, parent):
        # s = Style()
        # s.configure('My2.TFrame', background='#d3f5d3')
        ttk.Frame.__init__(self, parent)

        self.selected_folder = ''
        self.outputPath = ''

        self.font = Font(family="Times New Roman", size=16)
        self.pdf_label = tk.Label(self, text="Select Folder or a PDF file:", font=self.font)
        self.pdf_label.place(x=90, y=30)

        self.pdf_button = tk.Button(self, text="Browse",fg='black', bg='#b4e67e',
                                font=Font(family="Times New Roman", size=18, weight='bold'), command=self.select_pdf).place(x=340, y=21)

        self.pdf_path_label = tk.Label(self, text="", font=self.font)
        self.pdf_path_label.place(x=450, y=30)


        Label(self, text="Folder Name: ", font=self.font).place(x=90, y=110)
        self.outputbox = Entry(self, font=self.font, bd=2)
        self.outputbox.place(x=230, y=100, width=400, height=50)
        self.output_button = tk.Button(self, text="Save Location", fg='black', bg='#fdbd7f',
                                font=Font(family="Times New Roman", size=18, weight='bold'), command=self.select_output_folder).place(x=655, y=100)

        Label(self, text="Choose your style: ", font=self.font).place(x=90, y=181)
        self.articleName1 = StringVar()
        self.articleName1.set("Title")  # default value
        self.articleName2 = StringVar()
        self.articleName2.set("None")  # default value
        self.articleName3 = StringVar()
        self.articleName3.set("None")  # default value
        self.articleName4 = StringVar()
        self.articleName4.set("None")  # default value
        self.articleName_formats = [
            "None", # for ignoring
            "First author",
            "All authors",
            "Year",
            "Title",
            "Journal"
        ]  # These are supported, can be added more later!

        OptionMenu(self, self.articleName1, *self.articleName_formats).place(x=270, y=180)
        OptionMenu(self, self.articleName2, *self.articleName_formats).place(x=395, y=180)
        OptionMenu(self, self.articleName3, *self.articleName_formats).place(x=520, y=180)
        OptionMenu(self, self.articleName4, *self.articleName_formats).place(x=645, y=180)

        self.statusbar = ScrolledText(self, state='disabled')
        self.statusbar.place(x=170, y=230, width=650, height=250)

        self.runbutton = Button(self, text='Start', fg='black', bg='#c1f3ff',
                                font=Font(family="Times New Roman", size=18, weight='bold'), command=self.runbutton_click, state=tk.DISABLED)
        self.runbutton.place(x=300, y=500, width=145, height=50)

        self.openbutton = Button(self, text='Open', fg='black', bg='#ffac99',
                                font=Font(family="Times New Roman", size=18, weight='bold'), command=self.open_click, state=tk.DISABLED)
        self.openbutton.place(x=505, y=500, width=145, height=50)

    def select_pdf(self):
        try:
            choice = tkinter.messagebox.askquestion("Choice",
                                                    "Select a single PDF file (YES) or a whole folder (NO)?")
            if choice == 'yes':
                self.pdf_path = tkinter.filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")])
            elif choice == 'no':
                self.pdf_path = tkinter.filedialog.askdirectory()

            if not self.pdf_path:
                tkinter.messagebox.showerror("Error", "No file or folder selected.")
                return
            else:
                self.runbutton.config(state=tk.NORMAL)
                head, tail = os.path.split(self.pdf_path)
                self.pdf_path_label.config(text=".../" + tail)

        except Exception as e:
            print(e)
            # Display an error message in a pop-up window
            tkinter.messagebox.showerror("Error",
                                         "An error occurred while selecting the PDF file.\n\n" + traceback.format_exc())

    def select_output_folder(self):

        try:
            self.selected_folder = tkinter.filedialog.askdirectory()
            if self.selected_folder:
                self.outputbox.delete(0, END)
                self.outputbox.insert(0, self.selected_folder)
        except Exception as e:
            print(e)
            tkinter.messagebox.showerror("Error",
                                         "An error occurred while selecting the output folder.\n\n" + traceback.format_exc())

    def Message(self, title, message):
        messagebox.showinfo(title=title, message=message)

    def update_status_box(self, text, decision):
        if decision:
            self.statusbar.configure(state='normal')
            lines = self.statusbar.get("1.0", "end-1c").splitlines()
            if lines:
                self.statusbar.delete("1.0", "end")
                self.statusbar.insert("1.0", '\n'.join(lines[:-1]))
            self.statusbar.insert(END, text)
            self.statusbar.see(END)
            self.statusbar.configure(state='disabled')
        else:
            self.statusbar.configure(state='normal')
            self.statusbar.insert(END, text)
            self.statusbar.see(END)
            self.statusbar.configure(state='disabled')

    def clear_status_box(self):
        self.statusbar.configure(state='normal')
        self.statusbar.delete(1.0, END)
        self.statusbar.see(END)
        self.statusbar.configure(state='disabled')

    def open_click(self):
        try:
            os.startfile(self.outputPath) # Now I changed it to open the folder instead.
        except:
            self.outputPath = str(self.outputbox.get())
            try:
                os.startfile(self.outputPath)
            except:
                self.Message('Warning', 'No folder name given!')
                return 0

    def runbutton_click(self):
        self.runbutton.config(state=tk.DISABLED)
        self.clear_status_box()
        self.outputPath = self.outputbox.get()

        if self.outputPath != '':
            if not os.path.isabs(self.outputPath):
                try:
                    self.pathLocation = f'~/Desktop/{self.outputPath}/' # for letting the user know but necessary
                    path = os.path.expanduser(f'~/Desktop/{self.outputPath}/')
                    if not os.path.exists(path):
                        os.makedirs(path)
                    self.outputPath = path # final path created!
                except:
                    pass
        else:
            self.runbutton.config(state=tk.NORMAL)
            tkinter.messagebox.showerror("Error", "Please provide save location!")
            return

        self.update_status_box('\n\t\t >> :: Article Formatter Started! :: <<\n', decision=False)
        self.update_status_box('\n------------------------------------------------------------------------------\n', decision=False)

        self.update_status_box(f'\n\t Chosen file or folder: {self.pdf_path}\n', decision=False)
        # self.update_status_box(f'\n\t Articles will be renamed in: {self.pathLocation}\n')

        formatChosen = ''
        orderList = ['None', 'Perfect H.', 'Mrs Perfect H. and Mr Perfect S.', '2023', 'One ring to multiplex them all', 'Nature Publishing']

        self.order = []
        selected_value_1 = self.articleName1.get()
        index_number_1 = self.articleName_formats.index(selected_value_1)
        selected_value_2 = self.articleName2.get()
        index_number_2 = self.articleName_formats.index(selected_value_2)
        selected_value_3 = self.articleName3.get()
        index_number_3 = self.articleName_formats.index(selected_value_3)
        selected_value_4 = self.articleName4.get()
        index_number_4 = self.articleName_formats.index(selected_value_4)
        self.order.append(index_number_1)
        self.order.append(index_number_2)
        self.order.append(index_number_3)
        self.order.append(index_number_4)

        for i in self.order:
            if i != 0:
                formatChosen += f'{orderList[i]}_'

        formatChosen = formatChosen[:-1] + ".pdf"

        self.update_status_box(f'\n\t Example Format: {formatChosen}\n', decision=False)

        self.myThread = Thread(target=self.maindecision)
        self.myThread.daemon = True
        self.myThread.start()
        root.after(1000, self.check_main_thread)

    def check_main_thread(self):
        root.update()
        if self.myThread.is_alive():
            root.after(1000, self.check_main_thread)
        else:
            self.x = True

    def maindecision(self):
        try:
            self.engine(self.pdf_path, self.outputPath, self.order)
            self.update_status_box('\n\t\t\t >> :: Complete! :: <<\n', decision=False)
            self.update_status_box('\n------------------------------------------------------------------------------\n', decision=False)
            self.Message('Complete', '.:: Reformatting Complete! ::.')
            self.openbutton.config(state=tk.NORMAL)
            self.runbutton.config(state=tk.NORMAL)
        except Exception as e:
            print(e)
            tkinter.messagebox.showerror("Error",
                                         "Please report the error. Error:\n\n" + traceback.format_exc())
            self.update_status_box('\n\t\t\t >> :: Error! :: <<\n', decision=False)

    def pubmed(self, searchTerm):
            status = False
            title = 'None'
            publishedDate = 'None'
            fullAuthorList = ['None']
            publishedJournal = 'None'

            try:
                handle = Entrez.esearch(db="pubmed",
                                        term=searchTerm)
                record = Entrez.read(handle)
                IDList = record['IdList']

            except Exception as e:
                print(e)
                return status, title, publishedDate, fullAuthorList, publishedJournal # nothing found!

            for pmid in IDList:
                handle = Entrez.efetch(db="pubmed", id=pmid, rettype="medline", retmode="text")
                records = Medline.parse(handle)
                records = list(records)
                for record in records:
                    title = str(record.get("TI", "?"))
                    if '.' == title[-1]:
                        title = title[:-1]
                    fullAuthorList = record.get("AU", "?")
                    publishedJournal = str(record.get("JT", "?"))

                    if publishedJournal == '':
                        publishedJournal = record.get("TA", "?")

                    publishedDate = record.get("EDAT", "?").split('/')[0]

                if len(IDList) != 1:
                    if '.' == str(searchTerm[-1]):
                        searchTerm = searchTerm[:-1]
                    if str(title).lower() == str(searchTerm).lower():
                        status = True

                        return status, title, publishedDate, fullAuthorList, publishedJournal
                else:
                    status = True
                    return status, title, publishedDate, fullAuthorList, publishedJournal

            return status, title, publishedDate, fullAuthorList, publishedJournal

    def engine(self, pathFolder, outputPath, order):

        pdfFiles = []
        forbidden_chars = '<>:"\?/*|'
        if '.pdf' not in pathFolder:
            pdfFiles = glob.glob(f'{pathFolder}/*.pdf')
        else:
            pdfFiles.append(pathFolder)

        num = 1
        for pdf in pdfFiles:
            head, tail = os.path.split(pdf)
            try:
                self.update_status_box(f'\n\t {num}. Renaming: {tail}...\n', decision=False)

                file = open(pdf, 'rb')

                # creating a pdf reader object
                reader = PyPDF2.PdfReader(file)

                info = reader.metadata
                title = str(info.title)

                fullAuthors = 'None'

                status, title, publishedDate, fullAuthorList, publishedJournal = self.pubmed(title)

                if status:
                    creationdate = publishedDate
                    fullAuthors = ", ".join(w for w in fullAuthorList)
                    author = str(fullAuthorList[0])
                else:
                    title = str(info.title)
                    creationdate = str(info['/CreationDate']).split(':')[1][:4]

                    author = str(info.author)
                    if author == '':
                        author = str(info.creator)
                        if author == '':
                            author = 'None'

                if '.' in str(title[-1]):
                    title = title[:-1]

                for fb in forbidden_chars:
                    title = title.replace(fb, " ")
                    author = author.replace(fb, " ")
                    fullAuthors = fullAuthors.replace(fb, " ")

                file.close()

                try:
                    isExist = os.path.exists(outputPath)
                    if not isExist:
                        # Create a new directory because it does not exist
                        os.makedirs(outputPath)
                except:
                    pass

                # newPDF_name = f'{author}_{creationdate}_{title}.pdf'

                orderList = ['None', author, fullAuthors, creationdate, title, publishedJournal]

                newPDF_name = ""
                for i in order:
                    if i != 0:
                        newPDF_name += f'{orderList[i]}_'
                newPDF_name = newPDF_name[:-1] + ".pdf"

                #newPDF_name = f'{orderList[order[0]]}_{orderList[order[1]]}_{orderList[order[2]]}_{orderList[order[3]]}.pdf'
                # print(newPDF_name)
                try:
                    shutil.copy(pdf, f'{outputPath}/{newPDF_name}')
                except shutil.SameFileError:
                    pass

                self.update_status_box(f'\n\t {num}. Renaming: {tail} Success!\n', decision=True)
            except Exception as e:
                self.update_status_box(f'\n\t {num}. Renaming: {tail} Fail!\n', decision=True)

            num += 1

class MyWindow():

    def __init__(self, root):
        self.root = root
        self.notebook = ttk.Notebook(self.root)

        self.notebook.pack(expand=1, fill="both")
        self.fomatterFrame = fomatter(self.notebook)

        self.fomatterFrame.bind("<<NotebookTabChanged>>", self.on_tab_selected)

        self.notebook.add(self.fomatterFrame, text="PDF Formatter")

        self.HowToFrame = HowTo(self.notebook)
        self.notebook.add(self.HowToFrame, text="How It Works")

        self.aboutFrame = about(self.notebook)
        self.notebook.add(self.aboutFrame, text="About")

        self.supportFrame = support(self.notebook)
        self.notebook.add(self.supportFrame, text="Support")

        #self.notebook.grid()
    def on_tab_selected(self):
        selected_tab = self.widget.select()
        tab_text = self.widget.tab(selected_tab, "text")

if __name__ == '__main__':
    root = Tk()
    root.title("Article Formatter v2.2 @2023", )
    root.geometry("960x600+480+250")
    root.resizable(0, 0)
    root.wm_iconbitmap('./files/icon.ico')
    MyWindow(root)
    root.mainloop()