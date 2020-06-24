from tkinter import *
from nclib import Netcat

class MyWindow:
    def __init__(self, win):

        self.tk=win
        self.lbl1=Label(win, text='IP')
        self.lbl2=Label(win, text='Port')
        self.lbl3=Label(win, text='User')
        self.lbl4=Label(win, text='Pass')

        self.t1=Entry()
        self.t2=Entry()
        self.t3=Entry()
        self.t4=Entry()

        self.t1.insert(0,"localhost")
        self.t2.insert(0,"3001")
        self.t3.insert(0,"admin")
        self.t4.insert(0,"admin")
        #self.btn1 = Button(win, text='Login')
        #self.btn2=Button(win, text='Subtract')

        self.lbl1.place(x=40, y=20)
        self.lbl2.place(x=40, y=50)
        self.lbl3.place(x=40, y=80)
        self.lbl4.place(x=40, y=110)

        self.t1.place(x=130, y=20)
        self.t2.place(x=130, y=50)
        self.t3.place(x=130, y=80)
        self.t4.place(x=130, y=110)

        self.b1=Button(win, text='Connect',highlightbackground='#b8b8b8' ,command=self.login)
        #self.b2=Button(win, text='Subtract')
        #self.b2.bind('<Button-1>', self.sub)
        self.b1.place(x=360, y=35)
        #self.b2.place(x=200, y=150)


        ######

        self.cmdt=Label(self.tk, text='Command : ')
        #self.cmd=Entry(self.tk)
        self.cmd=Text(self.tk,bg='#e8e8e8', height=5, width=50)
        self.cmdb=Button(self.tk, text='Send',highlightbackground='#b8b8b8', command=self.send)

        self.cmdt.place(x=20, y=200)
        self.cmd.place(x=100, y=200)
        self.cmdb.place(x=360, y=95)

        #####Recive
        self.cmdrt=Label(self.tk, text='Result : ')
        #self.cmdr=Entry(self.tk)
        self.cmdr=Text(self.tk ,bg='#e8e8e8' , height=10, width=50)

        self.cmdr.place(x=100, y=350)
        self.cmdrt.place(x=20, y=350)

    def login(self):
        print("Login")
        self.ip=str(self.t1.get())
        self.port=int(self.t2.get())
        self.user=str(self.t3.get())
        self.passw=str(self.t4.get())
        #print(ip+port+user+passw)
        self.connection()


    #def createNewWindow(self):
        #self.t1.destroy()


    def send(self):

        self.command="\x00\x0d"+str(self.cmd.get("1.0",END))
        #self.prereq=""
        #self.aftreq=""
        #self.command=""

        self.nc.send(bytes(self.command, 'utf-8'))
        self.recive()

    def recive(self):
        #self.cmd.delete(0)
        #self.cmd.insert("")
        self.cmdr.insert("end-1c", "---------------------\n")
        self.cmdr.insert("end-1c", "Req >> "+self.cmd.get("1.0",END))
        result=self.nc.recv()
        self.cmdr.insert("end-1c", "Res >> "+str(result, 'utf-8'))
        self.cmdr.insert("end-1c", "---------------------\n")
        print("---------"+str(result))

    def connection(self):
        print("connectiong to "+self.ip+":"+str(self.port))
        #self.createNewWindow()
        try:
            self.nc = Netcat((self.ip, self.port), verbose=True, echo_hex=True)
            self.b1.configure(highlightbackground="#34a318")
        except Exception as e:
            print("error: "+str(e))
            self.b1.configure(highlightbackground="#a31818")
        #self.nc.send(b'\x00\x0dHello, world!')
        #self.nc.send(b'\x00\x0dHello, world!')
        #self.nc.recv()


window=Tk()
mywin=MyWindow(window)
window.title('TCP Client')
window.geometry("520x600+10+10")
window.mainloop()
