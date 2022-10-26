from socketIO_client import SocketIO
from tkinter import *
from functools import partial

print("Comenzando...")
socketIO = SocketIO('34.173.19.239', 5001)
print("Conectado al servidor.")

class Window(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)        
        self.master = master
        # widget can take all window
        self.pack(fill=BOTH, expand=1)

        # entry = Entry(takefocus=True)
        # entry.place(x=75,y=5)
        # entry.insert(0,'1')
        # entry.focus()

        value_inside = StringVar(root)
        value_inside.set("Seleccionar Motor")
        options_list = ["1", "2", "3", "4", "5"]
        question_menu = OptionMenu(root, value_inside, *options_list)
        question_menu.location(75, 10)
        question_menu.pack()

        tem_on_Button = Button(self, text="+", width=10, height=8, command=partial(self.increase,value_inside))
        tem_on_Button.place(x=25, y=30)

        tem_on_Button = Button(self, text="-", width=10, height=8, command=partial(self.decrease,value_inside))
        tem_on_Button.place(x=200, y=30)
        

    def increase(self,value_inside):
        message = {'motor':value_inside.get(),'command':"+"}
        # print("Selected Option: {}".format())
        # print(message)
        socketIO.emit("ctrl_from_python", message)

    def decrease(self,value_inside):
        message = {'motor':value_inside.get(),'command':"-"}
        socketIO.emit("ctrl_from_python", message)

root = Tk()
app = Window(root)
root.wm_title("CONTROL")
root.geometry("320x200+700+400")
root.mainloop()
