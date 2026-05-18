from google import genai
import json,os
import customtkinter as ctk

etapa=0

busca = os.path.dirname(__file__)
caminho_json = os.path.join(busca, "json")

janela = ctk.CTk()
janela.geometry("600x500")

texto = ctk.CTkEntry(janela, placeholder_text="xxxx",width=280)
texto.pack()


frame_scroll = ctk.CTkScrollableFrame(janela,width=310)
frame_scroll.pack()

resposta = ctk.CTkTextbox(frame_scroll, width=310,wrap="word")
resposta.pack()


def bot(event=None):
    with open(os.path.join(caminho_json,"resposta.json"), "r", encoding="utf-8") as f:
     dados = json.load(f)
    
    etapa=1
    print(etapa)
    frase = texto.get()
    response = client.models.generate_content(model="gemini-3.1-flash-lite-preview", contents='responda como o Optimus Prime:'+ frase)
    
    etapa=2
    print(etapa)

    resposta.configure(state="normal")
    resposta.delete("0.0", "end")
    resposta.insert("0.0", response.text)
    resposta.configure(state="disabled")
    etapa=3
    print(etapa)
    dados["responses"].append(response.text)

    with open(os.path.join(caminho_json, "resposta.json"), "w", encoding="utf-8") as arquivo:
     json.dump(dados, arquivo, ensure_ascii=False, indent=4)



texto.bind("<Return>", bot)
    
   
janela.mainloop()