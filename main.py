from tkinter import filedialog
import tkinter as tk
from sph import *
from element import *
import platform

class tk_main_window():
    def __init__(self):
        self.root = tk.Tk()
        if platform.system == "Windows" or platform.system == "Linux":
            self.root.title("SPHUI")
            self.sph_arg = sph_arg()
            self.add_init_page()
            self.add_setting_page()
            self.add_help_page()
            self.add_menu()
            self.page_list = [self.init_page,self.setting_page,self.help_page]
            self.page_head = 0
            self.show_init()
        else:
            tk.messagebox.showwarning(title="Fuck Mac OS!",message="Fuck Mac OS!\nTk in MAC is a SHIT!")
            exit()
    def add_init_page(self):
        self.init_page = tk_page_element(self.root,6,3)
        self.init_page.add("button","Creat a New File",1,1,com=self.creat_file)
        self.init_page.add("file","Load",2,1)
        self.init_page.add("button","pre-page",4,0,com=self.pre_page)
        self.init_page.add("button","next-page",4,2,com=self.next_page)
        self.init_page.setting()
        #self.init_page = tk.Frame(self.root)
        #button = tk.Button(self.init_page,text="button")
        #button.grid(row=0,column=1)
        #self.init_page_element = tk_page_element(3,3)
        #self.init_page_element.add("flie","open_file",self.init_page,0,1)  
    def add_setting_page(self):
        self.setting_page = tk_page_element(self.root,6,3)
        self.setting_page.add("button","pre-page",4,0,com=self.pre_page)
        self.setting_page.add("button","next-page",4,2,com=self.next_page)
        self.setting_page.setting()
    def add_help_page(self):
        self.help_page = tk_page_element(self.root,6,3)
        self.help_page.add("button","pre-page",4,0,com=self.pre_page)
        self.help_page.add("button","next-page",4,2,com=self.next_page)  
        self.help_page.setting()
    def add_menu(self):
        if platform.system == "Windows" or platform.system == "Linux":
            self.menu = tk.Menu(self.root)
            self.sub_menu = tk.Menu(self.menu)
            self.sub_menu.add_command(label="load",command=self.load_file)
            self.sub_menu.add_command(label="creat",command=self.creat_file)
            self.sub_menu.add_command(label="close",command=self.close_file)
            self.menu.add_cascade(label="File",menu=self.sub_menu)
            self.menu.add_command(label="Setting",command=self.show_setting)
            self.menu.add_command(label="Help",command=self.show_help)
            self.root.config(menu=self.menu)
        #self.menu_page.grid(row=0,column=0)
    def show_init(self):
        self.page_head = 0
        #print(self.init_page.element_list)
        self.init_page.show()
        self.setting_page.remove()
        self.help_page.remove()
    def show_setting(self):
        self.page_head = 1
        self.setting_page.show()
        self.init_page.remove()
        self.help_page.remove()
    def show_help(self):
        self.page_head = 2
        self.help_page.show()
        self.init_page.remove()
        self.setting_page.remove()        
    def load_file(self):
        self.sph_arg.set_file_name(filedialog.askopenfilename())
        self.sph_arg.load()
    def creat_file(self):
        print("creat a new file!")
        return 0
    def close_file(self):
        self.sph_arg = sph_arg()
        exit()
    def pre_page(self):
        if self.page_head == 0:
            self.show_help()
        elif self.page_head == 1:
            self.show_init()
        elif self.page_head == 2:
            self.show_setting()

    def next_page(self):
        if self.page_head == 0:
            self.show_setting()
        elif self.page_head == 1:
            self.show_help()
        elif self.page_head == 2:
            self.show_init()

    def show(self):
        self.root.mainloop()

            
sph_ui = tk_main_window()
sph_ui.show()