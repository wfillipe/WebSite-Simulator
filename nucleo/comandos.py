from nucleo.estrutura_sites import EstruturaSites
from pathlib import Path
from tkinter import messagebox

estrutura = EstruturaSites()

def pesquisa(url_digitada):
    url = url_digitada.strip()

    # Comando de ajuda
    if url == "#help":
        return (
            "━━━━━━━━━━  AJUDA  ━━━━━━━━━━\n"
            "Comandos disponíveis:\n\n"
            "• #help\n"
            "• #back: retornar à página anterior\n\n"
            "• +add site\n"
            "  Exemplo: +add google.com\n\n"
            "• +addpagina site/pagina\n"
            "  Exemplo: +addpagina google.com/imagens\n\n"
            "• www.site.com ou www.site.com/pagina\n"
            "━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
        )

    # Adicionar site
    if url.startswith("+add "):
        dominio = url[5:].strip()
        if not dominio.startswith("www."):
            dominio = "www." + dominio

        if dominio in estrutura.listar_sites():
            return f"Site '{dominio}' já existe."

        estrutura.adicionar_site(dominio)
        return f"Site '{dominio}' adicionado com sucesso."

    # Adicionar página
    if url.startswith("+addpagina "):
        caminho = url[11:].strip()

        if "/" not in caminho:
            return "Formato inválido. Use: +addpagina site/pagina"

        dominio, pagina = caminho.split("/", 1)

        if not dominio.startswith("www."):
            dominio = "www." + dominio

        estrutura.adicionar_pagina(dominio, pagina)
        return f"Página '{pagina}' adicionada ao site '{dominio}'."

    # Acesso a site ou página
    if "/" in url:
        dominio, pagina = url.split("/", 1)
    else:
        dominio, pagina = url, ""

    if estrutura.existe_url(dominio, pagina):
        if pagina:
            return f"Página aberta: {dominio}/{pagina}"
        return f"Site aberto: {dominio}"

    messagebox.showerror(
        "Erro",
        f"URL '{url}' não encontrada.\n\n"
        f"Use +add ou +addpagina para cadastrar."
    )
    return ""
