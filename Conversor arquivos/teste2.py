import customtkinter as ctk
from pdf2docx import Converter
from tkinter import filedialog, messagebox

janela = ctk.CTk()
janela.geometry("1080x600")
janela.maxsize(1080, 600)
janela.minsize(1080, 600)
janela.title("")
janela._set_appearance_mode("system")   

frame1= ctk.CTkFrame(master=janela, width=500, height=100).place(x=290, y=30)

frame2= ctk.CTkFrame(master=janela, width=1040, height=430).place(x=20, y=150)

















janela.mainloop()
