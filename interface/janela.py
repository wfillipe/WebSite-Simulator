from tkinter import *


def iniciar_janela(funcao_pesquisa): #FUNÇÃO DA INTERFACE GRÁFICA

    navegador1 = Tk()
    navegador1.title("Navegador v0.1")
    navegador1.geometry("400x450")

    texto1 = Label(navegador1, text="Histórico de Visitas: [ ]")
    texto1.grid(column=0, row=0)

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

   
    def ao_clicar():  #FUNÇÃO DO BOTÃO BUSCAR
        texto = funcao_pesquisa(entrada.get())
        resultado.config(text=texto)

    botao = Button(navegador1, text='Buscar', command=ao_clicar)
    botao.grid(column=0, row=6)

    navegador1.mainloop()
