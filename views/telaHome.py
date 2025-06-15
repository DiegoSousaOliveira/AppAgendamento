import flet as ft

class Home(ft.View):
    def __init__(self, page: ft.Page, logo: ft.Image, title: str, bgcolor: str):
        super().__init__()
        self.route = "/home"
        self.page = page
        self.logo = logo
        self.title = title
        self.bgcolor = "#e0e0e0"

        self.drawer = ft.NavigationDrawer(
            on_dismiss=self.handle_dismissal,
            on_change=self.handle_change,
            controls=[
                ft.Container(height=12),
                ft.NavigationDrawerDestination(
                    label="Home",
                    icon=ft.icons.HOME_OUTLINED,
                    selected_icon=ft.icons.HOME
                ),
                ft.Divider(thickness=2),
                ft.NavigationDrawerDestination(
                    icon=ft.icons.CALENDAR_MONTH_OUTLINED,
                    label="Consultas",
                    selected_icon=ft.icons.CALENDAR_MONTH
                ),
                ft.NavigationDrawerDestination(
                    icon=ft.icons.LOCAL_HOSPITAL_OUTLINED,
                    label="Agendamento por Setor",
                    selected_icon=ft.icons.LOCAL_HOSPITAL
                ),
                ft.NavigationDrawerDestination(
                    icon=ft.icons.ACCESS_TIME_OUTLINED,
                    label="Agendamento Disponibilidade",
                    selected_icon=ft.icons.ACCESS_TIME
                ),
            ],
        )

        self.appbar = ft.AppBar(
            leading=ft.IconButton(ft.icons.MENU, icon_color=ft.colors.BLACK,on_click=lambda e: page.open(self.drawer)),
            leading_width=40,
            title=ft.Row(
                controls=[
                    self.logo,
                    ft.Text("HugoMed", size=22, weight=ft.FontWeight.BOLD, color="#2a688a")
                ],
                alignment=ft.MainAxisAlignment.START
            ),
            center_title=False,
            bgcolor="#dddddd",
            actions=[ft.IconButton(ft.icons.WB_SUNNY_OUTLINED, icon_color=ft.colors.BLACK)],
        )

        self.body = ft.SafeArea(
            ft.Column([
                ft.Container(
                    content=ft.Text(
                        "Cuidar da sua saúde nunca foi tão simples!",
                        size=20,
                        weight=ft.FontWeight.W_600,
                        color="#2a688a"
                    ),
                    alignment=ft.alignment.center,
                    margin=ft.margin.only(top=20, bottom=10)
                ),
                ft.Container(
                    content=ft.Text(
                        "O que você deseja?",
                        size=16,
                        color=ft.colors.BLACK87
                    ),
                    alignment=ft.alignment.center
                ),
                ft.Column(
                    controls=[
                        self.opcao_card(
                            "AGENDAR CONSULTA",
                            ft.icons.ADD_CIRCLE_OUTLINE,
                            "#f45557",
                            lambda e: self.page.go("/agendarConsulta")
                        ),
                        self.opcao_card(
                            "CANCELAR CONSULTA",
                            ft.icons.CANCEL_OUTLINED,
                            "#ff9a00",
                            lambda e: self.page.go("/CancelamentoConsulta")
                        ),
                        self.opcao_card(
                            "MINHAS CONSULTAS",
                            ft.icons.CALENDAR_VIEW_DAY_OUTLINED,
                            "#5e17eb",
                            lambda e: self.page.go("/listaConsultas")
                        ),
                    ],
                    spacing=25,
                    alignment=ft.MainAxisAlignment.CENTER,
                    expand=True
                ),
            ],
            alignment=ft.MainAxisAlignment.START,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            expand=True,
            )
        )

        self.controls = [
            self.appbar,
            self.body
        ]

    def opcao_card(self, titulo, icone, cor, ao_clicar):
        return ft.Container(
            content=ft.Row(
                [
                    ft.Icon(icone, color="white", size=30),
                    ft.Text(titulo, size=18, weight=ft.FontWeight.W_600, color="white")
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                spacing=15
            ),
            bgcolor=cor,
            height=90,
            border_radius=12,
            on_click=ao_clicar,
            width=300,
            shadow=ft.BoxShadow(blur_radius=6, color="#aaa"),
            padding=ft.padding.all(10),
        )

    def handle_dismissal(self, e):
        print("Drawer dismissed!")

    def handle_change(self, e):
        rotas = [
            "/home",
            "/consultas",
            "/agendamentoSetor",
            "/agendamentoDisponibilidade"
        ]
        index = int(e.control.selected_index)
        if index < len(rotas):
            self.page.go(rotas[index])
        self.page.close(self.drawer)
