import nltk, pygame,json,time,os
from nltk.chat.util import Chat, reflections


pygame.mixer.init()
pygame.init()
busca = os.path.dirname(__file__)

caminho_json = os.path.join(busca, "json")
caminho_discursos = os.path.join(busca, "optimus")

with open(os.path.join(caminho_json,'text.json'), "r", encoding="utf-8") as f:
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
                    pygame.mixer.music.load(os.path.join(caminho_discursos, dados['grupos'][chat]))
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

if __name__ == "__main__":
    Primus().prime()