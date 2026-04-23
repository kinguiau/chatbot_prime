import random,os,json,pygame




class reagir:
    def __init__(self):
     pygame.mixer.init()
     pygame.init()
     busca = os.path.dirname(__file__)
     self.caminho_json = os.path.join(busca, "json")
     self.caminho_discursos = os.path.join(busca, "optimus")
     with open(os.path.join(self.caminho_json,'text.json'), "r", encoding="utf-8") as f:
        self.dados = json.load(f)

    def saudacao(self):
        self.resposta=random.choice(self.dados['saudacao_bot'])
        return(self.resposta)
    def denominacao(self):
        self.resposta=random.choice(self.dados['denominacao_bot'])
        return(self.resposta)
    
    def escolha_discurso(self):
       return random.choice(self.dados["discursos_bot"])
       
    
    def discursar(self,escolha):
        pygame.mixer.music.load(os.path.join(self.caminho_discursos, self.dados['grupos'][escolha]))
        pygame.mixer.music.play()
        pygame.mixer.music.get_busy()
        
        




if __name__=="__main__":
 reagir()