import flet as ft

class Cadastro(ft.View):
    def __init__(self, page: ft.Page, logo: ft.Image, title: str, bgcolor: str = "#f0f4f8"):
        super().__init__()
        self.route = "\\cadastro"
        self.page = page
        self.logo = logo
        self.title = title
        self.bgcolor = bgcolor

        self.banner = ft.Row(
            controls=[logo, ft.Text(self.title)],
            expand=True,
            alignment=ft.MainAxisAlignment.CENTER
        )

        # AppBar igual ao Login
        self.appbar = ft.AppBar(
            title=self.banner,
            center_title=True,
            bgcolor=ft.Colors.SURFACE_CONTAINER_HIGHEST,
            actions=[ft.IconButton(ft.Icons.WB_SUNNY_OUTLINED)],
        )

        self.text_cadastro = ft.Text(
            "Cadastro",
            color="#2a688a",
            size=28,
            font_family="League Spartan",
            weight=ft.FontWeight.W_700,
            text_align=ft.TextAlign.CENTER
        )

        self.field_cpf = self.create_field("CPF", False)
        self.field_name = self.create_field("Nome", False)
        self.field_email = self.create_field("Email", False)
        self.field_call = self.create_field("Telefone", False)
        self.field_senha = self.create_field("Senha", True)

        self.botao_cadastro = ft.ElevatedButton(
            "Cadastrar",
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

        self.form_container = ft.Container(
            content=ft.Column(
                [
                    self.text_cadastro,
                    self.field_cpf,
                    self.field_name,
                    self.field_email,
                    self.field_call,
                    self.field_senha,
                    self.botao_cadastro,
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
                        self.form_container
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    expand=True,
                ),
                expand=True,
                bgcolor=self.bgcolor,
                alignment=ft.alignment.center,
                padding=ft.padding.symmetric(horizontal=24)
            )
        )

        self.controls = [
            self.appbar,
            self.body
        ]

    def create_field(self, nome: str, password: bool, size: int = 18):
        return ft.TextField(
            label=nome,
            password=password,
            can_reveal_password=password,
            label_style=ft.TextStyle(
                color="#2a688a",
                font_family="Open Sans",
                weight=ft.FontWeight.W_700,
                size=size
            ),
            color="#222222",
            border_color="#b8b9bb",
            cursor_color="#2a688a",
            bgcolor="white",
            width=400,
            text_size=18,
            border_radius=8,
            content_padding=12,
        )

    def entrar_click(self, e):
        # Aqui você pode adicionar validação e cadastro real
        self.page.go("/home")
