import nltk, pygame,json,time,os
import tkinter as tk
from tkinter import ttk
from nltk.chat.util import Chat, reflections
from PIL import Image, ImageTk


pygame.mixer.init()
pygame.init()
busca = os.path.dirname(__file__)
caminho_json = os.path.join(busca, "json")
caminho_lilith = os.path.join(busca, "lilith")
caminho_discursos = os.path.join(busca, "optimus")

with open(os.path.join(caminho_json,'text.json'), "r", encoding="utf-8") as f:
    dados = json.load(f)

Pares = [
  [
    r"oi|ola|viado|bom dia",dados["saudacoes"]  
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



caminho = os.path.join(caminho_lilith, "lilith 1.png")
img = Image.open(caminho)
img = img.resize((200, 120))


class Unicron:
    def __init__(self):
        self.resposta = Chat(Pares, reflections)

        self.img = ImageTk.PhotoImage(img)
        self.imagem = ttk.Label(janela, image=self.img)  #imagem da lilith
        self.imagem.pack(pady=n)


        self.cabeca = ttk.Label(janela, text="autobots",font=18) #frase autobots
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
        chat = "chat: "+self.resposta.respond(texto.lower()) #chama a reação do bot
        self.resposta_label.pack(pady=(n+int(6))) #resposta do bot

        if chat in dados["discursos"]: #tocar discursos
            self.resposta_label.config(text=chat)
            pygame.mixer.music.load(os.path.join(caminho_discursos, dados['grupos'][chat])) 
            pygame.mixer.music.play()
            pygame.mixer.music.get_busy()
                        
                    

        elif chat in ["olha que dialogo merda!!!"]:   #fechar de forma dramatica
            self.resposta_label.config(text=chat)
            janela.after(3000,janela.destroy)
            

        elif chat == None:     #caso o bot não tenha uma reação configurada
            self.resposta_label.config(text="isso está fora das interações")

        else:   #chamar reações normais do bot
            self.resposta_label.config(text=chat)



#ttk.Label(janela, text="Hello World!" ).grid(column=0, row=0)







if __name__ == "__main__":
    
    Unicron()
    janela.mainloop()
    