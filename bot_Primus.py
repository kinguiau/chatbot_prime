import nltk, pygame,json,time,os
import tkinter as tk
from tkinter import ttk
from nltk.chat.util import Chat, reflections
from PIL import Image, ImageTk

pygame.mixer.init()
pygame.init()
busca = os.path.dirname(__file__)



"""discursos = [
 "Sem o Allspark não podemos levar a vida de volta ao nosso planeta.\n Então o destino trouxe sua recompensa. Um novo mundo para chamarmos de casa.\n Vivemos entre os humanos agora, sempre escondidos, mas vigiando eles em segredo.\n Esperando, protegendo. Eu testemunhei a capacidade e a coragem deles.\n E embora sejamos de mundos distintos, como nós eles são mais do que os olhos podem ver.\n Eu sou Optimus Prime. E mando esta mensagem para qualquer Autobot sobrevivente que esteja refugiando entre as estrelas.\n Nós estamos aqui. Nós estamos esperando",
 "Nossas espécies unidas por um passado há muito esquecido e aliadas para enfrentar o futuro.\n Eu sou Optimus Prime e deixo esta mensagem para que nossas histórias sejam lembradas.\n Pois nestas memórias seremos eternos",
 "Em qualquer guerra, a calmaria vem entre as tempestades.\n Terão dias em que perderemos a fé, dias em que nossos aliados se voltarão contra nós,\n mas nunca chegará o dia em que deixaremos este planeta e seu povo.",
 "Existem mistérios no Universo que nunca desvendaremos, mas quem nós somos e por que estamos aqui não faz parte desses segredos,\n as respostas carregamos dentro de nós. Eu sou Optimus Prime, e essa mensagem é para meus criadores:\n deixem o Planeta Terra em paz, porque estou indo pegar vocês.",
 "Na essência de todas as lendas existe uma verdade, alguns poucos bravos unidos para salvar seus mundos,\n podemos ser heróis em nossa própria vida, cada um de nós, se tivermos coragem para tentar.\n Nossos destinos sempre estiveram interligados, mas agora, nossos mundos nos uniram num só.\n Temos que concertar nossos planetas e trabalhar juntos se quisermos sobreviver. Um segredo perigoso está enterrado no interior da terra,\n neste planeta há mais do que os olhos podem ver. Eu sou Optimus Prime,\n chamando todos os Autobots, está na hora de vir para casa."
]

grupos = {
 "Sem o Allspark não podemos levar a vida de volta ao nosso planeta.\n Então o destino trouxe sua recompensa. Um novo mundo para chamarmos de casa.\n Vivemos entre os humanos agora, sempre escondidos, mas vigiando eles em segredo.\n Esperando, protegendo. Eu testemunhei a capacidade e a coragem deles.\n E embora sejamos de mundos distintos, como nós eles são mais do que os olhos podem ver.\n Eu sou Optimus Prime. E mando esta mensagem para qualquer Autobot sobrevivente que esteja refugiando entre as estrelas.\n Nós estamos aqui. Nós estamos esperando":os.path.join(busca, 'Discurso do Optimus prime (Transformers 1) #1.mp3'),
 "Nossas espécies unidas por um passado há muito esquecido e aliadas para enfrentar o futuro.\n Eu sou Optimus Prime e deixo esta mensagem para que nossas histórias sejam lembradas.\n Pois nestas memórias seremos eternos":os.path.join(busca, 'Discurso do Optimus prime (Transformers 2) #2.mp3'),
 "Em qualquer guerra, a calmaria vem entre as tempestades.\n Terão dias em que perderemos a fé, dias em que nossos aliados se voltarão contra nós,\n mas nunca chegará o dia em que deixaremos este planeta e seu povo.":os.path.join(busca, 'Discurso do Optimus prime (Transformers 3) #3.mp3'),
 "Existem mistérios no Universo que nunca desvendaremos, mas quem nós somos e por que estamos aqui não faz parte desses segredos,\n as respostas carregamos dentro de nós. Eu sou Optimus Prime, e essa mensagem é para meus criadores:\n deixem o Planeta Terra em paz, porque estou indo pegar vocês.":os.path.join(busca, 'Discurso do Optimus prime (Transformers 4) #4.mp3'),
 "Na essência de todas as lendas existe uma verdade, alguns poucos bravos unidos para salvar seus mundos,\n podemos ser heróis em nossa própria vida, cada um de nós, se tivermos coragem para tentar.\n Nossos destinos sempre estiveram interligados, mas agora, nossos mundos nos uniram num só.\n Temos que concertar nossos planetas e trabalhar juntos se quisermos sobreviver. Um segredo perigoso está enterrado no interior da terra,\n neste planeta há mais do que os olhos podem ver. Eu sou Optimus Prime,\n chamando todos os Autobots, está na hora de vir para casa.":os.path.join(busca, 'Discurso do Optimus prime (Transformers 5) #5.mp3')
}"""

with open(os.path.join(busca, 'text.json'), "r", encoding="utf-8") as f:
    dados = json.load(f)



Pares = [
  [
    r"oi|ola|viado|bom dia",["oi","saudações"]  
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

class Primus:
    def __init__(self):
        print("carregando", end="", flush=True)
        time.sleep(1)
        print(".", end="", flush=True)
        time.sleep(0.3)
        print(".", end="", flush=True)
        time.sleep(0.3)
        print(".")
        print("operando")

        self.resposta = Chat(Pares, reflections)

    def prime(self):
        while True:
            try:
                chat = self.resposta.respond(str(input('-->')))

                if chat in dados["discursos"]:
                    print(chat)
                    pygame.mixer.music.load(dados["grupos"][chat])
                    pygame.mixer.music.play()
                    while pygame.mixer.music.get_busy():
                        time.sleep(0.5)
                    continue

                elif chat in ["olha que dialogo merda!!!"]:
                    print(chat)
                    break

            except KeyboardInterrupt:
                break

            else:
                print(chat)

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
    #Primus().prime()
    Unicron()
    root.mainloop()
    