from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import os
import splitter as splitter
class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()
        #self.title("Background Maker")

        #self.pack()
    def createWidgets(self):
        ########################################################################
        self.title = Frame(self, bg="#dfdfdf")
        Label(self.title, text = "Splither Background Maker", font=("Courier", 44)).pack(side="top")
        #naming: split-her. the app splits people. it works like magic, magicians
        #split people. My original name was splitter and slicer. splither works too.
        self.title.pack(side = "top")
        ########################################################################

        self.left = Frame(self, bg="#dfdfdf")
        self.QUIT = Button(self.left, text="QUIT", fg="red",command=root.destroy)
        self.QUIT.grid(row = 0, column = 0)

        self.calc = Button(self.left, text="Run Splither", fg="green")
        self.calc["command"] = self.calculate
        self.calc.grid(row = 1, column = 0)

        self.init = Button(self.left, text="Create folders", fg="blue")
        self.init["command"] = self.init
        self.init.grid(row = 1, column = 1)

        self.savecon = Button(self.left, text="Save Config", fg="orange")
        self.savecon["command"] = self.saveconfig
        self.savecon.grid(row = 2, column = 0)

        self.savecon = Button(self.left, text="Load Config", fg="green")
        self.savecon["command"] = self.loadconfig
        self.savecon.grid(row = 2, column = 1)

        Label(self.left, text = "place right mon at: ").grid( row = 4, column  = 0)
        self.label1 = Label(self.left, text = "0")
        self.label1.grid( row = 4, column  = 1)

        Label(self.left, text = "place left mon at: ").grid( row = 5, column  = 0)
        self.label2 = Label(self.left, text = "0")
        self.label2.grid( row = 5, column  = 1)

        self.left.pack(side = "left")
        ########################################################################
        self.input = Frame(self)
        Label(self.input,text="Input: ", font = ("Courier, 20")).grid(row=0,column=0, columnspan =3)

        Label(self.input,text="Resolution measurements: ", font = ("Courier 14 bold")).grid(row=1,column=0)
        titles = ("Left mon x ","Left mon y ","Right mon x ","Right mon y ")

        self.entries = []
        i = 0
        self.input1 = Entry(self.input)
        Label(self.input,text=titles[i]).grid(row=i+2,column=0)
        self.input1.grid(row=i+2, column=1)
        self.entries.append(self.input1)
        i+=1
        self.input2 = Entry(self.input)
        Label(self.input,text=titles[i]).grid(row=i+2,column=0)
        self.input2.grid(row=i+2, column=1)
        self.entries.append(self.input2)
        i+=1
        self.input3 = Entry(self.input)
        Label(self.input,text=titles[i]).grid(row=i+2,column=0)
        self.input3.grid(row=i+2, column=1)
        self.entries.append(self.input3)
        i+=1
        self.input4 = Entry(self.input)
        Label(self.input,text=titles[i]).grid(row=i+2,column=0)
        self.input4.grid(row=i+2, column=1)
        self.entries.append(self.input4)
        i+=1

        Label(self.input,text="Physical measurements: ", font = ("Courier 14 bold")).grid(row=i+2,column=0)
        i+=1
        titles = ("Left mon x ","Left mon y ","Right mon x ","Right mon y ","Pysical vertical offset (tops)", "horizontal space between monitors (bezels)")

        j=0
        self.input5 = Entry(self.input)
        Label(self.input,text=titles[j]).grid(row=i+2,column=0)
        self.input5.grid(row=i+2, column=1)
        self.entries.append(self.input5)
        i+=1
        j+=1
        self.input6 = Entry(self.input)
        Label(self.input,text=titles[j]).grid(row=i+2,column=0)
        self.input6.grid(row=i+2, column=1)
        self.entries.append(self.input6)
        i+=1
        j+=1
        self.input7 = Entry(self.input)
        Label(self.input,text=titles[j]).grid(row=i+2,column=0)
        self.input7.grid(row=i+2, column=1)
        self.entries.append(self.input7)
        i+=1
        j+=1
        self.input8 = Entry(self.input)
        Label(self.input,text=titles[j]).grid(row=i+2,column=0)
        self.input8.grid(row=i+2, column=1)
        self.entries.append(self.input8)
        i+=1
        j+=1
        self.input9 = Entry(self.input)
        Label(self.input,text=titles[j]).grid(row=i+2,column=0)
        self.input9.grid(row=i+2, column=1)
        self.entries.append(self.input9)
        i+=1
        j+=1
        self.input10 = Entry(self.input)
        Label(self.input,text=titles[j]).grid(row=i+2,column=0)
        self.input10.grid(row=i+2, column=1)
        self.entries.append(self.input10)
        i+=1
        j+=1
        self.input.pack(side = "left")
