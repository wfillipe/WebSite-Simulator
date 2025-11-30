from tkinter import * #Importando toda a biblioteca de interface grafica 
from tkinter import messagebox



with open("sites.txt", "r") as i:
    sites_validos = [linha.strip() for linha in i]

def pesquisa():
    url = busca.get().strip()

    if url in sites_validos:
        resultado['text'] = 'Site aberto: ' + url

    else: 
        messagebox.showerror('site invalido')






navegador1 = Tk()  
navegador1.title("Navegador v0.1") 
navegador1.geometry("500x500")  


texto1 = Label(navegador1, text="Histórico de Visitas: [ ]")
texto1.grid(column=0,row=0)

texto2 = Label(navegador1, text="Home: [ ]")
texto2.grid(column=0, row=1)

texto3 = Label(navegador1, text="Digite a url ou #back para retornar à última página visitada.")
texto3.grid(column=0, row=2)

busca = Entry(navegador1) 
busca.grid(column=0, row=3)

botao = Button(navegador1, text='Buscar', command=pesquisa)
botao.grid(column=0, row=5)

resultado = Label(navegador1, text="")
resultado.grid(column=0, row=4)










navegador1.mainloop() 

