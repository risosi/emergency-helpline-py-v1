from PIL import ImageTk
import tkinter as tk
from tkvideo import tkvideo
import customtkinter as cTk
from assets.music import convert_video_to_audio_moviepy
root = tk.Tk()

root.title('Helpline')
root.eval('tk::PlaceWindow . center')
root['bg']='#ffffff'
#root.geometry('500x750+'+str(root.winfo_screenwidth()//2)+'+'+str(int(root.winfo_screenheight()*0.1)))
frame1 = tk.Frame(root, height=350, width=500,bg="#ffffff")
frame2=tk.Frame(root,width=500,height=500,bg="#ffffff")
frame3 = tk.Frame(root, width=500,height=500,bg="#ffffff")
logo = ImageTk.PhotoImage(file='./assets/banner2.jpg')
icon = ImageTk.PhotoImage(file='./assets/details.png')

def clear_children(frame):
    for widget in frame.winfo_children():
        widget.destroy()



def load_frame3():
    clear_children(frame1)
    clear_children(frame2)
    frame3.tkraise()
    
    frame3.pack(side='top',fill='both')
    frame3.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
    frame3.pack_propagate(False)
    
    vl=tk.Label(master=frame3)
    vl.pack()
    player = tkvideo("assets/t.mp4",vl,loop=1,size=(500,200))
    player.play()

    
    
    logo_widget2 = tk.Label(frame3,image=logo,bg="#ffffff")
    logo_widget2.image=logo
    logo_widget2.pack()
    cTk.CTkLabel(master=frame3,
    text="All Helplines are hear",
    font=("Roboto black",50),
    pady=35,
    text_color="#000000").pack()
    
    
    cTk.CTkButton(master=frame3,
        text="Back",
        height=50,
        width=140,
        font=('Roboto black',55),
        border_spacing=5,
       command=lambda:load_frame1and2()
    ).pack()

    
def load_frame1and2():
    clear_children(frame3)
    frame1.tkraise()
    # frame1.place(relx=0.5,rely=0.3,anchor=tk.CENTER)
    #grid(row=0,column=0)
    frame1.pack(side='top',fill='both')
    frame1.pack_propagate(False)
    
    
    frame2.tkraise()
    # frame2.place(relx=0.5,rely=0.6,anchor=tk.CENTER)
    frame2.pack(side='top',fill='both')
    frame2.pack_propagate(False)
    


    logo_widget = tk.Label(frame1,image=logo,bg="#ffffff")
    logo_widget.image=logo
    logo_widget.pack()
    
    
    cTk.CTkLabel(master=frame1,
    text="All Helplines are hear",
    font=("Roboto black",50),
    pady=35,
    text_color="#000000").pack()
    
    
    #.place(relx=0.5,rely=0.2,anchor=tk.CENTER)
    
    
    
    #button = cTk.CTkButton(master=frame1, text="CTkButton", command=None)
    #button.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
    
    cTk.CTkButton(master=frame2,
        text="999",
        height=50,
        width=140,
        font=('Roboto black',55),
        image=icon,
        compound='top',
        border_spacing=5,
        fg_color='#8B00FF',
        command=lambda:load_frame3()
    ).place(relx=0.5,rely=0.2,anchor=tk.CENTER)
    
    cTk.CTkButton(master=frame2,
        text="999",
        height=50,
        width=140,
        font=('Roboto black',55),
        image=icon,
        compound='top',
        border_spacing=5,
        fg_color='#008080'
    ).place(relx=0.25,rely=0.2,anchor=tk.CENTER)
    
    cTk.CTkButton(master=frame2,
        text="999",
        height=50,
        width=140,
        font=('Roboto black',55),
        image=icon,
        compound='top',
        border_spacing=5,
        fg_color='#FFCC00'
    ).place(relx=0.75,rely=0.2,anchor=tk.CENTER)
    
    
    cTk.CTkButton(master=frame2,
        text="999",
        height=50,
        width=140,
        font=('Roboto black',55),
        image=icon,
        compound='top',
        border_spacing=5,
        fg_color="#660066"
    ).place(relx=0.5,rely=0.5,anchor=tk.CENTER)
    
    cTk.CTkButton(master=frame2,
        text="999",
        height=50,
        width=140,
        font=('Roboto black',55),
        image=icon,
        compound='top',
        border_spacing=5,
        fg_color="#03c03c"
    ).place(relx=0.25,rely=0.5,anchor=tk.CENTER)
    
    cTk.CTkButton(master=frame2,
        text="999",
        height=50,
        width=140,
        font=('Roboto black',55),
        image=icon,
        compound='top',
        border_spacing=5,
        fg_color="#ff6347"
    ).place(relx=0.75,rely=0.5,anchor=tk.CENTER)
    
    
    
    cTk.CTkButton(master=frame2,
        text="999",
        height=50,
        width=140,
        font=('Roboto black',55),
        image=icon,
        compound='top',
        border_spacing=5,
        fg_color="#E5AA70"
    ).place(relx=0.25,rely=0.8,anchor=tk.CENTER)
    
    cTk.CTkButton(master=frame2,
        text="999",
        height=50,
        width=140,
        font=('Roboto black',55),
        image=icon,
        compound='top',
        border_spacing=5,
        fg_color="#007DFF",
        command=lambda:load_frame3()
    ).place(relx=0.75,rely=0.8,anchor=tk.CENTER)

load_frame1and2()

root.mainloop()
