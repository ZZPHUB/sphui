from tkinter import filedialog
import tkinter as tk


class tk_arg_element:
    def __init__(self,name=str,root=tk.Tk,row=0,column=0):
        self.name = name
        self.label = tk.Label(root,text=name)
        self.label.grid(row=row,column=column)
        self.entry = tk.Entry(root)
        self.entry.grid(row=row,column=column+1)
    def get_name(self):
        return self.name
    def get_value(self):
        return self.entry.get()
    
class tk_file_element(tk_arg_element):
    def __init__(self,name=str,root=tk.Tk,row=0,column=0):
        tk_arg_element.__init__(self,name,root,row,column)
        self.button = tk.Button(root,text="select",command=self.button_event)
        self.button.grid(row=row,column=column+2)
    def button_event(self):
        self.file_name = filedialog.askopenfilename()
        self.entry.select_clear()
        #print(type(self.file_name))
        self.entry.insert(0,self.file_name)

class tk_page_element():
    def __init__(self,xnum=1,ynum=1):
        self.grid_xnum = xnum
        self.grid_ynum = ynum
        self.element_num = 0
        self.element_list = list()
    def add(self,type=str,name=str,root=tk.Tk,row=0,column=0):
        try:
            if row < self.grid_xnum and column < self.grid_ynum:
                if type == "arg":
                    column = column * 3
                    self.element_list.append(tk_arg_element(name,root,row,column))
                    self.element_num = self.element_num + 1
                elif type == "file":
                    column = column * 3
                    self.element_list.append(tk_file_element(name,root,row,column))
                    self.element_num = self.element_num + 1
                else:
                    raise "element type error!"
            else:
                raise "element position error!"
        except Exception as err:
            print(err)


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