import customtkinter as ctk
janela = ctk.CTk()


janela.title("")
janela.geometry("700x400")
janela.minsize(width=500, height=300)


janela._set_appearance_mode("system")



def nova_tela():
    nova_janela = ctk.CTkToplevel(janela, fg_color="green")
    nova_janela.geometry("500x250")
btn_novatela = ctk.CTkButton(master=janela,  text="nova janela", command=nova_tela).place(x=300, y=100)

janela.mainloop()
 