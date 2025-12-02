from pathlib import Path
from tkinter import messagebox

BASE_DIR = Path(__file__).resolve().parent.parent #Aqui o python abre e lê o arquivo sites.txt na pasta dados
SITES_FILE = BASE_DIR / "dados" / "sites.txt" 




def carregar_sites(): #Carrega sites do arquivo .txt
    if not SITES_FILE.exists():
        return 
    return SITES_FILE.read_text(encoding="utf-8").splitlines()


def pesquisa(url_digitada): #Função principal: processa as urls
    historico = []
    url = url_digitada.strip()
    
    if url.startswith("+add "): #Comando para adicionar urls
        nova_url = url[5:].strip()
        
        if not nova_url.startswith("www."):  #Formatação do texto digitado
            nova_url = "www." + nova_url
        
        sites = carregar_sites()

        if nova_url in sites:  #Verifica se o site digitado já existe 
            historico.append(url)
            return f"Site '{nova_url}' já existe"
        
        
        with open(SITES_FILE, 'a', encoding='utf-8') as f: #Cadastra as novas urls 
            f.write(f"\n{nova_url}")
            return f" Site '{nova_url}' adicionado"
            
        
    
    
    sites = carregar_sites() #Aqui carrega as mensagens para o usuário de +add sites  
    if url in sites:
        return f"Site aberto: {url}\n"
    
    messagebox.showerror("Erro", 
        f"Site '{url}' não encontrado.\n\n"
        f"Use '+add {url}' para adicionar a lista.")
    return ""