################################################################################
        self.checkboxes = Frame(self)
        Label(self.checkboxes,text="Parameters: ", font = ("Courier 14 bold")).grid(row=0)

        self.var1 = IntVar()
        self.var2 = IntVar()
        self.var3 = IntVar()
        self.var4 = IntVar()
        self.var5 = IntVar()
        self.var6 = IntVar()
        self.var7 = IntVar() #gap between monitors

        self.c1 = Checkbutton(self.checkboxes, text="left monitor higher?", variable = self.var1)
        self.c1.grid(row = 1)
        self.c2 = Checkbutton(self.checkboxes, text="left monitor main?", variable = self.var2)
        self.c2.grid(row = 2)
        Label(self.checkboxes,text="Options: ", font = ("Courier 14 bold")).grid(row=3)
        self.c3 = Checkbutton(self.checkboxes, text="force centre split?", variable = self.var3)
        self.c3.grid(row = 4)
        self.c4 = Checkbutton(self.checkboxes, text="maintain PPI?", variable = self.var4)
        self.c4.grid(row = 5)
        self.c5 = Checkbutton(self.checkboxes, text="fill horizontal?", variable = self.var5)
        self.c5.grid(row = 6)
        self.c6 = Checkbutton(self.checkboxes, text="fill vertical?", variable = self.var6)
        self.c6.grid(row = 7)
        self.c7 = Checkbutton(self.checkboxes, text="mind the gap?", variable = self.var7)
        self.c7.grid(row = 8)
        self.checkboxes.pack(side = "right")

################################################################################
    def usetxt(self):
        print('text1')

    def calculate(self):
        m1,m2 = splitter.monitor_placement(float(self.input9.get()),float(self.input6.get()),float(self.input8.get()),int(self.input2.get()),int(self.input4.get()),self.var1.get())
        self.label1.config(text=m1)
        self.label2.config(text=m2)
        #print(self.c4.get())
        splitter.main(float(self.input6.get()),float(self.input8.get()),float(self.input5.get()),float(self.input7.get()),int(self.input1.get()), int(self.input2.get()),int(self.input3.get()),int(self.input4.get()),float(self.input9.get()),float(self.input10.get()),self.var1.get(),self.var2.get(),self.var3.get(),self.var4.get(),self.var7.get())
        messagebox.showinfo("Notice", "She is split")


    def init(self):
        print('test2')
        for i in ('./splitterinput','./output'):
            print('test')
            if not os.path.exists(i):
                print(i)
                os.makedirs(i)

    def saveconfig(self):
        print('saving config')
        with open('./config.config', 'w+') as f1:
            for i in self.entries:
                f1.write(str(i.get()) + '\n')
        messagebox.showinfo("Notice", "Saving complete")


    def loadconfig(self):
        my_file = "./config.config"
        if  os.path.exists(my_file)==True:
            print('loading config')
            with open(my_file) as f:
                content = f.readlines()
                content = [x.strip() for x in content]
                for i in zip(content,(self.input1, self.input2, self.input3, self.input4, self.input5, self.input6, self.input7, self.input8, self.input9, self.input10) ):
                    i[1].delete(0,END)
                    i[1].insert(0,i[0])
        else:
            messagebox.showinfo("Error", "No config files were found")
root = Tk()
root.wm_title("Background Maker")
app = Application(master=root)
app.mainloop()
root.destroy()
