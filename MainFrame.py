import time
import tkinter.ttk as tk
from tkinter import *
from tkinter import messagebox  # importing the messagebox
import threading  # importing threading module

# importing song class from song.py
from Playlist import PlayList
from Song import Song


# frame that containing all widgets
class MainFrame(tk.Frame):

    def __init__(self, win):

        super().__init__()

        # variabels
        self.window = win

        self.song_playlist = []
        self.current_song = 0

        self.volum_counter = IntVar(value=30)
        # self.progress=IntVar(value=1)

        # initialinzeing buttons,frams etc
        self._Frames()
        self._Song_info()
        self._control_buttons()

        self._binding()

        # setting the variables

    # difining containers for widgets
    def _Frames(self):
        self.song_title_frame = tk.Frame(master=self.window)
        self.song_title_frame.pack(expand=True, fill=X, side=TOP)
        self.control_frame = tk.Frame(master=self.window)
        self.control_frame.pack(expand=True, fill=X, side=TOP)

    # displaying song info on the screen
    def _Song_info(self):
        self.song_label = tk.Label(master=self.song_title_frame, text='Music Player', font=('serif', 23, 'italic'),
                                   anchor=N, background='#6a85ad', foreground='#474d57')
        self.song_label.pack(expand=True, fill=X, ipady=5)

        # self.song_progress=tk.Progressbar(master=self.song_title_frame,orient=HORIZONTAL,variable=self.progress,
        #                                   value=self.progress.get())
        # self.song_progress.pack(expand=True,fill=X,pady=5,padx=10)

    # difinging control widgets of song
    def _control_buttons(self):
        # creating buttons for song control(play,pause,next,previous,playlist...)
        self.play_btn = tk.Button(master=self.control_frame, text='Play')
        self.pause_btn = tk.Button(master=self.control_frame, text='Pause')
        self.prev_btn = tk.Button(master=self.control_frame, text='Previous')
        self.next_btn = tk.Button(master=self.control_frame, text='Next')
        self.playlist_btn = tk.Button(master=self.control_frame, text='Playlist')
        self.view_playlist = tk.Button(master=self.control_frame, text=f'View-{len(self.song_playlist)}')

        self.volum = tk.Scale(master=self.control_frame, from_=0, to=100, variable=self.volum_counter,
                              value=self.volum_counter.get())
        self.volum_label = tk.Label(master=self.control_frame, text=str(self.volum_counter.get()) + ' %')

        # placing buttons
        self.play_btn.grid(row=0, column=0, padx=5, pady=5, sticky=W)
        self.pause_btn.grid(row=0, column=1, padx=5, pady=5, sticky=W)
        self.prev_btn.grid(row=0, column=2, padx=5, pady=5, sticky=W)
        self.next_btn.grid(row=0, column=3, pady=5, padx=5, sticky=W)
        self.playlist_btn.grid(row=0, column=4, padx=5, pady=5, sticky=W)

        self.view_playlist.grid(row=0, column=5, padx=5, pady=5, sticky=W)
        self.volum.grid(row=0, column=6, padx=5, pady=5, sticky=W)
        self.volum_label.grid(row=0, column=7, padx=5, pady=5, sticky=W)

    # working
    # opening file dialog in order to get songs
    def _openPlaylist(self, e):
        from tkinter import filedialog  # importing filedialog
        import os
        names = filedialog.askopenfilename(multiple=True, initialdir=os.getcwd(), filetypes=[('MP3 Files', '*.mp3')])
        # adding multiple selction to the quee of songs
        [self.song_playlist.append(Song(i)) for i in names]

        # play the first song
        self.song_playlist[self.current_song].PlaySong()
        self.song_label.config(text=self.song_playlist[self.current_song])
        # self.t=threading.Thread(target=self._incProgress)
        # self.t.start()
        self.song_title_frame.update_idletasks()
        self.view_playlist.config(text=f'View -{len(self.song_playlist)}')
        self.control_frame.update_idletasks()

        # testing
        # print('----open playlist function call----')

    # def _incProgress(self):
    #     song=self.song_playlist[self.current_song]
    #     self.song_lenth=song.GetLength()
    #     self.song_current_pos=song.GetPos()
    #
    #     self.song_progress.config(maximum=self.song_lenth)
    #
    #
    #     # testing
    #     # print('----prograssbar incre.. function call----')

    def _updatevolum(self, e):
        if (len(self.song_playlist) > 0):
            song = self.song_playlist[self.current_song]
            if (song.is_busy()):
                self.volum_counter.set(int(e.widget.get()))
                self.volum_label.config(text=f'{self.volum_counter.get()} %')
                self.control_frame.update_idletasks()
                #
                self.song_playlist[self.current_song].incVolumn(float(self.volum_counter.get()))

                # print for testin
                print('----volumn update function call----')
            else:
                messagebox.showerror(title='Error !', message='No Playing song found!')

        else:
            messagebox.showerror(title='Error !', message='No Song Found!')

    # working
    def _update_song_counter(self, e):
        # incresing the song position in the list

        if (self.current_song < len(self.song_playlist) - 1):

            self.current_song += 1
            # play the song in new thread
            self.thrad = threading.Thread(target=self._playmusic)
            self.thrad.setName('Playing Song')
            self.thrad.start()



        else:
            messagebox.showinfo(title='Playlist Ended', message='Your Playlist has ended!')

            # TODO
            # play the first song

            # testing
        # print('----song number update function call----')

    def _playmusic(self):
        self.song_playlist[self.current_song].PlaySong()
        self.song_label.config(text=self.song_playlist[self.current_song])

        self.song_title_frame.update_idletasks()

        # testing
        # print('----play music function call----')

    def _playSong(self, e):
        if (len(self.song_playlist) > 0):
            self._playmusic()
        else:
            messagebox.showerror(title='Error !', message='No Song Selected!')

    def _decrese_song_counter(self, e):
        # del self.thrad

        if (len(self.song_playlist) > 1):
            if (not self.current_song < 0):
                self.current_song -= 1
                # play the song in new thread
                pre_thread = threading.Thread(target=self._playmusic, name='Play Prev Song')
                pre_thread.start()
                print(self.current_song)

                # TODO
                # play the previous song
            else:
                messagebox.showinfo(title='Starting Point', message='You have reched the begining of the playlist')
                self.current_song = 0

                print(self.current_song)

            # testing
            # print('----dec song number function call----')
        else:
            messagebox.showinfo(title='Playlist Error!', message='No Songs Found!')

    def _viewPlaylist(self, e):
        if (len(self.song_playlist) == 0):
            messagebox.showerror(title='Playlist Error!', message='No Playlist Found')
        else:
            self.playlist = Toplevel()
            self.playlist.title('PlayList')
            # for i in self.song_playlist:
            #     tk.Label(master=self.playlist,text=str(i)).pack(pady=5,padx=5)
            self.new_window = PlayList(self.playlist, self.song_playlist)
            t = threading.Thread(target=self.update)
            t.start()

    def update(self):
        nl = self.new_window.newList
        if not nl:
            [self.song_playlist.append(i) for i in nl]
            self.view_playlist.update_idletasks()

    # function for pausing the song
    def _pauseSong(self, e):
        self.song_playlist[self.current_song].PauseSong()

        # testing
        # print('----pause function call----')

    # binding events to the buttons
    def _binding(self):
        self.playlist_btn.bind('<Button>', self._openPlaylist)
        self.volum.bind('<ButtonRelease-1>', self._updatevolum)
        self.next_btn.bind('<Button>', self._update_song_counter)
        self.prev_btn.bind('<Button>', self._decrese_song_counter)
        self.pause_btn.bind('<Button>', self._pauseSong)
        self.view_playlist.bind('<Button>', self._viewPlaylist)
        self.play_btn.bind('<Button>', self._playSong)
