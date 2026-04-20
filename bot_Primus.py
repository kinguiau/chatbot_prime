import json,time,os
from bot_reactions import reagir


busca = os.path.dirname(__file__)

caminho_json = os.path.join(busca, "json")
caminho_discursos = os.path.join(busca, "optimus")

with open(os.path.join(caminho_json,'text.json'), "r", encoding="utf-8") as f:
    dados = json.load(f)


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

        
        
    def prime(self):
        while True:
            try:
                texto=str(input('-->'))
                
                if texto.lower() in dados['saudacao_user']:
                    print(reagir().saudacao())
                
                elif texto.lower() in dados['nome_pergunta']:
                    print(reagir().denominacao())

                elif texto.lower() in dados["discurso_pedido"]:
                    self.resposta=reagir().escolha_discurso()
                    print(self.resposta)
                    reagir().discursar(self.resposta)
                    
                elif texto.lower() in dados["encerrar_user"]:
                    print("olha que dialogo merda!!!")
                    break

                else:
                    print("fora das opções")
            except KeyboardInterrupt:
                break

            

if __name__ == "__main__":
    Primus().prime()