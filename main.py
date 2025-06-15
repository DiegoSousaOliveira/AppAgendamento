import flet as ft
from views.telaLogin import Login
from views.telaHome import Home
from views.telaCadastro import Cadastro
from views.telaConsultas import Consultas, CancelarConsultaView
from views.TelaAgendamento import Agendamento

def home_page(page: ft.Page, logo: ft.Image, title: str, bgcolor: str):
    home = Home(page, logo, title, bgcolor)
    page.views.append(home)

def login_page(page: ft.Page, logo: ft.Image, title: str, bgcolor: str):
    login = Login(page, logo, title, bgcolor)
    page.views.append(login)

def registration_page(page: ft.Page, logo: ft.Image, title: str, bgcolor: str):
    cadastro = Cadastro(page, logo, title, bgcolor)
    page.views.append(cadastro)

def consultation_page(page: ft.Page):
    consultation = Consultas(page)
    page.views.append(consultation)

def cancel_appointment_page(page: ft.Page):
    consultation = CancelarConsultaView(page)
    page.views.append(consultation)

def schedule_appointment_page(page: ft.Page):
    schedule_appointment = Agendamento(page)
    page.views.append(schedule_appointment)

def main(page: ft.Page):
    # Configurações globais
    title = "HugoMed"
    bgcolor = "#e0e0e0"
    logo = ft.Image(src=r"img\logo.png", width=50, height=50)

    # Controle de rotas
    def route_change(route):
        page.views.clear()

        if page.route == "/home":
            home_page(page, logo, title, bgcolor)
        elif page.route == "/cadastro":
            registration_page(page, logo, title, bgcolor)

        elif page.route == "/agendarConsulta":
            schedule_appointment_page(page)

        elif page.route == "/CancelamentoConsulta":
            cancel_appointment_page(page)

        elif page.route == "/listaConsultas":
            consultation_page(page)

        else:
            login_page(page, logo, title, bgcolor)

        page.update()

    page.on_route_change = route_change
    page.go("/login")

# App inicial
ft.app(target=main, assets_dir="assets")
