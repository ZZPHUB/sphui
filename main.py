from tkinter import filedialog
import tkinter as tk

class tk_main_window():
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("SPHUI")
    def add_menu(self):
        self.menu = tk.Menu(self.root)
        self.sub_menu = tk.Menu(self.menu)
        self.sub_menu.add_command(label="load",command=self.open_file)
        self.sub_menu.add_command(label="creat",command=self.creat_file)
        self.sub_menu.add_command(label="close",command=self.close_file)
        self.menu.add_cascade(label="File",menu=self.sub_menu)
        #self.menu.add_command(label="File",command=self.show_init)
        self.menu.add_command(label="Setting",command=self.show_setting)
        self.menu.add_command(label="Help",command=self.show_help)
        self.root.config(menu=self.menu)
    def show_init(self):
        self.init_page.grid(row=0,column=0)
        self.setting_page.grid_remove()
        self.help_page.gird_remove()
    def show_setting(self):
        self.setting_page.grid(row=0,column=0)
        self.init_page.grid_remove()
        self.help_page.grid_remove()
    def show_help(self):
        self.help_page.grid(row=0,column=0)
        self.init_page.gird_remove()
        self.setting_page.grid_remove()
    def open_file(self):
        self.file_name = filedialog.askopenfilename()
    def creat_file(self):
        return 0
    def close_file(self):
        return 0
    def show(self):
        self.root.mainloop()

            
sph_ui = tk_main_window()
sph_ui.add_menu()
sph_ui.show()