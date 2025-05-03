import flet as ft

class Home(ft.View):
    def __init__(self, page: ft.Page, logo: ft.Image, title: str, bgcolor: str):
        super().__init__()
        self.route                  = "\home"
        self.page                   = page
        self.logo                   = logo
        self.title                  = title
        self.bgcolor                = bgcolor

        self.drawer = ft.NavigationDrawer(
            on_dismiss=self.handle_dismissal,
            on_change=self.handle_change,
            controls=[
                ft.Container(height=12),
                ft.NavigationDrawerDestination(
                    label="Item 1",
                    icon=ft.Icons.DOOR_BACK_DOOR_OUTLINED,
                    selected_icon=ft.Icon(ft.Icons.DOOR_BACK_DOOR),
                ),
                ft.Divider(thickness=2),
                ft.NavigationDrawerDestination(
                    icon=ft.Icon(ft.Icons.MAIL_OUTLINED),
                    label="Item 2",
                    selected_icon=ft.Icons.MAIL,
                ),
                ft.NavigationDrawerDestination(
                    icon=ft.Icon(ft.Icons.PHONE_OUTLINED),
                    label="Item 3",
                    selected_icon=ft.Icons.PHONE,
                ),
            ],
        )

        self.banner = ft.Row(
            controls=[logo, ft.Text("HugoMed")],
            expand=True,
            alignment=ft.MainAxisAlignment.CENTER
        )

        self.appbar = ft.AppBar(
            leading=ft.IconButton(ft.icons.MENU, on_click=lambda e: page.open(self.drawer)),
            leading_width=40,
            title=self.banner,
            center_title=False,
            bgcolor=ft.Colors.SURFACE_CONTAINER_HIGHEST,
            actions=[ft.IconButton(ft.Icons.WB_SUNNY_OUTLINED)],
        )

        self.body = ft.SafeArea(
            ft.Column([
                ft.Container(
                    content=ft.Text("Cuidar da sua saúde nunca foi tão simples!", color="#000000"),
                    expand=True,
                    alignment=ft.alignment.center,
                    margin=ft.margin.only(top=10)
                ),
                ft.Container(
                    content=ft.Text("O que você deseja?", color="#2a688a"),
                    expand=True,
                    alignment=ft.alignment.center,
                    margin=ft.margin.only(top=5, bottom=20)
                ),
                ft.Column(
                    controls=[
                        ft.Container(
                            content=ft.Text("AGENDAR CONSULTA"),
                            bgcolor="#f45557",
                            expand=True,
                            height=100,
                            alignment=ft.alignment.center
                        ),
                        ft.Container(
                            content=ft.Text("CANCELAR CONSULTA"),
                            bgcolor="#ff9a00",
                            expand=True,
                            height=100,
                            alignment=ft.alignment.center,
                        ),
                        ft.Container(
                            content=ft.Text("MINHAS CONSULTAS"),
                            bgcolor="#5e17eb",
                            height=100,
                            expand=True,
                            alignment=ft.alignment.center,
                        ),
                    ],
                    expand=True,
                    spacing=60,
                    alignment=ft.MainAxisAlignment.CENTER
                ),
            ])
        )

        self.controls = [
            self.body
        ]

    def handle_dismissal(self, e):
        print("Drawer dismissed!")

    def handle_change(self, e):
        print(f"Selected Index changed: {e.control.selected_index}")
        self.page.close(self.drawer)

