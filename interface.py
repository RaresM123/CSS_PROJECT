from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox
from compute import get_result
import xmltodict


class ResultWindows(Frame):
    def __init__(self, sentences ,master=None):
        Frame.__init__(self, master)   
        self.sentences = sentences
        self.master = master

        self.init_window()

    
    def init_window(self):
        self.master.title("Calculation steps")
        self.configure(background='AntiqueWhite')

        self.pack(fill=BOTH, expand=1)

        for key in self.sentences:
            label = Label(self,text=key + ' : ' + str(self.sentences[key]),background='#BEC2BC')
            label.pack(side="top", fill="x",ipady=10)






class MainWindow(Frame):
    file = ''
    distance = None
    equation_entry = None
    compressButton = None
    frames = []
    labels = []
    var_name_widgets = []
    var_value_widgets = []


    def __init__(self, master=None):
        Frame.__init__(self, master)   

        self.master = master

        self.init_window()

    def init_window(self):

        self.master.title("Expression calculator")
        self.configure(background='AntiqueWhite')

        self.pack(fill=BOTH, expand=1)

        label = Label(self,text='Enter expression',background='#BEC2BC')
        label.pack(side="top", fill="x",ipady=10)

        self.equation_entry = Entry(self,font = "Helvetica 24 bold",justify="center")
        self.equation_entry.pack(side="top", fill="x",ipady=10)


        self.calculateButton = Button(self,text="Calculate",highlightbackground='#3E4149',command=self.calculate)
        self.calculateButton.pack(side="top", fill="x")

        self.addVariableButton = Button(self, text="Calculate from xml",highlightbackground='#3E4149', command=self.compute_from_xml)
        self.addVariableButton.pack(side="bottom", fill="x")

        self.addVariableButton = Button(self, text="Add variable",highlightbackground='#3E4149', command=self.create_widgets)
        self.addVariableButton.pack(side="bottom", fill="x")




    def client_exit(self):
        exit()
   
    def create_widgets(self):
        frame = Frame(self, borderwidth=2, relief="groove")
        self.frames.append(frame)

        frame.pack(side="top", fill="x")

        label = Label(frame,text='Enter variable name and value:',width=40)
        self.labels.append(label)
        label.pack(side='left')

        valueWidget = Entry(frame)
        valueWidget.insert(0, 'value')
        valueWidget.configure(state=DISABLED)
        self.var_value_widgets.append(valueWidget)
        valueWidget.pack(side="right")
        def on_click1(event):
            valueWidget.configure(state=NORMAL)
            valueWidget.delete(0, END)
            valueWidget.unbind('<Button-1>', on_click_id)

        on_click_id = valueWidget.bind('<Button-1>', on_click1)
        

        variableWidget = Entry(frame)
        variableWidget.insert(0, 'var name')
        variableWidget.configure(state=DISABLED)
        self.var_name_widgets.append(variableWidget)
        variableWidget.pack(side="right")
        def on_click2(event):
            variableWidget.configure(state=NORMAL)
            variableWidget.delete(0, END)
            variableWidget.unbind('<Button-1>', on_click_id)

        on_click_id = variableWidget.bind('<Button-1>', on_click2)

        


    def calculate(self):
        equation = self.equation_entry.get()

        variables = {self.var_name_widgets[i].get():self.var_value_widgets[i].get() for i in range(len(self.var_name_widgets))}
        for frame in self.frames:
            frame.destroy()

        self.frames = []
        self.var_name_widgets = []
        self.var_value_widgets = [] 

        try:
            result,sentences = get_result(equation,variables)
        except ValueError as e:
            print(e)
            self.equation_entry.delete(0, END)
            messagebox.showerror(title='Equation error', message=e)
            return

        self.equation_entry.delete(0, END)
        self.equation_entry.insert(0, str(result))

        root = Tk()
        root.geometry("600x400")
        app = ResultWindows(sentences,root)
        root.mainloop()

    def compute_from_xml(self):
        xml_contents = xmltodict.parse(open("equation.xml","r").read())
        equation = xml_contents['root']['Equation']
        variables = dict(xml_contents['root']['Parameters'])

        try:
            result,sentences = get_result(equation,variables)
        except ValueError as e:
            print(e)
            self.equation_entry.delete(0, END)
            messagebox.showerror(title='Equation error', message=e)
            return


        self.equation_entry.delete(0, END)
        self.equation_entry.insert(0, str(result))

        with open('result.xml', 'w') as result_file:
            result_file.write(xmltodict.unparse({"Steps":sentences},pretty=True))




if __name__ == '__main__':
    root = Tk()
    root.geometry("600x400")
    app = MainWindow(root)
    root.mainloop() 
