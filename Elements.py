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

class GUITable:
    def __handle_click__(self, event):
        if(self.table.identify_region(event.x, event.y) == "separator"):
            return "break"

    def __init__(self, root, font, keys : tuple):
        self.root = root
        self.keys = keys                
        self.font = font
        
        self.table = ttk.Treeview(self.root, selectmode="none", columns=self.keys[0], show="headings")                
        self.table.configure(selectmode="browse")
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
        if(not self.shown):            
            self.shown = True
            self.table.pack(anchor="s", expand=False)
    
    def hide(self):
        if(self.shown):
            self.table.pack_forget()        


    def add_elements(self, *elements):
        for elem in elements: #pa el futuro cercano
            pass

class GUITableCustom:
    def __init__(self, root, font, **keys_type):
        self.root = root
        self.font = font
        
        self.bg = "white"
        self.table = Frame(self.root, bg=self.bg, bd=1, relief="solid", highlightcolor="gray")

        self.keys_type = keys_type

        self.widgets = []
        n = 0
        for key, type in self.keys_type.items():
            sep = ttk.Separator(self.table, orient="vertical")            
            
            match type: #Agregar mas si necesario
                case "LABEL":
                    wid = Label(self.table, text=key, bg=self.bg, font=self.font, justify="center")
                case "BUTTON": #Despues pasar command
                    wid = Button(self.table, text=key, bg=self.bg, relief="sunken", font=self.font)

            wid.grid(column=n, row=0)
            sep.grid(padx=10,column=n + 1, row=0, sticky="NSEW")
            n+=2
            self.widgets.append(wid)         
            self.widgets.append(sep)   

        self.widgets[-1].grid_remove()
        self.widgets.pop()
        self.shown = False
    
    def insert_elements(self, *elements):                 
        for c in range(len(elements)):
            if(self.widgets[c].winfo_class() != "Button"):
                n = self.widgets[c].cget("text") + elements[c]
                self.widgets[c].configure(text = n)
            else:
                pass



    def insert_elemnt(self, key, element):
        pass

    
    def show(self):
        if(not self.shown):            
            self.shown = True
            self.table.pack(anchor="s", expand=False)
    
    def hide(self):
        if(self.shown):
            self.table.pack_forget()        
