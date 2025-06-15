import flet as ft

class Login(ft.View):
    def __init__(self, page: ft.Page, logo: ft.Image, title: str, bgcolor: str = "#f0f4f8"):
        super().__init__()
        self.route = "\\login"
        self.page = page
        self.logo = logo
        self.title = title
        self.bgcolor = bgcolor

        self.banner = ft.Row(
            controls=[logo, ft.Text(self.title)],
            expand=True,
            alignment=ft.MainAxisAlignment.CENTER
        )

        # AppBar original (igual ao seu código)
        self.appbar = ft.AppBar(
            title=self.banner,
            center_title=True,
            bgcolor=ft.Colors.SURFACE_CONTAINER_HIGHEST,
            actions=[ft.IconButton(ft.Icons.WB_SUNNY_OUTLINED)],
        )

        self.texto_login = ft.Text(
            "Faça seu Login",
            color="#2a688a",
            size=28,
            font_family="League Spartan",
            weight=ft.FontWeight.W_700,
            text_align=ft.TextAlign.CENTER
        )

        self.campo_cpf = ft.TextField(
            label="CPF",
            label_style=ft.TextStyle(
                color="#2a688a",
                font_family="Open Sans",
                weight=ft.FontWeight.W_700,
                size=18
            ),
            color="#222222",  # texto dentro do campo mais escuro
            border_color="#b8b9bb",
            cursor_color="#2a688a",
            bgcolor="white",
            width=400,
            text_size=18,
            border_radius=8,
            content_padding=12,
            autofocus=True
        )

        self.campo_senha = ft.TextField(
            label="Senha",
            password=True,
            can_reveal_password=True,
            label_style=ft.TextStyle(
                color="#2a688a",
                font_family="Open Sans",
                weight=ft.FontWeight.W_700,
                size=18
            ),
            color="#222222",  # texto dentro do campo mais escuro
            border_color="#b8b9bb",
            cursor_color="#2a688a",
            bgcolor="white",
            width=400,
            text_size=18,
            border_radius=8,
            content_padding=12,
        )

        self.texto_cadastro = ft.TextButton(
            "Não tem cadastro? Cadastre-se Aqui",
            on_click=self.cadastrar,
            style=ft.ButtonStyle(
                text_style=ft.TextStyle(
                    color="#2a688a",
                    font_family="Open Sans",
                    weight=ft.FontWeight.W_600,
                    size=16
                )
            ),
            tooltip="Ir para página de cadastro"
        )

        self.botao_entrar = ft.ElevatedButton(
            "Entrar",
            width=400,
            height=50,
            bgcolor="#2a688a",
            color="white",
            on_click=self.entrar_click,
            style=ft.ButtonStyle(
                shape=ft.RoundedRectangleBorder(radius=8),
                overlay_color="#1f4f7a",
                text_style=ft.TextStyle(
                    size=20,
                    font_family="Open Sans",
                    weight=ft.FontWeight.W_700
                )
            )
        )

        self.login_box = ft.Container(
            content=ft.Column(
                [
                    self.texto_login,
                    self.campo_cpf,
                    self.campo_senha,
                    self.texto_cadastro,
                    self.botao_entrar
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=24,
            ),
            width=480,
            padding=ft.padding.symmetric(vertical=48, horizontal=48),
            bgcolor="white",
            border_radius=15,
            shadow=ft.BoxShadow(
                blur_radius=18,
                color="#00000033",
                offset=ft.Offset(0, 6)
            ),
            alignment=ft.alignment.center,
        )

        self.body = ft.SafeArea(
            ft.Container(
                content=ft.Column(
                    [
                        self.login_box
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    expand=True,
                ),
                expand=True,
                bgcolor=self.bgcolor,
                alignment=ft.alignment.center,
                padding=ft.padding.symmetric(horizontal=24)
            ), expand=True
        )

        self.controls = [
            self.appbar,
            self.body
        ]

    def entrar_click(self, e):
        self.page.go("/home")

    def cadastrar(self, e):
        self.page.go("/cadastro")
