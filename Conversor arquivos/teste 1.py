import customtkinter as ctk
from pdf2docx import Converter

janela = ctk.CTk()
janela.geometry("1080x600")
janela.maxsize(1080, 600)
janela.minsize(1080, 600)
janela.title("")
janela._set_appearance_mode("system")

frame1 = ctk.CTkFrame(master=janela, width=300, height=560).place(x=20, y=20)

frame2 = ctk.CTkFrame(master=janela, width= 700, height=350).place(x=350, y=230)

frame3 = ctk.CTkFrame(master=janela, width= 700, height=190).place(x=350, y=20)


botão1 = ctk.CTkButton(master=frame1, text="Pdf para word", width=200, height=50).place(x= 70, y=250)


def selecionar_arquivo():
    caminho_arquivo = ctk.filedialog.askopenfilename(title="Selecionar arquivo PDF", filetypes=[("Arquivos PDF", "*.pdf")])
    if caminho_arquivo:
        caminho_salvar = ctk.filedialog.asksaveasfilename(defaultextension=".docx", filetypes=[("Arquivos Word", "*.docx")])
        if caminho_salvar:
            converter = Converter(caminho_arquivo)
            converter.convert(caminho_salvar, start=0, end=None)
            converter.close()
            ctk.messagebox.showinfo("Sucesso", "Arquivo convertido com sucesso!")
botão2 = ctk.CTkButton(master=frame1, text="Selecionar arquivo", width=200, height=50, command=selecionar_arquivo).place(x= 600, y=100)




janela.mainloop()
