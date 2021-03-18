from tkinter import *




from MainFrame import MainFrame



def runGUI():
    window=Tk()
    window.title('MP3 Player Max')
    window.geometry('700x120')
    logo=PhotoImage(file='./logo-mp3.png')

    window.iconphoto(True,logo)
    window.resizable(False,False)
    f=MainFrame(window)


    window.mainloop()


def main():
    runGUI()

if __name__=='__main__':
    main()


