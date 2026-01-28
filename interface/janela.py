from tkinter import *
from pathlib import Path


def iniciar_janela(funcao_pesquisa):
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
        resposta = funcao_pesquisa(url)
        resultado.config(text=resposta["mensagem"])

        if url == "#sair":
            navegador1.quit()
            navegador1.destroy()
            return
        
        if resposta["url"]:
            historico_box.insert(END, resposta["url"])

    botao = Button(navegador1, text='Buscar', command=ao_clicar)
    botao.grid(column=0, row=6)

    navegador1.mainloop()
