import pygame.mixer as mx
from tkinter import messagebox
import os

class Song:

    def __init__(self,path):
        self.path=path
        self.is_playing=False
        if( not mx.get_init()):
            mx.init()


    def PlaySong(self):
        if(not mx.music.get_busy()):
            try:
                mx.music.load(self.path)
                mx.music.play()
                self.is_playing=True
            except Exception:
                messagebox.showerror(title='Error!',message='Can not Load the media file')
        else:

            mx.music.stop()
            mx.music.unload()
            try:
                mx.music.load(self.path)
                mx.music.play()
            except Exception:
                messagebox.showerror(title='Error!',message='Can not Load the media file')





    def PauseSong(self):
        if(mx.music.get_busy()):
            if(self.is_playing):
                mx.music.pause()
                self.is_playing=False
                return True
            else:
                mx.music.unpause()
                self.is_playing=True
                return False
        else:
            messagebox.showerror(title='Can not Pause/UnPause',message='You have no any paused musics!')

    def incVolumn(self,vol):
        if(mx.music.get_busy()):
            mx.music.set_volume(vol/100)
        else:
            messagebox.showerror(title='Error !',message='No Song Selected!')

    def __repr__(self):
        return f'{os.path.basename(self.path)}'

    def GetPos(self):
        if(mx.music.get_busy()):
            return int(mx.music.get_pos()/1000)
        else:
            return 1
    def GetLength(self):
        # return the lenght in seconds
        if(mx.music.get_busy()):
            return int(mx.Sound(file=self.path).get_length())
        else:
            return 1

    def is_busy(self):
        return mx.music.get_busy()


