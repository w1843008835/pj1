import tkinter as tk
from tkinter import ttk
import tkinter.messagebox
from tkinter.filedialog import (askopenfilename,
                                    askopenfilenames,
                                    askdirectory,
                                    asksaveasfilename)


class app:
    def __init__(self,master):
        frame = tk.Frame(master)
        # frame.pack(side=tk.LEFT,padx=200,pady=100)
        frame.grid(row=4,column=3)

        checkVar2 = tk.StringVar(value="1")
        checkVar3 = tk.StringVar(value="1")
        path = tk.StringVar()
        msg = tk.StringVar()
        self.hi_there4 = tk.Label(frame,text = "目标路径:").grid(row=0,column=0,sticky="W")
        self.hi_there5 = tk.Entry(frame, textvariable = path,width="50").grid(row=0,column=1,sticky="W")
        self.hi_there6 = tk.Button(frame, text="路径选择",command=lambda :self.selectPath(path)).grid(row=0,column=2,sticky="W")
        self.hi_there2 = tk.Checkbutton(frame, text='WebOTX参照', variable=checkVar2).grid(row=1,column=0,sticky="W")
        self.hi_there3 = tk.Checkbutton(frame, text='SDE参照', variable=checkVar3).grid(row=1,column=2,sticky="W")
        self.hi_there7 = tk.Label(frame, textvariable=msg, fg='red').grid(row=2, column=1, sticky="W")
        self.hi_there = tk.Button(frame, text="削除", command=lambda: self.delReference(checkVar2, checkVar3, path,msg)).grid(row=2, column=0, sticky="W")



        # self.hi_there.pack(side=tk.LEFT)
        # self.hi_there2.pack(side=tk.LEFT)
        # self.hi_there3.pack(side=tk.LEFT)
        # self.hi_there4.pack(side=tk.LEFT)
        # self.hi_there5.pack(side=tk.LEFT)
        # self.hi_there6.pack(side=tk.LEFT)



    def delReference(self,checkVar2,checkVar3,path,msg):
        # print(checkVar2.get(),checkVar3.get(),path.get())
        if path.get() == "":
            msg.set("please select folder!")

    def selectPath(self,path):
        path_ = askdirectory()
        path.set(path_)



if __name__ == '__main__':
    root = tkinter.Tk()
    root.title(".classpath参照パス削除")
    app = app(root)
    root.mainloop()