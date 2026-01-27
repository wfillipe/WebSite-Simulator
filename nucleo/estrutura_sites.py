from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SITES_FILE = BASE_DIR / "dados" / "sites.txt"


class EstruturaSites:
    def __init__(self):
        self.sites = {}
        self._carregar_sites_do_arquivo()

    def _carregar_sites_do_arquivo(self):
        if not SITES_FILE.exists():
            return

        linhas = SITES_FILE.read_text(encoding="utf-8").splitlines()
        for site in linhas:
            site = site.strip()
            if site:
                self.sites[site] = set([""])  # "" representa a página inicial

    def adicionar_site(self, dominio):
        if dominio not in self.sites:
            self.sites[dominio] = set([""])
            with open(SITES_FILE, "a", encoding="utf-8") as f:
                f.write(f"\n{dominio}")

    def adicionar_pagina(self, dominio, pagina):
        self.adicionar_site(dominio)
        self.sites[dominio].add(pagina)

    def existe_url(self, dominio, pagina=""):
        return dominio in self.sites and pagina in self.sites[dominio]
