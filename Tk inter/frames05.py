import customtkinter as ctk
janela = ctk.CTk()


janela.title("")
janela.geometry("700x400")
janela.minsize(width=700, height=400)
janela._set_appearance_mode("system")


frame1 = ctk.CTkFrame(master=janela, width=200, height=330).place(x=10, y= 60)

janela.mainloop()
 