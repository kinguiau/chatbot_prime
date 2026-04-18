from google import genai
import json,os 

client = genai.Client(api_key="API_KEY")
a=True

busca = os.path.dirname(__file__)
caminho_json = os.path.join(busca, "json")

while a==True:

    frase = str(input("//"))
    response = client.models.generate_content(model="gemini-3.1-flash-lite-preview", contents='responda como o Optimus Prime:'+ frase)
    print(response.text)
    with open(os.path.join(caminho_json, "resposta.json"), "w", encoding="utf-8") as arquivo:
     json.dump(response.text, arquivo, ensure_ascii=False, indent=4)
   
