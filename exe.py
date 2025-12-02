from interface.janela import iniciar_janela #Importa a função da interface gráfica na pasta interface 
from nucleo.comandos import pesquisa # Importa o  +add

'''
BASE_DIR = Path(__file__).resolve().parent #código antigo que foi modificado/movido para outro lugar
caminho = BASE_DIR / "dados" / "sites.txt"
sites_validos = caminho.read_text().splitlines()


def pesquisa(url_digitada):
    url = url_digitada.strip()

    if url in sites_validos:
        return "Site aberto: " + url
    else:
        messagebox.showerror("Erro", "Site inválido")
'''
        

if __name__ == "__main__": #código para executar todo o programa 
    iniciar_janela(pesquisa)




