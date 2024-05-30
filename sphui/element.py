import tkinter as tk
from tkinter import filedialog
import numpy as np
import platform
from sphui.sph import *

class tk_none_element:
    def __init__(self,root=any,row=0,column=0):
        self.row = row
        self.columu = column
        self.label0 = tk.Label(root,text='.',width=5,height=5)
        self.label0.grid(row=row,column=column)
        self.label1 = tk.Label(root,text='.',width=5,height=5)
        self.label1.grid(row=row,column=column+1)
        self.label2 = tk.Label(root,text='.',width=5,height=5)
        self.label2.grid(row=row,column=column+2)
    def show(self):
        self.label0.grid()
        self.label1.grid()
        self.label2.grid()
        #self.label0.grid(row=self.row,column=self.columu)
        #self.label1.grid(row=self.row,column=self.columu+1)
        #self.label2.grid(row=self.row,column=self.columu)
    def remove(self):
        self.label0.grid_remove()
        self.label1.grid_remove()
        self.label2.grid_remove()


class tk_arg_element:
    def __init__(self,name=str,root=None,row=0,column=0):
        self.name = name
        self.row = row
        self.column = column
        self.label = tk.Label(root,text=name)
        self.label.grid(row=row,column=column)
        self.entry = tk.Entry(root)
        self.entry.grid(row=row,column=column+1)
    def get_name(self):
        return self.name
    def get_value(self):
        return self.entry.get()
    def show(self):
        self.label.grid()
        self.entry.grid()
        #self.label.grid(row=self.row,column=self.column)
        #self.entry.grid(row=self.row,column=self.column+1)
    def remove(self):
        self.label.grid_remove()
        self.entry.grid_remove()
    
class tk_file_element(tk_arg_element):
    def __init__(self,name=str,root=None,row=0,column=0):
        tk_arg_element.__init__(self,name,root,row,column)
        self.button = tk.Button(root,text="select",command=self.button_event)
        self.button.grid(row=row,column=column+2)
    def button_event(self):
        self.file_name = filedialog.askopenfilename()
        self.entry.delete(0,tk.END)
        self.entry.insert(0,self.file_name)
    def get_name(self):
        return super().get_name()
    def get_value(self):
        return super().get_value()
    def show(self):
        super().show()
        #self.button.grid(row=self.row,column=self.column+2)
        self.button.grid()
    def remove(self):
        super().remove()
        self.button.grid_remove()

class tk_button_element:
    def __init__(self,name=str,root=any,row=0,column=0,com=any):
        self.name = name
        self.row = row
        self.column = column
        self.button = tk.Button(root,text=name,command=com)
        self.button.grid(row=row,column=column+1)
    def get_name(self):
        return self.name
    def show(self):
        #self.button.grid(row=self.row,column=self.column+1)
        self.button.grid()
    def remove(self):
        self.button.grid_remove()

class tk_label_element:
    def __init__(self,name=str,root=any,row=0,column=0):
        self.name = name
        self.row = row
        self.column = column
        self.label = tk.Label(root,text=name)
        self.label.grid(row=row,column=column+1)
    def get_name(self):
        return self.name
    def show(self):
        self.label.grid()
    def remove(self):
        self.label.grid_remove()

class tk_page_element:
    def __init__(self,root=any,ynum=1,xnum=1):
        self.root = root
        self.page = tk.Frame(self.root)
        self.row_num = ynum
        self.column_num = xnum
        self.element_index = np.zeros((self.row_num,self.column_num))
        print(self.element_index)
        self.element_num = 0
        self.element_list = list()
    def add(self,type=str,name=str,row=0,column=0,com=any):
        try:
            if row < self.row_num and column < self.column_num:
                self.element_index[row][column] = 1
                column = column * 3
                if type == "arg":
                    self.element_list.append(tk_arg_element(name,self.page,row,column))
                    self.element_num = self.element_num + 1
                elif type == "file":
                    self.element_list.append(tk_file_element(name,self.page,row,column))
                    self.element_num = self.element_num + 1
                elif type == "none":
                    tk_none_element(self.page,row,column)
                elif type == "button":
                    self.element_list.append(tk_button_element(name,self.page,row,column,com))
                    self.element_num = self.element_num + 1 
                elif type == "label":
                    self.element_list.append(tk_label_element(name,self.page,row,column))
                    self.element_num = self.element_num + 1
                else:
                    raise "element type error!"
            else:
                raise "element position error!"
        except Exception as err:
            print(err)
    def setting(self):
        for i in range(self.row_num):
            for j in range(self.column_num):
                if self.element_index[i][j]==0:
                    self.add("none","",i,j)
                    print("add a none element!")
        self.page.grid(row=0,column=0)
    def show(self):
        for i in self.element_list:
            i.show()
            #print('0k')
        self.page.grid()
    def remove(self):
        for i in self.element_list:
            i.remove()
        self.page.grid_remove()

def new_event():
    print("hello!")

class tk_main_window():
    def __init__(self):
        self.root = tk.Tk()
        if platform.system() == "Windows" or platform.system() == "Linux":
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
            print(platform.system)
            tk.messagebox.showwarning(title="Fuck Mac OS!",message="Fuck Mac OS!\nTk in MAC is a SHIT!")
            exit()
    def add_init_page(self):
        self.init_page = tk_page_element(self.root,6,3)
        self.init_page.add("button","Creat a New File",1,1,com=self.creat_file)
        self.init_page.add("file","Load",2,1)
        self.init_page.add("button","Close File",3,1,com=self.close_file)
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
        self.help_page.add("label","Author:ZZP",1,1)
        self.help_page.add("label","Version:0.001",2,1)
        self.help_page.add("button","pre-page",4,0,com=self.pre_page)
        self.help_page.add("button","next-page",4,2,com=self.next_page)  
        self.help_page.setting()
    def add_menu(self):
        if platform.system() == "Windows" or platform.system() == "Linux":
            self.menu = tk.Menu(self.root)
            #self.sub_menu = tk.Menu(self.menu)
            #self.sub_menu.add_command(label="load",command=self.load_file)
            #self.sub_menu.add_command(label="creat",command=self.creat_file)
            #self.sub_menu.add_command(label="close",command=self.close_file)
            #self.menu.add_cascade(label="File",menu=self.sub_menu,command=self.show_init)
            self.menu.add_command(label="File",command=self.show_init)
            self.menu.add_command(label="Setting",command=self.show_setting)
            self.menu.add_command(label="Run",command=self.show_run)
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
    def show_run(self):
        return 0        
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

