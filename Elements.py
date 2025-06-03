from tkinter import *

class GUIEntry:
    def __init__(self, root, row_pad = 0, **inputs_n_type):
        self.root = root                   
        self.data : dict = inputs_n_type
        
        self.row_pad = row_pad

        self.vars = []
        self.widgets = []
        self.text = []

        color = root.cget("background")

        for name, type in self.data.items():
            self.vars.append(StringVar())
            match type: #se puede agregar mas si necesario XD
                case "ENTRY":
                    wid = Entry(self.root, textvariable=self.vars[-1], background=color)
                case "OPTIONMENU":
                    wid = OptionMenu(self.root, variable=self.vars[-1], value=""),
                    self.vars[-1].set('(...)')
            texto = Label(self.root, text=name, background=color)
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

    def load_option_menu(self, name,*data):
        n = 0
        for x in self.data.keys():
            if(x == name and self.data[x] == "OPTIONMENU"):
                self.vars[n].set("(...)")
                self.widgets[n][0]['menu'].delete(0, "end")
                for y in data:
                    self.widgets[n][0]['menu'].add_command(label=y, command=lambda v=y: self.vars[1].set(v))
                break                
            n+=1
    
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
    def __init__(self, root, *inputs):
        self.root = root    
        self.text = []
        self.row_pad = 0 
        color = root.cget("background")

        #font = root.cget()
        for name in inputs:
            texto = Label(self.root, text=name, background=color, font="customFont")
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
    def __init__(self, root, *keys):
        self.root = root
        self.keys = keys

        self.widgets = {}
        color = root.cget("background")
        for key in self.keys:
            texto_ev = Label(self.root, background=color, relief="raised", font="customFont")
            self.widgets[key] = [texto_ev]

    def add_elements(self, *elements):
        for elem in elements: #pa el futuro cercano
            pass
