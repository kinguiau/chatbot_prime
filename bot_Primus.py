import nltk, pygame,json,time
from nltk.chat.util import Chat, reflections

pygame.mixer.init()
pygame.init()




discursos = [
 "Sem o Allspark não podemos levar a vida de volta ao nosso planeta.\n Então o destino trouxe sua recompensa. Um novo mundo para chamarmos de casa.\n Vivemos entre os humanos agora, sempre escondidos, mas vigiando eles em segredo.\n Esperando, protegendo. Eu testemunhei a capacidade e a coragem deles.\n E embora sejamos de mundos distintos, como nós eles são mais do que os olhos podem ver.\n Eu sou Optimus Prime. E mando esta mensagem para qualquer Autobot sobrevivente que esteja refugiando entre as estrelas.\n Nós estamos aqui. Nós estamos esperando",
 "Nossas espécies unidas por um passado há muito esquecido e aliadas para enfrentar o futuro.\n Eu sou Optimus Prime e deixo esta mensagem para que nossas histórias sejam lembradas.\n Pois nestas memórias seremos eternos",
 "Em qualquer guerra, a calmaria vem entre as tempestades.\n Terão dias em que perderemos a fé, dias em que nossos aliados se voltarão contra nós,\n mas nunca chegará o dia em que deixaremos este planeta e seu povo.",
 "Existem mistérios no Universo que nunca desvendaremos, mas quem nós somos e por que estamos aqui não faz parte desses segredos,\n as respostas carregamos dentro de nós. Eu sou Optimus Prime, e essa mensagem é para meus criadores:\n deixem o Planeta Terra em paz, porque estou indo pegar vocês.",
 "Na essência de todas as lendas existe uma verdade, alguns poucos bravos unidos para salvar seus mundos, podemos ser heróis em nossa própria vida, cada um de nós, se tivermos coragem para tentar. Nossos destinos sempre estiveram interligados, mas agora, nossos mundos nos uniram num só. Temos que concertar nossos planetas e trabalhar juntos se quisermos sobreviver. Um segredo perigoso está enterrado no interior da terra, neste planeta há mais do que os olhos podem ver. Eu sou Optimus Prime, chamando todos os Autobots, está na hora de vir para casa."
]

grupos = {
 "Sem o Allspark não podemos levar a vida de volta ao nosso planeta.\n Então o destino trouxe sua recompensa. Um novo mundo para chamarmos de casa.\n Vivemos entre os humanos agora, sempre escondidos, mas vigiando eles em segredo.\n Esperando, protegendo. Eu testemunhei a capacidade e a coragem deles.\n E embora sejamos de mundos distintos, como nós eles são mais do que os olhos podem ver.\n Eu sou Optimus Prime. E mando esta mensagem para qualquer Autobot sobrevivente que esteja refugiando entre as estrelas.\n Nós estamos aqui. Nós estamos esperando":'bot\cybertron\Discurso do Optimus prime (Transformers 1) #1.mp3',
 "Nossas espécies unidas por um passado há muito esquecido e aliadas para enfrentar o futuro.\n Eu sou Optimus Prime e deixo esta mensagem para que nossas histórias sejam lembradas.\n Pois nestas memórias seremos eternos":'bot\cybertron\Discurso do Optimus prime (Transformers 2) #2.mp3',
 "Em qualquer guerra, a calmaria vem entre as tempestades.\n Terão dias em que perderemos a fé, dias em que nossos aliados se voltarão contra nós,\n mas nunca chegará o dia em que deixaremos este planeta e seu povo.":'bot\cybertron\Discurso do Optimus prime (Transformers 3) #3.mp3',
 "Existem mistérios no Universo que nunca desvendaremos, mas quem nós somos e por que estamos aqui não faz parte desses segredos,\n as respostas carregamos dentro de nós. Eu sou Optimus Prime, e essa mensagem é para meus criadores:\n deixem o Planeta Terra em paz, porque estou indo pegar vocês.":'bot\cybertron\Discurso do Optimus prime (Transformers 4) #4.mp3',
 "Na essência de todas as lendas existe uma verdade, alguns poucos bravos unidos para salvar seus mundos, podemos ser heróis em nossa própria vida, cada um de nós, se tivermos coragem para tentar. Nossos destinos sempre estiveram interligados, mas agora, nossos mundos nos uniram num só. Temos que concertar nossos planetas e trabalhar juntos se quisermos sobreviver. Um segredo perigoso está enterrado no interior da terra, neste planeta há mais do que os olhos podem ver. Eu sou Optimus Prime, chamando todos os Autobots, está na hora de vir para casa.":'bot\cybertron\Discurso do Optimus prime (Transformers 5) #5.mp3'
}

Pares = [
  [
    r"oi|ola|viado",["oi","saudações"]  
  ],
  [
    r"qual seu nome?|como você se chama?",["meu nome é PRIMUS","sou denominado PRIMUS"]  
  ],
  [
    r"mande a braba|farme aura|discurso", discursos
  ],
  [
    r"isso acaba aqui|comunicação encerrada|tchau|quitei|gg ez", ["olha que dialogo merda!!!"]
  ]
  ]

class Allspark:
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

    def iniciar(self):
        while True:
            try:
                chat = self.resposta.respond(str(input('-->')))

                if chat in discursos:
                    print(chat)
                    pygame.mixer.music.load(grupos[chat])
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


# 🔥 EXECUTA SÓ SE RODAR DIRETO
if __name__ == "__main__":
    bot = Allspark()
    bot.iniciar()