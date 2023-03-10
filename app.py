from PIL import ImageTk
import tkinter as tk
import customtkinter as cTk
root = tk.Tk()

root.title('Helpline')
root.eval('tk::PlaceWindow . center')
root['bg']='#ffffff'
#root.geometry('500x750+'+str(root.winfo_screenwidth()//2)+'+'+str(int(root.winfo_screenheight()*0.1)))

frame1 = tk.Frame(root, height=350, width=500,bg="#ffffff")
frame1.place(relx=0.5,rely=0.35,anchor=tk.CENTER)
#grid(row=0,column=0)
#pack(side='top',fill='both')
frame1.pack_propagate(False)

logo = ImageTk.PhotoImage(file='./assets/banner2.jpg')
logo_widget = tk.Label(frame1,image=logo,bg="#ffffff")
logo_widget.image=logo
logo_widget.pack()


tk.Label(frame1,
text="All Helplines are hear",
bg="#ffffff",
fg="#000000",
font=("TkMenuFont",12),
pady=25).pack()

frame2=tk.Frame(root,width=500,height=400,bg="#ffffff")
frame2.place(relx=0.5,rely=0.6,anchor=tk.CENTER)
#frame2.pack(side='top',fill='both')
frame2.grid_propagate(False)

#button = cTk.CTkButton(master=frame1, text="CTkButton", command=None)
#button.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

cTk.CTkButton(master=frame2,
text="999",
height=50,
width=140,
font=('TkMenuFont',30)
).place(relx=0.5,rely=0.3,anchor=tk.CENTER)
cTk.CTkButton(master=frame2,
text="999",
height=50,
width=140,
font=('TkMenuFont',30)
).place(relx=0.2,rely=0.3,anchor=tk.CENTER)
cTk.CTkButton(master=frame2,
text="999",
height=50,
width=140,
font=('TkMenuFont',30)
).place(relx=0.8,rely=0.3,anchor=tk.CENTER)


cTk.CTkButton(master=frame2,
text="999",
height=50,
width=140,
font=('TkMenuFont',30)
).place(relx=0.5,rely=0.6,anchor=tk.CENTER)
cTk.CTkButton(master=frame2,
text="999",
height=50,
width=140,
font=('TkMenuFont',30)
).place(relx=0.2,rely=0.6,anchor=tk.CENTER)
cTk.CTkButton(master=frame2,
text="999",
height=50,
width=140,
font=('TkMenuFont',30)
).place(relx=0.8,rely=0.6,anchor=tk.CENTER)



root.mainloop()
