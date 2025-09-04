import customtkinter as ctk
from pdf2docx import Converter
from tkinter import filedialog, messagebox

janela = ctk.CTk() # criando a janela
janela.geometry("1080x600") # definindo o tamanho da janela
janela.maxsize(1080, 600) # definindo o tamanho máximo da janela
janela.minsize(1080, 600) # definindo o tamanho mínimo da janela
janela.title("") # definindo o título da janela
janela._set_appearance_mode("system")   # definindo o modo de aparência da janela escuro,claro ou a que estiver no sistema


texto1= ctk.CTkLabel(master=janela, text="Conversor de arquivos", font=("Arial", 20),).place(x=680, y=30, anchor="n")# criando o título da janela

frame2= ctk.CTkFrame(master=janela, width=260, height=560).place(x=20, y=20)

frame3 = ctk.CTkFrame(master=janela, width=246, height=280).place(x=282, y=160)

frame4 = ctk.CTkFrame(master=janela, width=246, height=280).place(x=548, y=160)

frame5 = ctk.CTkFrame(master=janela, width=246, height=280).place(x=814, y=160)

texto2= ctk.CTkLabel(master=janela, text="Selecione o arquivo \nque deseja converter", font=("Arial", 20),).place(x=60, y=40)# criando o título da janela


def selecionar_docx(): # função para selecionar o arquivo docx
    arquivo_docx = filedialog.askopenfilename(filetypes=[("Arquivos Docx", "*.docx")]) # abre a janela para selecionar o arquivo docx
    if arquivo_docx: # se o arquivo docx for selecionado
        texto1= ctk.CTkLabel(master=frame2, text=f"Você selecionou o arquivo: {arquivo_docx}", font=("Arial", 12),).place(x=300, y=200) # exibe o caminho do arquivo docx selecionado
    else: # se o arquivo docx não for selecionado
        messagebox.showwarning("Nenhum Arquivo", "Nenhum arquivo foi selecionado.") # exibe uma mensagem de aviso

botao1= ctk.CTkButton(master=frame2, text="Selecionar arquivo docx", width=200, height=50, command=selecionar_docx).place(x=50, y=200)

def selecionar_pdf():
    arquivo_pdf = filedialog.askopenfilename(filetypes=[("Arquivos PDF", "*.pdf")]) # abre a janela para selecionar o arquivo pdf
    if arquivo_pdf: # se o arquivo pdf for selecionado
        messagebox.showinfo("Arquivo Selecionado", f"Você selecionou o arquivo: {arquivo_pdf}") # exibe o caminho do arquivo pdf selecionado
    else: # se o arquivo pdf não for selecionado
        messagebox.showwarning("Nenhum Arquivo", "Nenhum arquivo foi selecionado.") # exibe uma mensagem de aviso
botao2= ctk.CTkButton(master=frame2, text="Selecionar arquivo pdf", width=200, height=50, command=selecionar_pdf).place(x=50, y=270)


def converter_arquivo():
    caminho_arquivo = filedialog.askopenfilename(title="Selecionar arquivo PDF", filetypes=[("Arquivos PDF", "*.pdf")])
    if caminho_arquivo:
        caminho_salvar = filedialog.asksaveasfilename(defaultextension=".docx", filetypes=[("Arquivos Word", "*.docx")])
        if caminho_salvar:
            converter = Converter(caminho_arquivo)
            converter.convert(caminho_salvar, start=0, end=None)
            converter.close()
            messagebox.showinfo("Sucesso", "Arquivo convertido com sucesso!")
botao3= ctk.CTkButton(master=frame2, text="Converter", width=200, height=50).place(x=50, y=340)












janela.mainloop()
