import tkinter as tk
from tkinter import filedialog

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
        self.button = tk.Button(root,text=name,command=self.button_event)
        self.button.grid(row=row,column=column+2)
    def button_event(self):
        self.file_name = filedialog.askopenfilename()
        self.entry.select_clear()
        self.entry.insert(self.file_name)

class tk_main_window():
    def __init__(self,xnum=1,ynum=1):
        self.grid_xnum = xnum
        self.grid_ynum = ynum
        self.element_num = 0
        self.element_list = list()
    def add(self,type=str,name=str,root=tk.Tk,row=0,column=0):
        try:
            if row < self.grid_xnum and column < self.grid_ynum:
                if type == "arg":
                    column = column * 2
                    self.element_list.append(tk_arg_element(name,root,row,column))
                elif type == "file":
                    column = column * 3
                    self.element_list.append(tk_file_element(name,root,row,column))
                else:
                    raise "element type error!"
            else:
                raise "element position error!"
        except Exception as err:
            print(err)
            
root = tk.Tk
main = tk_main_window(2,2)
main.add("arg","desity",root,0,0)
main.add("arg","pressure",root,0,1)
main.add("file","rigid",1,0)
main.add("file","fluid",1,1)

root.mainloop()