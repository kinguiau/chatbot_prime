import nltk, pygame,json,time,os
import tkinter as tk
from tkinter import ttk
from nltk.chat.util import Chat, reflections
from PIL import Image, ImageTk

pygame.mixer.init()
pygame.init()
busca = os.path.dirname(__file__)

with open(os.path.join(busca, 'text.json'), "r", encoding="utf-8") as f:
    dados = json.load(f)

Pares = [
  [
    r"oi|ola|viado|bom dia",["oi","saudações"]  
  ],
  [
    r"puto|disgraça|arrombado",["não foi o que tua mãe disse","bem tu seu arrombado de merda, fela da puta disgraçado","tua mãe é minha"]
  ],
  [
    r"uau",["que massa","que legal"]
  ],
  [
    r"qual seu nome?|como você se chama?",["meu nome é PRIMUS","sou denominado PRIMUS"]  
  ],
  [
    r"mande a braba|farme aura|discurso", dados["discursos"]
  ],
  [
    r"isso acaba aqui|comunicação encerrada|tchau|quitei|gg ez", ["olha que dialogo merda!!!"]
  ]
  ]

root = tk.Tk()
root.title("Que desperte Optimus Prime")
ttk.Style().configure("Barra_Carregar.TLabel", background="blue", foreground="blue")
ttk.Style().configure("Remover_Fundo.TLabel", background="#696969", foreground="black")
frm = ttk.Frame(root, style='Remover_Fundo.TLabel', padding=60)
frm.grid()

class Unicron:
    def __init__(self):
        self.resposta = Chat(Pares, reflections)


        caminho = os.path.join(busca, "lilith 1.png")

        img = Image.open(caminho)
        img = img.resize((200, 120))  # (largura, altura)

        self.img = ImageTk.PhotoImage(img)

        self.imagem = ttk.Label(frm, image=self.img)
        self.imagem.grid(column=0, row=0)
        self.imagem.lower()

        ttk.Label(frm, text="autobots").grid(column=0, row=0)

        self.label = ttk.Label(frm, text="carregando")
        self.label.grid(column=0, row=2)

        self.comando = ttk.Label(frm, text="")
        self.comando.grid(column=0, row=5)

        self.barra = ttk.Label(frm, text="", style="Barra_Carregar.TLabel")
        self.barra.grid(column=0, row=3)

        self.resposta_label = ttk.Label(frm, text="")
        self.resposta_label.grid(column=0, row=6)
        
        self.entrada = tk.StringVar()
        
        self.conversa = ttk.Entry(frm, textvariable=self.entrada)
        
        self.button = ttk.Button(frm, text="<>", command=self.megatron)
    
        self.animar()
    
    
    def animar(self, pontos=0):
        if pontos <= 3:
            self.label.config(text="carregando" + "." * pontos, font= 30)
            self.barra.config(text="_____" * (pontos + 1))
            root.after(500, lambda: self.animar(pontos + 1))
        
        else:
            self.label.config(text="operando", font=22)
            self.conversa.grid(column=0, row=3)
            self.button.grid(column=0, row=4)
    
    def megatron(self):
        texto= self.entrada.get()
        self.comando.config(text="vc: {}".format(texto))
        chat = self.resposta.respond(texto)
        
        if chat in dados["discursos"]:
            self.resposta_label.config(text=chat)
            pygame.mixer.music.load(os.path.join(busca, dados['grupos'][chat]))
            pygame.mixer.music.play()
            pygame.mixer.music.get_busy()
                        
                    

        elif chat in ["olha que dialogo merda!!!"]:
            self.resposta_label.config(text=chat)
            root.after(3000,root.destroy)
            

        elif chat == None:
            self.resposta_label.config(text="isso está fora das interações")

        else:
            self.resposta_label.config(text=chat)



#ttk.Label(frm, text="Hello World!" ).grid(column=0, row=0)







if __name__ == "__main__":
    
    Unicron()
    root.mainloop()
    