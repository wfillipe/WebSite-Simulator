from pathlib import Path
from tkinter import messagebox

BASE_DIR = Path(__file__).resolve().parent.parent
SITES_FILE = BASE_DIR / "dados" / "sites.txt"


def carregar_sites():
    if not SITES_FILE.exists():
        return []
    return SITES_FILE.read_text(encoding="utf-8").splitlines()


def pesquisa(url_digitada):
    url = url_digitada.strip()

    # Comando de ajuda
    if url == "#help":
        return (
            "━━━━━━━━━━  AJUDA  ━━━━━━━━━━\n"
            "Comandos disponíveis:\n\n"
            "• #help\n"
            "• #back: retornar à página anterior\n"
            "  Mostra esta tela de ajuda.\n\n"
            "• +add site\n"
            "  Adiciona um site à lista.\n"
            "  Exemplo: +add google.com\n\n"
            "• www.site.com\n"
            "  Abre um site já cadastrado.\n"
            "━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
        )

    # Comando para adicionar URLs
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
