from pathlib import Path
from tkinter import messagebox

BASE_DIR = Path(__file__).resolve().parent.parent #Aqui o python abre e lê o arquivo sites.txt na pasta dados
SITES_FILE = BASE_DIR / "dados" / "sites.txt" 

def carregar_sites(): #Carrega sites do arquivo
    
    try:
        if SITES_FILE.exists():
            with open(SITES_FILE, 'r', encoding='utf-8') as f:
                return [linha.strip() for linha in f if linha.strip()]
    except:
        pass 
    return []

def pesquisa(url_digitada): #Função principal: processa as urls
    
    url = url_digitada.strip()
    
    print(f"[SISTEMA] Comando: '{url}'")
    
   
    if url.startswith("+add "): # Comando para adicionar urls
        nova_url = url[5:].strip()
        
        # Formata
        if not nova_url.startswith("www."):
            nova_url = "www." + nova_url
        
        print(f"[SISTEMA] Adicionando: {nova_url}")
        
        
        sites = carregar_sites() # Verifica se já existe
        if nova_url in sites:
            messagebox.showinfo("Aviso", f"Site '{nova_url}' já existe!")
            return f"Site '{nova_url}' já existe."
        
        
        try:
            with open(SITES_FILE, 'a', encoding='utf-8') as f: # Cadastra as urls
                f.write(f"\n{nova_url}")
            
            print(f"[SISTEMA] ✓ Adicionado com sucesso!")
            messagebox.showinfo("Sucesso", f"Site '{nova_url}' adicionado!")
            return f"✅ Site '{nova_url}' adicionado!"
            
        except Exception as e:
            print(f"[SISTEMA] ✗ Erro: {e}")
            messagebox.showerror("Erro", f"Não foi possível adicionar: {e}")
            return "❌ Erro ao adicionar."
    
    
    sites = carregar_sites()
    
    if url in sites:
        return f"Site aberto: {url}"
    else:
        messagebox.showerror("Erro", 
            f"Site '{url}' não encontrado.\n\n"
            f"Use '+add {url}' para adicionar à lista.")
        return ""