#frontend
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox,filedialog
import time
from Model.model import *
from PIL import Image, ImageTk

class View:
    def __init__(self,master):
        self.master = master
        style = ttk.Style()
        style.theme_use("alt")
        style.configure(
            "TButton",
            font = ("Arial", 14),
            padding=6,
            relief="flat",
            foreground = "white",
            background="#6d7575",
            activeforeground="white",
            activebackground="#6d7575"
        )
def menu_principal():
    janela_main = tk.Tk()
    janela_main.title("Menu")
    janela_main.geometry("400x300")

    def menu_reconhecer():
        em_treino()


    def sair():
        janela_main.destroy()
    
    botao_comecar = tk.Button(janela_main, text="Reconhecimento Facial", font=("Arial", 15), command=menu_reconhecer)
    botao_comecar.pack(pady=20)
    
    botao_sair = tk.Button(janela_main, text="Sair", font=("Arial", 15), command=sair)
    botao_sair.pack(pady=20)

    janela_main.mainloop()

def em_treino():
    root = tk.Tk()
    root.title("Janela de treino")
    root.geometry("400x300")
    
    label = tk.Label(root, text="A treinar a ferramenta", font=("Arial", 20))
    label.pack(padx=20, pady=20)

    def proxima_janela():
        root.destroy()
        upload()



    def comecar_treino():
        if treino:  
            root.after(1000, proxima_janela)  
        else:
            label.config(text="Erro durante o treino!")

    comecar_treino()
    root.mainloop()

def upload():

    janela_upload = tk.Tk()
    janela_upload.title("Carregar Imagem")
    janela_upload.geometry("400x300")
    
    def carregar_imagem():

        ficheiro = selecionar_foto()
        
        if ficheiro:
            
            upload2(ficheiro)
            janela_upload.destroy()


    upload_button = tk.Button(janela_upload, text="Selecionar Imagem", font=("Arial", 15), command=carregar_imagem)
    upload_button.pack(expand=True)

    janela_upload.mainloop()
def upload2(ficheiro):
    janela_upload2 = tk.Toplevel()
    janela_upload2.title("Opções")
    janela_upload2.geometry("800x600")
    imagem = Image.open(ficheiro)
    imagem = imagem.resize((200,200), Image.Resampling.LANCZOS)
    imagem = ImageTk.PhotoImage(imagem)
    imagem_label = tk.Label(janela_upload2,image=imagem,bg="Black")
    imagem_label.pack(pady=(50,20))

    def usar_reconhecimento():
        resultados(ficheiro)  
    
    def pixel(ficheiro):
        pixelizado = pixelizacao(ficheiro)
        pasta = os.path.join("Fotos de Treino", "temp1.jpg")
        cv2.imwrite(pasta,pixelizado)
        janela_upload2.destroy()
        upload2(pasta)
        

    def cancelar():
        janela_upload2.destroy() 


    proceed_button = tk.Button(janela_upload2, text="Usar Reconhecimento facial", font=("Arial", 14), command=usar_reconhecimento)
    proceed_button.pack(pady=20)

    pixel_button = tk.Button(janela_upload2, text="Pixelizar foto", font=("Arial", 14), command=lambda: pixel(ficheiro))
    pixel_button.pack(pady=20)

    cancel_button = tk.Button(janela_upload2, text="Cancelar", font=("Arial", 14), command=cancelar)
    cancel_button.pack(pady=20)

    janela_upload2.mainloop()
def resultados(ficheiro):
    janela_resultados = tk.Tk()
    janela_resultados.title("Reconhecimento Facial Completo.")
    janela_resultados.geometry("600x450")
    sujeito,confianca= reconhecimento_facial(ficheiro)
    emocao,emocao_confianca= reconhecimento_emocao(ficheiro)
    values = {
        "Sujeito detectado": sujeito,
        "Confiança": f"{round(100-confianca,2)}%",
        "Emoção": emocao,
        "Confiança Emoção": f"{round(100-emocao_confianca,2)}%"
    }
    label = tk.Label(janela_resultados, text="Reconhecimento Completo\n", font=("Arial", 20))
    label.pack(padx=20, pady=20)
    
    for key, value in values.items():
        value_label = tk.Label(janela_resultados, text=f"{key}: {value}", font=("Arial", 12))
        value_label.pack(padx=10, pady=5)
    
    def fechar():
        janela_resultados.destroy()

    fechar_botao = tk.Button(janela_resultados,text= "Fechar",font=("Arial",14),command=fechar)
    fechar_botao.pack(pady=20)
    janela_resultados.mainloop()
def main():
    treino()
    menu_principal()
