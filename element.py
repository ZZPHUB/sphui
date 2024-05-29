import tkinter as tk
from tkinter import filedialog
import numpy as np

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

'''
root = tk.Tk()
#root.geometry("900x500")
page_e = tk_page_element(root,3,4)
page_e.add("file","new",0,1)
page_e.add("button","creat new",1,1,new_event)
print(page_e.element_index)
page_e.show()
print(page_e.element_index)
root.mainloop()
'''