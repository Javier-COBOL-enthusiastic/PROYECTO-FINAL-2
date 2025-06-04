from tkinter import *
from tkinter import ttk


class GUIEntry:
    def __init__(self, root, font, row_pad = 0, **inputs_n_type):
        self.root = root                   
        self.data : dict = inputs_n_type
        
        self.row_pad = row_pad

        self.font = font

        self.vars = []
        self.widgets = []
        self.text = []

        color = root.cget("background")

        for name, type in self.data.items():
            self.vars.append(StringVar())
            match type: #se puede agregar mas si necesario XD
                case "ENTRY":
                    wid = Entry(self.root, textvariable=self.vars[-1], background=color, font=self.font)
                case "OPTIONMENU":
                    wid = OptionMenu(self.root,variable=self.vars[-1], value="")
                    wid.configure(font=self.font)                    
                    self.vars[-1].set('(...)')
            texto = Label(self.root, text=name, background=color, font=self.font)
            self.widgets.append(wid)
            self.text.append(texto)

    def show(self):                       
        for x in range(len(self.widgets)):            
            self.text[x].grid(column=0, row=self.row_pad)
            if(type(self.widgets[x]) == tuple): self.widgets[x][0].grid(column=1, row=self.row_pad)
            else: self.widgets[x].grid(column=1, row=self.row_pad)            
            self.row_pad+=1    

    def hide(self):        
        for x in range(len(self.widgets)):            
            self.text[x].grid_remove()
            if(type(self.widgets[x]) == tuple): self.widgets[x][0].grid_remove()
            else: self.widgets[x].grid_remove()
            self.row_pad -=1    

    def load_option_menu(self, name, data):
        n = 0
        for x in self.data.keys():
            if x == name and self.data[x] == "OPTIONMENU":
                self.vars[n].set("(...)")
                self.widgets[n][0]['menu'].delete(0, "end")
                for y in data:
                    self.widgets[n][0]['menu'].add_command(label=y, command=lambda v=y: self.vars[n].set(v))
                break
            n += 1

    
    def clear(self):
        for var in self.vars:
            var.set("")

    def get(self) -> list:
        n = []
        for x in self.vars:
            n.append(x.get())
        
        return n

    def get_current_row_pad(self):
        return self.row_pad

class GUIInformation: #jaja clase inutil :v
    def __init__(self, font, root, *inputs):
        self.root = root    
        self.text = []
        self.row_pad = 0 
        color = root.cget("background")

        self.font = font
        for name in inputs:
            texto = Label(self.root, text=name, background=color, font=self.font)
            self.text.append(texto)        

    def show(self):                       
        for x in range(len(self.text)):            
            self.text[x].grid(column=0, row=self.row_pad)
            self.row_pad+=1    

    def hide(self):        
        for x in range(len(self.text)):            
            self.text[x].grid_remove()           
            self.row_pad -=1    

class GUITable:
    def __handle_click__(self, event):
        if(self.table.identify_region(event.x, event.y) == "separator"):
            return "break"

    def __init__(self, root, font, keys : tuple):
        self.root = root
        self.keys = keys                
        self.font = font
        
        self.table = ttk.Treeview(self.root, selectmode="none", columns=self.keys[0], show="headings")                
        self.table.configure(selectmode="none")
        self.table.bind("<Button-1>", self.__handle_click__)
        
        for c in range(len(self.keys[0])):
            self.table.heading(self.keys[0][c], text=self.keys[1][c], anchor="center")            
            self.table.column(self.keys[0][c], anchor="center", stretch=False)
                
            
        self.shown = False

    def insert_item(self, *info):          
        self.table.insert(parent="",index="end", values=info)
    
    def configure_width_columns(self, *config):
        for c in range(len(self.keys[0])):
            self.table.column(self.keys[0][c], width=config[c])



    def show(self):
        self.show = True
        self.table.pack(fill="x", anchor="s")
    
    def hide(self):
        if(self.show):
            self.table.pack_forget()        


    def add_elements(self, *elements):
        for elem in elements: #pa el futuro cercano
            pass
