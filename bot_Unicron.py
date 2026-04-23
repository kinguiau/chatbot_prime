import json,time,os,pygame
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from bot_reactions import reagir


busca = os.path.dirname(__file__)
caminho_json = os.path.join(busca, "json")
caminho_lilith = os.path.join(busca, "lilith")


with open(os.path.join(caminho_json,'text.json'), "r", encoding="utf-8") as f:
    dados = json.load(f)


janela = tk.Tk()
janela.geometry("500x300")
janela.configure(bg="#696969")
janela.title("Que desperte Optimus Prime")


ttk.Style().configure("Barra_Carregar.TLabel", background="blue", foreground="blue")
ttk.Style().configure("Remover_Fundo.TLabel", background="#696969", foreground="black")
ttk.Style().configure("Entrada_Texto.TLabel",background="#949494",  foreground="black", borderwidth=1)
animation = "Barra_Carregar.TLabel"
cor_fundo = "Remover_Fundo.TLabel"
entrada_texto = "Entrada_Texto.TLabel"

n=int(0)


frm = ttk.Frame(janela)



caminho_imagem = os.path.join(caminho_lilith, "lilith 2.png")
img = Image.open(caminho_imagem)
img = img.resize((200, 200))


class Unicron:
    def __init__(self):
        

        self.img = ImageTk.PhotoImage(img)
        self.imagem = ttk.Label(janela, image=self.img)  #imagem da lilith
        self.imagem.pack(pady=n)


        self.cabeca = ttk.Label(janela, text="AUTOBOTS",font=("helvetica",18,"bold")) #frase autobots
        self.cabeca.pack(pady=(n+int(1)))


        self.aviso = ttk.Label(janela, text="carregando")
        self.aviso.pack(pady=(n+int(2)))
        
        
        self.barra = ttk.Label(janela, text="", style=animation)  #barra de loading
        self.barra.pack(pady=(n+int(3)))
        
        
        self.conversa = ttk.Entry(frm,style=entrada_texto, font=12) #caixa de texto
        
        self.button = ttk.Button(janela, text="<>", command=self.megatron) #envia o texto
        

        self.comando = ttk.Label(janela, text="") #última mensagem mandada para o bot
        


        self.resposta_label = ttk.Label(janela, text="") #resposta do chat
        
      
          
        self.animar()
    
    
    def animar(self, pontos=0):
        if pontos <= 3:
            self.aviso.config(text="carregando" + "." * pontos, font= 30)
            self.barra.config(text="_____" * (pontos + 1))
            janela.after(500, lambda: self.animar(pontos + 1))
        

        else:
            self.aviso.config(text="operando", font=22)
            self.barra.forget()
            frm.pack(pady=(n+int(3)))
            self.conversa.pack() #coloca caixa de texto
            self.button.pack(pady=(n+int(4)))   #coloca botão
            self.comando.pack(pady=(n+int(5)))  #coloca última mensagem mandada para o bot
    
    def megatron(self):
        texto= self.conversa.get()
        self.comando.config(text=f"vc: {texto}")
        
        self.resposta_label.pack(pady=(n+int(6))) #posição da resposta do bot

        if texto.lower() in dados['saudacao_user']: #falar uma saudação
            self.resposta_label.config(text=reagir().saudacao())

        elif texto.lower() in dados['denominacao_user']: #dizer nome
            self.resposta_label.config(text=reagir().denominacao())

        elif texto.lower() in dados["discurso_user"]: #tocar discursos
            self.escolha =reagir().escolha_discurso()
            self.resposta_label.config(text=self.escolha)
            reagir().discursar(self.escolha)
                      
        elif texto.lower() in dados["encerrar_user"]:   #fechar de forma dramatica
            self.resposta_label.config(text=dados['encerrar_bot'])
            janela.after(3000,janela.destroy)
          
        else:     #caso o bot não tenha uma reação configurada
            self.resposta_label.config(text="isso está fora das interações")

        



#ttk.Label(janela, text="Hello World!" ).grid(column=0, row=0)







if __name__ == "__main__":
    
    Unicron()
    janela.mainloop()
    