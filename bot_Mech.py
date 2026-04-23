from google import genai
import json,os 

busca = os.path.dirname(__file__)
caminho_json = os.path.join(busca, "json")

while True:
    with open(os.path.join(caminho_json,"resposta.json"), "r", encoding="utf-8") as f:
     dados = json.load(f)
    
    frase = str(input("//"))
    response = client.models.generate_content(model="gemini-3.1-flash-lite-preview", contents='responda como o Optimus Prime:'+ frase)
    print(response.text)
    
    dados["responses"].append(response.text)

    with open(os.path.join(caminho_json, "resposta.json"), "w", encoding="utf-8") as arquivo:
     json.dump(dados, arquivo, ensure_ascii=False, indent=4)
    
    
    
    
   
