from tkinter import messagebox
from nucleo.estrutura_sites import EstruturaSites

estrutura = EstruturaSites()
historico = []  # Histórico centralizado aqui
<<<<<<< HEAD
<<<<<<< HEAD


<<<<<<< HEAD


def pesquisa(url_digitada):
    url = url_digitada.strip()    

    
    # Comando de ajuda
=======
def pesquisa(url_digitada):
    global historico
    url = url_digitada.strip()

>>>>>>> 1c7fa3f4a4be9ded3b53405310067810fc624b43
=======


def pesquisa(url_digitada):
    global historico
    url = url_digitada.strip()

>>>>>>> 1c7fa3f4a4be9ded3b53405310067810fc624b43
=======


def pesquisa(url_digitada):
    global historico
    url = url_digitada.strip()

>>>>>>> 1c7fa3f4a4be9ded3b53405310067810fc624b43
    if url == "#help":
        return {
            "mensagem": (
                "━━━━━━━━━━  AJUDA  ━━━━━━━━━━\n"
                "Comandos disponíveis:\n\n"
                "• #help\n"
                "• #back: voltar para a página anterior\n\n"
                "• +add site\n"
                "  Exemplo: +add google.com\n\n"
                "• +addpagina site/pagina\n"
                "  Exemplo: +addpagina google.com/imagens\n\n"
                "• www.site.com ou www.site.com/pagina\n"
                "━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
            ),
            "url": None
        }

    if url == "#back":
        if len(historico) <= 1:
            return {
                "mensagem": "Nenhuma página anterior no histórico.",
                "url": None
            }

        historico.pop()  # remove a atual
        pagina_anterior = historico[-1]
        return {
            "mensagem": f"Voltando para: {pagina_anterior}",
            "url": pagina_anterior
        }

    if url.startswith("+add "):
        dominio = url[5:].strip()
        if not dominio.startswith("www."):
            dominio = "www." + dominio

        if estrutura.existe_url(dominio):
            return {
                "mensagem": f"Site '{dominio}' já existe.",
                "url": None
            }

        estrutura.adicionar_site(dominio)
        return {
            "mensagem": f"Site '{dominio}' adicionado com sucesso.",
            "url": None
        }

    if url.startswith("+addpagina "):
        caminho = url[11:].strip()

        if "/" not in caminho:
            return {
                "mensagem": "Formato inválido. Use: +addpagina site/pagina",
                "url": None
            }

        dominio, pagina = caminho.split("/", 1)
        if not dominio.startswith("www."):
            dominio = "www." + dominio

        estrutura.adicionar_pagina(dominio, pagina)
        return {
            "mensagem": f"Página '{pagina}' adicionada ao site '{dominio}'.",
            "url": None
        }

    if "/" in url:
        dominio, pagina = url.split("/", 1)
    else:
        dominio, pagina = url, ""

    if estrutura.existe_url(dominio, pagina):
        pagina_completa = f"{dominio}/{pagina}" if pagina else dominio
        historico.append(pagina_completa)
        return {
            "mensagem": f"Página aberta: {pagina_completa}",
            "url": pagina_completa
        }

    messagebox.showerror(
        "Erro",
        f"URL '{url}' não encontrada.\n\n"
        f"Use +add ou +addpagina para cadastrar."
    )
    return {
        "mensagem": "",
        "url": None
    }
