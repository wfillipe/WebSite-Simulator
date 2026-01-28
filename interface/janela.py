from tkinter import * 
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent #No início eu tenho o mesmo código aqui e no comandos.py, serve para ler o arquivo sites.txt da pasta dados
SITES_FILE = BASE_DIR / "dados" / "sites.txt" 

def carregar_sites(): 
    if not SITES_FILE.exists(): #Carrega sites do arquivo .txt
        return 
    return SITES_FILE.read_text(encoding="utf-8").splitlines() 


def iniciar_janela(funcao_pesquisa): #Maior parte da formatação da janela do tkinter e também a função historico 
    historico = []
    global navegador1
    navegador1 = Tk()
    navegador1.title("Navegador v0.1")
    navegador1.geometry("400x450")

    historico_box = Listbox(navegador1, width=40, height=5)
    historico_box.grid(column=0, row=8, padx=10, pady=5)
 
    texto2 = Label(navegador1, text="Home: [ ]\n")
    texto2.grid(column=0, row=1) 

    texto3 = Label(navegador1, text="Digite a url ou #back para retornar à última página visitada.\n ")
    texto3.grid(column=0, row=2)

    entrada = Entry(navegador1)
    entrada.grid(column=0, row=3)

    texto4 = Label(navegador1, text="Digite +add site para adicionar um novo site")
    texto4.grid(column=0, row=4)

    resultado = Label(navegador1, text="")
    resultado.grid(column=0, row=5)

   
    def ao_clicar():
        url = entrada.get().strip()
        
        if url == "#sair":
            navegador1.quit()
            navegador1.destroy()
            return

        texto = funcao_pesquisa(url)
        resultado.config(text=texto)

        if texto.startswith("Site aberto:"):  #Se o site for válido, adiciona ao histórico
            historico.append(url)
            historico_box.insert(END, url)
        

        
    botao = Button(navegador1, text='Buscar', command=ao_clicar)
    botao.grid(column=0, row=6)

    navegador1.mainloop() #Código para o tkinter não fechar sozinho 
