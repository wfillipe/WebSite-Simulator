from pathlib import Path
from tkinter import messagebox

estrutura = EstruturaSites()
historico = []  # Historico centralizado aqui


def pesquisa(url_digitada):
    url = url_digitada.strip()

    # Comando de ajuda
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
                "• #sair: para encerrar o programa\n"
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
        nova_url = url[5:].strip()

        if not nova_url.startswith("www."):
            nova_url = "www." + nova_url

        sites = carregar_sites()

        if nova_url in sites:
            return f"Site '{nova_url}' já existe."

        with open(SITES_FILE, 'a', encoding='utf-8') as f:
            f.write(f"\n{nova_url}")
            return f"Site '{nova_url}' adicionado com sucesso."

    sites = carregar_sites()
    if url in sites:
        return f"Site aberto: {url}\n"

    messagebox.showerror(
        "Erro",
        f"Site '{url}' não encontrado.\n\n"
        f"Use '+add {url}' para adicionar à lista."
    )
    return ""
