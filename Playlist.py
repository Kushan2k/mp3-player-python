import tkinter.ttk as tk
from tkinter import Y, X, LEFT, filedialog

from Song import Song


class PlayList(tk.Frame):
    def __init__(self, top, songlist):
        super().__init__(top)
        self.window = top
        self._newlist = []
        self.pack()
        self.songFrame()
        self._songlist = songlist
        self.viewlist()
        self.addButtons()
        self.binding()

    def songFrame(self):
        self.song_box = tk.Frame(master=self.window)
        self.option_box = tk.Frame(master=self.window)

        self.song_box.pack(expand=True, fill=Y, padx=5, pady=10, side=LEFT)
        self.option_box.pack(expand=True, fill=Y, padx=5, pady=10, side=LEFT)

    def viewlist(self):
        import os
        for i in range(len(self._songlist)):
            self.l = tk.Label(master=self.song_box, text=f'{i}-{self._songlist[i]}',
                              borderwidth=2, font=('monospace', 12, 'italic'))
            self.l.pack(fill=X, padx=5, pady=3)

    def addButtons(self):
        self.addbtn = tk.Button(master=self.option_box, text='Add')
        self.addbtn.pack(ipadx=5, ipady=5)

    def openfile(self, e):

        import os
        _names = filedialog.askopenfilename(multiple=True, initialdir=os.getcwd(), filetypes=[('MP3 Files', '*.mp3')])

        [self._newlist.append(Song(i)) for i in _names]

        [self._songlist.append(i) for i in self._newlist]

        self.la = self.song_box.pack_slaves()
        for i in self.la:
            i.pack_forget()
        self.viewlist()

    @property
    def newList(self):

        if len(self._newlist) > 0:
            print(self._newlist)
            return self._newlist
        else:
            return []

    def binding(self):
        self.addbtn.bind('<Button>', self.openfile)
