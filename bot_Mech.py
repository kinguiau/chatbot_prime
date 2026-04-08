from google import genai
import json,os 

client = genai.Client(api_key="API_KEY")
a=True






while a==True:

    frase = str(input("//"))
    response = client.models.generate_content(model="gemini-3-flash-preview", 
               contents='responda como o Optimus Prime:'+ frase)
    print(response.text)
    with open(os.path.join(os.path.dirname(__file__), "resposta.json"), "w", encoding="utf-8") as arquivo:
     json.dump(response.text, arquivo, ensure_ascii=False, indent=4)
    if KeyboardInterrupt:
        a=False
