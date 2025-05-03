import flet as ft
from views.telaLogin import Login
from views.telaHome import Home

def pagina_home(page: ft.Page, logo: ft.Image, title: str, bgcolor: str):
    home = Home(page, logo, title, bgcolor)
    page.views.append(home)

def pagina_login(page: ft.Page, logo: ft.Image, title: str, bgcolor: str):
    login = Login(page, logo, title, bgcolor)
    page.views.append(login)


def main(page: ft.Page):
    # Configurações globais
    title = "HugoMed"
    bgcolor = "#e0e0e0"
    logo = ft.Image(src=r"img\logo.png", width=50, height=50)

    # Controle de rotas
    def route_change(route):
        page.views.clear()

        if page.route == "/home":
            pagina_home(page, logo, title, bgcolor)
        else:
            pagina_login(page, logo, title, bgcolor)

        page.update()

    page.on_route_change = route_change
    page.go("/login")

# App inicial
ft.app(target=main, assets_dir="assets")
